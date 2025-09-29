# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/JANUS/janusParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .janusParser import janusParser
else:
    from janusParser import janusParser

# This class defines a complete listener for a parse tree produced by janusParser.
class janusParserListener(ParseTreeListener):

    # Enter a parse tree produced by janusParser#program.
    def enterProgram(self, ctx:janusParser.ProgramContext):
        pass

    # Exit a parse tree produced by janusParser#program.
    def exitProgram(self, ctx:janusParser.ProgramContext):
        pass


    # Enter a parse tree produced by janusParser#statements.
    def enterStatements(self, ctx:janusParser.StatementsContext):
        pass

    # Exit a parse tree produced by janusParser#statements.
    def exitStatements(self, ctx:janusParser.StatementsContext):
        pass


    # Enter a parse tree produced by janusParser#statement.
    def enterStatement(self, ctx:janusParser.StatementContext):
        pass

    # Exit a parse tree produced by janusParser#statement.
    def exitStatement(self, ctx:janusParser.StatementContext):
        pass


    # Enter a parse tree produced by janusParser#ifstmt.
    def enterIfstmt(self, ctx:janusParser.IfstmtContext):
        pass

    # Exit a parse tree produced by janusParser#ifstmt.
    def exitIfstmt(self, ctx:janusParser.IfstmtContext):
        pass


    # Enter a parse tree produced by janusParser#dostmt.
    def enterDostmt(self, ctx:janusParser.DostmtContext):
        pass

    # Exit a parse tree produced by janusParser#dostmt.
    def exitDostmt(self, ctx:janusParser.DostmtContext):
        pass


    # Enter a parse tree produced by janusParser#callstmt.
    def enterCallstmt(self, ctx:janusParser.CallstmtContext):
        pass

    # Exit a parse tree produced by janusParser#callstmt.
    def exitCallstmt(self, ctx:janusParser.CallstmtContext):
        pass


    # Enter a parse tree produced by janusParser#readstmt.
    def enterReadstmt(self, ctx:janusParser.ReadstmtContext):
        pass

    # Exit a parse tree produced by janusParser#readstmt.
    def exitReadstmt(self, ctx:janusParser.ReadstmtContext):
        pass


    # Enter a parse tree produced by janusParser#writestmt.
    def enterWritestmt(self, ctx:janusParser.WritestmtContext):
        pass

    # Exit a parse tree produced by janusParser#writestmt.
    def exitWritestmt(self, ctx:janusParser.WritestmtContext):
        pass


    # Enter a parse tree produced by janusParser#lvalstmt.
    def enterLvalstmt(self, ctx:janusParser.LvalstmtContext):
        pass

    # Exit a parse tree produced by janusParser#lvalstmt.
    def exitLvalstmt(self, ctx:janusParser.LvalstmtContext):
        pass


    # Enter a parse tree produced by janusParser#modstmt.
    def enterModstmt(self, ctx:janusParser.ModstmtContext):
        pass

    # Exit a parse tree produced by janusParser#modstmt.
    def exitModstmt(self, ctx:janusParser.ModstmtContext):
        pass


    # Enter a parse tree produced by janusParser#swapstmt.
    def enterSwapstmt(self, ctx:janusParser.SwapstmtContext):
        pass

    # Exit a parse tree produced by janusParser#swapstmt.
    def exitSwapstmt(self, ctx:janusParser.SwapstmtContext):
        pass


    # Enter a parse tree produced by janusParser#expression.
    def enterExpression(self, ctx:janusParser.ExpressionContext):
        pass

    # Exit a parse tree produced by janusParser#expression.
    def exitExpression(self, ctx:janusParser.ExpressionContext):
        pass


    # Enter a parse tree produced by janusParser#minexp.
    def enterMinexp(self, ctx:janusParser.MinexpContext):
        pass

    # Exit a parse tree produced by janusParser#minexp.
    def exitMinexp(self, ctx:janusParser.MinexpContext):
        pass


    # Enter a parse tree produced by janusParser#lvalue.
    def enterLvalue(self, ctx:janusParser.LvalueContext):
        pass

    # Exit a parse tree produced by janusParser#lvalue.
    def exitLvalue(self, ctx:janusParser.LvalueContext):
        pass


    # Enter a parse tree produced by janusParser#constant.
    def enterConstant(self, ctx:janusParser.ConstantContext):
        pass

    # Exit a parse tree produced by janusParser#constant.
    def exitConstant(self, ctx:janusParser.ConstantContext):
        pass



del janusParser