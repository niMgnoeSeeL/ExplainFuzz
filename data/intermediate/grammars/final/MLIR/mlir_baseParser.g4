parser grammar mlir_baseParser;

options { tokenVocab=mlir_baseLexer;}

bool_literal : TRUE 
| FALSE ;

decimal_literal : DIGITS ;

integer_literal : HEXADECIMAL_LITERAL 
| DIGITS ;

negated_integer_literal : TERM_0 integer_literal ;

string_literal : ESCAPED_STRING ;

constant_literal : FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS ;

suffix_id : DIGITS 
| BARE_ID ;

block_0 : TERM_2 DIGITS ;

ssa_id : TERM_1 suffix_id block_0_question ;

block_0_question :  
| TERM_2 DIGITS ;

symbol_ref_id : TERM_3 block_1 ;

block_id : TERM_4 suffix_id ;

block_56 : BARE_ID 
| TERM_6 ;

block_2 : BARE_ID 
| ESCAPED_STRING 
| block_56 block_56_plus 
| BARE_ID 
| TERM_6 ;

block_56_plus : block_56 block_56_plus 
| BARE_ID 
| TERM_6 ;

type_alias : TERM_5 block_2 ;

map_or_set_id : TERM_2 suffix_id ;

block_4 : BARE_ID 
| ESCAPED_STRING ;

attribute_alias : TERM_2 block_4 ;

block_5 : TERM_7 ssa_id ;

ssa_id_list : ssa_id block_5_star 
| TERM_1 suffix_id block_0_question ;

block_5_star : block_5 block_5_star 
| TERM_7 ssa_id ;

block_6 : TERM_7 ssa_use ;

ssa_use_list : ssa_use block_6_star 
| TERM_1 suffix_id block_0_question 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS ;

block_6_star : block_6 block_6_star 
| TERM_7 ssa_use ;

opaque_dialect_item : BARE_ID TERM_8 string_literal TERM_9 ;

block_7 : BARE_ID TERM_6 ;

pretty_dialect_item : block_7_question BARE_ID pretty_dialect_item_body_question ;

pretty_dialect_item_body_question :  
| TERM_8 pretty_dialect_item_contents block_8_star TERM_9 
| TERM_8 pretty_dialect_item_contents TERM_9 ;

block_7_question :  
| BARE_ID TERM_6 ;

block_8 : TERM_7 pretty_dialect_item_contents ;

pretty_dialect_item_body : TERM_8 pretty_dialect_item_contents block_8_star TERM_9 
| TERM_8 pretty_dialect_item_contents TERM_9 ;

block_8_star : block_8 block_8_star 
| TERM_7 pretty_dialect_item_contents ;

block_9 : TERM_10 pretty_dialect_item_contents TERM_11 ;

block_57 : TERM_7 pretty_dialect_item_contents ;

block_10 : TERM_12 pretty_dialect_item_contents_question block_57_star TERM_13 
| TERM_12 pretty_dialect_item_contents_question TERM_13 ;

block_57_star : block_57 block_57_star 
| TERM_7 pretty_dialect_item_contents ;

pretty_dialect_item_contents_question :  
| TERM_10 pretty_dialect_item_contents TERM_11 
| TERM_12 pretty_dialect_item_contents_question block_57_star TERM_13 
| TERM_14 pretty_dialect_item_contents TERM_15 
| pretty_dialect_item_other_content pretty_dialect_item_other_content_plus 
| BARE_ID 
| TERM_16 
| TERM_17 
| TERM_7 
| TERM_18 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| BARE_ID 
| function_type_list block_34 function_type_list 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| DIGITS 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| TERM_12 pretty_dialect_item_contents_question TERM_13 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 ;

block_12 : TERM_14 pretty_dialect_item_contents TERM_15 ;

pretty_dialect_item_other_content_plus : pretty_dialect_item_other_content pretty_dialect_item_other_content_plus 
| BARE_ID 
| TERM_16 
| TERM_17 
| TERM_7 
| TERM_18 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| BARE_ID 
| function_type_list block_34 function_type_list 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| DIGITS 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| block_34 function_type_list 
| function_type_list block_34 
| TERM_21 
| TERM_22 
| TERM_23 ;

pretty_dialect_item_other_content : BARE_ID 
| TERM_16 
| TERM_17 
| TERM_7 
| TERM_18 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| BARE_ID 
| function_type_list block_34 function_type_list 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| DIGITS 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 ;

