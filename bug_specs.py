BUG_SPECS_SQL = {
    # === Simple projection / PII leakage ===
    "BUG01_order_email": {
        "required": ["ORDER", "BY"],
        "sensitive": ["email"],
        "complexity": "easy",
        "motivation": (
            "Ordering on long text fields like emails can expose encoding or collation "
            "bugs. Several DBMS have exhibited ordering instability and string comparator "
            "crashes on large text values."
        ),
    },

    "BUG02_order_salary_ssn": {
        "required": ["ORDER", "BY"],
        "sensitive": ["salary", "ssn_number"],
        "complexity": "medium",
        "motivation": (
            "Collation and locale-handling issues under ORDER BY on mixed or large "
            "data types have triggered correctness and stability bugs across MySQL, "
            "SQLite, and PostgreSQL."
        ),
    },

    "BUG03_where_salary": {
        "required": ["WHERE"],
        "sensitive": ["salary"],
        "complexity": "easy",
        "motivation": (
            "Type coercion and implicit cast issues—e.g., comparing numeric columns "
            "against text literals—have led to incorrect filtering or planner errors in "
            "PostgreSQL, MySQL, and SQLite."
        ),
    },

        # === Logical operator / short-circuiting ===
    "BUG04_where_or_salary": {
        "required": ["WHERE", "OR"],
        "sensitive": ["salary"],
        "complexity": "medium",
        "motivation": (
            "Short-circuit or NULL-handling inconsistencies in WHERE/OR evaluation can "
            "lead to incorrect row selection—an issue historically found in SQLite "
            "and SQL Server."
        ),
    },

    "BUG05_where_or_email_salary": {
        "required": ["WHERE", "OR"],
        "sensitive": ["email", "salary"],
        "complexity": "medium",
        "motivation": (
            "Compound OR conditions on sensitive fields mimic injection payloads and can "
            "trigger null-handling errors or logic simplification bugs."
        ),
    },

    # === JOIN / multi-table exposure ===
    "BUG06_join_email_ssn": {
        "required": ["JOIN"],
        "sensitive": ["email", "ssn_number"],
        "complexity": "medium",
        "motivation": (
            "Join reordering and incorrect join elimination can unintentionally expose "
            "columns from protected tables or bypass row-level filters. Similar regressions "
            "have been observed in PostgreSQL and MySQL optimizers."
        ),
    },

    "BUG07_join_where_ssn": {
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
    "BUG08_group_salary_email": {
        "required": ["GROUP", "BY"],
        "sensitive": ["salary", "email"],
        "complexity": "medium",
        "motivation": (
            "Aggregation on sensitive numeric fields may trigger overflow, rounding, "
            "or mis-grouping errors. GROUP BY regressions of this form have appeared "
            "in several DBMS changelogs."
        ),
    },

    "BUG09_group_by_having_ssn": {
        "required": ["GROUP", "BY", "HAVING"],
        "sensitive": ["ssn_number"],
        "complexity": "medium",
        "motivation": (
            "HAVING clause mis-evaluation after aggregation has been observed in optimizer "
            "regressions, producing incorrect inclusion or exclusion of grouped rows."
        ),
    },

    "BUG10_group_distinct_email_salary": {
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
    "BUG11_nested_salary": {
        "required": ["SELECT", "FROM", "SELECT"],
        "sensitive": ["salary"],
        "complexity": "hard",
        "motivation": (
            "Nested subqueries performing aggregation are prone to planner correlation "
            "bugs, causing crashes or wrong join conditions in analytical queries."
        ),
    },

    "BUG12_nested_select_ssn": {
        "required": ["SELECT", "FROM", "SELECT"],
        "sensitive": ["ssn_number"],
        "complexity": "hard",
        "motivation": (
            "Deeply nested SELECT statements referencing sensitive columns can expose "
            "semantic errors in permission propagation or subquery flattening."
        ),
    },

    # === UNION and set operators ===
    "BUG13_union_email": {
        "required": ["UNION"],
        "sensitive": ["email"],
        "complexity": "medium",
        "motivation": (
            "UNION-based injection and projection mismatches are classic exfiltration "
            "patterns; attackers leverage UNION to append sensitive fields. Numerous "
            "plugin CVEs exhibit this structure."
        ),
    },

    "BUG14_union_salary_budget": {
        "required": ["UNION"],
        "sensitive": ["salary", "budget"],
        "complexity": "hard",
        "motivation": (
            "UNION across mismatched numeric types can cause coercion, overflow, or "
            "schema mismatch bugs. Real-world advisories describe such planner failures."
        ),
    },



    # === Complex combined operators ===
    "BUG15_join_group_email_salary": {
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

BUG_SPECS_XML = {
    "BUG01_control_bug": {
        "static_triggers": ["incorrect_start_query"],
        "dynamic_triggers": [],
        "cond_token": "Name",
        "complexity":"very easy",
        "description": "The control bug simulates a structural validation failure where the XPath expression in a <query> element does not start with '/'. Grammarinator can easily generate such malformed queries by mutating the attribute 'q'.",
        "motivation": "This control bug is introduced to validate that the fuzzer can explore the input space deeply enough to produce syntactically valid yet semantically incorrect queries. It serves as a reachability baseline: the initial seeds comply with the schema (e.g., q='/user'), but Grammarinator mutations are expected to produce invalid paths like q='user', triggering the bug."
    },
    "BUG02_numeric_overflow_bug": {
        "static_triggers": ["numeric_overflow_candidate"],
        "dynamic_triggers": [],
        "cond_token": "Name",
        "complexity":"easy", 
        "description": "Large numeric values or runtime overflows were detected in XML attributes, suggesting arithmetic logic issues.",
        "motivation": "Numeric overflows or excessively large numeric inputs can cause logic errors, data corruption, or denial-of-service conditions."
    },
    "BUG03_read_system_file": {
        "static_triggers": [],
        "dynamic_triggers": ["system_file_read"],
        "cond_token": "Name",
        "complexity":"medium", 
        "description": "The application read a file from the filesystem at runtime, potentially exposing sensitive data.",
        "motivation": "Dynamic file reads indicate successful exploitation of XXE or path traversal vulnerabilities, which could leak sensitive data or allow file manipulation."
    },
     "BUG04_read_sensitive_local_files": {
        "static_triggers": [],
        "dynamic_triggers": ["local_repo_file_read"],
        "cond_token": "Name", 
        "complexity":"medium",
        "description": "The application read sensitive files from the local filesystem at runtime, potentially exposing secrets or critical configuration data.",
        "motivation": "Dynamic reads of sensitive local files indicate that attacker-controlled input or unprotected logic allowed access to critical data, which could lead to information leakage or compromise of the application environment."
    },
    "BUG05_xpath_injection_observed": {
        "static_triggers": ["xpath_injection_candidate"],
        "dynamic_triggers": ["xpath_query_executed"],
        "cond_token": "Name",
        "complexity":"medium", 
        "description": "Suspicious XPath expressions from the XML input were successfully executed at runtime, indicating that untrusted input influenced query results.",
        "motivation": "Execution of attacker-controlled XPath queries can bypass authorization checks or extract sensitive data from XML documents. Even if no errors occurred, this shows that the input reached the query processor and could be exploited."
    },
    "BUG06_xpath_injection_error": {
        "static_triggers": ["xpath_injection_candidate"],
        "dynamic_triggers": ["BUG06_xpath_injection_error"],
        "cond_token": "CDATA", 
        "complexity":"medium",
        "description": "Suspicious XPath expressions caused runtime errors when executed, revealing that untrusted input reached the query interpreter.",
        "motivation": "Errors from attacker-controlled XPath queries demonstrate input validation flaws and potential denial-of-service vectors. Malformed input reaching the query processor can destabilize the application or expose sensitive processing logic."
    },
    "BUG07_namespace_confusion": {
        "static_triggers": ["namespace_confusion_candidate"],
        "dynamic_triggers": [],
        "cond_token": "Name",
        "complexity":"medium", 
        "description": "Unusually high number of XML namespaces may be used to confuse schema validation or security filters.",
        "motivation": "Namespace confusion can allow malicious content to bypass structural or access controls, even without runtime evidence."
    },
    "BUG08_cdata_injection": {
        "static_triggers": ["cdata_injection_candidate"],
        "dynamic_triggers": [],
        "cond_token": "CDATA",
        "complexity":"hard",
        "description": "CDATA sections embed unescaped markup or payloads that downstream processors render or re-parse unsafely, resulting in unsafe execution or data leakage.",
        "motivation": "Conditioning on CDATA biases generation toward XMLs containing <![CDATA[...]]> blocks that are syntactically valid yet semantically risky for downstream consumers."
    },
    "BUG09_comment_logic_bypass": {
        "static_triggers": ["auth_bypass_detected"],
        "dynamic_triggers": [],
        "cond_token": "COMMENT",
        "complexity":"hard",
        "description": "Comments placed inside or around critical configuration/authorization elements cause the application to misinterpret configuration or skip elements, leading to logic bypasses.",
        "motivation": "Conditioning on COMMENT encourages generation of documents that include comments in sensitive positions; these are valid XML but can change application behavior if comments are not pre-processed correctly."
    },
    "BUG10_entity_expansion_bomb": {
        "static_triggers": ["entity_expansion_critic"],
        "dynamic_triggers": [],
        "cond_token": "EntityRef",
        "complexity":"hard",
        "description": "High-density or repeated entity references (e.g. &x;&x;&x; ...) lead to exponential expansion or heavy processing, causing resource exhaustion or parser timeouts while remaining well-formed XML.",
        "motivation": "Conditioning on EntityRef encourages generation of inputs with many entity references, creating a high-signal target for measuring parser resilience against entity expansion attacks."
    }

}
