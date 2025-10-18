parser grammar SQLSimplifiedParser;

options {
    tokenVocab = SQLSimplifiedLexer;
}

start : select_statement SEMI EOF;

select_statement
    : SELECT column_list_or_star FROM from_clause join_clause where_clause group_clause having_clause sort_clause union_list
    | SELECT DISTINCT column_list_or_star FROM from_clause sort_clause
    ;

union_list: | UNION select_statement;

c_expr
    : columnref
    | columnref binary_op_columnref_list
    | unary_op c_expr
    | binary_op c_expr
    | f_expr
    | OPEN_PAREN select_statement CLOSE_PAREN
    | STAR
    | Integral
    | Numeric
    | DISTINCT c_expr
    | OPEN_PAREN string_list CLOSE_PAREN
    | OPEN_PAREN integral_list CLOSE_PAREN
    ;

f_expr
    : Identifier OPEN_PAREN c_expr CLOSE_PAREN
    | OPEN_PAREN c_expr CLOSE_PAREN
    | EXTRACT OPEN_PAREN YEAR_P FROM c_expr CLOSE_PAREN
    | Identifier OPEN_PAREN CASE WHEN c_expr THEN c_expr ELSE integral_or_null END_P CLOSE_PAREN binary_op_fexpr_list
    | SUBSTRING OPEN_PAREN c_expr FROM Integral FOR Integral CLOSE_PAREN
    | ROUND OPEN_PAREN c_expr SLASH c_expr COMMA Integral CLOSE_PAREN
    | OPEN_PAREN CASE WHEN c_expr THEN c_expr ELSE integral_or_null END_P CLOSE_PAREN binary_op_fexpr_list
    ;

integral_or_null: Integral | NULL_P;

binary_op_fexpr_list: | binary_op_fexpr_list binary_op f_expr;

string_list
    : StringConstant
    | StringConstant COMMA string_list
    ;

integral_list
    : Integral
    | Integral COMMA integral_list
    ;

binary_op_columnref_list: math_op columnref | binary_op_columnref_list binary_op columnref;

where_clause: WHERE c_expr | ;

join_clause:
    JOIN table_ref ON on_clause
    | JOIN OPEN_PAREN select_statement CLOSE_PAREN AS Identifier ON on_clause
    |
    ;

on_clause:
    columnref binary_op_columnref_list 
    | unary_op columnref binary_op_columnref_list
    ;

group_clause: GROUP_P BY group_by_list | ;

group_by_list
    : columnref
    | group_by_list COMMA columnref
    ;

having_clause: HAVING c_expr | ;

sort_clause: ORDER BY sortby_list | ;

column_list_or_star
    : STAR
    | column_list
    ;

column_list
    : columnref
    | column_list COMMA columnref
    ;

sortby_list
    : sortby
    | sortby COMMA sortby_list
    ;

from_list
    : table_ref
    | from_list COMMA table_ref
    ;

from_clause
    : from_list
    | OPEN_PAREN select_statement CLOSE_PAREN AS table_ref
    ;

sortby
    : columnref
    | Identifier USING gt_lt
    | Identifier asc_desc
    ;


columnref
    : Identifier
    | Identifier AS collabel
    | table_ref DOT identifier_or_star
    | table_ref DOT identifier_or_star AS collabel
    | Integral
    | StringConstant AS collabel
    | StringConstant
    | Numeric
    | Numeric AS collabel
    | typeidentifier StringConstant
    | typeidentifier StringConstant typeidentifier
    | f_expr
    | f_expr AS collabel
    | f_expr AS VALUE_P
    ;

table_ref
    : Identifier
    | Identifier AS collabel
    | f_expr AS Identifier
;

typeidentifier:
    Identifier | TIME | INTERVAL | DAY_P
;

binary_op: logic_op | math_op;

math_op : LT | GT | EQUAL;

logic_op : AND | OR;

unary_op: NOT | EXISTS;

identifier_or_star: Identifier | STAR;

gt_lt: GT | LT;

asc_desc: ASC | DESC;

collabel: Identifier;