# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/C/CParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete listener for a parse tree produced by CParser.
class CParserListener(ParseTreeListener):

    # Enter a parse tree produced by CParser#start.
    def enterStart(self, ctx:CParser.StartContext):
        pass

    # Exit a parse tree produced by CParser#start.
    def exitStart(self, ctx:CParser.StartContext):
        pass


    # Enter a parse tree produced by CParser#statement.
    def enterStatement(self, ctx:CParser.StatementContext):
        pass

    # Exit a parse tree produced by CParser#statement.
    def exitStatement(self, ctx:CParser.StatementContext):
        pass


    # Enter a parse tree produced by CParser#block.
    def enterBlock(self, ctx:CParser.BlockContext):
        pass

    # Exit a parse tree produced by CParser#block.
    def exitBlock(self, ctx:CParser.BlockContext):
        pass


    # Enter a parse tree produced by CParser#declaration.
    def enterDeclaration(self, ctx:CParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CParser#declaration.
    def exitDeclaration(self, ctx:CParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CParser#expr.
    def enterExpr(self, ctx:CParser.ExprContext):
        pass

    # Exit a parse tree produced by CParser#expr.
    def exitExpr(self, ctx:CParser.ExprContext):
        pass



del CParser