dialect_type : term_5_question block_13 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question ;

term_5_question : TERM_5 ;

non_function_type : BARE_ID 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question ;

block_14 : TERM_7 type ;

type_list_no_parens : type block_14_star 
| BARE_ID 
| function_type_list block_34 function_type_list 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 ;

block_14_star : block_14 block_14_star 
| TERM_7 type ;

block_15 : TERM_10 TERM_11 ;

block_16 : TERM_10 type_list_no_parens TERM_11 ;

ssa_use_and_type : ssa_use TERM_18 type ;

block_17 : TERM_7 ssa_use_and_type ;

ssa_use_and_type_list : ssa_use_and_type block_17_star 
| ssa_use TERM_18 type ;

block_17_star : block_17 block_17_star 
| TERM_7 ssa_use_and_type ;

block_58 : TERM_7 attribute_value ;

block_18 : attribute_value block_58_star 
| TERM_2 block_4 
| term_2_question block_29 block_30_question 
| TERM_12 block_18_question TERM_13 
| TERM_14 block_20_question TERM_15 
| posneg_integer_literal optional_type 
| string_literal optional_type 
| TRUE 
| FALSE 
| FLOAT_LITERAL optional_type 
| HEXADECIMAL_LITERAL TERM_18 type 
| symbol_ref_id block_60_star 
| BARE_ID 
| function_type_list block_34 function_type_list 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| FLOAT_LITERAL 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| ESCAPED_STRING 
| TERM_3 block_1 
| term_2_question block_29 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 
| block_29 block_30_question 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question ;

block_58_star : block_58 block_58_star 
| TERM_7 attribute_value ;

array_attribute : TERM_12 block_18_question TERM_13 ;

block_18_question :  
| attribute_value block_58_star 
| TERM_2 block_4 
| term_2_question block_29 block_30_question 
| TERM_12 block_18_question TERM_13 
| TERM_14 block_20_question TERM_15 
| posneg_integer_literal optional_type 
| string_literal optional_type 
| TRUE 
| FALSE 
| FLOAT_LITERAL optional_type 
| HEXADECIMAL_LITERAL TERM_18 type 
| symbol_ref_id block_60_star 
| BARE_ID 
| function_type_list block_34 function_type_list 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| FLOAT_LITERAL 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| ESCAPED_STRING 
| TERM_3 block_1 
| term_2_question block_29 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 
| block_29 block_30_question 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question ;

block_59 : TERM_7 attribute_entry ;

block_20 : attribute_entry block_59_star 
| BARE_ID 
| BARE_ID TERM_20 attribute_value 
| BARE_ID TERM_6 BARE_ID 
| BARE_ID TERM_6 BARE_ID TERM_20 attribute_value 
| string_literal TERM_20 attribute_value ;

block_59_star : block_59 block_59_star 
| TERM_7 attribute_entry ;

dictionary_attribute : TERM_14 block_20_question TERM_15 ;

block_20_question :  
| attribute_entry block_59_star 
| BARE_ID 
| BARE_ID TERM_20 attribute_value 
| BARE_ID TERM_6 BARE_ID 
| BARE_ID TERM_6 BARE_ID TERM_20 attribute_value 
| string_literal TERM_20 attribute_value ;

block_22 : FLOAT_LITERAL optional_type 
| FLOAT_LITERAL ;

block_23 : HEXADECIMAL_LITERAL TERM_18 type ;

integer_attribute : posneg_integer_literal optional_type 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS ;

string_attribute : string_literal optional_type 
| ESCAPED_STRING ;

block_60 : TERM_19 symbol_ref_id ;

block_24 : symbol_ref_id block_60_star 
| TERM_3 block_1 ;

block_60_star : block_60 block_60_star 
| TERM_19 symbol_ref_id ;

dependent_attribute_entry : BARE_ID TERM_20 attribute_value ;

block_26 : BARE_ID TERM_6 BARE_ID ;

block_27 : BARE_ID TERM_6 BARE_ID TERM_20 attribute_value ;

block_28 : string_literal TERM_20 attribute_value ;

block_30 : TERM_18 type ;

dialect_attribute : term_2_question block_29 block_30_question 
| term_2_question block_29 
| block_29 block_30_question 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question ;

term_2_question : TERM_2 ;

property_dict : TERM_8 attribute_dict TERM_9 ;

