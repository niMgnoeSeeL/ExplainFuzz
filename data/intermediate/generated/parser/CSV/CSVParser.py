# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/CSV/CSVParser.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,6,70,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,31,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,45,
        8,3,1,4,1,4,1,4,1,4,1,4,3,4,52,8,4,1,5,1,5,1,5,3,5,57,8,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,68,8,6,1,6,0,0,7,0,2,4,6,8,10,
        12,0,0,69,0,14,1,0,0,0,2,30,1,0,0,0,4,32,1,0,0,0,6,44,1,0,0,0,8,
        51,1,0,0,0,10,56,1,0,0,0,12,67,1,0,0,0,14,15,3,12,6,0,15,16,3,2,
        1,0,16,17,5,0,0,1,17,1,1,0,0,0,18,19,3,6,3,0,19,20,3,2,1,0,20,31,
        1,0,0,0,21,22,3,10,5,0,22,23,3,8,4,0,23,24,5,6,0,0,24,25,5,3,0,0,
        25,31,1,0,0,0,26,27,3,10,5,0,27,28,5,6,0,0,28,29,5,3,0,0,29,31,1,
        0,0,0,30,18,1,0,0,0,30,21,1,0,0,0,30,26,1,0,0,0,31,3,1,0,0,0,32,
        33,5,1,0,0,33,34,3,10,5,0,34,5,1,0,0,0,35,36,3,10,5,0,36,37,3,8,
        4,0,37,38,5,6,0,0,38,39,5,3,0,0,39,45,1,0,0,0,40,41,3,10,5,0,41,
        42,5,6,0,0,42,43,5,3,0,0,43,45,1,0,0,0,44,35,1,0,0,0,44,40,1,0,0,
        0,45,7,1,0,0,0,46,47,3,4,2,0,47,48,3,8,4,0,48,52,1,0,0,0,49,50,5,
        1,0,0,50,52,3,10,5,0,51,46,1,0,0,0,51,49,1,0,0,0,52,9,1,0,0,0,53,
        57,5,4,0,0,54,57,5,5,0,0,55,57,1,0,0,0,56,53,1,0,0,0,56,54,1,0,0,
        0,56,55,1,0,0,0,57,11,1,0,0,0,58,59,3,10,5,0,59,60,3,8,4,0,60,61,
        5,6,0,0,61,62,5,3,0,0,62,68,1,0,0,0,63,64,3,10,5,0,64,65,5,6,0,0,
        65,66,5,3,0,0,66,68,1,0,0,0,67,58,1,0,0,0,67,63,1,0,0,0,68,13,1,
        0,0,0,5,30,44,51,56,67
    ]

