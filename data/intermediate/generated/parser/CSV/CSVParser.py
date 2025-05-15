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
        4,1,5,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,3,3,47,8,3,1,4,1,4,3,4,51,8,4,1,5,1,5,1,5,1,5,1,5,3,5,58,8,5,1,
        6,1,6,1,6,3,6,63,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,74,
        8,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,0,75,0,16,1,0,0,0,2,32,1,0,0,
        0,4,34,1,0,0,0,6,46,1,0,0,0,8,50,1,0,0,0,10,57,1,0,0,0,12,62,1,0,
        0,0,14,73,1,0,0,0,16,17,3,14,7,0,17,18,3,2,1,0,18,19,5,0,0,1,19,
        1,1,0,0,0,20,21,3,6,3,0,21,22,3,2,1,0,22,33,1,0,0,0,23,24,3,12,6,
        0,24,25,3,10,5,0,25,26,3,8,4,0,26,27,5,3,0,0,27,33,1,0,0,0,28,29,
        3,12,6,0,29,30,3,8,4,0,30,31,5,3,0,0,31,33,1,0,0,0,32,20,1,0,0,0,
        32,23,1,0,0,0,32,28,1,0,0,0,33,3,1,0,0,0,34,35,5,1,0,0,35,36,3,12,
        6,0,36,5,1,0,0,0,37,38,3,12,6,0,38,39,3,10,5,0,39,40,3,8,4,0,40,
        41,5,3,0,0,41,47,1,0,0,0,42,43,3,12,6,0,43,44,3,8,4,0,44,45,5,3,
        0,0,45,47,1,0,0,0,46,37,1,0,0,0,46,42,1,0,0,0,47,7,1,0,0,0,48,51,
        5,2,0,0,49,51,1,0,0,0,50,48,1,0,0,0,50,49,1,0,0,0,51,9,1,0,0,0,52,
        53,3,4,2,0,53,54,3,10,5,0,54,58,1,0,0,0,55,56,5,1,0,0,56,58,3,12,
        6,0,57,52,1,0,0,0,57,55,1,0,0,0,58,11,1,0,0,0,59,63,5,4,0,0,60,63,
        5,5,0,0,61,63,1,0,0,0,62,59,1,0,0,0,62,60,1,0,0,0,62,61,1,0,0,0,
        63,13,1,0,0,0,64,65,3,12,6,0,65,66,3,10,5,0,66,67,3,8,4,0,67,68,
        5,3,0,0,68,74,1,0,0,0,69,70,3,12,6,0,70,71,3,8,4,0,71,72,5,3,0,0,
        72,74,1,0,0,0,73,64,1,0,0,0,73,69,1,0,0,0,74,15,1,0,0,0,6,32,46,
        50,57,62,73
    ]

class CSVParser ( Parser ):

    grammarFileName = "CSVParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'\\r'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "TERMINAL0", "TERMINAL1", "TERMINAL2", 
                      "TEXT", "STRING" ]

    RULE_csvFile = 0
    RULE_row_plus = 1
    RULE_block_0 = 2
    RULE_row = 3
    RULE_terminal1_question = 4
    RULE_block_0_star = 5
    RULE_field = 6
    RULE_hdr = 7

    ruleNames =  [ "csvFile", "row_plus", "block_0", "row", "terminal1_question", 
                   "block_0_star", "field", "hdr" ]

    EOF = Token.EOF
    TERMINAL0=1
    TERMINAL1=2
    TERMINAL2=3
    TEXT=4
    STRING=5

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
            self.state = 16
            self.hdr()
            self.state = 17
            self.row_plus()
            self.state = 18
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


        def terminal1_question(self):
            return self.getTypedRuleContext(CSVParser.Terminal1_questionContext,0)


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
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.row()
                self.state = 21
                self.row_plus()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.field()
                self.state = 24
                self.block_0_star()
                self.state = 25
                self.terminal1_question()
                self.state = 26
                self.match(CSVParser.TERMINAL2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.field()
                self.state = 29
                self.terminal1_question()
                self.state = 30
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
            self.state = 34
            self.match(CSVParser.TERMINAL0)
            self.state = 35
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


        def terminal1_question(self):
            return self.getTypedRuleContext(CSVParser.Terminal1_questionContext,0)


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
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.field()
                self.state = 38
                self.block_0_star()
                self.state = 39
                self.terminal1_question()
                self.state = 40
                self.match(CSVParser.TERMINAL2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.field()
                self.state = 43
                self.terminal1_question()
                self.state = 44
                self.match(CSVParser.TERMINAL2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Terminal1_questionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERMINAL1(self):
            return self.getToken(CSVParser.TERMINAL1, 0)

        def getRuleIndex(self):
            return CSVParser.RULE_terminal1_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal1_question" ):
                listener.enterTerminal1_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal1_question" ):
                listener.exitTerminal1_question(self)




    def terminal1_question(self):

        localctx = CSVParser.Terminal1_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_terminal1_question)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(CSVParser.TERMINAL1)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)

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
        self.enterRule(localctx, 10, self.RULE_block_0_star)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.block_0()
                self.state = 53
                self.block_0_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(CSVParser.TERMINAL0)
                self.state = 56
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
        self.enterRule(localctx, 12, self.RULE_field)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(CSVParser.TEXT)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(CSVParser.STRING)
                pass
            elif token in [1, 2, 3]:
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


        def terminal1_question(self):
            return self.getTypedRuleContext(CSVParser.Terminal1_questionContext,0)


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
        self.enterRule(localctx, 14, self.RULE_hdr)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.field()
                self.state = 65
                self.block_0_star()
                self.state = 66
                self.terminal1_question()
                self.state = 67
                self.match(CSVParser.TERMINAL2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.field()
                self.state = 70
                self.terminal1_question()
                self.state = 71
                self.match(CSVParser.TERMINAL2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