attribute_entry : BARE_ID 
| BARE_ID TERM_20 attribute_value 
| BARE_ID TERM_6 BARE_ID 
| BARE_ID TERM_6 BARE_ID TERM_20 attribute_value 
| string_literal TERM_20 attribute_value ;

block_31 : TERM_14 TERM_15 ;

block_61 : TERM_7 attribute_entry ;

block_32 : TERM_14 attribute_entry block_61_star TERM_15 
| TERM_14 attribute_entry TERM_15 ;

block_61_star : block_61 block_61_star 
| TERM_7 attribute_entry ;

trailing_type : TERM_18 function_type ;

block_34 : TERM_21 
| TERM_22 
| TERM_23 ;

function_type : function_type_list block_34 function_type_list 
| block_34 function_type_list 
| function_type_list block_34 
| TERM_21 
| TERM_22 
| TERM_23 ;

block_35 : TERM_7 non_function_type ;

function_type_list : TERM_10 non_function_type_question block_35_star TERM_11 
| non_function_type_question block_35_star 
| TERM_10 non_function_type_question TERM_11 
| BARE_ID 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| TERM_10 block_35_star TERM_11 
| TERM_10 TERM_11 
| block_35 block_35_star 
| TERM_7 non_function_type ;

block_35_star : block_35 block_35_star 
| TERM_7 non_function_type ;

op_result : ssa_id optional_int_literal 
| TERM_1 suffix_id block_0_question ;

block_37 : TERM_7 op_result ;

op_result_list : op_result block_37_star TERM_20 
| op_result TERM_20 ;

block_37_star : block_37 block_37_star 
| TERM_7 op_result ;

location : string_literal TERM_18 decimal_literal TERM_18 decimal_literal ;

block_38 : TERM_24 TERM_10 location TERM_11 ;

generic_operation : string_literal TERM_10 optional_ssa_use_list TERM_11 optional_successor_list optional_prop_dict optional_region_list optional_attr_dict trailing_type 
| string_literal TERM_10 optional_ssa_use_list TERM_11 optional_successor_list optional_prop_dict optional_region_list trailing_type ;

custom_operation : BARE_ID TERM_6 BARE_ID optional_ssa_use_list trailing_type ;

operation : optional_op_result_list block_39 optional_trailing_loc 
| block_39 optional_trailing_loc 
| optional_op_result_list block_39 
| BARE_ID TERM_6 BARE_ID optional_ssa_use_list trailing_type 
| string_literal TERM_10 optional_ssa_use_list TERM_11 optional_successor_list optional_prop_dict optional_region_list optional_attr_dict trailing_type 
| string_literal TERM_10 argument_list_question TERM_11 TERM_10 region TERM_11 attribute_dict_question trailing_type trailing_location_question 
| string_literal TERM_10 optional_ssa_use_list TERM_11 optional_successor_list optional_prop_dict optional_region_list trailing_type ;

ssa_id_and_type : ssa_id TERM_18 type ;

block_40 : TERM_7 ssa_id_and_type ;

ssa_id_and_type_list : ssa_id_and_type block_40_star 
| ssa_id TERM_18 type ;

block_40_star : block_40 block_40_star 
| TERM_7 ssa_id_and_type ;

block_arg_list : TERM_10 optional_ssa_and_type_list TERM_11 ;

operation_plus : operation operation_plus 
| optional_op_result_list block_39 optional_trailing_loc 
| block_39 optional_trailing_loc 
| optional_op_result_list block_39 
| BARE_ID TERM_6 BARE_ID optional_ssa_use_list trailing_type 
| string_literal TERM_10 optional_ssa_use_list TERM_11 optional_successor_list optional_prop_dict optional_region_list optional_attr_dict trailing_type 
| string_literal TERM_10 argument_list_question TERM_11 TERM_10 region TERM_11 attribute_dict_question trailing_type trailing_location_question 
| string_literal TERM_10 optional_ssa_use_list TERM_11 optional_successor_list optional_prop_dict optional_region_list trailing_type ;

block_label : block_id optional_block_arg_list TERM_18 ;

block_41 : TERM_7 block_id ;

successor_list : TERM_12 block_id_question block_41_star TERM_13 
| TERM_12 block_id_question TERM_13 ;

block_41_star : block_41 block_41_star 
| TERM_7 block_id ;

