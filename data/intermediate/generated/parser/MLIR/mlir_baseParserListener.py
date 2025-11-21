# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/MLIR/mlir_baseParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .mlir_baseParser import mlir_baseParser
else:
    from mlir_baseParser import mlir_baseParser

# This class defines a complete listener for a parse tree produced by mlir_baseParser.
class mlir_baseParserListener(ParseTreeListener):

    # Enter a parse tree produced by mlir_baseParser#start.
    def enterStart(self, ctx:mlir_baseParser.StartContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#start.
    def exitStart(self, ctx:mlir_baseParser.StartContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#bool_literal.
    def enterBool_literal(self, ctx:mlir_baseParser.Bool_literalContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#bool_literal.
    def exitBool_literal(self, ctx:mlir_baseParser.Bool_literalContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#decimal_literal.
    def enterDecimal_literal(self, ctx:mlir_baseParser.Decimal_literalContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#decimal_literal.
    def exitDecimal_literal(self, ctx:mlir_baseParser.Decimal_literalContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#integer_literal.
    def enterInteger_literal(self, ctx:mlir_baseParser.Integer_literalContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#integer_literal.
    def exitInteger_literal(self, ctx:mlir_baseParser.Integer_literalContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#negated_integer_literal.
    def enterNegated_integer_literal(self, ctx:mlir_baseParser.Negated_integer_literalContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#negated_integer_literal.
    def exitNegated_integer_literal(self, ctx:mlir_baseParser.Negated_integer_literalContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#posneg_integer_literal.
    def enterPosneg_integer_literal(self, ctx:mlir_baseParser.Posneg_integer_literalContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#posneg_integer_literal.
    def exitPosneg_integer_literal(self, ctx:mlir_baseParser.Posneg_integer_literalContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#string_literal.
    def enterString_literal(self, ctx:mlir_baseParser.String_literalContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#string_literal.
    def exitString_literal(self, ctx:mlir_baseParser.String_literalContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#constant_literal.
    def enterConstant_literal(self, ctx:mlir_baseParser.Constant_literalContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#constant_literal.
    def exitConstant_literal(self, ctx:mlir_baseParser.Constant_literalContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#suffix_id.
    def enterSuffix_id(self, ctx:mlir_baseParser.Suffix_idContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#suffix_id.
    def exitSuffix_id(self, ctx:mlir_baseParser.Suffix_idContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#ssa_id.
    def enterSsa_id(self, ctx:mlir_baseParser.Ssa_idContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#ssa_id.
    def exitSsa_id(self, ctx:mlir_baseParser.Ssa_idContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#symbol_ref_id.
    def enterSymbol_ref_id(self, ctx:mlir_baseParser.Symbol_ref_idContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#symbol_ref_id.
    def exitSymbol_ref_id(self, ctx:mlir_baseParser.Symbol_ref_idContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#block_id.
    def enterBlock_id(self, ctx:mlir_baseParser.Block_idContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#block_id.
    def exitBlock_id(self, ctx:mlir_baseParser.Block_idContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#type_alias.
    def enterType_alias(self, ctx:mlir_baseParser.Type_aliasContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#type_alias.
    def exitType_alias(self, ctx:mlir_baseParser.Type_aliasContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#map_or_set_id.
    def enterMap_or_set_id(self, ctx:mlir_baseParser.Map_or_set_idContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#map_or_set_id.
    def exitMap_or_set_id(self, ctx:mlir_baseParser.Map_or_set_idContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#attribute_alias.
    def enterAttribute_alias(self, ctx:mlir_baseParser.Attribute_aliasContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#attribute_alias.
    def exitAttribute_alias(self, ctx:mlir_baseParser.Attribute_aliasContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#ssa_id_list.
    def enterSsa_id_list(self, ctx:mlir_baseParser.Ssa_id_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#ssa_id_list.
    def exitSsa_id_list(self, ctx:mlir_baseParser.Ssa_id_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#ssa_use.
    def enterSsa_use(self, ctx:mlir_baseParser.Ssa_useContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#ssa_use.
    def exitSsa_use(self, ctx:mlir_baseParser.Ssa_useContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#ssa_use_list.
    def enterSsa_use_list(self, ctx:mlir_baseParser.Ssa_use_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#ssa_use_list.
    def exitSsa_use_list(self, ctx:mlir_baseParser.Ssa_use_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#opaque_dialect_item.
    def enterOpaque_dialect_item(self, ctx:mlir_baseParser.Opaque_dialect_itemContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#opaque_dialect_item.
    def exitOpaque_dialect_item(self, ctx:mlir_baseParser.Opaque_dialect_itemContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#pretty_dialect_item.
    def enterPretty_dialect_item(self, ctx:mlir_baseParser.Pretty_dialect_itemContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#pretty_dialect_item.
    def exitPretty_dialect_item(self, ctx:mlir_baseParser.Pretty_dialect_itemContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#pretty_dialect_item_body.
    def enterPretty_dialect_item_body(self, ctx:mlir_baseParser.Pretty_dialect_item_bodyContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#pretty_dialect_item_body.
    def exitPretty_dialect_item_body(self, ctx:mlir_baseParser.Pretty_dialect_item_bodyContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#pretty_dialect_item_contents.
    def enterPretty_dialect_item_contents(self, ctx:mlir_baseParser.Pretty_dialect_item_contentsContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#pretty_dialect_item_contents.
    def exitPretty_dialect_item_contents(self, ctx:mlir_baseParser.Pretty_dialect_item_contentsContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#pretty_dialect_item_other_content.
    def enterPretty_dialect_item_other_content(self, ctx:mlir_baseParser.Pretty_dialect_item_other_contentContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#pretty_dialect_item_other_content.
    def exitPretty_dialect_item_other_content(self, ctx:mlir_baseParser.Pretty_dialect_item_other_contentContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#dialect_type.
    def enterDialect_type(self, ctx:mlir_baseParser.Dialect_typeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#dialect_type.
    def exitDialect_type(self, ctx:mlir_baseParser.Dialect_typeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#non_function_type.
    def enterNon_function_type(self, ctx:mlir_baseParser.Non_function_typeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#non_function_type.
    def exitNon_function_type(self, ctx:mlir_baseParser.Non_function_typeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#type.
    def enterType(self, ctx:mlir_baseParser.TypeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#type.
    def exitType(self, ctx:mlir_baseParser.TypeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#type_list_no_parens.
    def enterType_list_no_parens(self, ctx:mlir_baseParser.Type_list_no_parensContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#type_list_no_parens.
    def exitType_list_no_parens(self, ctx:mlir_baseParser.Type_list_no_parensContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#type_list_parens.
    def enterType_list_parens(self, ctx:mlir_baseParser.Type_list_parensContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#type_list_parens.
    def exitType_list_parens(self, ctx:mlir_baseParser.Type_list_parensContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#ssa_use_and_type.
    def enterSsa_use_and_type(self, ctx:mlir_baseParser.Ssa_use_and_typeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#ssa_use_and_type.
    def exitSsa_use_and_type(self, ctx:mlir_baseParser.Ssa_use_and_typeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#ssa_use_and_type_list.
    def enterSsa_use_and_type_list(self, ctx:mlir_baseParser.Ssa_use_and_type_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#ssa_use_and_type_list.
    def exitSsa_use_and_type_list(self, ctx:mlir_baseParser.Ssa_use_and_type_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#array_attribute.
    def enterArray_attribute(self, ctx:mlir_baseParser.Array_attributeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#array_attribute.
    def exitArray_attribute(self, ctx:mlir_baseParser.Array_attributeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#bool_attribute.
    def enterBool_attribute(self, ctx:mlir_baseParser.Bool_attributeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#bool_attribute.
    def exitBool_attribute(self, ctx:mlir_baseParser.Bool_attributeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#dictionary_attribute.
    def enterDictionary_attribute(self, ctx:mlir_baseParser.Dictionary_attributeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#dictionary_attribute.
    def exitDictionary_attribute(self, ctx:mlir_baseParser.Dictionary_attributeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#float_attribute.
    def enterFloat_attribute(self, ctx:mlir_baseParser.Float_attributeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#float_attribute.
    def exitFloat_attribute(self, ctx:mlir_baseParser.Float_attributeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#integer_attribute.
    def enterInteger_attribute(self, ctx:mlir_baseParser.Integer_attributeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#integer_attribute.
    def exitInteger_attribute(self, ctx:mlir_baseParser.Integer_attributeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#string_attribute.
    def enterString_attribute(self, ctx:mlir_baseParser.String_attributeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#string_attribute.
    def exitString_attribute(self, ctx:mlir_baseParser.String_attributeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#symbol_ref_attribute.
    def enterSymbol_ref_attribute(self, ctx:mlir_baseParser.Symbol_ref_attributeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#symbol_ref_attribute.
    def exitSymbol_ref_attribute(self, ctx:mlir_baseParser.Symbol_ref_attributeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#type_attribute.
    def enterType_attribute(self, ctx:mlir_baseParser.Type_attributeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#type_attribute.
    def exitType_attribute(self, ctx:mlir_baseParser.Type_attributeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#standard_attribute.
    def enterStandard_attribute(self, ctx:mlir_baseParser.Standard_attributeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#standard_attribute.
    def exitStandard_attribute(self, ctx:mlir_baseParser.Standard_attributeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#attribute_value.
    def enterAttribute_value(self, ctx:mlir_baseParser.Attribute_valueContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#attribute_value.
    def exitAttribute_value(self, ctx:mlir_baseParser.Attribute_valueContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#dependent_attribute_entry.
    def enterDependent_attribute_entry(self, ctx:mlir_baseParser.Dependent_attribute_entryContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#dependent_attribute_entry.
    def exitDependent_attribute_entry(self, ctx:mlir_baseParser.Dependent_attribute_entryContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#dialect_attribute_entry.
    def enterDialect_attribute_entry(self, ctx:mlir_baseParser.Dialect_attribute_entryContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#dialect_attribute_entry.
    def exitDialect_attribute_entry(self, ctx:mlir_baseParser.Dialect_attribute_entryContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#dialect_attribute.
    def enterDialect_attribute(self, ctx:mlir_baseParser.Dialect_attributeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#dialect_attribute.
    def exitDialect_attribute(self, ctx:mlir_baseParser.Dialect_attributeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#property_dict.
    def enterProperty_dict(self, ctx:mlir_baseParser.Property_dictContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#property_dict.
    def exitProperty_dict(self, ctx:mlir_baseParser.Property_dictContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#attribute_entry.
    def enterAttribute_entry(self, ctx:mlir_baseParser.Attribute_entryContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#attribute_entry.
    def exitAttribute_entry(self, ctx:mlir_baseParser.Attribute_entryContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#attribute_dict.
    def enterAttribute_dict(self, ctx:mlir_baseParser.Attribute_dictContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#attribute_dict.
    def exitAttribute_dict(self, ctx:mlir_baseParser.Attribute_dictContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#trailing_type.
    def enterTrailing_type(self, ctx:mlir_baseParser.Trailing_typeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#trailing_type.
    def exitTrailing_type(self, ctx:mlir_baseParser.Trailing_typeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#function_type.
    def enterFunction_type(self, ctx:mlir_baseParser.Function_typeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#function_type.
    def exitFunction_type(self, ctx:mlir_baseParser.Function_typeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#function_type_list.
    def enterFunction_type_list(self, ctx:mlir_baseParser.Function_type_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#function_type_list.
    def exitFunction_type_list(self, ctx:mlir_baseParser.Function_type_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#op_result.
    def enterOp_result(self, ctx:mlir_baseParser.Op_resultContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#op_result.
    def exitOp_result(self, ctx:mlir_baseParser.Op_resultContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#op_result_list.
    def enterOp_result_list(self, ctx:mlir_baseParser.Op_result_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#op_result_list.
    def exitOp_result_list(self, ctx:mlir_baseParser.Op_result_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#location.
    def enterLocation(self, ctx:mlir_baseParser.LocationContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#location.
    def exitLocation(self, ctx:mlir_baseParser.LocationContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#trailing_location.
    def enterTrailing_location(self, ctx:mlir_baseParser.Trailing_locationContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#trailing_location.
    def exitTrailing_location(self, ctx:mlir_baseParser.Trailing_locationContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#generic_operation.
    def enterGeneric_operation(self, ctx:mlir_baseParser.Generic_operationContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#generic_operation.
    def exitGeneric_operation(self, ctx:mlir_baseParser.Generic_operationContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#custom_operation.
    def enterCustom_operation(self, ctx:mlir_baseParser.Custom_operationContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#custom_operation.
    def exitCustom_operation(self, ctx:mlir_baseParser.Custom_operationContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#operation.
    def enterOperation(self, ctx:mlir_baseParser.OperationContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#operation.
    def exitOperation(self, ctx:mlir_baseParser.OperationContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#ssa_id_and_type.
    def enterSsa_id_and_type(self, ctx:mlir_baseParser.Ssa_id_and_typeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#ssa_id_and_type.
    def exitSsa_id_and_type(self, ctx:mlir_baseParser.Ssa_id_and_typeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#ssa_id_and_type_list.
    def enterSsa_id_and_type_list(self, ctx:mlir_baseParser.Ssa_id_and_type_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#ssa_id_and_type_list.
    def exitSsa_id_and_type_list(self, ctx:mlir_baseParser.Ssa_id_and_type_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#block_arg_list.
    def enterBlock_arg_list(self, ctx:mlir_baseParser.Block_arg_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#block_arg_list.
    def exitBlock_arg_list(self, ctx:mlir_baseParser.Block_arg_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#operation_list.
    def enterOperation_list(self, ctx:mlir_baseParser.Operation_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#operation_list.
    def exitOperation_list(self, ctx:mlir_baseParser.Operation_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#block_label.
    def enterBlock_label(self, ctx:mlir_baseParser.Block_labelContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#block_label.
    def exitBlock_label(self, ctx:mlir_baseParser.Block_labelContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#successor_list.
    def enterSuccessor_list(self, ctx:mlir_baseParser.Successor_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#successor_list.
    def exitSuccessor_list(self, ctx:mlir_baseParser.Successor_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#block.
    def enterBlock(self, ctx:mlir_baseParser.BlockContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#block.
    def exitBlock(self, ctx:mlir_baseParser.BlockContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#region.
    def enterRegion(self, ctx:mlir_baseParser.RegionContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#region.
    def exitRegion(self, ctx:mlir_baseParser.RegionContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#region_list.
    def enterRegion_list(self, ctx:mlir_baseParser.Region_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#region_list.
    def exitRegion_list(self, ctx:mlir_baseParser.Region_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_symbol_ref_id.
    def enterOptional_symbol_ref_id(self, ctx:mlir_baseParser.Optional_symbol_ref_idContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_symbol_ref_id.
    def exitOptional_symbol_ref_id(self, ctx:mlir_baseParser.Optional_symbol_ref_idContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_func_mod_attrs.
    def enterOptional_func_mod_attrs(self, ctx:mlir_baseParser.Optional_func_mod_attrsContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_func_mod_attrs.
    def exitOptional_func_mod_attrs(self, ctx:mlir_baseParser.Optional_func_mod_attrsContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_arg_list.
    def enterOptional_arg_list(self, ctx:mlir_baseParser.Optional_arg_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_arg_list.
    def exitOptional_arg_list(self, ctx:mlir_baseParser.Optional_arg_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_fn_result_list.
    def enterOptional_fn_result_list(self, ctx:mlir_baseParser.Optional_fn_result_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_fn_result_list.
    def exitOptional_fn_result_list(self, ctx:mlir_baseParser.Optional_fn_result_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_fn_body.
    def enterOptional_fn_body(self, ctx:mlir_baseParser.Optional_fn_bodyContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_fn_body.
    def exitOptional_fn_body(self, ctx:mlir_baseParser.Optional_fn_bodyContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_symbol_id_list.
    def enterOptional_symbol_id_list(self, ctx:mlir_baseParser.Optional_symbol_id_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_symbol_id_list.
    def exitOptional_symbol_id_list(self, ctx:mlir_baseParser.Optional_symbol_id_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_type.
    def enterOptional_type(self, ctx:mlir_baseParser.Optional_typeContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_type.
    def exitOptional_type(self, ctx:mlir_baseParser.Optional_typeContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_int_literal.
    def enterOptional_int_literal(self, ctx:mlir_baseParser.Optional_int_literalContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_int_literal.
    def exitOptional_int_literal(self, ctx:mlir_baseParser.Optional_int_literalContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_ssa_use_list.
    def enterOptional_ssa_use_list(self, ctx:mlir_baseParser.Optional_ssa_use_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_ssa_use_list.
    def exitOptional_ssa_use_list(self, ctx:mlir_baseParser.Optional_ssa_use_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_prop_dict.
    def enterOptional_prop_dict(self, ctx:mlir_baseParser.Optional_prop_dictContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_prop_dict.
    def exitOptional_prop_dict(self, ctx:mlir_baseParser.Optional_prop_dictContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_attr_dict.
    def enterOptional_attr_dict(self, ctx:mlir_baseParser.Optional_attr_dictContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_attr_dict.
    def exitOptional_attr_dict(self, ctx:mlir_baseParser.Optional_attr_dictContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_trailing_loc.
    def enterOptional_trailing_loc(self, ctx:mlir_baseParser.Optional_trailing_locContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_trailing_loc.
    def exitOptional_trailing_loc(self, ctx:mlir_baseParser.Optional_trailing_locContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_op_result_list.
    def enterOptional_op_result_list(self, ctx:mlir_baseParser.Optional_op_result_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_op_result_list.
    def exitOptional_op_result_list(self, ctx:mlir_baseParser.Optional_op_result_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_ssa_and_type_list.
    def enterOptional_ssa_and_type_list(self, ctx:mlir_baseParser.Optional_ssa_and_type_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_ssa_and_type_list.
    def exitOptional_ssa_and_type_list(self, ctx:mlir_baseParser.Optional_ssa_and_type_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_block_arg_list.
    def enterOptional_block_arg_list(self, ctx:mlir_baseParser.Optional_block_arg_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_block_arg_list.
    def exitOptional_block_arg_list(self, ctx:mlir_baseParser.Optional_block_arg_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_block_label.
    def enterOptional_block_label(self, ctx:mlir_baseParser.Optional_block_labelContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_block_label.
    def exitOptional_block_label(self, ctx:mlir_baseParser.Optional_block_labelContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_symbol_use_list.
    def enterOptional_symbol_use_list(self, ctx:mlir_baseParser.Optional_symbol_use_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_symbol_use_list.
    def exitOptional_symbol_use_list(self, ctx:mlir_baseParser.Optional_symbol_use_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_successor_list.
    def enterOptional_successor_list(self, ctx:mlir_baseParser.Optional_successor_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_successor_list.
    def exitOptional_successor_list(self, ctx:mlir_baseParser.Optional_successor_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#optional_region_list.
    def enterOptional_region_list(self, ctx:mlir_baseParser.Optional_region_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#optional_region_list.
    def exitOptional_region_list(self, ctx:mlir_baseParser.Optional_region_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#named_argument.
    def enterNamed_argument(self, ctx:mlir_baseParser.Named_argumentContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#named_argument.
    def exitNamed_argument(self, ctx:mlir_baseParser.Named_argumentContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#argument_list.
    def enterArgument_list(self, ctx:mlir_baseParser.Argument_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#argument_list.
    def exitArgument_list(self, ctx:mlir_baseParser.Argument_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#function_result.
    def enterFunction_result(self, ctx:mlir_baseParser.Function_resultContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#function_result.
    def exitFunction_result(self, ctx:mlir_baseParser.Function_resultContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#function_result_list_no_parens.
    def enterFunction_result_list_no_parens(self, ctx:mlir_baseParser.Function_result_list_no_parensContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#function_result_list_no_parens.
    def exitFunction_result_list_no_parens(self, ctx:mlir_baseParser.Function_result_list_no_parensContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#function_result_list_parens.
    def enterFunction_result_list_parens(self, ctx:mlir_baseParser.Function_result_list_parensContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#function_result_list_parens.
    def exitFunction_result_list_parens(self, ctx:mlir_baseParser.Function_result_list_parensContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#function_result_list.
    def enterFunction_result_list(self, ctx:mlir_baseParser.Function_result_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#function_result_list.
    def exitFunction_result_list(self, ctx:mlir_baseParser.Function_result_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#function_body.
    def enterFunction_body(self, ctx:mlir_baseParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#function_body.
    def exitFunction_body(self, ctx:mlir_baseParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#generic_module.
    def enterGeneric_module(self, ctx:mlir_baseParser.Generic_moduleContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#generic_module.
    def exitGeneric_module(self, ctx:mlir_baseParser.Generic_moduleContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#dim_id_list.
    def enterDim_id_list(self, ctx:mlir_baseParser.Dim_id_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#dim_id_list.
    def exitDim_id_list(self, ctx:mlir_baseParser.Dim_id_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#symbol_id_list.
    def enterSymbol_id_list(self, ctx:mlir_baseParser.Symbol_id_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#symbol_id_list.
    def exitSymbol_id_list(self, ctx:mlir_baseParser.Symbol_id_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#dim_and_symbol_id_lists.
    def enterDim_and_symbol_id_lists(self, ctx:mlir_baseParser.Dim_and_symbol_id_listsContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#dim_and_symbol_id_lists.
    def exitDim_and_symbol_id_lists(self, ctx:mlir_baseParser.Dim_and_symbol_id_listsContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#symbol_or_const.
    def enterSymbol_or_const(self, ctx:mlir_baseParser.Symbol_or_constContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#symbol_or_const.
    def exitSymbol_or_const(self, ctx:mlir_baseParser.Symbol_or_constContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#dim_use_list.
    def enterDim_use_list(self, ctx:mlir_baseParser.Dim_use_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#dim_use_list.
    def exitDim_use_list(self, ctx:mlir_baseParser.Dim_use_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#symbol_use_list.
    def enterSymbol_use_list(self, ctx:mlir_baseParser.Symbol_use_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#symbol_use_list.
    def exitSymbol_use_list(self, ctx:mlir_baseParser.Symbol_use_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#dim_and_symbol_use_list.
    def enterDim_and_symbol_use_list(self, ctx:mlir_baseParser.Dim_and_symbol_use_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#dim_and_symbol_use_list.
    def exitDim_and_symbol_use_list(self, ctx:mlir_baseParser.Dim_and_symbol_use_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#type_alias_def.
    def enterType_alias_def(self, ctx:mlir_baseParser.Type_alias_defContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#type_alias_def.
    def exitType_alias_def(self, ctx:mlir_baseParser.Type_alias_defContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#attribute_alias_def.
    def enterAttribute_alias_def(self, ctx:mlir_baseParser.Attribute_alias_defContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#attribute_alias_def.
    def exitAttribute_alias_def(self, ctx:mlir_baseParser.Attribute_alias_defContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#definition.
    def enterDefinition(self, ctx:mlir_baseParser.DefinitionContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#definition.
    def exitDefinition(self, ctx:mlir_baseParser.DefinitionContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#definition_list.
    def enterDefinition_list(self, ctx:mlir_baseParser.Definition_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#definition_list.
    def exitDefinition_list(self, ctx:mlir_baseParser.Definition_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#module_list.
    def enterModule_list(self, ctx:mlir_baseParser.Module_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#module_list.
    def exitModule_list(self, ctx:mlir_baseParser.Module_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#definition_and_module_list.
    def enterDefinition_and_module_list(self, ctx:mlir_baseParser.Definition_and_module_listContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#definition_and_module_list.
    def exitDefinition_and_module_list(self, ctx:mlir_baseParser.Definition_and_module_listContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#mlir_file.
    def enterMlir_file(self, ctx:mlir_baseParser.Mlir_fileContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#mlir_file.
    def exitMlir_file(self, ctx:mlir_baseParser.Mlir_fileContext):
        pass


    # Enter a parse tree produced by mlir_baseParser#start_rule.
    def enterStart_rule(self, ctx:mlir_baseParser.Start_ruleContext):
        pass

    # Exit a parse tree produced by mlir_baseParser#start_rule.
    def exitStart_rule(self, ctx:mlir_baseParser.Start_ruleContext):
        pass



del mlir_baseParser