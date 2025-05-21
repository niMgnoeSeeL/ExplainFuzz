parser grammar mdxParser;

options { tokenVocab=mdxLexer;}

mdx_statement : select_statement EOF ;

block_0 : WITH formula_specification ;

block_1 : WHERE slicer_specification ;

select_statement : block_0_question SELECT axis_specification_list_question FROM cube_specification block_1_question cell_props_question ;

cell_props_question :  
| cell_question PROPERTIES cell_property_list ;

block_1_question :  
| WHERE slicer_specification ;

axis_specification_list_question :  
| axis_specification block_5_star 
| block_8_question expression dim_props_question ON axis_name ;

block_0_question :  
| WITH formula_specification ;

single_formula_specification_plus : single_formula_specification single_formula_specification_plus 
| MEMBER member_name AS block_3 
| SET set_name AS block_2 ;

block_2 : QUOTE expression QUOTE 
| value_expression block_11_star 
| term5 block_12_star 
| term4 block_13_star 
| NOT term4 
| term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

set_specification : SET set_name AS block_2 ;

block_31 : QUOTE value_expression QUOTE 
| term5 block_12_star 
| term4 block_13_star 
| NOT term4 
| term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_3 : block_31 COMMA member_property_def_list_question ;

member_property_def_list_question :  
| member_property_definition block_6_star 
| identifier EQ value_expression ;

member_specification : MEMBER member_name AS block_3 ;

block_5 : COMMA axis_specification ;

axis_specification_list : axis_specification block_5_star 
| block_8_question expression dim_props_question ON axis_name ;

block_5_star : block_5 block_5_star 
| COMMA axis_specification ;

block_6 : COMMA member_property_definition ;

member_property_def_list : member_property_definition block_6_star 
| identifier EQ value_expression ;

block_6_star : block_6 block_6_star 
| COMMA member_property_definition ;

member_property_definition : identifier EQ value_expression ;

block_7 : DOT identifier ;

compound_id : identifier block_7_star 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_7_star : block_7 block_7_star 
| DOT identifier ;

block_8 : NON EMPTY ;

axis_specification : block_8_question expression dim_props_question ON axis_name ;

dim_props_question :  
| dimension_question PROPERTIES property_list ;

block_8_question :  
| NON EMPTY ;

dim_props : dimension_question PROPERTIES property_list ;

dimension_question : DIMENSION 
|  ;

block_9 : COMMA property_ ;

property_list : property_ block_9_star 
| identifier block_7_star 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_9_star : block_9 block_9_star 
| COMMA property_ ;

cell_props : cell_question PROPERTIES cell_property_list ;

cell_question : CELL 
|  ;

block_10 : COMMA cell_property ;

cell_property_list : cell_property block_10_star 
| CELL_ORDINAL 
| VALUE 
| FORMATTED_VALUE 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_10_star : block_10 block_10_star 
| COMMA cell_property ;

mandatory_cell_property : CELL_ORDINAL 
| VALUE 
| FORMATTED_VALUE ;

block_11 : COLON value_expression ;

expression : value_expression block_11_star 
| term5 block_12_star 
| term4 block_13_star 
| NOT term4 
| term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_11_star : block_11 block_11_star 
| COLON value_expression ;

value_expression : term5 block_12_star 
| term4 block_13_star 
| NOT term4 
| term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_12_star : block_12 block_12_star 
| XOR term5 
| OR term5 ;

value_xor_expression : XOR term5 ;

value_or_expression : OR term5 ;

block_13 : AND term4 ;

term5 : term4 block_13_star 
| NOT term4 
| term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_13_star : block_13 block_13_star 
| AND term4 ;

term4 : NOT term4 
| term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_14 : comp_op term2 ;

term3 : term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_14_star : block_14 block_14_star 
| comp_op term2 ;

block_32 : CONCAT 
| PLUS 
| MINUS ;

block_15 : block_32 term ;

term2 : term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_15_star : block_15 block_15_star 
| block_32 term ;

block_33 : SOLIDUS 
| ASTERISK ;