block_id_question :  
| TERM_4 suffix_id ;

block : optional_block_label operation_list 
| operation operation_plus 
| optional_op_result_list block_39 optional_trailing_loc 
| block_39 optional_trailing_loc 
| optional_op_result_list block_39 
| BARE_ID TERM_6 BARE_ID optional_ssa_use_list trailing_type 
| string_literal TERM_10 optional_ssa_use_list TERM_11 optional_successor_list optional_prop_dict optional_region_list optional_attr_dict trailing_type 
| string_literal TERM_10 argument_list_question TERM_11 TERM_10 region TERM_11 attribute_dict_question trailing_type trailing_location_question 
| string_literal TERM_10 optional_ssa_use_list TERM_11 optional_successor_list optional_prop_dict optional_region_list trailing_type ;

region : TERM_14 block_star TERM_15 
| TERM_14 TERM_15 ;

block_star : block block_star 
| optional_block_label operation_list 
| operation operation_plus 
| optional_op_result_list block_39 optional_trailing_loc 
| block_39 optional_trailing_loc 
| optional_op_result_list block_39 
| BARE_ID TERM_6 BARE_ID optional_ssa_use_list trailing_type 
| string_literal TERM_10 optional_ssa_use_list TERM_11 optional_successor_list optional_prop_dict optional_region_list optional_attr_dict trailing_type 
| string_literal TERM_10 argument_list_question TERM_11 TERM_10 region TERM_11 attribute_dict_question trailing_type trailing_location_question 
| string_literal TERM_10 optional_ssa_use_list TERM_11 optional_successor_list optional_prop_dict optional_region_list trailing_type ;

block_42 : TERM_7 region ;

region_list : TERM_10 region_question block_42_star TERM_11 
| TERM_10 region_question TERM_11 ;

block_42_star : block_42 block_42_star 
| TERM_7 region ;

region_question :  
| TERM_14 block_star TERM_15 
| TERM_14 TERM_15 ;

symbol_ref_id_question :  
| TERM_3 block_1 ;

block_43 : TERM_25 attribute_dict ;

block_43_question :  
| TERM_25 attribute_dict ;

argument_list_question :  
| named_argument block_62_star 
| type optional_attr_dict block_63_star 
| ssa_id TERM_18 type optional_attr_dict 
| type optional_attr_dict 
| type block_63_star 
| ssa_id TERM_18 type 
| BARE_ID 
| function_type_list block_34 function_type_list 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 ;

block_44 : TERM_21 function_result_list ;

block_44_question :  
| TERM_21 function_result_list ;

function_body_question :  
| TERM_14 block_star TERM_15 
| TERM_14 TERM_15 ;

symbol_id_list_question :  
| TERM_12 bare_id_question block_55_star TERM_13 
| TERM_12 bare_id_question TERM_13 ;

block_45 : TERM_18 type ;

block_45_question :  
| TERM_18 type ;

block_46 : TERM_18 integer_literal ;

block_46_question :  
| TERM_18 integer_literal ;

ssa_use_list_question :  
| ssa_use block_6_star 
| TERM_1 suffix_id block_0_question 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS ;

property_dict_question :  
| TERM_8 attribute_dict TERM_9 ;

attribute_dict_question :  
| TERM_14 TERM_15 
| TERM_14 attribute_entry block_61_star TERM_15 
| TERM_14 attribute_entry TERM_15 ;

trailing_location_question :  
| TERM_24 TERM_10 location TERM_11 ;

op_result_list_question :  
| op_result block_37_star TERM_20 
| op_result TERM_20 ;

ssa_id_and_type_list_question :  
| ssa_id_and_type block_40_star 
| ssa_id TERM_18 type ;

block_arg_list_question :  
| TERM_10 optional_ssa_and_type_list TERM_11 ;

block_label_question :  
| block_id optional_block_arg_list TERM_18 ;

symbol_use_list_question :  
| TERM_12 ssa_use_list_question TERM_13 ;

successor_list_question :  
| TERM_12 block_id_question block_41_star TERM_13 
| TERM_12 block_id_question TERM_13 ;

region_list_question :  
| TERM_10 region_question block_42_star TERM_11 
| TERM_10 region_question TERM_11 ;

named_argument : ssa_id TERM_18 type optional_attr_dict 
| ssa_id TERM_18 type ;

block_62 : TERM_7 named_argument ;

