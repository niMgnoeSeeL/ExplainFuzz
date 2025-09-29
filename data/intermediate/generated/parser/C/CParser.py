# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/C/CParser.g4 by ANTLR 4.13.0
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
        4,1,21,107,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,
        0,11,0,12,0,13,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,26,8,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,47,8,1,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,67,8,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,3,4,76,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,102,
        8,4,10,4,12,4,105,9,4,1,4,0,1,8,5,0,2,4,6,8,0,0,121,0,11,1,0,0,0,
        2,46,1,0,0,0,4,48,1,0,0,0,6,66,1,0,0,0,8,75,1,0,0,0,10,12,3,2,1,
        0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,15,
        1,0,0,0,15,16,5,0,0,1,16,1,1,0,0,0,17,47,3,4,2,0,18,19,5,1,0,0,19,
        20,5,2,0,0,20,21,3,8,4,0,21,22,5,3,0,0,22,25,3,2,1,0,23,24,5,4,0,
        0,24,26,3,2,1,0,25,23,1,0,0,0,25,26,1,0,0,0,26,47,1,0,0,0,27,28,
        5,5,0,0,28,29,5,2,0,0,29,30,3,8,4,0,30,31,5,3,0,0,31,32,3,2,1,0,
        32,47,1,0,0,0,33,34,5,6,0,0,34,35,3,2,1,0,35,36,5,5,0,0,36,37,5,
        2,0,0,37,38,3,8,4,0,38,39,5,3,0,0,39,40,5,7,0,0,40,47,1,0,0,0,41,
        47,3,6,3,0,42,43,3,8,4,0,43,44,5,7,0,0,44,47,1,0,0,0,45,47,5,7,0,
        0,46,17,1,0,0,0,46,18,1,0,0,0,46,27,1,0,0,0,46,33,1,0,0,0,46,41,
        1,0,0,0,46,42,1,0,0,0,46,45,1,0,0,0,47,3,1,0,0,0,48,52,5,8,0,0,49,
        51,3,2,1,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,
        0,53,55,1,0,0,0,54,52,1,0,0,0,55,56,5,9,0,0,56,5,1,0,0,0,57,58,5,
        10,0,0,58,59,5,19,0,0,59,60,5,11,0,0,60,61,3,8,4,0,61,62,5,7,0,0,
        62,67,1,0,0,0,63,64,5,10,0,0,64,65,5,19,0,0,65,67,5,7,0,0,66,57,
        1,0,0,0,66,63,1,0,0,0,67,7,1,0,0,0,68,69,6,4,-1,0,69,70,5,2,0,0,
        70,71,3,8,4,0,71,72,5,3,0,0,72,76,1,0,0,0,73,76,5,19,0,0,74,76,5,
        20,0,0,75,68,1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,103,1,0,0,0,
        77,78,10,11,0,0,78,79,5,11,0,0,79,102,3,8,4,12,80,81,10,10,0,0,81,
        82,5,12,0,0,82,102,3,8,4,11,83,84,10,9,0,0,84,85,5,13,0,0,85,102,
        3,8,4,10,86,87,10,8,0,0,87,88,5,14,0,0,88,102,3,8,4,9,89,90,10,7,
        0,0,90,91,5,15,0,0,91,102,3,8,4,8,92,93,10,6,0,0,93,94,5,16,0,0,
        94,102,3,8,4,7,95,96,10,5,0,0,96,97,5,17,0,0,97,102,3,8,4,6,98,99,
        10,4,0,0,99,100,5,18,0,0,100,102,3,8,4,5,101,77,1,0,0,0,101,80,1,
        0,0,0,101,83,1,0,0,0,101,86,1,0,0,0,101,89,1,0,0,0,101,92,1,0,0,
        0,101,95,1,0,0,0,101,98,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,
        103,104,1,0,0,0,104,9,1,0,0,0,105,103,1,0,0,0,8,13,25,46,52,66,75,
        101,103
    ]

