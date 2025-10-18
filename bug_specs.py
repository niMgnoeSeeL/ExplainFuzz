BUG_SPECS = {
    # === Simple projection / PII leakage ===
    "BUG01_select_email_order": {
        "required": ["ORDER", "BY"],
        "sensitive": ["email"],
        "complexity": "easy",
        "motivation": (
            "Ordering on long text fields like emails can expose encoding or collation "
            "bugs. Several DBMS have exhibited ordering instability and string comparator "
            "crashes on large text values."
        ),
    },

    "BUG02_where_type_mismatch_salary": {
        "required": ["WHERE"],
        "sensitive": ["salary"],
        "complexity": "easy",
        "motivation": (
            "Type coercion and implicit cast issues—e.g., comparing numeric columns "
            "against text literals—have led to incorrect filtering or planner errors in "
            "PostgreSQL, MySQL, and SQLite."
        ),
    },

    # === JOIN / multi-table exposure ===
    "BUG03_join_expose_email_ssn": {
        "required": ["JOIN"],
        "sensitive": ["email", "ssn_number"],
        "complexity": "medium",
        "motivation": (
            "Join reordering and incorrect join elimination can unintentionally expose "
            "columns from protected tables or bypass row-level filters. Similar regressions "
            "have been observed in PostgreSQL and MySQL optimizers."
        ),
    },

    "BUG04_join_mixed_numeric_types": {
        "required": ["JOIN"],
        "sensitive": ["salary", "dep_budget"],
        "complexity": "medium",
        "motivation": (
            "Joining on columns of mismatched numeric types (e.g., integer vs. decimal) "
            "can trigger coercion or overflow errors and lead to incorrect results—issues "
            "seen in MySQL and SQLite planner reports."
        ),
    },

    "BUG05_join_and_where_ssn": {
        "required": ["JOIN", "WHERE"],
        "sensitive": ["ssn_number"],
        "complexity": "medium",
        "motivation": (
            "When JOIN conditions interact with WHERE filters, planner reorderings "
            "can change the effective visibility of rows. Real cases have caused "
            "row-level security violations in complex policies."
        ),
    },

    # === Aggregation / HAVING / GROUP BY ===
    "BUG06_group_by_avg_salary": {
        "required": ["GROUP", "BY"],
        "sensitive": ["salary", "email"],
        "complexity": "medium",
        "motivation": (
            "Aggregation on sensitive numeric fields may trigger overflow, rounding, "
            "or mis-grouping errors. GROUP BY regressions of this form have appeared "
            "in several DBMS changelogs."
        ),
    },

    "BUG07_group_by_having_ssn": {
        "required": ["GROUP", "BY", "HAVING"],
        "sensitive": ["ssn_number"],
        "complexity": "medium",
        "motivation": (
            "HAVING clause mis-evaluation after aggregation has been observed in optimizer "
            "regressions, producing incorrect inclusion or exclusion of grouped rows."
        ),
    },

    "BUG08_group_by_distinct_interaction": {
        "required": ["GROUP", "BY", "DISTINCT"],
        "sensitive": ["email", "salary"],
        "complexity": "hard",
        "motivation": (
            "Interactions between DISTINCT and GROUP BY can yield incorrect deduplication "
            "or aggregation corruption. Such planner regressions were documented in "
            "PostgreSQL and Oracle."
        ),
    },

    # === Subqueries ===
    "BUG09_subquery_avg_salary": {
        "required": ["SELECT", "FROM", "SELECT"],
        "sensitive": ["salary"],
        "complexity": "hard",
        "motivation": (
            "Nested subqueries performing aggregation are prone to planner correlation "
            "bugs, causing crashes or wrong join conditions in analytical queries."
        ),
    },

    "BUG10_nested_select_ssn": {
        "required": ["SELECT", "FROM", "SELECT"],
        "sensitive": ["ssn_number"],
        "complexity": "hard",
        "motivation": (
            "Deeply nested SELECT statements referencing sensitive columns can expose "
            "semantic errors in permission propagation or subquery flattening."
        ),
    },

    # === UNION and set operators ===
    "BUG11_union_projection_leak": {
        "required": ["UNION"],
        "sensitive": ["email"],
        "complexity": "medium",
        "motivation": (
            "UNION-based injection and projection mismatches are classic exfiltration "
            "patterns; attackers leverage UNION to append sensitive fields. Numerous "
            "plugin CVEs exhibit this structure."
        ),
    },

    "BUG12_union_type_coercion": {
        "required": ["UNION"],
        "sensitive": ["salary", "budget"],
        "complexity": "hard",
        "motivation": (
            "UNION across mismatched numeric types can cause coercion, overflow, or "
            "schema mismatch bugs. Real-world advisories describe such planner failures."
        ),
    },

    # === Logical operator / short-circuiting ===
    "BUG13_where_or_salary": {
        "required": ["WHERE", "OR"],
        "sensitive": ["salary"],
        "complexity": "medium",
        "motivation": (
            "Short-circuit or NULL-handling inconsistencies in WHERE/OR evaluation can "
            "lead to incorrect row selection—an issue historically found in SQLite "
            "and SQL Server."
        ),
    },

    "BUG14_where_or_email_salary": {
        "required": ["WHERE", "OR"],
        "sensitive": ["email", "salary"],
        "complexity": "medium",
        "motivation": (
            "Compound OR conditions on sensitive fields mimic injection payloads and can "
            "trigger null-handling errors or logic simplification bugs."
        ),
    },

    "BUG15_not_in_null_semantics": {
        "required": ["NOT", "IN"],
        "sensitive": ["salary"],
        "complexity": "hard",
        "motivation": (
            "NOT IN semantics with NULL values are a common source of logical errors "
            "and optimizer misbehavior. Several DBMS have fixed incorrect NULL "
            "interpretations in recent versions."
        ),
    },

    # === ORDER / collation edge ===
    "BUG16_order_by_collation_edge": {
        "required": ["ORDER", "BY"],
        "sensitive": ["salary", "ssn_number"],
        "complexity": "medium",
        "motivation": (
            "Collation and locale-handling issues under ORDER BY on mixed or large "
            "data types have triggered correctness and stability bugs across MySQL, "
            "SQLite, and PostgreSQL."
        ),
    },

    # === Complex combined operators ===
    "BUG17_aggregate_join_exposure": {
        "required": ["JOIN", "GROUP", "BY"],
        "sensitive": ["salary", "email"],
        "complexity": "hard",
        "motivation": (
            "Interactions between joins and aggregations often produce planner errors "
            "or wrong visibility for sensitive columns. Such multi-operator regressions "
            "are among the most common in optimizer issue trackers."
        ),
    },
}