block_47 : named_argument block_62_star 
| ssa_id TERM_18 type optional_attr_dict 
| ssa_id TERM_18 type ;

block_62_star : block_62 block_62_star 
| TERM_7 named_argument ;

block_63 : TERM_7 type optional_attr_dict 
| TERM_7 type ;

block_49 : type optional_attr_dict block_63_star 
| type optional_attr_dict 
| type block_63_star 
| BARE_ID 
| function_type_list block_34 function_type_list 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 ;

block_63_star : block_63 block_63_star 
| TERM_7 type optional_attr_dict 
| TERM_7 type ;

function_result : type optional_attr_dict 
| BARE_ID 
| function_type_list block_34 function_type_list 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 ;

block_51 : TERM_7 function_result ;

function_result_list_no_parens : function_result block_51_star 
| type optional_attr_dict 
| BARE_ID 
| function_type_list block_34 function_type_list 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 ;

block_51_star : block_51 block_51_star 
| TERM_7 function_result ;

block_52 : TERM_10 TERM_11 ;

block_53 : TERM_10 function_result_list_no_parens TERM_11 ;

generic_module : string_literal TERM_10 argument_list_question TERM_11 TERM_10 region TERM_11 attribute_dict_question trailing_type trailing_location_question ;

block_54 : TERM_7 BARE_ID ;

dim_id_list : TERM_10 bare_id_question block_54_star TERM_11 
| TERM_10 bare_id_question TERM_11 ;

block_54_star : block_54 block_54_star 
| TERM_7 BARE_ID ;

bare_id_question : BARE_ID 
|  ;

block_55 : TERM_7 BARE_ID ;

symbol_id_list : TERM_12 bare_id_question block_55_star TERM_13 
| TERM_12 bare_id_question TERM_13 ;

block_55_star : block_55 block_55_star 
| TERM_7 BARE_ID ;

dim_and_symbol_id_lists : dim_id_list optional_symbol_id_list 
| TERM_10 bare_id_question block_54_star TERM_11 
| TERM_10 bare_id_question TERM_11 ;

symbol_or_const : BARE_ID 
| TERM_1 suffix_id block_0_question 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS ;

dim_use_list : TERM_10 ssa_use_list_question TERM_11 ;

symbol_use_list : TERM_12 ssa_use_list_question TERM_13 ;

dim_and_symbol_use_list : dim_use_list optional_symbol_use_list 
| TERM_10 ssa_use_list_question TERM_11 ;

type_alias_def : type_alias TERM_20 TERM_26 type ;

attribute_alias_def : attribute_alias TERM_20 attribute_value ;

definition_plus : definition definition_plus 
| type_alias TERM_20 TERM_26 type 
| attribute_alias TERM_20 attribute_value ;

generic_module_plus : generic_module generic_module_plus 
| string_literal TERM_10 argument_list_question TERM_11 TERM_10 region TERM_11 attribute_dict_question trailing_type trailing_location_question ;

definition_and_module_list : definition_list module_list 
| definition definition_plus 
| generic_module generic_module_plus 
| string_literal TERM_10 argument_list_question TERM_11 TERM_10 region TERM_11 attribute_dict_question trailing_type trailing_location_question 
| type_alias TERM_20 TERM_26 type 
| attribute_alias TERM_20 attribute_value ;

definition_and_module_list_plus : definition_and_module_list definition_and_module_list_plus 
| definition_list module_list 
| definition definition_plus 
| generic_module generic_module_plus 
| string_literal TERM_10 argument_list_question TERM_11 TERM_10 region TERM_11 attribute_dict_question trailing_type trailing_location_question 
| type_alias TERM_20 TERM_26 type 
| attribute_alias TERM_20 attribute_value ;

posneg_integer_literal : HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS ;

block_1 : DIGITS 
| BARE_ID 
| ESCAPED_STRING ;

ssa_use : TERM_1 suffix_id block_0_question 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS ;

pretty_dialect_item_contents : TERM_10 pretty_dialect_item_contents TERM_11 
| TERM_12 pretty_dialect_item_contents_question block_57_star TERM_13 
| TERM_14 pretty_dialect_item_contents TERM_15 
| pretty_dialect_item_other_content pretty_dialect_item_other_content_plus 
| BARE_ID 
| TERM_16 
| TERM_17 
| TERM_7 
| TERM_18 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| BARE_ID 
| function_type_list block_34 function_type_list 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| DIGITS 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| TERM_12 pretty_dialect_item_contents_question TERM_13 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 ;

