# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/CSV/CSVParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSVParser import CSVParser
else:
    from CSVParser import CSVParser

# This class defines a complete listener for a parse tree produced by CSVParser.
class CSVParserListener(ParseTreeListener):

    # Enter a parse tree produced by CSVParser#csvFile.
    def enterCsvFile(self, ctx:CSVParser.CsvFileContext):
        pass

    # Exit a parse tree produced by CSVParser#csvFile.
    def exitCsvFile(self, ctx:CSVParser.CsvFileContext):
        pass


    # Enter a parse tree produced by CSVParser#row_plus.
    def enterRow_plus(self, ctx:CSVParser.Row_plusContext):
        pass

    # Exit a parse tree produced by CSVParser#row_plus.
    def exitRow_plus(self, ctx:CSVParser.Row_plusContext):
        pass


    # Enter a parse tree produced by CSVParser#block_0.
    def enterBlock_0(self, ctx:CSVParser.Block_0Context):
        pass

    # Exit a parse tree produced by CSVParser#block_0.
    def exitBlock_0(self, ctx:CSVParser.Block_0Context):
        pass


    # Enter a parse tree produced by CSVParser#row.
    def enterRow(self, ctx:CSVParser.RowContext):
        pass

    # Exit a parse tree produced by CSVParser#row.
    def exitRow(self, ctx:CSVParser.RowContext):
        pass


    # Enter a parse tree produced by CSVParser#terminal1_question.
    def enterTerminal1_question(self, ctx:CSVParser.Terminal1_questionContext):
        pass

    # Exit a parse tree produced by CSVParser#terminal1_question.
    def exitTerminal1_question(self, ctx:CSVParser.Terminal1_questionContext):
        pass


    # Enter a parse tree produced by CSVParser#block_0_star.
    def enterBlock_0_star(self, ctx:CSVParser.Block_0_starContext):
        pass

    # Exit a parse tree produced by CSVParser#block_0_star.
    def exitBlock_0_star(self, ctx:CSVParser.Block_0_starContext):
        pass


    # Enter a parse tree produced by CSVParser#field.
    def enterField(self, ctx:CSVParser.FieldContext):
        pass

    # Exit a parse tree produced by CSVParser#field.
    def exitField(self, ctx:CSVParser.FieldContext):
        pass


    # Enter a parse tree produced by CSVParser#hdr.
    def enterHdr(self, ctx:CSVParser.HdrContext):
        pass

    # Exit a parse tree produced by CSVParser#hdr.
    def exitHdr(self, ctx:CSVParser.HdrContext):
        pass



del CSVParser