class CSVParser ( Parser ):

    grammarFileName = "CSVParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'\\r'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "TERMINAL0", "TERMINAL1", "TERMINAL2", 
                      "TEXT", "STRING", "TERMINAL1_question" ]

    RULE_csvFile = 0
    RULE_row_plus = 1
    RULE_block_0 = 2
    RULE_row = 3
    RULE_block_0_star = 4
    RULE_field = 5
    RULE_hdr = 6

    ruleNames =  [ "csvFile", "row_plus", "block_0", "row", "block_0_star", 
                   "field", "hdr" ]

    EOF = Token.EOF
    TERMINAL0=1
    TERMINAL1=2
    TERMINAL2=3
    TEXT=4
    STRING=5
    TERMINAL1_question=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CsvFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hdr(self):
            return self.getTypedRuleContext(CSVParser.HdrContext,0)


        def row_plus(self):
            return self.getTypedRuleContext(CSVParser.Row_plusContext,0)


        def EOF(self):
            return self.getToken(CSVParser.EOF, 0)

        def getRuleIndex(self):
            return CSVParser.RULE_csvFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCsvFile" ):
                listener.enterCsvFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCsvFile" ):
                listener.exitCsvFile(self)




    def csvFile(self):

        localctx = CSVParser.CsvFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_csvFile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.hdr()
            self.state = 15
            self.row_plus()
            self.state = 16
            self.match(CSVParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Row_plusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self):
            return self.getTypedRuleContext(CSVParser.RowContext,0)


        def row_plus(self):
            return self.getTypedRuleContext(CSVParser.Row_plusContext,0)


        def field(self):
            return self.getTypedRuleContext(CSVParser.FieldContext,0)


        def block_0_star(self):
            return self.getTypedRuleContext(CSVParser.Block_0_starContext,0)


        def TERMINAL1_question(self):
            return self.getToken(CSVParser.TERMINAL1_question, 0)

        def TERMINAL2(self):
            return self.getToken(CSVParser.TERMINAL2, 0)

        def getRuleIndex(self):
            return CSVParser.RULE_row_plus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow_plus" ):
                listener.enterRow_plus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow_plus" ):
                listener.exitRow_plus(self)




    def row_plus(self):

        localctx = CSVParser.Row_plusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_row_plus)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.row()
                self.state = 19
                self.row_plus()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.field()
                self.state = 22
                self.block_0_star()
                self.state = 23
                self.match(CSVParser.TERMINAL1_question)
                self.state = 24
                self.match(CSVParser.TERMINAL2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.field()
                self.state = 27
                self.match(CSVParser.TERMINAL1_question)
                self.state = 28
                self.match(CSVParser.TERMINAL2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERMINAL0(self):
            return self.getToken(CSVParser.TERMINAL0, 0)

        def field(self):
            return self.getTypedRuleContext(CSVParser.FieldContext,0)


        def getRuleIndex(self):
            return CSVParser.RULE_block_0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_0" ):
                listener.enterBlock_0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_0" ):
                listener.exitBlock_0(self)




    def block_0(self):

        localctx = CSVParser.Block_0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block_0)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(CSVParser.TERMINAL0)
            self.state = 33
            self.field()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(CSVParser.FieldContext,0)


        def block_0_star(self):
            return self.getTypedRuleContext(CSVParser.Block_0_starContext,0)


        def TERMINAL1_question(self):
            return self.getToken(CSVParser.TERMINAL1_question, 0)

        def TERMINAL2(self):
            return self.getToken(CSVParser.TERMINAL2, 0)

        def getRuleIndex(self):
            return CSVParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)




    def row(self):

        localctx = CSVParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_row)
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.field()
                self.state = 36
                self.block_0_star()
                self.state = 37
                self.match(CSVParser.TERMINAL1_question)
                self.state = 38
                self.match(CSVParser.TERMINAL2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.field()
                self.state = 41
                self.match(CSVParser.TERMINAL1_question)
                self.state = 42
                self.match(CSVParser.TERMINAL2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_0_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_0(self):
            return self.getTypedRuleContext(CSVParser.Block_0Context,0)


        def block_0_star(self):
            return self.getTypedRuleContext(CSVParser.Block_0_starContext,0)


        def TERMINAL0(self):
            return self.getToken(CSVParser.TERMINAL0, 0)

        def field(self):
            return self.getTypedRuleContext(CSVParser.FieldContext,0)


        def getRuleIndex(self):
            return CSVParser.RULE_block_0_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_0_star" ):
                listener.enterBlock_0_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_0_star" ):
                listener.exitBlock_0_star(self)




    def block_0_star(self):

        localctx = CSVParser.Block_0_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block_0_star)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.block_0()
                self.state = 47
                self.block_0_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(CSVParser.TERMINAL0)
                self.state = 50
                self.field()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(CSVParser.TEXT, 0)

        def STRING(self):
            return self.getToken(CSVParser.STRING, 0)

        def getRuleIndex(self):
            return CSVParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)




    def field(self):

        localctx = CSVParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_field)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(CSVParser.TEXT)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(CSVParser.STRING)
                pass
            elif token in [1, 6]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HdrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(CSVParser.FieldContext,0)


        def block_0_star(self):
            return self.getTypedRuleContext(CSVParser.Block_0_starContext,0)


        def TERMINAL1_question(self):
            return self.getToken(CSVParser.TERMINAL1_question, 0)

        def TERMINAL2(self):
            return self.getToken(CSVParser.TERMINAL2, 0)

        def getRuleIndex(self):
            return CSVParser.RULE_hdr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHdr" ):
                listener.enterHdr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHdr" ):
                listener.exitHdr(self)




    def hdr(self):

        localctx = CSVParser.HdrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_hdr)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.field()
                self.state = 59
                self.block_0_star()
                self.state = 60
                self.match(CSVParser.TERMINAL1_question)
                self.state = 61
                self.match(CSVParser.TERMINAL2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.field()
                self.state = 64
                self.match(CSVParser.TERMINAL1_question)
                self.state = 65
                self.match(CSVParser.TERMINAL2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





