# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/REST/RESTLexer.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,16,69,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,
        1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,
        1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,0,0,16,1,1,3,2,
        5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,
        15,31,16,1,0,9,7,0,9,10,12,13,32,41,43,91,93,94,97,122,126,126,5,
        0,33,41,43,91,93,94,97,122,126,126,5,0,9,9,32,32,40,41,44,44,59,
        59,6,0,9,9,32,32,40,41,44,44,46,46,59,59,1,0,97,122,1,0,49,57,1,
        0,48,57,5,0,12,12,32,91,93,94,97,122,126,126,7,0,33,41,44,44,46,
        60,62,91,93,94,97,122,126,126,68,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,
        0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,
        0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,1,33,1,0,0,0,3,38,1,0,0,
        0,5,40,1,0,0,0,7,42,1,0,0,0,9,45,1,0,0,0,11,47,1,0,0,0,13,49,1,0,
        0,0,15,51,1,0,0,0,17,53,1,0,0,0,19,55,1,0,0,0,21,57,1,0,0,0,23,59,
        1,0,0,0,25,61,1,0,0,0,27,63,1,0,0,0,29,65,1,0,0,0,31,67,1,0,0,0,
        33,34,5,46,0,0,34,35,5,46,0,0,35,36,5,32,0,0,36,37,5,95,0,0,37,2,
        1,0,0,0,38,39,5,58,0,0,39,4,1,0,0,0,40,41,5,95,0,0,41,6,1,0,0,0,
        42,43,5,46,0,0,43,44,5,32,0,0,44,8,1,0,0,0,45,46,5,61,0,0,46,10,
        1,0,0,0,47,48,5,45,0,0,48,12,1,0,0,0,49,50,7,0,0,0,50,14,1,0,0,0,
        51,52,7,1,0,0,52,16,1,0,0,0,53,54,7,2,0,0,54,18,1,0,0,0,55,56,7,
        3,0,0,56,20,1,0,0,0,57,58,7,4,0,0,58,22,1,0,0,0,59,60,7,5,0,0,60,
        24,1,0,0,0,61,62,7,6,0,0,62,26,1,0,0,0,63,64,7,7,0,0,64,28,1,0,0,
        0,65,66,7,8,0,0,66,30,1,0,0,0,67,68,5,10,0,0,68,32,1,0,0,0,1,0,0
    ]

class RESTLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TERM_0 = 1
    TERM_1 = 2
    TERM_2 = 3
    TERM_3 = 4
    TERM_4 = 5
    TERM_5 = 6
    PARAGRAPH_CHAR = 7
    PARAGRAPH_CHAR_NOSPACE = 8
    PRESEP = 9
    POSTSEP = 10
    ID = 11
    DIGIT_NONZERO = 12
    DIGIT = 13
    NOBR_CHAR = 14
    TITLE_FIRST_CHAR = 15
    NEWLINE = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.. _'", "':'", "'_'", "'. '", "'='", "'-'", "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "TERM_0", "TERM_1", "TERM_2", "TERM_3", "TERM_4", "TERM_5", 
            "PARAGRAPH_CHAR", "PARAGRAPH_CHAR_NOSPACE", "PRESEP", "POSTSEP", 
            "ID", "DIGIT_NONZERO", "DIGIT", "NOBR_CHAR", "TITLE_FIRST_CHAR", 
            "NEWLINE" ]

    ruleNames = [ "TERM_0", "TERM_1", "TERM_2", "TERM_3", "TERM_4", "TERM_5", 
                  "PARAGRAPH_CHAR", "PARAGRAPH_CHAR_NOSPACE", "PRESEP", 
                  "POSTSEP", "ID", "DIGIT_NONZERO", "DIGIT", "NOBR_CHAR", 
                  "TITLE_FIRST_CHAR", "NEWLINE" ]

    grammarFileName = "RESTLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


