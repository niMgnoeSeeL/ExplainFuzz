# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/XML/XMLParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .XMLParser import XMLParser
else:
    from XMLParser import XMLParser

# This class defines a complete listener for a parse tree produced by XMLParser.
class XMLParserListener(ParseTreeListener):

    # Enter a parse tree produced by XMLParser#document.
    def enterDocument(self, ctx:XMLParser.DocumentContext):
        pass

    # Exit a parse tree produced by XMLParser#document.
    def exitDocument(self, ctx:XMLParser.DocumentContext):
        pass


    # Enter a parse tree produced by XMLParser#misc_star.
    def enterMisc_star(self, ctx:XMLParser.Misc_starContext):
        pass

    # Exit a parse tree produced by XMLParser#misc_star.
    def exitMisc_star(self, ctx:XMLParser.Misc_starContext):
        pass


    # Enter a parse tree produced by XMLParser#prolog_question.
    def enterProlog_question(self, ctx:XMLParser.Prolog_questionContext):
        pass

    # Exit a parse tree produced by XMLParser#prolog_question.
    def exitProlog_question(self, ctx:XMLParser.Prolog_questionContext):
        pass


    # Enter a parse tree produced by XMLParser#prolog.
    def enterProlog(self, ctx:XMLParser.PrologContext):
        pass

    # Exit a parse tree produced by XMLParser#prolog.
    def exitProlog(self, ctx:XMLParser.PrologContext):
        pass


    # Enter a parse tree produced by XMLParser#attribute_star.
    def enterAttribute_star(self, ctx:XMLParser.Attribute_starContext):
        pass

    # Exit a parse tree produced by XMLParser#attribute_star.
    def exitAttribute_star(self, ctx:XMLParser.Attribute_starContext):
        pass


    # Enter a parse tree produced by XMLParser#block_2.
    def enterBlock_2(self, ctx:XMLParser.Block_2Context):
        pass

    # Exit a parse tree produced by XMLParser#block_2.
    def exitBlock_2(self, ctx:XMLParser.Block_2Context):
        pass


    # Enter a parse tree produced by XMLParser#block_0.
    def enterBlock_0(self, ctx:XMLParser.Block_0Context):
        pass

    # Exit a parse tree produced by XMLParser#block_0.
    def exitBlock_0(self, ctx:XMLParser.Block_0Context):
        pass


    # Enter a parse tree produced by XMLParser#content.
    def enterContent(self, ctx:XMLParser.ContentContext):
        pass

    # Exit a parse tree produced by XMLParser#content.
    def exitContent(self, ctx:XMLParser.ContentContext):
        pass


    # Enter a parse tree produced by XMLParser#block_0_star.
    def enterBlock_0_star(self, ctx:XMLParser.Block_0_starContext):
        pass

    # Exit a parse tree produced by XMLParser#block_0_star.
    def exitBlock_0_star(self, ctx:XMLParser.Block_0_starContext):
        pass


    # Enter a parse tree produced by XMLParser#element.
    def enterElement(self, ctx:XMLParser.ElementContext):
        pass

    # Exit a parse tree produced by XMLParser#element.
    def exitElement(self, ctx:XMLParser.ElementContext):
        pass


    # Enter a parse tree produced by XMLParser#reference.
    def enterReference(self, ctx:XMLParser.ReferenceContext):
        pass

    # Exit a parse tree produced by XMLParser#reference.
    def exitReference(self, ctx:XMLParser.ReferenceContext):
        pass


    # Enter a parse tree produced by XMLParser#attribute.
    def enterAttribute(self, ctx:XMLParser.AttributeContext):
        pass

    # Exit a parse tree produced by XMLParser#attribute.
    def exitAttribute(self, ctx:XMLParser.AttributeContext):
        pass


    # Enter a parse tree produced by XMLParser#chardata.
    def enterChardata(self, ctx:XMLParser.ChardataContext):
        pass

    # Exit a parse tree produced by XMLParser#chardata.
    def exitChardata(self, ctx:XMLParser.ChardataContext):
        pass


    # Enter a parse tree produced by XMLParser#misc.
    def enterMisc(self, ctx:XMLParser.MiscContext):
        pass

    # Exit a parse tree produced by XMLParser#misc.
    def exitMisc(self, ctx:XMLParser.MiscContext):
        pass


    # Enter a parse tree produced by XMLParser#chardata_question.
    def enterChardata_question(self, ctx:XMLParser.Chardata_questionContext):
        pass

    # Exit a parse tree produced by XMLParser#chardata_question.
    def exitChardata_question(self, ctx:XMLParser.Chardata_questionContext):
        pass



del XMLParser