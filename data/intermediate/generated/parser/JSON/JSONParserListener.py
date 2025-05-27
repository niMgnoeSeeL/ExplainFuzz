# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/JSON/JSONParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JSONParser import JSONParser
else:
    from JSONParser import JSONParser

# This class defines a complete listener for a parse tree produced by JSONParser.
class JSONParserListener(ParseTreeListener):

    # Enter a parse tree produced by JSONParser#json.
    def enterJson(self, ctx:JSONParser.JsonContext):
        pass

    # Exit a parse tree produced by JSONParser#json.
    def exitJson(self, ctx:JSONParser.JsonContext):
        pass


    # Enter a parse tree produced by JSONParser#block_0.
    def enterBlock_0(self, ctx:JSONParser.Block_0Context):
        pass

    # Exit a parse tree produced by JSONParser#block_0.
    def exitBlock_0(self, ctx:JSONParser.Block_0Context):
        pass


    # Enter a parse tree produced by JSONParser#obj.
    def enterObj(self, ctx:JSONParser.ObjContext):
        pass

    # Exit a parse tree produced by JSONParser#obj.
    def exitObj(self, ctx:JSONParser.ObjContext):
        pass


    # Enter a parse tree produced by JSONParser#block_0_star.
    def enterBlock_0_star(self, ctx:JSONParser.Block_0_starContext):
        pass

    # Exit a parse tree produced by JSONParser#block_0_star.
    def exitBlock_0_star(self, ctx:JSONParser.Block_0_starContext):
        pass


    # Enter a parse tree produced by JSONParser#pair.
    def enterPair(self, ctx:JSONParser.PairContext):
        pass

    # Exit a parse tree produced by JSONParser#pair.
    def exitPair(self, ctx:JSONParser.PairContext):
        pass


    # Enter a parse tree produced by JSONParser#block_1.
    def enterBlock_1(self, ctx:JSONParser.Block_1Context):
        pass

    # Exit a parse tree produced by JSONParser#block_1.
    def exitBlock_1(self, ctx:JSONParser.Block_1Context):
        pass


    # Enter a parse tree produced by JSONParser#arr.
    def enterArr(self, ctx:JSONParser.ArrContext):
        pass

    # Exit a parse tree produced by JSONParser#arr.
    def exitArr(self, ctx:JSONParser.ArrContext):
        pass


    # Enter a parse tree produced by JSONParser#block_1_star.
    def enterBlock_1_star(self, ctx:JSONParser.Block_1_starContext):
        pass

    # Exit a parse tree produced by JSONParser#block_1_star.
    def exitBlock_1_star(self, ctx:JSONParser.Block_1_starContext):
        pass


    # Enter a parse tree produced by JSONParser#value.
    def enterValue(self, ctx:JSONParser.ValueContext):
        pass

    # Exit a parse tree produced by JSONParser#value.
    def exitValue(self, ctx:JSONParser.ValueContext):
        pass



del JSONParser