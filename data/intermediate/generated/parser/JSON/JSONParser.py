# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/JSON/JSONParser.g4 by ANTLR 4.11.1
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
        4,1,12,101,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,1,3,1,3,3,3,43,8,3,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,3,6,63,8,6,1,7,1,7,1,7,1,7,1,7,3,7,70,8,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,99,8,8,1,8,0,0,9,0,2,4,6,8,10,
        12,14,16,0,0,107,0,18,1,0,0,0,2,21,1,0,0,0,4,35,1,0,0,0,6,42,1,0,
        0,0,8,44,1,0,0,0,10,48,1,0,0,0,12,62,1,0,0,0,14,69,1,0,0,0,16,98,
        1,0,0,0,18,19,3,16,8,0,19,20,5,0,0,1,20,1,1,0,0,0,21,22,5,2,0,0,
        22,23,3,8,4,0,23,3,1,0,0,0,24,25,5,1,0,0,25,26,3,8,4,0,26,27,3,6,
        3,0,27,28,5,3,0,0,28,36,1,0,0,0,29,30,5,1,0,0,30,36,5,3,0,0,31,32,
        5,1,0,0,32,33,3,8,4,0,33,34,5,3,0,0,34,36,1,0,0,0,35,24,1,0,0,0,
        35,29,1,0,0,0,35,31,1,0,0,0,36,5,1,0,0,0,37,38,3,2,1,0,38,39,3,6,
        3,0,39,43,1,0,0,0,40,41,5,2,0,0,41,43,3,8,4,0,42,37,1,0,0,0,42,40,
        1,0,0,0,43,7,1,0,0,0,44,45,5,10,0,0,45,46,5,4,0,0,46,47,3,16,8,0,
        47,9,1,0,0,0,48,49,5,2,0,0,49,50,3,16,8,0,50,11,1,0,0,0,51,52,5,
        5,0,0,52,53,3,16,8,0,53,54,3,14,7,0,54,55,5,6,0,0,55,63,1,0,0,0,
        56,57,5,5,0,0,57,63,5,6,0,0,58,59,5,5,0,0,59,60,3,16,8,0,60,61,5,
        6,0,0,61,63,1,0,0,0,62,51,1,0,0,0,62,56,1,0,0,0,62,58,1,0,0,0,63,
        13,1,0,0,0,64,65,3,10,5,0,65,66,3,14,7,0,66,70,1,0,0,0,67,68,5,2,
        0,0,68,70,3,16,8,0,69,64,1,0,0,0,69,67,1,0,0,0,70,15,1,0,0,0,71,
        99,5,10,0,0,72,99,5,11,0,0,73,99,5,7,0,0,74,99,5,8,0,0,75,99,5,9,
        0,0,76,77,5,1,0,0,77,78,3,8,4,0,78,79,3,6,3,0,79,80,5,3,0,0,80,99,
        1,0,0,0,81,82,5,1,0,0,82,99,5,3,0,0,83,84,5,5,0,0,84,85,3,16,8,0,
        85,86,3,14,7,0,86,87,5,6,0,0,87,99,1,0,0,0,88,89,5,5,0,0,89,99,5,
        6,0,0,90,91,5,1,0,0,91,92,3,8,4,0,92,93,5,3,0,0,93,99,1,0,0,0,94,
        95,5,5,0,0,95,96,3,16,8,0,96,97,5,6,0,0,97,99,1,0,0,0,98,71,1,0,
        0,0,98,72,1,0,0,0,98,73,1,0,0,0,98,74,1,0,0,0,98,75,1,0,0,0,98,76,
        1,0,0,0,98,81,1,0,0,0,98,83,1,0,0,0,98,88,1,0,0,0,98,90,1,0,0,0,
        98,94,1,0,0,0,99,17,1,0,0,0,5,35,42,62,69,98
    ]