class CParser ( Parser ):

    grammarFileName = "CParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'('", "')'", "'else'", "'while'", 
                     "'do'", "';'", "'{'", "'}'", "'int'", "'='", "'=='", 
                     "'<'", "'+'", "'-'", "'*'", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "TERM_0", "TERM_1", "TERM_2", "TERM_3", 
                      "TERM_4", "TERM_5", "TERM_6", "TERM_7", "TERM_8", 
                      "TERM_9", "TERM_10", "TERM_11", "TERM_12", "TERM_13", 
                      "TERM_14", "TERM_15", "TERM_16", "TERM_17", "ID", 
                      "INT", "WS" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_block = 2
    RULE_declaration = 3
    RULE_expr = 4

    ruleNames =  [ "start", "statement", "block", "declaration", "expr" ]

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
    TERM_9=10
    TERM_10=11
    TERM_11=12
    TERM_12=13
    TERM_13=14
    TERM_14=15
    TERM_15=16
    TERM_16=17
    TERM_17=18
    ID=19
    INT=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.StatementContext)
            else:
                return self.getTypedRuleContext(CParser.StatementContext,i)


        def getRuleIndex(self):
            return CParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = CParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.statement()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1574374) != 0)):
                    break

            self.state = 15
            self.match(CParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CParser.BlockContext,0)


        def TERM_0(self):
            return self.getToken(CParser.TERM_0, 0)

        def TERM_1(self):
            return self.getToken(CParser.TERM_1, 0)

        def expr(self):
            return self.getTypedRuleContext(CParser.ExprContext,0)


        def TERM_2(self):
            return self.getToken(CParser.TERM_2, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.StatementContext)
            else:
                return self.getTypedRuleContext(CParser.StatementContext,i)


        def TERM_3(self):
            return self.getToken(CParser.TERM_3, 0)

        def TERM_4(self):
            return self.getToken(CParser.TERM_4, 0)

        def TERM_5(self):
            return self.getToken(CParser.TERM_5, 0)

        def TERM_6(self):
            return self.getToken(CParser.TERM_6, 0)

        def declaration(self):
            return self.getTypedRuleContext(CParser.DeclarationContext,0)


        def getRuleIndex(self):
            return CParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = CParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.block()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(CParser.TERM_0)
                self.state = 19
                self.match(CParser.TERM_1)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(CParser.TERM_2)
                self.state = 22
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 23
                    self.match(CParser.TERM_3)
                    self.state = 24
                    self.statement()


                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.match(CParser.TERM_4)
                self.state = 28
                self.match(CParser.TERM_1)
                self.state = 29
                self.expr(0)
                self.state = 30
                self.match(CParser.TERM_2)
                self.state = 31
                self.statement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.match(CParser.TERM_5)
                self.state = 34
                self.statement()
                self.state = 35
                self.match(CParser.TERM_4)
                self.state = 36
                self.match(CParser.TERM_1)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(CParser.TERM_2)
                self.state = 39
                self.match(CParser.TERM_6)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                self.declaration()
                pass
            elif token in [2, 19, 20]:
                self.enterOuterAlt(localctx, 6)
                self.state = 42
                self.expr(0)
                self.state = 43
                self.match(CParser.TERM_6)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 45
                self.match(CParser.TERM_6)
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


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_7(self):
            return self.getToken(CParser.TERM_7, 0)

        def TERM_8(self):
            return self.getToken(CParser.TERM_8, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.StatementContext)
            else:
                return self.getTypedRuleContext(CParser.StatementContext,i)


        def getRuleIndex(self):
            return CParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = CParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(CParser.TERM_7)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1574374) != 0):
                self.state = 49
                self.statement()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(CParser.TERM_8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_9(self):
            return self.getToken(CParser.TERM_9, 0)

        def ID(self):
            return self.getToken(CParser.ID, 0)

        def TERM_10(self):
            return self.getToken(CParser.TERM_10, 0)

        def expr(self):
            return self.getTypedRuleContext(CParser.ExprContext,0)


        def TERM_6(self):
            return self.getToken(CParser.TERM_6, 0)

        def getRuleIndex(self):
            return CParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = CParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.match(CParser.TERM_9)
                self.state = 58
                self.match(CParser.ID)
                self.state = 59
                self.match(CParser.TERM_10)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.match(CParser.TERM_6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(CParser.TERM_9)
                self.state = 64
                self.match(CParser.ID)
                self.state = 65
                self.match(CParser.TERM_6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_1(self):
            return self.getToken(CParser.TERM_1, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExprContext)
            else:
                return self.getTypedRuleContext(CParser.ExprContext,i)


        def TERM_2(self):
            return self.getToken(CParser.TERM_2, 0)

        def ID(self):
            return self.getToken(CParser.ID, 0)

        def INT(self):
            return self.getToken(CParser.INT, 0)

        def TERM_10(self):
            return self.getToken(CParser.TERM_10, 0)

        def TERM_11(self):
            return self.getToken(CParser.TERM_11, 0)

        def TERM_12(self):
            return self.getToken(CParser.TERM_12, 0)

        def TERM_13(self):
            return self.getToken(CParser.TERM_13, 0)

        def TERM_14(self):
            return self.getToken(CParser.TERM_14, 0)

        def TERM_15(self):
            return self.getToken(CParser.TERM_15, 0)

        def TERM_16(self):
            return self.getToken(CParser.TERM_16, 0)

        def TERM_17(self):
            return self.getToken(CParser.TERM_17, 0)

        def getRuleIndex(self):
            return CParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 69
                self.match(CParser.TERM_1)
                self.state = 70
                self.expr(0)
                self.state = 71
                self.match(CParser.TERM_2)
                pass
            elif token in [19]:
                self.state = 73
                self.match(CParser.ID)
                pass
            elif token in [20]:
                self.state = 74
                self.match(CParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 103
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 101
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = CParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 77
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 78
                        self.match(CParser.TERM_10)
                        self.state = 79
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = CParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 80
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 81
                        self.match(CParser.TERM_11)
                        self.state = 82
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = CParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 83
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 84
                        self.match(CParser.TERM_12)
                        self.state = 85
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = CParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 86
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 87
                        self.match(CParser.TERM_13)
                        self.state = 88
                        self.expr(9)
                        pass

                    elif la_ == 5:
                        localctx = CParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 90
                        self.match(CParser.TERM_14)
                        self.state = 91
                        self.expr(8)
                        pass

                    elif la_ == 6:
                        localctx = CParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 92
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 93
                        self.match(CParser.TERM_15)
                        self.state = 94
                        self.expr(7)
                        pass

                    elif la_ == 7:
                        localctx = CParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 95
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 96
                        self.match(CParser.TERM_16)
                        self.state = 97
                        self.expr(6)
                        pass

                    elif la_ == 8:
                        localctx = CParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 98
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 99
                        self.match(CParser.TERM_17)
                        self.state = 100
                        self.expr(5)
                        pass

             
                self.state = 105
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         