block_17 : block_33 factor ;

term : factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_17_star : block_17 block_17_star 
| block_33 factor ;

factor : MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

function_ : identifier LPAREN block_19_question RPAREN ;

block_19_question :  
| expression block_25_star 
| value_expression block_11_star 
| term5 block_12_star 
| term4 block_13_star 
| NOT term4 
| term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_20 : DOT block_34 ;

value_expression_primary : value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_20_star : block_20 block_20_star 
| DOT block_34 ;

block_22 : LPAREN exp_list RPAREN ;

block_23 : LBRACE block_35_question RBRACE ;

block_35_question :  
| expression block_25_star 
| value_expression block_11_star 
| term5 block_12_star 
| term4 block_13_star 
| NOT term4 
| term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

value_expression_primary0 : STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_25 : COMMA expression ;

exp_list : expression block_25_star 
| value_expression block_11_star 
| term5 block_12_star 
| term4 block_13_star 
| NOT term4 
| term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_25_star : block_25 block_25_star 
| COMMA expression ;

block_28 : ELSE value_expression ;

case_expression : CASE block_26_question block_27_question block_28_question END ;

block_28_question :  
| ELSE value_expression ;

block_27_question :  
| when_clause block_29_star 
| WHEN value_expression THEN value_expression ;

block_26_question :  
| term5 block_12_star 
| term4 block_13_star 
| NOT term4 
| term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

when_list : when_clause block_29_star 
| WHEN value_expression THEN value_expression ;

block_29_star : block_29 block_29_star 
| WHEN value_expression THEN value_expression ;

when_clause : WHEN value_expression THEN value_expression ;

comp_op : EQ 
| NE 
| LT 
| GT 
| LE 
| GE ;

unquoted_identifier : ID 
| DIMENSION 
| PROPERTIES ;

amp_quoted_identifier : AMP_QUOTED_ID ;

quoted_identifier : QUOTED_ID ;

keyword : DIMENSION 
| PROPERTIES ;

formula_specification : single_formula_specification single_formula_specification_plus 
| MEMBER member_name AS block_3 
| SET set_name AS block_2 ;

single_formula_specification : MEMBER member_name AS block_3 
| SET set_name AS block_2 ;

member_name : identifier block_7_star 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

set_name : identifier block_7_star 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

property_ : identifier block_7_star 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

cube_name : identifier block_7_star 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

slicer_specification : value_expression block_11_star 
| term5 block_12_star 
| term4 block_13_star 
| NOT term4 
| term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

cell_property : CELL_ORDINAL 
| VALUE 
| FORMATTED_VALUE 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_12 : XOR term5 
| OR term5 ;

block_19 : expression block_25_star 
| value_expression block_11_star 
| term5 block_12_star 
| term4 block_13_star 
| NOT term4 
| term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_34 : ID 
| QUOTED_ID 
| AMP_QUOTED_ID 
| identifier LPAREN block_19_question RPAREN 
| DIMENSION 
| PROPERTIES ;

block_35 : expression block_25_star 
| value_expression block_11_star 
| term5 block_12_star 
| term4 block_13_star 
| NOT term4 
| term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_26 : term5 block_12_star 
| term4 block_13_star 
| NOT term4 
| term2 block_14_star 
| term block_15_star 
| factor block_17_star 
| MINUS value_expression_primary 
| PLUS value_expression_primary 
| value_expression_primary0 block_20_star 
| STRING 
| NUMBER 
| identifier LPAREN block_19_question RPAREN 
| LPAREN exp_list RPAREN 
| LBRACE block_35_question RBRACE 
| CASE block_26_question block_27_question block_28_question END 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

block_27 : when_clause block_29_star 
| WHEN value_expression THEN value_expression ;

block_29 : WHEN value_expression THEN value_expression ;

block_30 : ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

cube_specification : identifier block_7_star 
| ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

identifier : ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

axis_name : ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

provider_specific_cell_property : ID 
| QUOTED_ID 
| DIMENSION 
| PROPERTIES ;