class JSONParser ( Parser ):

    grammarFileName = "JSONParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'", "':'", "'['", "']'", 
                     "'true'", "'false'", "'null'" ]

    symbolicNames = [ "<INVALID>", "TERM_0", "TERM_1", "TERM_2", "TERM_3", 
                      "TERM_4", "TERM_5", "TERM_6", "TERM_7", "TERM_8", 
                      "STRING", "NUMBER", "WS" ]

    RULE_json = 0
    RULE_block_0 = 1
    RULE_obj = 2
    RULE_block_0_star = 3
    RULE_pair = 4
    RULE_block_1 = 5
    RULE_arr = 6
    RULE_block_1_star = 7
    RULE_value = 8

    ruleNames =  [ "json", "block_0", "obj", "block_0_star", "pair", "block_1", 
                   "arr", "block_1_star", "value" ]

    EOF = Token.EOF
    TERM_0=1
    TERM_1=2
    TERM_2=3
    TERM_3=4
    TERM_4=5
    TERM_5=6
    TERM_6=7
    TERM_7=8
    TERM_8=9
    STRING=10
    NUMBER=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class JsonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


        def EOF(self):
            return self.getToken(JSONParser.EOF, 0)

        def getRuleIndex(self):
            return JSONParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)




    def json(self):

        localctx = JSONParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_json)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.value()
            self.state = 19
            self.match(JSONParser.EOF)
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

        def TERM_1(self):
            return self.getToken(JSONParser.TERM_1, 0)

        def pair(self):
            return self.getTypedRuleContext(JSONParser.PairContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_block_0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_0" ):
                listener.enterBlock_0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_0" ):
                listener.exitBlock_0(self)




    def block_0(self):

        localctx = JSONParser.Block_0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block_0)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(JSONParser.TERM_1)
            self.state = 22
            self.pair()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_0(self):
            return self.getToken(JSONParser.TERM_0, 0)

        def pair(self):
            return self.getTypedRuleContext(JSONParser.PairContext,0)


        def block_0_star(self):
            return self.getTypedRuleContext(JSONParser.Block_0_starContext,0)


        def TERM_2(self):
            return self.getToken(JSONParser.TERM_2, 0)

        def getRuleIndex(self):
            return JSONParser.RULE_obj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObj" ):
                listener.enterObj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObj" ):
                listener.exitObj(self)




    def obj(self):

        localctx = JSONParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_obj)
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(JSONParser.TERM_0)
                self.state = 25
                self.pair()
                self.state = 26
                self.block_0_star()
                self.state = 27
                self.match(JSONParser.TERM_2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(JSONParser.TERM_0)
                self.state = 30
                self.match(JSONParser.TERM_2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(JSONParser.TERM_0)
                self.state = 32
                self.pair()
                self.state = 33
                self.match(JSONParser.TERM_2)
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
            return self.getTypedRuleContext(JSONParser.Block_0Context,0)


        def block_0_star(self):
            return self.getTypedRuleContext(JSONParser.Block_0_starContext,0)


        def TERM_1(self):
            return self.getToken(JSONParser.TERM_1, 0)

        def pair(self):
            return self.getTypedRuleContext(JSONParser.PairContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_block_0_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_0_star" ):
                listener.enterBlock_0_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_0_star" ):
                listener.exitBlock_0_star(self)




    def block_0_star(self):

        localctx = JSONParser.Block_0_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block_0_star)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.block_0()
                self.state = 38
                self.block_0_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(JSONParser.TERM_1)
                self.state = 41
                self.pair()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)

        def TERM_3(self):
            return self.getToken(JSONParser.TERM_3, 0)

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = JSONParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(JSONParser.STRING)
            self.state = 45
            self.match(JSONParser.TERM_3)
            self.state = 46
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_1(self):
            return self.getToken(JSONParser.TERM_1, 0)

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_block_1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_1" ):
                listener.enterBlock_1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_1" ):
                listener.exitBlock_1(self)




    def block_1(self):

        localctx = JSONParser.Block_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block_1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(JSONParser.TERM_1)
            self.state = 49
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_4(self):
            return self.getToken(JSONParser.TERM_4, 0)

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


        def block_1_star(self):
            return self.getTypedRuleContext(JSONParser.Block_1_starContext,0)


        def TERM_5(self):
            return self.getToken(JSONParser.TERM_5, 0)

        def getRuleIndex(self):
            return JSONParser.RULE_arr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArr" ):
                listener.enterArr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArr" ):
                listener.exitArr(self)




    def arr(self):

        localctx = JSONParser.ArrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arr)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(JSONParser.TERM_4)
                self.state = 52
                self.value()
                self.state = 53
                self.block_1_star()
                self.state = 54
                self.match(JSONParser.TERM_5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(JSONParser.TERM_4)
                self.state = 57
                self.match(JSONParser.TERM_5)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.match(JSONParser.TERM_4)
                self.state = 59
                self.value()
                self.state = 60
                self.match(JSONParser.TERM_5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_1_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_1(self):
            return self.getTypedRuleContext(JSONParser.Block_1Context,0)


        def block_1_star(self):
            return self.getTypedRuleContext(JSONParser.Block_1_starContext,0)


        def TERM_1(self):
            return self.getToken(JSONParser.TERM_1, 0)

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_block_1_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_1_star" ):
                listener.enterBlock_1_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_1_star" ):
                listener.exitBlock_1_star(self)




    def block_1_star(self):

        localctx = JSONParser.Block_1_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block_1_star)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.block_1()
                self.state = 65
                self.block_1_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(JSONParser.TERM_1)
                self.state = 68
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(JSONParser.NUMBER, 0)

        def TERM_6(self):
            return self.getToken(JSONParser.TERM_6, 0)

        def TERM_7(self):
            return self.getToken(JSONParser.TERM_7, 0)

        def TERM_8(self):
            return self.getToken(JSONParser.TERM_8, 0)

        def TERM_0(self):
            return self.getToken(JSONParser.TERM_0, 0)

        def pair(self):
            return self.getTypedRuleContext(JSONParser.PairContext,0)


        def block_0_star(self):
            return self.getTypedRuleContext(JSONParser.Block_0_starContext,0)


        def TERM_2(self):
            return self.getToken(JSONParser.TERM_2, 0)

        def TERM_4(self):
            return self.getToken(JSONParser.TERM_4, 0)

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


        def block_1_star(self):
            return self.getTypedRuleContext(JSONParser.Block_1_starContext,0)


        def TERM_5(self):
            return self.getToken(JSONParser.TERM_5, 0)

        def getRuleIndex(self):
            return JSONParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = JSONParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(JSONParser.STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(JSONParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.match(JSONParser.TERM_6)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.match(JSONParser.TERM_7)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.match(JSONParser.TERM_8)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 76
                self.match(JSONParser.TERM_0)
                self.state = 77
                self.pair()
                self.state = 78
                self.block_0_star()
                self.state = 79
                self.match(JSONParser.TERM_2)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 81
                self.match(JSONParser.TERM_0)
                self.state = 82
                self.match(JSONParser.TERM_2)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 83
                self.match(JSONParser.TERM_4)
                self.state = 84
                self.value()
                self.state = 85
                self.block_1_star()
                self.state = 86
                self.match(JSONParser.TERM_5)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 88
                self.match(JSONParser.TERM_4)
                self.state = 89
                self.match(JSONParser.TERM_5)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 90
                self.match(JSONParser.TERM_0)
                self.state = 91
                self.pair()
                self.state = 92
                self.match(JSONParser.TERM_2)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 94
                self.match(JSONParser.TERM_4)
                self.state = 95
                self.value()
                self.state = 96
                self.match(JSONParser.TERM_5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





