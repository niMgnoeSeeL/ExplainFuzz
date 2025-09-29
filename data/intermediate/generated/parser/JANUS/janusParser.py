# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/JANUS/janusParser.g4 by ANTLR 4.13.0
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
        4,1,29,153,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,0,3,0,35,8,0,5,0,37,8,0,10,0,12,0,40,9,0,
        1,0,1,0,1,0,5,0,45,8,0,10,0,12,0,48,9,0,1,0,1,0,1,1,4,1,53,8,1,11,
        1,12,1,54,1,2,1,2,1,2,1,2,1,2,1,2,3,2,63,8,2,1,3,1,3,1,3,1,3,3,3,
        69,8,3,1,3,1,3,3,3,73,8,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,82,8,4,
        1,4,1,4,3,4,86,8,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,95,8,5,1,6,1,
        6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,109,8,8,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,3,9,119,8,9,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,3,11,129,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,3,12,141,8,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,149,8,
        13,1,14,1,14,1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        0,0,161,0,38,1,0,0,0,2,52,1,0,0,0,4,62,1,0,0,0,6,64,1,0,0,0,8,77,
        1,0,0,0,10,94,1,0,0,0,12,96,1,0,0,0,14,99,1,0,0,0,16,108,1,0,0,0,
        18,118,1,0,0,0,20,120,1,0,0,0,22,128,1,0,0,0,24,140,1,0,0,0,26,148,
        1,0,0,0,28,150,1,0,0,0,30,34,5,26,0,0,31,32,5,1,0,0,32,33,5,27,0,
        0,33,35,5,2,0,0,34,31,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,30,
        1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,46,1,0,0,0,
        40,38,1,0,0,0,41,42,5,3,0,0,42,43,5,26,0,0,43,45,3,2,1,0,44,41,1,
        0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,
        46,1,0,0,0,49,50,5,0,0,1,50,1,1,0,0,0,51,53,3,4,2,0,52,51,1,0,0,
        0,53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,3,1,0,0,0,56,63,3,
        6,3,0,57,63,3,8,4,0,58,63,3,10,5,0,59,63,3,12,6,0,60,63,3,14,7,0,
        61,63,3,16,8,0,62,56,1,0,0,0,62,57,1,0,0,0,62,58,1,0,0,0,62,59,1,
        0,0,0,62,60,1,0,0,0,62,61,1,0,0,0,63,5,1,0,0,0,64,65,5,4,0,0,65,
        68,3,22,11,0,66,67,5,5,0,0,67,69,3,2,1,0,68,66,1,0,0,0,68,69,1,0,
        0,0,69,72,1,0,0,0,70,71,5,6,0,0,71,73,3,2,1,0,72,70,1,0,0,0,72,73,
        1,0,0,0,73,74,1,0,0,0,74,75,5,7,0,0,75,76,3,22,11,0,76,7,1,0,0,0,
        77,78,5,8,0,0,78,81,3,22,11,0,79,80,5,9,0,0,80,82,3,2,1,0,81,79,
        1,0,0,0,81,82,1,0,0,0,82,85,1,0,0,0,83,84,5,10,0,0,84,86,3,2,1,0,
        85,83,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,88,5,11,0,0,88,89,3,
        22,11,0,89,9,1,0,0,0,90,91,5,12,0,0,91,95,5,26,0,0,92,93,5,13,0,
        0,93,95,5,26,0,0,94,90,1,0,0,0,94,92,1,0,0,0,95,11,1,0,0,0,96,97,
        5,14,0,0,97,98,5,26,0,0,98,13,1,0,0,0,99,100,5,15,0,0,100,101,5,
        26,0,0,101,15,1,0,0,0,102,103,3,26,13,0,103,104,3,18,9,0,104,109,
        1,0,0,0,105,106,3,26,13,0,106,107,3,20,10,0,107,109,1,0,0,0,108,
        102,1,0,0,0,108,105,1,0,0,0,109,17,1,0,0,0,110,111,5,16,0,0,111,
        119,3,22,11,0,112,113,5,17,0,0,113,119,3,22,11,0,114,115,5,18,0,
        0,115,119,3,22,11,0,116,117,5,19,0,0,117,119,3,22,11,0,118,110,1,
        0,0,0,118,112,1,0,0,0,118,114,1,0,0,0,118,116,1,0,0,0,119,19,1,0,
        0,0,120,121,5,20,0,0,121,122,3,26,13,0,122,21,1,0,0,0,123,129,3,
        24,12,0,124,125,3,24,12,0,125,126,5,25,0,0,126,127,3,22,11,0,127,
        129,1,0,0,0,128,123,1,0,0,0,128,124,1,0,0,0,129,23,1,0,0,0,130,131,
        5,21,0,0,131,132,3,22,11,0,132,133,5,22,0,0,133,141,1,0,0,0,134,
        135,5,23,0,0,135,141,3,22,11,0,136,137,5,24,0,0,137,141,3,22,11,
        0,138,141,3,26,13,0,139,141,3,28,14,0,140,130,1,0,0,0,140,134,1,
        0,0,0,140,136,1,0,0,0,140,138,1,0,0,0,140,139,1,0,0,0,141,25,1,0,
        0,0,142,149,5,26,0,0,143,144,5,26,0,0,144,145,5,1,0,0,145,146,3,
        22,11,0,146,147,5,2,0,0,147,149,1,0,0,0,148,142,1,0,0,0,148,143,
        1,0,0,0,149,27,1,0,0,0,150,151,5,27,0,0,151,29,1,0,0,0,15,34,38,
        46,54,62,68,72,81,85,94,108,118,128,140,148
    ]

