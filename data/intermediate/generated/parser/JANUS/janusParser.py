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
        4,1,29,329,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,
        2,1,2,1,2,3,2,72,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,3,4,89,8,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,97,8,5,1,
        6,1,6,1,6,1,6,1,6,3,6,104,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,137,8,7,1,8,1,8,1,8,1,9,1,9,1,9,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,3,11,155,8,11,1,
        12,1,12,1,12,3,12,160,8,12,1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,3,16,178,8,16,1,17,1,
        17,1,17,3,17,183,8,17,1,18,1,18,1,18,1,18,3,18,189,8,18,1,19,1,19,
        1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,3,21,203,8,21,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,213,8,22,1,23,1,23,
        1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,237,8,24,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,
        254,8,25,1,26,1,26,1,26,1,26,1,26,1,26,3,26,262,8,26,1,27,1,27,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,3,28,297,8,28,1,29,1,29,1,29,1,29,1,29,1,
        29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,
        29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,327,8,29,1,
        29,0,0,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,0,0,348,0,60,1,0,0,0,2,64,1,0,0,0,
        4,71,1,0,0,0,6,73,1,0,0,0,8,88,1,0,0,0,10,96,1,0,0,0,12,103,1,0,
        0,0,14,136,1,0,0,0,16,138,1,0,0,0,18,141,1,0,0,0,20,144,1,0,0,0,
        22,154,1,0,0,0,24,159,1,0,0,0,26,161,1,0,0,0,28,164,1,0,0,0,30,167,
        1,0,0,0,32,177,1,0,0,0,34,182,1,0,0,0,36,188,1,0,0,0,38,190,1,0,
        0,0,40,193,1,0,0,0,42,202,1,0,0,0,44,212,1,0,0,0,46,214,1,0,0,0,
        48,236,1,0,0,0,50,253,1,0,0,0,52,261,1,0,0,0,54,263,1,0,0,0,56,296,
        1,0,0,0,58,326,1,0,0,0,60,61,5,1,0,0,61,62,5,27,0,0,62,63,5,2,0,
        0,63,1,1,0,0,0,64,65,5,26,0,0,65,66,3,4,2,0,66,3,1,0,0,0,67,72,1,
        0,0,0,68,69,5,1,0,0,69,70,5,27,0,0,70,72,5,2,0,0,71,67,1,0,0,0,71,
        68,1,0,0,0,72,5,1,0,0,0,73,74,5,3,0,0,74,75,5,26,0,0,75,76,3,56,
        28,0,76,7,1,0,0,0,77,78,3,12,6,0,78,79,3,10,5,0,79,80,5,0,0,1,80,
        89,1,0,0,0,81,82,3,12,6,0,82,83,5,0,0,1,83,89,1,0,0,0,84,89,5,0,
        0,1,85,86,3,10,5,0,86,87,5,0,0,1,87,89,1,0,0,0,88,77,1,0,0,0,88,
        81,1,0,0,0,88,84,1,0,0,0,88,85,1,0,0,0,89,9,1,0,0,0,90,91,3,6,3,
        0,91,92,3,10,5,0,92,97,1,0,0,0,93,94,5,3,0,0,94,95,5,26,0,0,95,97,
        3,56,28,0,96,90,1,0,0,0,96,93,1,0,0,0,97,11,1,0,0,0,98,99,3,2,1,
        0,99,100,3,12,6,0,100,104,1,0,0,0,101,102,5,26,0,0,102,104,3,4,2,
        0,103,98,1,0,0,0,103,101,1,0,0,0,104,13,1,0,0,0,105,106,3,58,29,
        0,106,107,3,14,7,0,107,137,1,0,0,0,108,109,5,4,0,0,109,110,3,48,
        24,0,110,111,3,24,12,0,111,112,3,22,11,0,112,113,5,7,0,0,113,114,
        3,48,24,0,114,137,1,0,0,0,115,116,5,8,0,0,116,117,3,48,24,0,117,
        118,3,34,17,0,118,119,3,32,16,0,119,120,5,11,0,0,120,121,3,48,24,
        0,121,137,1,0,0,0,122,123,5,12,0,0,123,137,5,26,0,0,124,125,5,13,
        0,0,125,137,5,26,0,0,126,127,5,14,0,0,127,137,5,26,0,0,128,129,5,
        15,0,0,129,137,5,26,0,0,130,131,3,52,26,0,131,132,3,44,22,0,132,
        137,1,0,0,0,133,134,3,52,26,0,134,135,3,46,23,0,135,137,1,0,0,0,
        136,105,1,0,0,0,136,108,1,0,0,0,136,115,1,0,0,0,136,122,1,0,0,0,
        136,124,1,0,0,0,136,126,1,0,0,0,136,128,1,0,0,0,136,130,1,0,0,0,
        136,133,1,0,0,0,137,15,1,0,0,0,138,139,5,5,0,0,139,140,3,56,28,0,
        140,17,1,0,0,0,141,142,5,6,0,0,142,143,3,56,28,0,143,19,1,0,0,0,
        144,145,5,4,0,0,145,146,3,48,24,0,146,147,3,24,12,0,147,148,3,22,
        11,0,148,149,5,7,0,0,149,150,3,48,24,0,150,21,1,0,0,0,151,155,1,
        0,0,0,152,153,5,6,0,0,153,155,3,56,28,0,154,151,1,0,0,0,154,152,
        1,0,0,0,155,23,1,0,0,0,156,160,1,0,0,0,157,158,5,5,0,0,158,160,3,
        56,28,0,159,156,1,0,0,0,159,157,1,0,0,0,160,25,1,0,0,0,161,162,5,
        9,0,0,162,163,3,56,28,0,163,27,1,0,0,0,164,165,5,10,0,0,165,166,
        3,56,28,0,166,29,1,0,0,0,167,168,5,8,0,0,168,169,3,48,24,0,169,170,
        3,34,17,0,170,171,3,32,16,0,171,172,5,11,0,0,172,173,3,48,24,0,173,
        31,1,0,0,0,174,178,1,0,0,0,175,176,5,10,0,0,176,178,3,56,28,0,177,
        174,1,0,0,0,177,175,1,0,0,0,178,33,1,0,0,0,179,183,1,0,0,0,180,181,
        5,9,0,0,181,183,3,56,28,0,182,179,1,0,0,0,182,180,1,0,0,0,183,35,
        1,0,0,0,184,185,5,12,0,0,185,189,5,26,0,0,186,187,5,13,0,0,187,189,
        5,26,0,0,188,184,1,0,0,0,188,186,1,0,0,0,189,37,1,0,0,0,190,191,
        5,14,0,0,191,192,5,26,0,0,192,39,1,0,0,0,193,194,5,15,0,0,194,195,
        5,26,0,0,195,41,1,0,0,0,196,197,3,52,26,0,197,198,3,44,22,0,198,
        203,1,0,0,0,199,200,3,52,26,0,200,201,3,46,23,0,201,203,1,0,0,0,
        202,196,1,0,0,0,202,199,1,0,0,0,203,43,1,0,0,0,204,205,5,16,0,0,
        205,213,3,48,24,0,206,207,5,17,0,0,207,213,3,48,24,0,208,209,5,18,
        0,0,209,213,3,48,24,0,210,211,5,19,0,0,211,213,3,48,24,0,212,204,
        1,0,0,0,212,206,1,0,0,0,212,208,1,0,0,0,212,210,1,0,0,0,213,45,1,
        0,0,0,214,215,5,20,0,0,215,216,3,52,26,0,216,47,1,0,0,0,217,218,
        3,50,25,0,218,219,5,25,0,0,219,220,3,48,24,0,220,237,1,0,0,0,221,
        222,5,21,0,0,222,223,3,48,24,0,223,224,5,22,0,0,224,237,1,0,0,0,
        225,226,5,23,0,0,226,237,3,48,24,0,227,228,5,24,0,0,228,237,3,48,
        24,0,229,237,5,26,0,0,230,231,5,26,0,0,231,232,5,1,0,0,232,233,3,
        48,24,0,233,234,5,2,0,0,234,237,1,0,0,0,235,237,5,27,0,0,236,217,
        1,0,0,0,236,221,1,0,0,0,236,225,1,0,0,0,236,227,1,0,0,0,236,229,
        1,0,0,0,236,230,1,0,0,0,236,235,1,0,0,0,237,49,1,0,0,0,238,239,5,
        21,0,0,239,240,3,48,24,0,240,241,5,22,0,0,241,254,1,0,0,0,242,243,
        5,23,0,0,243,254,3,48,24,0,244,245,5,24,0,0,245,254,3,48,24,0,246,
        254,5,26,0,0,247,248,5,26,0,0,248,249,5,1,0,0,249,250,3,48,24,0,
        250,251,5,2,0,0,251,254,1,0,0,0,252,254,5,27,0,0,253,238,1,0,0,0,
        253,242,1,0,0,0,253,244,1,0,0,0,253,246,1,0,0,0,253,247,1,0,0,0,
        253,252,1,0,0,0,254,51,1,0,0,0,255,262,5,26,0,0,256,257,5,26,0,0,
        257,258,5,1,0,0,258,259,3,48,24,0,259,260,5,2,0,0,260,262,1,0,0,
        0,261,255,1,0,0,0,261,256,1,0,0,0,262,53,1,0,0,0,263,264,5,27,0,
        0,264,55,1,0,0,0,265,266,3,58,29,0,266,267,3,14,7,0,267,297,1,0,
        0,0,268,269,5,4,0,0,269,270,3,48,24,0,270,271,3,24,12,0,271,272,
        3,22,11,0,272,273,5,7,0,0,273,274,3,48,24,0,274,297,1,0,0,0,275,
        276,5,8,0,0,276,277,3,48,24,0,277,278,3,34,17,0,278,279,3,32,16,
        0,279,280,5,11,0,0,280,281,3,48,24,0,281,297,1,0,0,0,282,283,5,12,
        0,0,283,297,5,26,0,0,284,285,5,13,0,0,285,297,5,26,0,0,286,287,5,
        14,0,0,287,297,5,26,0,0,288,289,5,15,0,0,289,297,5,26,0,0,290,291,
        3,52,26,0,291,292,3,44,22,0,292,297,1,0,0,0,293,294,3,52,26,0,294,
        295,3,46,23,0,295,297,1,0,0,0,296,265,1,0,0,0,296,268,1,0,0,0,296,
        275,1,0,0,0,296,282,1,0,0,0,296,284,1,0,0,0,296,286,1,0,0,0,296,
        288,1,0,0,0,296,290,1,0,0,0,296,293,1,0,0,0,297,57,1,0,0,0,298,299,
        5,4,0,0,299,300,3,48,24,0,300,301,3,24,12,0,301,302,3,22,11,0,302,
        303,5,7,0,0,303,304,3,48,24,0,304,327,1,0,0,0,305,306,5,8,0,0,306,
        307,3,48,24,0,307,308,3,34,17,0,308,309,3,32,16,0,309,310,5,11,0,
        0,310,311,3,48,24,0,311,327,1,0,0,0,312,313,5,12,0,0,313,327,5,26,
        0,0,314,315,5,13,0,0,315,327,5,26,0,0,316,317,5,14,0,0,317,327,5,
        26,0,0,318,319,5,15,0,0,319,327,5,26,0,0,320,321,3,52,26,0,321,322,
        3,44,22,0,322,327,1,0,0,0,323,324,3,52,26,0,324,325,3,46,23,0,325,
        327,1,0,0,0,326,298,1,0,0,0,326,305,1,0,0,0,326,312,1,0,0,0,326,
        314,1,0,0,0,326,316,1,0,0,0,326,318,1,0,0,0,326,320,1,0,0,0,326,
        323,1,0,0,0,327,59,1,0,0,0,17,71,88,96,103,136,154,159,177,182,188,
        202,212,236,253,261,296,326
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

    RULE_block_7 = 0
    RULE_block_0 = 1
    RULE_block_7_question = 2
    RULE_block_2 = 3
    RULE_program = 4
    RULE_block_2_star = 5
    RULE_block_0_star = 6
    RULE_statement_plus = 7
    RULE_block_3 = 8
    RULE_block_4 = 9
    RULE_ifstmt = 10
    RULE_block_4_question = 11
    RULE_block_3_question = 12
    RULE_block_5 = 13
    RULE_block_6 = 14
    RULE_dostmt = 15
    RULE_block_6_question = 16
    RULE_block_5_question = 17
    RULE_callstmt = 18
    RULE_readstmt = 19
    RULE_writestmt = 20
    RULE_lvalstmt = 21
    RULE_modstmt = 22
    RULE_swapstmt = 23
    RULE_expression = 24
    RULE_minexp = 25
    RULE_lvalue = 26
    RULE_constant = 27
    RULE_statements = 28
    RULE_statement = 29

    ruleNames =  [ "block_7", "block_0", "block_7_question", "block_2", 
                   "program", "block_2_star", "block_0_star", "statement_plus", 
                   "block_3", "block_4", "ifstmt", "block_4_question", "block_3_question", 
                   "block_5", "block_6", "dostmt", "block_6_question", "block_5_question", 
                   "callstmt", "readstmt", "writestmt", "lvalstmt", "modstmt", 
                   "swapstmt", "expression", "minexp", "lvalue", "constant", 
                   "statements", "statement" ]

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




    class Block_7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_0(self):
            return self.getToken(janusParser.TERM_0, 0)

        def NUM(self):
            return self.getToken(janusParser.NUM, 0)

        def TERM_1(self):
            return self.getToken(janusParser.TERM_1, 0)

        def getRuleIndex(self):
            return janusParser.RULE_block_7

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_7" ):
                listener.enterBlock_7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_7" ):
                listener.exitBlock_7(self)




    def block_7(self):

        localctx = janusParser.Block_7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_block_7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(janusParser.TERM_0)
            self.state = 61
            self.match(janusParser.NUM)
            self.state = 62
            self.match(janusParser.TERM_1)
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

        def IDENT(self):
            return self.getToken(janusParser.IDENT, 0)

        def block_7_question(self):
            return self.getTypedRuleContext(janusParser.Block_7_questionContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_block_0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_0" ):
                listener.enterBlock_0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_0" ):
                listener.exitBlock_0(self)




    def block_0(self):

        localctx = janusParser.Block_0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block_0)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(janusParser.IDENT)
            self.state = 65
            self.block_7_question()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_7_questionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_0(self):
            return self.getToken(janusParser.TERM_0, 0)

        def NUM(self):
            return self.getToken(janusParser.NUM, 0)

        def TERM_1(self):
            return self.getToken(janusParser.TERM_1, 0)

        def getRuleIndex(self):
            return janusParser.RULE_block_7_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_7_question" ):
                listener.enterBlock_7_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_7_question" ):
                listener.exitBlock_7_question(self)




    def block_7_question(self):

        localctx = janusParser.Block_7_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block_7_question)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1, 3, 26]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(janusParser.TERM_0)
                self.state = 69
                self.match(janusParser.NUM)
                self.state = 70
                self.match(janusParser.TERM_1)
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


    class Block_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_2(self):
            return self.getToken(janusParser.TERM_2, 0)

        def IDENT(self):
            return self.getToken(janusParser.IDENT, 0)

        def statements(self):
            return self.getTypedRuleContext(janusParser.StatementsContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_block_2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_2" ):
                listener.enterBlock_2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_2" ):
                listener.exitBlock_2(self)




    def block_2(self):

        localctx = janusParser.Block_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block_2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(janusParser.TERM_2)
            self.state = 74
            self.match(janusParser.IDENT)
            self.state = 75
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_0_star(self):
            return self.getTypedRuleContext(janusParser.Block_0_starContext,0)


        def block_2_star(self):
            return self.getTypedRuleContext(janusParser.Block_2_starContext,0)


        def EOF(self):
            return self.getToken(janusParser.EOF, 0)

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
        self.enterRule(localctx, 8, self.RULE_program)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.block_0_star()
                self.state = 78
                self.block_2_star()
                self.state = 79
                self.match(janusParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.block_0_star()
                self.state = 82
                self.match(janusParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.match(janusParser.EOF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.block_2_star()
                self.state = 86
                self.match(janusParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_2_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_2(self):
            return self.getTypedRuleContext(janusParser.Block_2Context,0)


        def block_2_star(self):
            return self.getTypedRuleContext(janusParser.Block_2_starContext,0)


        def TERM_2(self):
            return self.getToken(janusParser.TERM_2, 0)

        def IDENT(self):
            return self.getToken(janusParser.IDENT, 0)

        def statements(self):
            return self.getTypedRuleContext(janusParser.StatementsContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_block_2_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_2_star" ):
                listener.enterBlock_2_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_2_star" ):
                listener.exitBlock_2_star(self)




    def block_2_star(self):

        localctx = janusParser.Block_2_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block_2_star)
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.block_2()
                self.state = 91
                self.block_2_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(janusParser.TERM_2)
                self.state = 94
                self.match(janusParser.IDENT)
                self.state = 95
                self.statements()
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
            return self.getTypedRuleContext(janusParser.Block_0Context,0)


        def block_0_star(self):
            return self.getTypedRuleContext(janusParser.Block_0_starContext,0)


        def IDENT(self):
            return self.getToken(janusParser.IDENT, 0)

        def block_7_question(self):
            return self.getTypedRuleContext(janusParser.Block_7_questionContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_block_0_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_0_star" ):
                listener.enterBlock_0_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_0_star" ):
                listener.exitBlock_0_star(self)




    def block_0_star(self):

        localctx = janusParser.Block_0_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block_0_star)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.block_0()
                self.state = 99
                self.block_0_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.match(janusParser.IDENT)
                self.state = 102
                self.block_7_question()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_plusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(janusParser.StatementContext,0)


        def statement_plus(self):
            return self.getTypedRuleContext(janusParser.Statement_plusContext,0)


        def TERM_3(self):
            return self.getToken(janusParser.TERM_3, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(janusParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(janusParser.ExpressionContext,i)


        def block_3_question(self):
            return self.getTypedRuleContext(janusParser.Block_3_questionContext,0)


        def block_4_question(self):
            return self.getTypedRuleContext(janusParser.Block_4_questionContext,0)


        def TERM_6(self):
            return self.getToken(janusParser.TERM_6, 0)

        def TERM_7(self):
            return self.getToken(janusParser.TERM_7, 0)

        def block_5_question(self):
            return self.getTypedRuleContext(janusParser.Block_5_questionContext,0)


        def block_6_question(self):
            return self.getTypedRuleContext(janusParser.Block_6_questionContext,0)


        def TERM_10(self):
            return self.getToken(janusParser.TERM_10, 0)

        def TERM_11(self):
            return self.getToken(janusParser.TERM_11, 0)

        def IDENT(self):
            return self.getToken(janusParser.IDENT, 0)

        def TERM_12(self):
            return self.getToken(janusParser.TERM_12, 0)

        def TERM_13(self):
            return self.getToken(janusParser.TERM_13, 0)

        def TERM_14(self):
            return self.getToken(janusParser.TERM_14, 0)

        def lvalue(self):
            return self.getTypedRuleContext(janusParser.LvalueContext,0)


        def modstmt(self):
            return self.getTypedRuleContext(janusParser.ModstmtContext,0)


        def swapstmt(self):
            return self.getTypedRuleContext(janusParser.SwapstmtContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_statement_plus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_plus" ):
                listener.enterStatement_plus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_plus" ):
                listener.exitStatement_plus(self)




    def statement_plus(self):

        localctx = janusParser.Statement_plusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement_plus)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.statement()
                self.state = 106
                self.statement_plus()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.match(janusParser.TERM_3)
                self.state = 109
                self.expression()
                self.state = 110
                self.block_3_question()
                self.state = 111
                self.block_4_question()
                self.state = 112
                self.match(janusParser.TERM_6)
                self.state = 113
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.match(janusParser.TERM_7)
                self.state = 116
                self.expression()
                self.state = 117
                self.block_5_question()
                self.state = 118
                self.block_6_question()
                self.state = 119
                self.match(janusParser.TERM_10)
                self.state = 120
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 122
                self.match(janusParser.TERM_11)
                self.state = 123
                self.match(janusParser.IDENT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 124
                self.match(janusParser.TERM_12)
                self.state = 125
                self.match(janusParser.IDENT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 126
                self.match(janusParser.TERM_13)
                self.state = 127
                self.match(janusParser.IDENT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 128
                self.match(janusParser.TERM_14)
                self.state = 129
                self.match(janusParser.IDENT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 130
                self.lvalue()
                self.state = 131
                self.modstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 133
                self.lvalue()
                self.state = 134
                self.swapstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_4(self):
            return self.getToken(janusParser.TERM_4, 0)

        def statements(self):
            return self.getTypedRuleContext(janusParser.StatementsContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_block_3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_3" ):
                listener.enterBlock_3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_3" ):
                listener.exitBlock_3(self)




    def block_3(self):

        localctx = janusParser.Block_3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block_3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(janusParser.TERM_4)
            self.state = 139
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_5(self):
            return self.getToken(janusParser.TERM_5, 0)

        def statements(self):
            return self.getTypedRuleContext(janusParser.StatementsContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_block_4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_4" ):
                listener.enterBlock_4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_4" ):
                listener.exitBlock_4(self)




    def block_4(self):

        localctx = janusParser.Block_4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block_4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(janusParser.TERM_5)
            self.state = 142
            self.statements()
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


        def block_3_question(self):
            return self.getTypedRuleContext(janusParser.Block_3_questionContext,0)


        def block_4_question(self):
            return self.getTypedRuleContext(janusParser.Block_4_questionContext,0)


        def TERM_6(self):
            return self.getToken(janusParser.TERM_6, 0)

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
        self.enterRule(localctx, 20, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(janusParser.TERM_3)
            self.state = 145
            self.expression()
            self.state = 146
            self.block_3_question()
            self.state = 147
            self.block_4_question()
            self.state = 148
            self.match(janusParser.TERM_6)
            self.state = 149
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_4_questionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_5(self):
            return self.getToken(janusParser.TERM_5, 0)

        def statements(self):
            return self.getTypedRuleContext(janusParser.StatementsContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_block_4_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_4_question" ):
                listener.enterBlock_4_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_4_question" ):
                listener.exitBlock_4_question(self)




    def block_4_question(self):

        localctx = janusParser.Block_4_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block_4_question)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(janusParser.TERM_5)
                self.state = 153
                self.statements()
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


    class Block_3_questionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_4(self):
            return self.getToken(janusParser.TERM_4, 0)

        def statements(self):
            return self.getTypedRuleContext(janusParser.StatementsContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_block_3_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_3_question" ):
                listener.enterBlock_3_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_3_question" ):
                listener.exitBlock_3_question(self)




    def block_3_question(self):

        localctx = janusParser.Block_3_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block_3_question)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.match(janusParser.TERM_4)
                self.state = 158
                self.statements()
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


    class Block_5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_8(self):
            return self.getToken(janusParser.TERM_8, 0)

        def statements(self):
            return self.getTypedRuleContext(janusParser.StatementsContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_block_5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_5" ):
                listener.enterBlock_5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_5" ):
                listener.exitBlock_5(self)




    def block_5(self):

        localctx = janusParser.Block_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block_5)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(janusParser.TERM_8)
            self.state = 162
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_9(self):
            return self.getToken(janusParser.TERM_9, 0)

        def statements(self):
            return self.getTypedRuleContext(janusParser.StatementsContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_block_6

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_6" ):
                listener.enterBlock_6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_6" ):
                listener.exitBlock_6(self)




    def block_6(self):

        localctx = janusParser.Block_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_block_6)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(janusParser.TERM_9)
            self.state = 165
            self.statements()
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


        def block_5_question(self):
            return self.getTypedRuleContext(janusParser.Block_5_questionContext,0)


        def block_6_question(self):
            return self.getTypedRuleContext(janusParser.Block_6_questionContext,0)


        def TERM_10(self):
            return self.getToken(janusParser.TERM_10, 0)

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
        self.enterRule(localctx, 30, self.RULE_dostmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(janusParser.TERM_7)
            self.state = 168
            self.expression()
            self.state = 169
            self.block_5_question()
            self.state = 170
            self.block_6_question()
            self.state = 171
            self.match(janusParser.TERM_10)
            self.state = 172
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_6_questionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_9(self):
            return self.getToken(janusParser.TERM_9, 0)

        def statements(self):
            return self.getTypedRuleContext(janusParser.StatementsContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_block_6_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_6_question" ):
                listener.enterBlock_6_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_6_question" ):
                listener.exitBlock_6_question(self)




    def block_6_question(self):

        localctx = janusParser.Block_6_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_block_6_question)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(janusParser.TERM_9)
                self.state = 176
                self.statements()
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


    class Block_5_questionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_8(self):
            return self.getToken(janusParser.TERM_8, 0)

        def statements(self):
            return self.getTypedRuleContext(janusParser.StatementsContext,0)


        def getRuleIndex(self):
            return janusParser.RULE_block_5_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_5_question" ):
                listener.enterBlock_5_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_5_question" ):
                listener.exitBlock_5_question(self)




    def block_5_question(self):

        localctx = janusParser.Block_5_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block_5_question)
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(janusParser.TERM_8)
                self.state = 181
                self.statements()
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
        self.enterRule(localctx, 36, self.RULE_callstmt)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(janusParser.TERM_11)
                self.state = 185
                self.match(janusParser.IDENT)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(janusParser.TERM_12)
                self.state = 187
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
        self.enterRule(localctx, 38, self.RULE_readstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(janusParser.TERM_13)
            self.state = 191
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
        self.enterRule(localctx, 40, self.RULE_writestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(janusParser.TERM_14)
            self.state = 194
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
        self.enterRule(localctx, 42, self.RULE_lvalstmt)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.lvalue()
                self.state = 197
                self.modstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.lvalue()
                self.state = 200
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
        self.enterRule(localctx, 44, self.RULE_modstmt)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(janusParser.TERM_15)
                self.state = 205
                self.expression()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(janusParser.TERM_16)
                self.state = 207
                self.expression()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.match(janusParser.TERM_17)
                self.state = 209
                self.expression()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 210
                self.match(janusParser.TERM_18)
                self.state = 211
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
        self.enterRule(localctx, 46, self.RULE_swapstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(janusParser.TERM_19)
            self.state = 215
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


        def TERM_20(self):
            return self.getToken(janusParser.TERM_20, 0)

        def TERM_21(self):
            return self.getToken(janusParser.TERM_21, 0)

        def TERM_22(self):
            return self.getToken(janusParser.TERM_22, 0)

        def TERM_23(self):
            return self.getToken(janusParser.TERM_23, 0)

        def IDENT(self):
            return self.getToken(janusParser.IDENT, 0)

        def TERM_0(self):
            return self.getToken(janusParser.TERM_0, 0)

        def TERM_1(self):
            return self.getToken(janusParser.TERM_1, 0)

        def NUM(self):
            return self.getToken(janusParser.NUM, 0)

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
        self.enterRule(localctx, 48, self.RULE_expression)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.minexp()
                self.state = 218
                self.match(janusParser.BINOP)
                self.state = 219
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(janusParser.TERM_20)
                self.state = 222
                self.expression()
                self.state = 223
                self.match(janusParser.TERM_21)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self.match(janusParser.TERM_22)
                self.state = 226
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 227
                self.match(janusParser.TERM_23)
                self.state = 228
                self.expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 229
                self.match(janusParser.IDENT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 230
                self.match(janusParser.IDENT)
                self.state = 231
                self.match(janusParser.TERM_0)
                self.state = 232
                self.expression()
                self.state = 233
                self.match(janusParser.TERM_1)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 235
                self.match(janusParser.NUM)
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

        def IDENT(self):
            return self.getToken(janusParser.IDENT, 0)

        def TERM_0(self):
            return self.getToken(janusParser.TERM_0, 0)

        def TERM_1(self):
            return self.getToken(janusParser.TERM_1, 0)

        def NUM(self):
            return self.getToken(janusParser.NUM, 0)

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
        self.enterRule(localctx, 50, self.RULE_minexp)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(janusParser.TERM_20)
                self.state = 239
                self.expression()
                self.state = 240
                self.match(janusParser.TERM_21)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(janusParser.TERM_22)
                self.state = 243
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.match(janusParser.TERM_23)
                self.state = 245
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.match(janusParser.IDENT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 247
                self.match(janusParser.IDENT)
                self.state = 248
                self.match(janusParser.TERM_0)
                self.state = 249
                self.expression()
                self.state = 250
                self.match(janusParser.TERM_1)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 252
                self.match(janusParser.NUM)
                pass


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
        self.enterRule(localctx, 52, self.RULE_lvalue)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(janusParser.IDENT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(janusParser.IDENT)
                self.state = 257
                self.match(janusParser.TERM_0)
                self.state = 258
                self.expression()
                self.state = 259
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
        self.enterRule(localctx, 54, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(janusParser.NUM)
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

        def statement(self):
            return self.getTypedRuleContext(janusParser.StatementContext,0)


        def statement_plus(self):
            return self.getTypedRuleContext(janusParser.Statement_plusContext,0)


        def TERM_3(self):
            return self.getToken(janusParser.TERM_3, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(janusParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(janusParser.ExpressionContext,i)


        def block_3_question(self):
            return self.getTypedRuleContext(janusParser.Block_3_questionContext,0)


        def block_4_question(self):
            return self.getTypedRuleContext(janusParser.Block_4_questionContext,0)


        def TERM_6(self):
            return self.getToken(janusParser.TERM_6, 0)

        def TERM_7(self):
            return self.getToken(janusParser.TERM_7, 0)

        def block_5_question(self):
            return self.getTypedRuleContext(janusParser.Block_5_questionContext,0)


        def block_6_question(self):
            return self.getTypedRuleContext(janusParser.Block_6_questionContext,0)


        def TERM_10(self):
            return self.getToken(janusParser.TERM_10, 0)

        def TERM_11(self):
            return self.getToken(janusParser.TERM_11, 0)

        def IDENT(self):
            return self.getToken(janusParser.IDENT, 0)

        def TERM_12(self):
            return self.getToken(janusParser.TERM_12, 0)

        def TERM_13(self):
            return self.getToken(janusParser.TERM_13, 0)

        def TERM_14(self):
            return self.getToken(janusParser.TERM_14, 0)

        def lvalue(self):
            return self.getTypedRuleContext(janusParser.LvalueContext,0)


        def modstmt(self):
            return self.getTypedRuleContext(janusParser.ModstmtContext,0)


        def swapstmt(self):
            return self.getTypedRuleContext(janusParser.SwapstmtContext,0)


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
        self.enterRule(localctx, 56, self.RULE_statements)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.statement()
                self.state = 266
                self.statement_plus()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(janusParser.TERM_3)
                self.state = 269
                self.expression()
                self.state = 270
                self.block_3_question()
                self.state = 271
                self.block_4_question()
                self.state = 272
                self.match(janusParser.TERM_6)
                self.state = 273
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
                self.match(janusParser.TERM_7)
                self.state = 276
                self.expression()
                self.state = 277
                self.block_5_question()
                self.state = 278
                self.block_6_question()
                self.state = 279
                self.match(janusParser.TERM_10)
                self.state = 280
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 282
                self.match(janusParser.TERM_11)
                self.state = 283
                self.match(janusParser.IDENT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 284
                self.match(janusParser.TERM_12)
                self.state = 285
                self.match(janusParser.IDENT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 286
                self.match(janusParser.TERM_13)
                self.state = 287
                self.match(janusParser.IDENT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 288
                self.match(janusParser.TERM_14)
                self.state = 289
                self.match(janusParser.IDENT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 290
                self.lvalue()
                self.state = 291
                self.modstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 293
                self.lvalue()
                self.state = 294
                self.swapstmt()
                pass


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

        def TERM_3(self):
            return self.getToken(janusParser.TERM_3, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(janusParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(janusParser.ExpressionContext,i)


        def block_3_question(self):
            return self.getTypedRuleContext(janusParser.Block_3_questionContext,0)


        def block_4_question(self):
            return self.getTypedRuleContext(janusParser.Block_4_questionContext,0)


        def TERM_6(self):
            return self.getToken(janusParser.TERM_6, 0)

        def TERM_7(self):
            return self.getToken(janusParser.TERM_7, 0)

        def block_5_question(self):
            return self.getTypedRuleContext(janusParser.Block_5_questionContext,0)


        def block_6_question(self):
            return self.getTypedRuleContext(janusParser.Block_6_questionContext,0)


        def TERM_10(self):
            return self.getToken(janusParser.TERM_10, 0)

        def TERM_11(self):
            return self.getToken(janusParser.TERM_11, 0)

        def IDENT(self):
            return self.getToken(janusParser.IDENT, 0)

        def TERM_12(self):
            return self.getToken(janusParser.TERM_12, 0)

        def TERM_13(self):
            return self.getToken(janusParser.TERM_13, 0)

        def TERM_14(self):
            return self.getToken(janusParser.TERM_14, 0)

        def lvalue(self):
            return self.getTypedRuleContext(janusParser.LvalueContext,0)


        def modstmt(self):
            return self.getTypedRuleContext(janusParser.ModstmtContext,0)


        def swapstmt(self):
            return self.getTypedRuleContext(janusParser.SwapstmtContext,0)


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
        self.enterRule(localctx, 58, self.RULE_statement)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(janusParser.TERM_3)
                self.state = 299
                self.expression()
                self.state = 300
                self.block_3_question()
                self.state = 301
                self.block_4_question()
                self.state = 302
                self.match(janusParser.TERM_6)
                self.state = 303
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.match(janusParser.TERM_7)
                self.state = 306
                self.expression()
                self.state = 307
                self.block_5_question()
                self.state = 308
                self.block_6_question()
                self.state = 309
                self.match(janusParser.TERM_10)
                self.state = 310
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.match(janusParser.TERM_11)
                self.state = 313
                self.match(janusParser.IDENT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 314
                self.match(janusParser.TERM_12)
                self.state = 315
                self.match(janusParser.IDENT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 316
                self.match(janusParser.TERM_13)
                self.state = 317
                self.match(janusParser.IDENT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 318
                self.match(janusParser.TERM_14)
                self.state = 319
                self.match(janusParser.IDENT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 320
                self.lvalue()
                self.state = 321
                self.modstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 323
                self.lvalue()
                self.state = 324
                self.swapstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