block_13 : BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question ;

type : BARE_ID 
| function_type_list block_34 function_type_list 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 ;

type_list_parens : TERM_10 TERM_11 
| TERM_10 type_list_no_parens TERM_11 ;

bool_attribute : TRUE 
| FALSE ;

float_attribute : FLOAT_LITERAL optional_type 
| HEXADECIMAL_LITERAL TERM_18 type 
| FLOAT_LITERAL ;

symbol_ref_attribute : symbol_ref_id block_60_star 
| TERM_3 block_1 ;

standard_attribute : TERM_12 block_18_question TERM_13 
| TERM_14 block_20_question TERM_15 
| posneg_integer_literal optional_type 
| string_literal optional_type 
| TRUE 
| FALSE 
| FLOAT_LITERAL optional_type 
| HEXADECIMAL_LITERAL TERM_18 type 
| symbol_ref_id block_60_star 
| BARE_ID 
| function_type_list block_34 function_type_list 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| FLOAT_LITERAL 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| ESCAPED_STRING 
| TERM_3 block_1 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 ;

attribute_value : TERM_2 block_4 
| term_2_question block_29 block_30_question 
| TERM_12 block_18_question TERM_13 
| TERM_14 block_20_question TERM_15 
| posneg_integer_literal optional_type 
| string_literal optional_type 
| TRUE 
| FALSE 
| FLOAT_LITERAL optional_type 
| HEXADECIMAL_LITERAL TERM_18 type 
| symbol_ref_id block_60_star 
| BARE_ID 
| function_type_list block_34 function_type_list 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| FLOAT_LITERAL 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| ESCAPED_STRING 
| TERM_3 block_1 
| term_2_question block_29 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 
| block_29 block_30_question 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question ;

dialect_attribute_entry : BARE_ID TERM_6 BARE_ID 
| BARE_ID TERM_6 BARE_ID TERM_20 attribute_value 
| string_literal TERM_20 attribute_value ;

block_29 : BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question ;

block_30_question : TERM_18 type ;

attribute_dict : TERM_14 TERM_15 
| TERM_14 attribute_entry block_61_star TERM_15 
| TERM_14 attribute_entry TERM_15 ;

non_function_type_question : BARE_ID 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question ;

trailing_location : TERM_24 TERM_10 location TERM_11 ;

block_39 : BARE_ID TERM_6 BARE_ID optional_ssa_use_list trailing_type 
| string_literal TERM_10 optional_ssa_use_list TERM_11 optional_successor_list optional_prop_dict optional_region_list optional_attr_dict trailing_type 
| string_literal TERM_10 argument_list_question TERM_11 TERM_10 region TERM_11 attribute_dict_question trailing_type trailing_location_question 
| string_literal TERM_10 optional_ssa_use_list TERM_11 optional_successor_list optional_prop_dict optional_region_list trailing_type ;

operation_list : operation operation_plus 
| optional_op_result_list block_39 optional_trailing_loc 
| block_39 optional_trailing_loc 
| optional_op_result_list block_39 
| BARE_ID TERM_6 BARE_ID optional_ssa_use_list trailing_type 
| string_literal TERM_10 optional_ssa_use_list TERM_11 optional_successor_list optional_prop_dict optional_region_list optional_attr_dict trailing_type 
| string_literal TERM_10 argument_list_question TERM_11 TERM_10 region TERM_11 attribute_dict_question trailing_type trailing_location_question 
| string_literal TERM_10 optional_ssa_use_list TERM_11 optional_successor_list optional_prop_dict optional_region_list trailing_type ;

optional_symbol_ref_id :  
| TERM_3 block_1 ;

optional_func_mod_attrs :  
| TERM_25 attribute_dict ;

optional_arg_list :  
| named_argument block_62_star 
| type optional_attr_dict block_63_star 
| ssa_id TERM_18 type optional_attr_dict 
| type optional_attr_dict 
| type block_63_star 
| ssa_id TERM_18 type 
| BARE_ID 
| function_type_list block_34 function_type_list 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 ;

optional_fn_result_list :  
| TERM_21 function_result_list ;

optional_fn_body :  
| TERM_14 block_star TERM_15 
| TERM_14 TERM_15 ;