class janusParser ( Parser ):

    grammarFileName = "janusParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'PROCEDURE'", "'IF'", "'THEN'", 
                     "'ELSE'", "'FI'", "'FROM'", "'DO'", "'LOOP'", "'UNTIL'", 
                     "'CALL'", "'UNCALL'", "'READ'", "'WRITE'", "'+='", 
                     "'-='", "'!='", "'<=>'", "':'", "'('", "')'", "'-'", 
                     "'~'" ]

    symbolicNames = [ "<INVALID>", "TERM_0", "TERM_1", "TERM_2", "TERM_3", 
                      "TERM_4", "TERM_5", "TERM_6", "TERM_7", "TERM_8", 
                      "TERM_9", "TERM_10", "TERM_11", "TERM_12", "TERM_13", 
                      "TERM_14", "TERM_15", "TERM_16", "TERM_17", "TERM_18", 
                      "TERM_19", "TERM_20", "TERM_21", "TERM_22", "TERM_23", 
                      "BINOP", "IDENT", "NUM", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_ifstmt = 3
    RULE_dostmt = 4
    RULE_callstmt = 5
    RULE_readstmt = 6
    RULE_writestmt = 7
    RULE_lvalstmt = 8
    RULE_modstmt = 9
    RULE_swapstmt = 10
    RULE_expression = 11
    RULE_minexp = 12
    RULE_lvalue = 13
    RULE_constant = 14

    ruleNames =  [ "program", "statements", "statement", "ifstmt", "dostmt", 
                   "callstmt", "readstmt", "writestmt", "lvalstmt", "modstmt", 
                   "swapstmt", "expression", "minexp", "lvalue", "constant" ]

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
    TERM_18=19
    TERM_19=20
    TERM_20=21
    TERM_21=22
    TERM_22=23
    TERM_23=24
    BINOP=25
    IDENT=26
    NUM=27
    COMMENT=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(janusParser.EOF, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(janusParser.IDENT)
            else:
                return self.getToken(janusParser.IDENT, i)

        def TERM_2(self, i:int=None):
            if i is None:
                return self.getTokens(janusParser.TERM_2)
            else:
                return self.getToken(janusParser.TERM_2, i)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(janusParser.StatementsContext)
            else:
                return self.getTypedRuleContext(janusParser.StatementsContext,i)


        def TERM_0(self, i:int=None):
            if i is None:
                return self.getTokens(janusParser.TERM_0)
            else:
                return self.getToken(janusParser.TERM_0, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(janusParser.NUM)
            else:
                return self.getToken(janusParser.NUM, i)

        def TERM_1(self, i:int=None):
            if i is None:
                return self.getTokens(janusParser.TERM_1)
            else:
                return self.getToken(janusParser.TERM_1, i)

        def getRuleIndex(self):
            return janusParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = janusParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 30
                self.match(janusParser.IDENT)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 31
                    self.match(janusParser.TERM_0)
                    self.state = 32
                    self.match(janusParser.NUM)
                    self.state = 33
                    self.match(janusParser.TERM_1)


                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 41
                self.match(janusParser.TERM_2)
                self.state = 42
                self.match(janusParser.IDENT)
                self.state = 43
                self.statements()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(janusParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(janusParser.StatementContext)
            else:
                return self.getTypedRuleContext(janusParser.StatementContext,i)


        def getRuleIndex(self):
            return janusParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = janusParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self.statement()
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 67170576) != 0)):
                    break

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

        def ifstmt(self):
            return self.getTypedRuleContext(janusParser.IfstmtContext,0)


        def dostmt(self):
            return self.getTypedRuleContext(janusParser.DostmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(janusParser.CallstmtContext,0)


        def readstmt(self):
            return self.getTypedRuleContext(janusParser.ReadstmtContext,0)


        def writestmt(self):
            return self.getTypedRuleContext(janusParser.WritestmtContext,0)


        def lvalstmt(self):
            return self.getTypedRuleContext(janusParser.LvalstmtContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = janusParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.ifstmt()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.dostmt()
                pass
            elif token in [12, 13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.callstmt()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.readstmt()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.writestmt()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 6)
                self.state = 61
                self.lvalstmt()
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


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_3(self):
            return self.getToken(janusParser.TERM_3, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(janusParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(janusParser.ExpressionContext,i)


        def TERM_6(self):
            return self.getToken(janusParser.TERM_6, 0)

        def TERM_4(self):
            return self.getToken(janusParser.TERM_4, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(janusParser.StatementsContext)
            else:
                return self.getTypedRuleContext(janusParser.StatementsContext,i)


        def TERM_5(self):
            return self.getToken(janusParser.TERM_5, 0)

        def getRuleIndex(self):
            return janusParser.RULE_ifstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstmt" ):
                listener.enterIfstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstmt" ):
                listener.exitIfstmt(self)




    def ifstmt(self):

        localctx = janusParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(janusParser.TERM_3)
            self.state = 65
            self.expression()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 66
                self.match(janusParser.TERM_4)
                self.state = 67
                self.statements()


            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 70
                self.match(janusParser.TERM_5)
                self.state = 71
                self.statements()


            self.state = 74
            self.match(janusParser.TERM_6)
            self.state = 75
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DostmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_7(self):
            return self.getToken(janusParser.TERM_7, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(janusParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(janusParser.ExpressionContext,i)


        def TERM_10(self):
            return self.getToken(janusParser.TERM_10, 0)

        def TERM_8(self):
            return self.getToken(janusParser.TERM_8, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(janusParser.StatementsContext)
            else:
                return self.getTypedRuleContext(janusParser.StatementsContext,i)


        def TERM_9(self):
            return self.getToken(janusParser.TERM_9, 0)

        def getRuleIndex(self):
            return janusParser.RULE_dostmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDostmt" ):
                listener.enterDostmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDostmt" ):
                listener.exitDostmt(self)




    def dostmt(self):

        localctx = janusParser.DostmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dostmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(janusParser.TERM_7)
            self.state = 78
            self.expression()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 79
                self.match(janusParser.TERM_8)
                self.state = 80
                self.statements()


            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 83
                self.match(janusParser.TERM_9)
                self.state = 84
                self.statements()


            self.state = 87
            self.match(janusParser.TERM_10)
            self.state = 88
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_11(self):
            return self.getToken(janusParser.TERM_11, 0)

        def IDENT(self):
            return self.getToken(janusParser.IDENT, 0)

        def TERM_12(self):
            return self.getToken(janusParser.TERM_12, 0)

        def getRuleIndex(self):
            return janusParser.RULE_callstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallstmt" ):
                listener.enterCallstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallstmt" ):
                listener.exitCallstmt(self)




    def callstmt(self):

        localctx = janusParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_callstmt)
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.match(janusParser.TERM_11)
                self.state = 91
                self.match(janusParser.IDENT)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.match(janusParser.TERM_12)
                self.state = 93
                self.match(janusParser.IDENT)
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


    class ReadstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_13(self):
            return self.getToken(janusParser.TERM_13, 0)

        def IDENT(self):
            return self.getToken(janusParser.IDENT, 0)

        def getRuleIndex(self):
            return janusParser.RULE_readstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadstmt" ):
                listener.enterReadstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadstmt" ):
                listener.exitReadstmt(self)




    def readstmt(self):

        localctx = janusParser.ReadstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_readstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(janusParser.TERM_13)
            self.state = 97
            self.match(janusParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WritestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_14(self):
            return self.getToken(janusParser.TERM_14, 0)

        def IDENT(self):
            return self.getToken(janusParser.IDENT, 0)

        def getRuleIndex(self):
            return janusParser.RULE_writestmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWritestmt" ):
                listener.enterWritestmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWritestmt" ):
                listener.exitWritestmt(self)




    def writestmt(self):

        localctx = janusParser.WritestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_writestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(janusParser.TERM_14)
            self.state = 100
            self.match(janusParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(janusParser.LvalueContext,0)


        def modstmt(self):
            return self.getTypedRuleContext(janusParser.ModstmtContext,0)


        def swapstmt(self):
            return self.getTypedRuleContext(janusParser.SwapstmtContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_lvalstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvalstmt" ):
                listener.enterLvalstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvalstmt" ):
                listener.exitLvalstmt(self)




    def lvalstmt(self):

        localctx = janusParser.LvalstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lvalstmt)
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.lvalue()
                self.state = 103
                self.modstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.lvalue()
                self.state = 106
                self.swapstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_15(self):
            return self.getToken(janusParser.TERM_15, 0)

        def expression(self):
            return self.getTypedRuleContext(janusParser.ExpressionContext,0)


        def TERM_16(self):
            return self.getToken(janusParser.TERM_16, 0)

        def TERM_17(self):
            return self.getToken(janusParser.TERM_17, 0)

        def TERM_18(self):
            return self.getToken(janusParser.TERM_18, 0)

        def getRuleIndex(self):
            return janusParser.RULE_modstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModstmt" ):
                listener.enterModstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModstmt" ):
                listener.exitModstmt(self)




    def modstmt(self):

        localctx = janusParser.ModstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_modstmt)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(janusParser.TERM_15)
                self.state = 111
                self.expression()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(janusParser.TERM_16)
                self.state = 113
                self.expression()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.match(janusParser.TERM_17)
                self.state = 115
                self.expression()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 116
                self.match(janusParser.TERM_18)
                self.state = 117
                self.expression()
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


    class SwapstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_19(self):
            return self.getToken(janusParser.TERM_19, 0)

        def lvalue(self):
            return self.getTypedRuleContext(janusParser.LvalueContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_swapstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwapstmt" ):
                listener.enterSwapstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwapstmt" ):
                listener.exitSwapstmt(self)




    def swapstmt(self):

        localctx = janusParser.SwapstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_swapstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(janusParser.TERM_19)
            self.state = 121
            self.lvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def minexp(self):
            return self.getTypedRuleContext(janusParser.MinexpContext,0)


        def BINOP(self):
            return self.getToken(janusParser.BINOP, 0)

        def expression(self):
            return self.getTypedRuleContext(janusParser.ExpressionContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = janusParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.minexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.minexp()
                self.state = 125
                self.match(janusParser.BINOP)
                self.state = 126
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MinexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_20(self):
            return self.getToken(janusParser.TERM_20, 0)

        def expression(self):
            return self.getTypedRuleContext(janusParser.ExpressionContext,0)


        def TERM_21(self):
            return self.getToken(janusParser.TERM_21, 0)

        def TERM_22(self):
            return self.getToken(janusParser.TERM_22, 0)

        def TERM_23(self):
            return self.getToken(janusParser.TERM_23, 0)

        def lvalue(self):
            return self.getTypedRuleContext(janusParser.LvalueContext,0)


        def constant(self):
            return self.getTypedRuleContext(janusParser.ConstantContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_minexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinexp" ):
                listener.enterMinexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinexp" ):
                listener.exitMinexp(self)




    def minexp(self):

        localctx = janusParser.MinexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_minexp)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(janusParser.TERM_20)
                self.state = 131
                self.expression()
                self.state = 132
                self.match(janusParser.TERM_21)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(janusParser.TERM_22)
                self.state = 135
                self.expression()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.match(janusParser.TERM_23)
                self.state = 137
                self.expression()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.lvalue()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 5)
                self.state = 139
                self.constant()
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


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(janusParser.IDENT, 0)

        def TERM_0(self):
            return self.getToken(janusParser.TERM_0, 0)

        def expression(self):
            return self.getTypedRuleContext(janusParser.ExpressionContext,0)


        def TERM_1(self):
            return self.getToken(janusParser.TERM_1, 0)

        def getRuleIndex(self):
            return janusParser.RULE_lvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvalue" ):
                listener.enterLvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvalue" ):
                listener.exitLvalue(self)




    def lvalue(self):

        localctx = janusParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_lvalue)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(janusParser.IDENT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(janusParser.IDENT)
                self.state = 144
                self.match(janusParser.TERM_0)
                self.state = 145
                self.expression()
                self.state = 146
                self.match(janusParser.TERM_1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(janusParser.NUM, 0)

        def getRuleIndex(self):
            return janusParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = janusParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(janusParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





