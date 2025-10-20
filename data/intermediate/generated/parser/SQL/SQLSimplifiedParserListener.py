# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/SQL/SQLSimplifiedParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SQLSimplifiedParser import SQLSimplifiedParser
else:
    from SQLSimplifiedParser import SQLSimplifiedParser

# This class defines a complete listener for a parse tree produced by SQLSimplifiedParser.
class SQLSimplifiedParserListener(ParseTreeListener):

    # Enter a parse tree produced by SQLSimplifiedParser#start.
    def enterStart(self, ctx:SQLSimplifiedParser.StartContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#start.
    def exitStart(self, ctx:SQLSimplifiedParser.StartContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#select_statement.
    def enterSelect_statement(self, ctx:SQLSimplifiedParser.Select_statementContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#select_statement.
    def exitSelect_statement(self, ctx:SQLSimplifiedParser.Select_statementContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#union_list.
    def enterUnion_list(self, ctx:SQLSimplifiedParser.Union_listContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#union_list.
    def exitUnion_list(self, ctx:SQLSimplifiedParser.Union_listContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#c_expr.
    def enterC_expr(self, ctx:SQLSimplifiedParser.C_exprContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#c_expr.
    def exitC_expr(self, ctx:SQLSimplifiedParser.C_exprContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#f_expr.
    def enterF_expr(self, ctx:SQLSimplifiedParser.F_exprContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#f_expr.
    def exitF_expr(self, ctx:SQLSimplifiedParser.F_exprContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#integral_or_null.
    def enterIntegral_or_null(self, ctx:SQLSimplifiedParser.Integral_or_nullContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#integral_or_null.
    def exitIntegral_or_null(self, ctx:SQLSimplifiedParser.Integral_or_nullContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#binary_op_fexpr_list.
    def enterBinary_op_fexpr_list(self, ctx:SQLSimplifiedParser.Binary_op_fexpr_listContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#binary_op_fexpr_list.
    def exitBinary_op_fexpr_list(self, ctx:SQLSimplifiedParser.Binary_op_fexpr_listContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#string_list.
    def enterString_list(self, ctx:SQLSimplifiedParser.String_listContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#string_list.
    def exitString_list(self, ctx:SQLSimplifiedParser.String_listContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#integral_list.
    def enterIntegral_list(self, ctx:SQLSimplifiedParser.Integral_listContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#integral_list.
    def exitIntegral_list(self, ctx:SQLSimplifiedParser.Integral_listContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#binary_op_columnref_list.
    def enterBinary_op_columnref_list(self, ctx:SQLSimplifiedParser.Binary_op_columnref_listContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#binary_op_columnref_list.
    def exitBinary_op_columnref_list(self, ctx:SQLSimplifiedParser.Binary_op_columnref_listContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#where_clause.
    def enterWhere_clause(self, ctx:SQLSimplifiedParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#where_clause.
    def exitWhere_clause(self, ctx:SQLSimplifiedParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#join_clause.
    def enterJoin_clause(self, ctx:SQLSimplifiedParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#join_clause.
    def exitJoin_clause(self, ctx:SQLSimplifiedParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#on_clause.
    def enterOn_clause(self, ctx:SQLSimplifiedParser.On_clauseContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#on_clause.
    def exitOn_clause(self, ctx:SQLSimplifiedParser.On_clauseContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#group_clause.
    def enterGroup_clause(self, ctx:SQLSimplifiedParser.Group_clauseContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#group_clause.
    def exitGroup_clause(self, ctx:SQLSimplifiedParser.Group_clauseContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#group_by_list.
    def enterGroup_by_list(self, ctx:SQLSimplifiedParser.Group_by_listContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#group_by_list.
    def exitGroup_by_list(self, ctx:SQLSimplifiedParser.Group_by_listContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#having_clause.
    def enterHaving_clause(self, ctx:SQLSimplifiedParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#having_clause.
    def exitHaving_clause(self, ctx:SQLSimplifiedParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#sort_clause.
    def enterSort_clause(self, ctx:SQLSimplifiedParser.Sort_clauseContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#sort_clause.
    def exitSort_clause(self, ctx:SQLSimplifiedParser.Sort_clauseContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#column_list_or_star.
    def enterColumn_list_or_star(self, ctx:SQLSimplifiedParser.Column_list_or_starContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#column_list_or_star.
    def exitColumn_list_or_star(self, ctx:SQLSimplifiedParser.Column_list_or_starContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#column_list.
    def enterColumn_list(self, ctx:SQLSimplifiedParser.Column_listContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#column_list.
    def exitColumn_list(self, ctx:SQLSimplifiedParser.Column_listContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#sortby_list.
    def enterSortby_list(self, ctx:SQLSimplifiedParser.Sortby_listContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#sortby_list.
    def exitSortby_list(self, ctx:SQLSimplifiedParser.Sortby_listContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#from_list.
    def enterFrom_list(self, ctx:SQLSimplifiedParser.From_listContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#from_list.
    def exitFrom_list(self, ctx:SQLSimplifiedParser.From_listContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#from_clause.
    def enterFrom_clause(self, ctx:SQLSimplifiedParser.From_clauseContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#from_clause.
    def exitFrom_clause(self, ctx:SQLSimplifiedParser.From_clauseContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#sortby.
    def enterSortby(self, ctx:SQLSimplifiedParser.SortbyContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#sortby.
    def exitSortby(self, ctx:SQLSimplifiedParser.SortbyContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#columnref.
    def enterColumnref(self, ctx:SQLSimplifiedParser.ColumnrefContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#columnref.
    def exitColumnref(self, ctx:SQLSimplifiedParser.ColumnrefContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#table_ref.
    def enterTable_ref(self, ctx:SQLSimplifiedParser.Table_refContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#table_ref.
    def exitTable_ref(self, ctx:SQLSimplifiedParser.Table_refContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#typeidentifier.
    def enterTypeidentifier(self, ctx:SQLSimplifiedParser.TypeidentifierContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#typeidentifier.
    def exitTypeidentifier(self, ctx:SQLSimplifiedParser.TypeidentifierContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#binary_op.
    def enterBinary_op(self, ctx:SQLSimplifiedParser.Binary_opContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#binary_op.
    def exitBinary_op(self, ctx:SQLSimplifiedParser.Binary_opContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#math_op.
    def enterMath_op(self, ctx:SQLSimplifiedParser.Math_opContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#math_op.
    def exitMath_op(self, ctx:SQLSimplifiedParser.Math_opContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#logic_op.
    def enterLogic_op(self, ctx:SQLSimplifiedParser.Logic_opContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#logic_op.
    def exitLogic_op(self, ctx:SQLSimplifiedParser.Logic_opContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#unary_op.
    def enterUnary_op(self, ctx:SQLSimplifiedParser.Unary_opContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#unary_op.
    def exitUnary_op(self, ctx:SQLSimplifiedParser.Unary_opContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#identifier_or_star.
    def enterIdentifier_or_star(self, ctx:SQLSimplifiedParser.Identifier_or_starContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#identifier_or_star.
    def exitIdentifier_or_star(self, ctx:SQLSimplifiedParser.Identifier_or_starContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#gt_lt.
    def enterGt_lt(self, ctx:SQLSimplifiedParser.Gt_ltContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#gt_lt.
    def exitGt_lt(self, ctx:SQLSimplifiedParser.Gt_ltContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#asc_desc.
    def enterAsc_desc(self, ctx:SQLSimplifiedParser.Asc_descContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#asc_desc.
    def exitAsc_desc(self, ctx:SQLSimplifiedParser.Asc_descContext):
        pass


    # Enter a parse tree produced by SQLSimplifiedParser#collabel.
    def enterCollabel(self, ctx:SQLSimplifiedParser.CollabelContext):
        pass

    # Exit a parse tree produced by SQLSimplifiedParser#collabel.
    def exitCollabel(self, ctx:SQLSimplifiedParser.CollabelContext):
        pass



del SQLSimplifiedParser