optional_ssa_use_list :  
| ssa_use block_6_star 
| TERM_1 suffix_id block_0_question 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS ;

optional_prop_dict :  
| TERM_8 attribute_dict TERM_9 ;

optional_ssa_and_type_list :  
| ssa_id_and_type block_40_star 
| ssa_id TERM_18 type ;

optional_block_arg_list :  
| TERM_10 optional_ssa_and_type_list TERM_11 ;

optional_successor_list :  
| TERM_12 block_id_question block_41_star TERM_13 
| TERM_12 block_id_question TERM_13 ;

optional_region_list :  
| TERM_10 region_question block_42_star TERM_11 
| TERM_10 region_question TERM_11 ;

argument_list : named_argument block_62_star 
| type optional_attr_dict block_63_star 
| ssa_id TERM_18 type optional_attr_dict 
| type optional_attr_dict 
| type block_63_star 
| ssa_id TERM_18 type 
| BARE_ID 
| function_type_list block_34 function_type_list 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| function_type_list block_34 
| block_34 function_type_list 
| TERM_21 
| TERM_22 
| TERM_23 ;

function_result_list_parens : TERM_10 TERM_11 
| TERM_10 function_result_list_no_parens TERM_11 ;

function_body : TERM_14 block_star TERM_15 
| TERM_14 TERM_15 ;

definition : type_alias TERM_20 TERM_26 type 
| attribute_alias TERM_20 attribute_value ;

definition_list : definition definition_plus 
| type_alias TERM_20 TERM_26 type 
| attribute_alias TERM_20 attribute_value ;

module_list : generic_module generic_module_plus 
| string_literal TERM_10 argument_list_question TERM_11 TERM_10 region TERM_11 attribute_dict_question trailing_type trailing_location_question ;

mlir_file : definition_and_module_list definition_and_module_list_plus 
| definition_list module_list 
| definition definition_plus 
| generic_module generic_module_plus 
| string_literal TERM_10 argument_list_question TERM_11 TERM_10 region TERM_11 attribute_dict_question trailing_type trailing_location_question 
| type_alias TERM_20 TERM_26 type 
| attribute_alias TERM_20 attribute_value ;

start : definition_and_module_list definition_and_module_list_plus 
| definition_list module_list 
| definition definition_plus 
| generic_module generic_module_plus 
| string_literal TERM_10 argument_list_question TERM_11 TERM_10 region TERM_11 attribute_dict_question trailing_type trailing_location_question 
| type_alias TERM_20 TERM_26 type 
| attribute_alias TERM_20 attribute_value ;

type_attribute : BARE_ID 
| function_type_list block_34 function_type_list 
| TERM_5 block_2 
| term_5_question block_13 
| FLOAT_LITERAL 
| TRUE 
| FALSE 
| ESCAPED_STRING 
| HEXADECIMAL_LITERAL 
| TERM_0 integer_literal 
| DIGITS 
| BARE_ID TERM_8 string_literal TERM_9 
| block_7_question BARE_ID pretty_dialect_item_body_question 
| block_34 function_type_list 
| function_type_list block_34 
| TERM_21 
| TERM_22 
| TERM_23 ;

optional_symbol_id_list : TERM_12 bare_id_question block_55_star TERM_13 
| TERM_12 bare_id_question TERM_13 ;

optional_type : TERM_18 type ;

optional_int_literal : TERM_18 integer_literal ;

optional_op_result_list : op_result block_37_star TERM_20 
| op_result TERM_20 ;

optional_block_label : block_id optional_block_arg_list TERM_18 ;

optional_symbol_use_list : TERM_12 ssa_use_list_question TERM_13 ;

function_result_list : TERM_10 TERM_11 
| TERM_10 function_result_list_no_parens TERM_11 ;

start_rule : definition_and_module_list definition_and_module_list_plus 
| definition_list module_list 
| definition definition_plus 
| generic_module generic_module_plus 
| string_literal TERM_10 argument_list_question TERM_11 TERM_10 region TERM_11 attribute_dict_question trailing_type trailing_location_question 
| type_alias TERM_20 TERM_26 type 
| attribute_alias TERM_20 attribute_value ;

optional_attr_dict : TERM_14 TERM_15 
| TERM_14 attribute_entry block_61_star TERM_15 
| TERM_14 attribute_entry TERM_15 ;

optional_trailing_loc : TERM_24 TERM_10 location TERM_11 ;

