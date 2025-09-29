# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/REST/RESTParser.g4 by ANTLR 4.13.0
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
        4,1,16,207,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,75,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,
        2,83,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,93,8,4,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,112,
        8,8,1,9,1,9,3,9,116,8,9,1,10,1,10,3,10,120,8,10,1,11,1,11,1,11,1,
        11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,
        14,3,14,139,8,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,149,
        8,16,1,17,1,17,1,17,1,17,3,17,155,8,17,1,18,1,18,1,19,1,19,1,20,
        1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,23,1,23,3,23,171,8,23,1,24,
        1,24,1,25,1,25,1,25,1,25,3,25,179,8,25,1,26,1,26,1,27,1,27,1,27,
        1,27,3,27,187,8,27,1,28,1,28,1,29,1,29,1,30,1,30,3,30,195,8,30,1,
        31,1,31,1,31,3,31,200,8,31,1,32,1,32,1,32,3,32,205,8,32,1,32,0,0,
        33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,0,0,190,0,66,1,0,0,0,2,74,1,0,0,
        0,4,82,1,0,0,0,6,84,1,0,0,0,8,92,1,0,0,0,10,94,1,0,0,0,12,98,1,0,
        0,0,14,103,1,0,0,0,16,111,1,0,0,0,18,115,1,0,0,0,20,119,1,0,0,0,
        22,121,1,0,0,0,24,126,1,0,0,0,26,130,1,0,0,0,28,138,1,0,0,0,30,140,
        1,0,0,0,32,148,1,0,0,0,34,154,1,0,0,0,36,156,1,0,0,0,38,158,1,0,
        0,0,40,160,1,0,0,0,42,162,1,0,0,0,44,164,1,0,0,0,46,170,1,0,0,0,
        48,172,1,0,0,0,50,178,1,0,0,0,52,180,1,0,0,0,54,186,1,0,0,0,56,188,
        1,0,0,0,58,190,1,0,0,0,60,194,1,0,0,0,62,199,1,0,0,0,64,204,1,0,
        0,0,66,67,3,2,1,0,67,68,5,0,0,1,68,1,1,0,0,0,69,70,3,4,2,0,70,71,
        5,16,0,0,71,72,3,2,1,0,72,75,1,0,0,0,73,75,3,4,2,0,74,69,1,0,0,0,
        74,73,1,0,0,0,75,3,1,0,0,0,76,77,3,6,3,0,77,78,5,16,0,0,78,83,1,
        0,0,0,79,83,3,12,6,0,80,83,3,10,5,0,81,83,3,26,13,0,82,76,1,0,0,
        0,82,79,1,0,0,0,82,80,1,0,0,0,82,81,1,0,0,0,83,5,1,0,0,0,84,85,3,
        8,4,0,85,86,5,16,0,0,86,87,3,60,30,0,87,7,1,0,0,0,88,93,3,58,29,
        0,89,90,3,58,29,0,90,91,3,54,27,0,91,93,1,0,0,0,92,88,1,0,0,0,92,
        89,1,0,0,0,93,9,1,0,0,0,94,95,3,18,9,0,95,96,3,16,8,0,96,97,5,16,
        0,0,97,11,1,0,0,0,98,99,3,14,7,0,99,100,5,16,0,0,100,101,5,16,0,
        0,101,102,3,10,5,0,102,13,1,0,0,0,103,104,5,1,0,0,104,105,3,44,22,
        0,105,106,5,2,0,0,106,15,1,0,0,0,107,108,3,20,10,0,108,109,3,16,
        8,0,109,112,1,0,0,0,110,112,3,20,10,0,111,107,1,0,0,0,111,110,1,
        0,0,0,112,17,1,0,0,0,113,116,3,34,17,0,114,116,3,24,12,0,115,113,
        1,0,0,0,115,114,1,0,0,0,116,19,1,0,0,0,117,120,3,32,16,0,118,120,
        3,22,11,0,119,117,1,0,0,0,119,118,1,0,0,0,120,21,1,0,0,0,121,122,
        3,40,20,0,122,123,3,44,22,0,123,124,5,3,0,0,124,125,3,42,21,0,125,
        23,1,0,0,0,126,127,3,44,22,0,127,128,5,3,0,0,128,129,3,42,21,0,129,
        25,1,0,0,0,130,131,3,28,14,0,131,132,5,16,0,0,132,27,1,0,0,0,133,
        134,3,30,15,0,134,135,5,16,0,0,135,136,3,28,14,0,136,139,1,0,0,0,
        137,139,3,30,15,0,138,133,1,0,0,0,138,137,1,0,0,0,139,29,1,0,0,0,
        140,141,3,46,23,0,141,142,5,4,0,0,142,143,3,54,27,0,143,31,1,0,0,
        0,144,145,3,36,18,0,145,146,3,32,16,0,146,149,1,0,0,0,147,149,3,
        36,18,0,148,144,1,0,0,0,148,147,1,0,0,0,149,33,1,0,0,0,150,151,3,
        38,19,0,151,152,3,34,17,0,152,155,1,0,0,0,153,155,3,38,19,0,154,
        150,1,0,0,0,154,153,1,0,0,0,155,35,1,0,0,0,156,157,5,7,0,0,157,37,
        1,0,0,0,158,159,5,8,0,0,159,39,1,0,0,0,160,161,5,9,0,0,161,41,1,
        0,0,0,162,163,5,10,0,0,163,43,1,0,0,0,164,165,5,11,0,0,165,45,1,
        0,0,0,166,167,3,48,24,0,167,168,3,50,25,0,168,171,1,0,0,0,169,171,
        3,52,26,0,170,166,1,0,0,0,170,169,1,0,0,0,171,47,1,0,0,0,172,173,
        5,12,0,0,173,49,1,0,0,0,174,175,3,52,26,0,175,176,3,50,25,0,176,
        179,1,0,0,0,177,179,3,52,26,0,178,174,1,0,0,0,178,177,1,0,0,0,179,
        51,1,0,0,0,180,181,5,13,0,0,181,53,1,0,0,0,182,187,3,56,28,0,183,
        184,3,56,28,0,184,185,3,54,27,0,185,187,1,0,0,0,186,182,1,0,0,0,
        186,183,1,0,0,0,187,55,1,0,0,0,188,189,5,14,0,0,189,57,1,0,0,0,190,
        191,5,15,0,0,191,59,1,0,0,0,192,195,3,62,31,0,193,195,3,64,32,0,
        194,192,1,0,0,0,194,193,1,0,0,0,195,61,1,0,0,0,196,200,5,5,0,0,197,
        198,5,5,0,0,198,200,3,62,31,0,199,196,1,0,0,0,199,197,1,0,0,0,200,
        63,1,0,0,0,201,205,5,6,0,0,202,203,5,6,0,0,203,205,3,64,32,0,204,
        201,1,0,0,0,204,202,1,0,0,0,205,65,1,0,0,0,15,74,82,92,111,115,119,
        138,148,154,170,178,186,194,199,204
    ]

class RESTParser ( Parser ):

    grammarFileName = "RESTParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.. _'", "':'", "'_'", "'. '", "'='", 
                     "'-'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "TERM_0", "TERM_1", "TERM_2", "TERM_3", 
                      "TERM_4", "TERM_5", "PARAGRAPH_CHAR", "PARAGRAPH_CHAR_NOSPACE", 
                      "PRESEP", "POSTSEP", "ID", "DIGIT_NONZERO", "DIGIT", 
                      "NOBR_CHAR", "TITLE_FIRST_CHAR", "NEWLINE" ]

    RULE_start = 0
    RULE_bodyElements = 1
    RULE_bodyElement = 2
    RULE_sectionTitle = 3
    RULE_titleText = 4
    RULE_paragraph = 5
    RULE_labeledParagraph = 6
    RULE_label = 7
    RULE_paragraphElements = 8
    RULE_firstParagraphElement = 9
    RULE_paragraphElement = 10
    RULE_internalReference = 11
    RULE_internalReferenceNoSpace = 12
    RULE_enumeration = 13
    RULE_enumerationItems = 14
    RULE_enumerationItem = 15
    RULE_paragraphChars = 16
    RULE_paragraphCharsNoSpace = 17
    RULE_paragraphChar = 18
    RULE_paragraphCharNoSpace = 19
    RULE_presep = 20
    RULE_postsep = 21
    RULE_id = 22
    RULE_number = 23
    RULE_digitNonZero = 24
    RULE_digits = 25
    RULE_digit = 26
    RULE_nobrString = 27
    RULE_nobrChar = 28
    RULE_titleFirstChar = 29
    RULE_underline = 30
    RULE_eqs = 31
    RULE_dashes = 32

    ruleNames =  [ "start", "bodyElements", "bodyElement", "sectionTitle", 
                   "titleText", "paragraph", "labeledParagraph", "label", 
                   "paragraphElements", "firstParagraphElement", "paragraphElement", 
                   "internalReference", "internalReferenceNoSpace", "enumeration", 
                   "enumerationItems", "enumerationItem", "paragraphChars", 
                   "paragraphCharsNoSpace", "paragraphChar", "paragraphCharNoSpace", 
                   "presep", "postsep", "id", "number", "digitNonZero", 
                   "digits", "digit", "nobrString", "nobrChar", "titleFirstChar", 
                   "underline", "eqs", "dashes" ]

    EOF = Token.EOF
    TERM_0=1
    TERM_1=2
    TERM_2=3
    TERM_3=4
    TERM_4=5
    TERM_5=6
    PARAGRAPH_CHAR=7
    PARAGRAPH_CHAR_NOSPACE=8
    PRESEP=9
    POSTSEP=10
    ID=11
    DIGIT_NONZERO=12
    DIGIT=13
    NOBR_CHAR=14
    TITLE_FIRST_CHAR=15
    NEWLINE=16

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

        def bodyElements(self):
            return self.getTypedRuleContext(RESTParser.BodyElementsContext,0)


        def EOF(self):
            return self.getToken(RESTParser.EOF, 0)

        def getRuleIndex(self):
            return RESTParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = RESTParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.bodyElements()
            self.state = 67
            self.match(RESTParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bodyElement(self):
            return self.getTypedRuleContext(RESTParser.BodyElementContext,0)


        def NEWLINE(self):
            return self.getToken(RESTParser.NEWLINE, 0)

        def bodyElements(self):
            return self.getTypedRuleContext(RESTParser.BodyElementsContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_bodyElements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBodyElements" ):
                listener.enterBodyElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBodyElements" ):
                listener.exitBodyElements(self)




    def bodyElements(self):

        localctx = RESTParser.BodyElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bodyElements)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.bodyElement()
                self.state = 70
                self.match(RESTParser.NEWLINE)
                self.state = 71
                self.bodyElements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.bodyElement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sectionTitle(self):
            return self.getTypedRuleContext(RESTParser.SectionTitleContext,0)


        def NEWLINE(self):
            return self.getToken(RESTParser.NEWLINE, 0)

        def labeledParagraph(self):
            return self.getTypedRuleContext(RESTParser.LabeledParagraphContext,0)


        def paragraph(self):
            return self.getTypedRuleContext(RESTParser.ParagraphContext,0)


        def enumeration(self):
            return self.getTypedRuleContext(RESTParser.EnumerationContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_bodyElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBodyElement" ):
                listener.enterBodyElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBodyElement" ):
                listener.exitBodyElement(self)




    def bodyElement(self):

        localctx = RESTParser.BodyElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bodyElement)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.sectionTitle()
                self.state = 77
                self.match(RESTParser.NEWLINE)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.labeledParagraph()
                pass
            elif token in [8, 11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.paragraph()
                pass
            elif token in [12, 13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.enumeration()
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


    class SectionTitleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def titleText(self):
            return self.getTypedRuleContext(RESTParser.TitleTextContext,0)


        def NEWLINE(self):
            return self.getToken(RESTParser.NEWLINE, 0)

        def underline(self):
            return self.getTypedRuleContext(RESTParser.UnderlineContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_sectionTitle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSectionTitle" ):
                listener.enterSectionTitle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSectionTitle" ):
                listener.exitSectionTitle(self)




    def sectionTitle(self):

        localctx = RESTParser.SectionTitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sectionTitle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.titleText()
            self.state = 85
            self.match(RESTParser.NEWLINE)
            self.state = 86
            self.underline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TitleTextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def titleFirstChar(self):
            return self.getTypedRuleContext(RESTParser.TitleFirstCharContext,0)


        def nobrString(self):
            return self.getTypedRuleContext(RESTParser.NobrStringContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_titleText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTitleText" ):
                listener.enterTitleText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTitleText" ):
                listener.exitTitleText(self)




    def titleText(self):

        localctx = RESTParser.TitleTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_titleText)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.titleFirstChar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.titleFirstChar()
                self.state = 90
                self.nobrString()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParagraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def firstParagraphElement(self):
            return self.getTypedRuleContext(RESTParser.FirstParagraphElementContext,0)


        def paragraphElements(self):
            return self.getTypedRuleContext(RESTParser.ParagraphElementsContext,0)


        def NEWLINE(self):
            return self.getToken(RESTParser.NEWLINE, 0)

        def getRuleIndex(self):
            return RESTParser.RULE_paragraph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParagraph" ):
                listener.enterParagraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParagraph" ):
                listener.exitParagraph(self)




    def paragraph(self):

        localctx = RESTParser.ParagraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paragraph)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.firstParagraphElement()
            self.state = 95
            self.paragraphElements()
            self.state = 96
            self.match(RESTParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabeledParagraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(RESTParser.LabelContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(RESTParser.NEWLINE)
            else:
                return self.getToken(RESTParser.NEWLINE, i)

        def paragraph(self):
            return self.getTypedRuleContext(RESTParser.ParagraphContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_labeledParagraph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeledParagraph" ):
                listener.enterLabeledParagraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeledParagraph" ):
                listener.exitLabeledParagraph(self)




    def labeledParagraph(self):

        localctx = RESTParser.LabeledParagraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_labeledParagraph)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.label()
            self.state = 99
            self.match(RESTParser.NEWLINE)
            self.state = 100
            self.match(RESTParser.NEWLINE)
            self.state = 101
            self.paragraph()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_0(self):
            return self.getToken(RESTParser.TERM_0, 0)

        def id_(self):
            return self.getTypedRuleContext(RESTParser.IdContext,0)


        def TERM_1(self):
            return self.getToken(RESTParser.TERM_1, 0)

        def getRuleIndex(self):
            return RESTParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = RESTParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(RESTParser.TERM_0)
            self.state = 104
            self.id_()
            self.state = 105
            self.match(RESTParser.TERM_1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParagraphElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paragraphElement(self):
            return self.getTypedRuleContext(RESTParser.ParagraphElementContext,0)


        def paragraphElements(self):
            return self.getTypedRuleContext(RESTParser.ParagraphElementsContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_paragraphElements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParagraphElements" ):
                listener.enterParagraphElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParagraphElements" ):
                listener.exitParagraphElements(self)




    def paragraphElements(self):

        localctx = RESTParser.ParagraphElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paragraphElements)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.paragraphElement()
                self.state = 108
                self.paragraphElements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.paragraphElement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FirstParagraphElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paragraphCharsNoSpace(self):
            return self.getTypedRuleContext(RESTParser.ParagraphCharsNoSpaceContext,0)


        def internalReferenceNoSpace(self):
            return self.getTypedRuleContext(RESTParser.InternalReferenceNoSpaceContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_firstParagraphElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFirstParagraphElement" ):
                listener.enterFirstParagraphElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFirstParagraphElement" ):
                listener.exitFirstParagraphElement(self)




    def firstParagraphElement(self):

        localctx = RESTParser.FirstParagraphElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_firstParagraphElement)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.paragraphCharsNoSpace()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.internalReferenceNoSpace()
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


    class ParagraphElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paragraphChars(self):
            return self.getTypedRuleContext(RESTParser.ParagraphCharsContext,0)


        def internalReference(self):
            return self.getTypedRuleContext(RESTParser.InternalReferenceContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_paragraphElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParagraphElement" ):
                listener.enterParagraphElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParagraphElement" ):
                listener.exitParagraphElement(self)




    def paragraphElement(self):

        localctx = RESTParser.ParagraphElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paragraphElement)
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.paragraphChars()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.internalReference()
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


    class InternalReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def presep(self):
            return self.getTypedRuleContext(RESTParser.PresepContext,0)


        def id_(self):
            return self.getTypedRuleContext(RESTParser.IdContext,0)


        def TERM_2(self):
            return self.getToken(RESTParser.TERM_2, 0)

        def postsep(self):
            return self.getTypedRuleContext(RESTParser.PostsepContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_internalReference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInternalReference" ):
                listener.enterInternalReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInternalReference" ):
                listener.exitInternalReference(self)




    def internalReference(self):

        localctx = RESTParser.InternalReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_internalReference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.presep()
            self.state = 122
            self.id_()
            self.state = 123
            self.match(RESTParser.TERM_2)
            self.state = 124
            self.postsep()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InternalReferenceNoSpaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(RESTParser.IdContext,0)


        def TERM_2(self):
            return self.getToken(RESTParser.TERM_2, 0)

        def postsep(self):
            return self.getTypedRuleContext(RESTParser.PostsepContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_internalReferenceNoSpace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInternalReferenceNoSpace" ):
                listener.enterInternalReferenceNoSpace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInternalReferenceNoSpace" ):
                listener.exitInternalReferenceNoSpace(self)




    def internalReferenceNoSpace(self):

        localctx = RESTParser.InternalReferenceNoSpaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_internalReferenceNoSpace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.id_()
            self.state = 127
            self.match(RESTParser.TERM_2)
            self.state = 128
            self.postsep()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumerationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumerationItems(self):
            return self.getTypedRuleContext(RESTParser.EnumerationItemsContext,0)


        def NEWLINE(self):
            return self.getToken(RESTParser.NEWLINE, 0)

        def getRuleIndex(self):
            return RESTParser.RULE_enumeration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumeration" ):
                listener.enterEnumeration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumeration" ):
                listener.exitEnumeration(self)




    def enumeration(self):

        localctx = RESTParser.EnumerationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_enumeration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.enumerationItems()
            self.state = 131
            self.match(RESTParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumerationItemsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumerationItem(self):
            return self.getTypedRuleContext(RESTParser.EnumerationItemContext,0)


        def NEWLINE(self):
            return self.getToken(RESTParser.NEWLINE, 0)

        def enumerationItems(self):
            return self.getTypedRuleContext(RESTParser.EnumerationItemsContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_enumerationItems

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumerationItems" ):
                listener.enterEnumerationItems(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumerationItems" ):
                listener.exitEnumerationItems(self)




    def enumerationItems(self):

        localctx = RESTParser.EnumerationItemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_enumerationItems)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.enumerationItem()
                self.state = 134
                self.match(RESTParser.NEWLINE)
                self.state = 135
                self.enumerationItems()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.enumerationItem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumerationItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(RESTParser.NumberContext,0)


        def TERM_3(self):
            return self.getToken(RESTParser.TERM_3, 0)

        def nobrString(self):
            return self.getTypedRuleContext(RESTParser.NobrStringContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_enumerationItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumerationItem" ):
                listener.enterEnumerationItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumerationItem" ):
                listener.exitEnumerationItem(self)




    def enumerationItem(self):

        localctx = RESTParser.EnumerationItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_enumerationItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.number()
            self.state = 141
            self.match(RESTParser.TERM_3)
            self.state = 142
            self.nobrString()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParagraphCharsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paragraphChar(self):
            return self.getTypedRuleContext(RESTParser.ParagraphCharContext,0)


        def paragraphChars(self):
            return self.getTypedRuleContext(RESTParser.ParagraphCharsContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_paragraphChars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParagraphChars" ):
                listener.enterParagraphChars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParagraphChars" ):
                listener.exitParagraphChars(self)




    def paragraphChars(self):

        localctx = RESTParser.ParagraphCharsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_paragraphChars)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.paragraphChar()
                self.state = 145
                self.paragraphChars()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.paragraphChar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParagraphCharsNoSpaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paragraphCharNoSpace(self):
            return self.getTypedRuleContext(RESTParser.ParagraphCharNoSpaceContext,0)


        def paragraphCharsNoSpace(self):
            return self.getTypedRuleContext(RESTParser.ParagraphCharsNoSpaceContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_paragraphCharsNoSpace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParagraphCharsNoSpace" ):
                listener.enterParagraphCharsNoSpace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParagraphCharsNoSpace" ):
                listener.exitParagraphCharsNoSpace(self)




    def paragraphCharsNoSpace(self):

        localctx = RESTParser.ParagraphCharsNoSpaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_paragraphCharsNoSpace)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.paragraphCharNoSpace()
                self.state = 151
                self.paragraphCharsNoSpace()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.paragraphCharNoSpace()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParagraphCharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAGRAPH_CHAR(self):
            return self.getToken(RESTParser.PARAGRAPH_CHAR, 0)

        def getRuleIndex(self):
            return RESTParser.RULE_paragraphChar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParagraphChar" ):
                listener.enterParagraphChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParagraphChar" ):
                listener.exitParagraphChar(self)




    def paragraphChar(self):

        localctx = RESTParser.ParagraphCharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_paragraphChar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(RESTParser.PARAGRAPH_CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParagraphCharNoSpaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAGRAPH_CHAR_NOSPACE(self):
            return self.getToken(RESTParser.PARAGRAPH_CHAR_NOSPACE, 0)

        def getRuleIndex(self):
            return RESTParser.RULE_paragraphCharNoSpace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParagraphCharNoSpace" ):
                listener.enterParagraphCharNoSpace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParagraphCharNoSpace" ):
                listener.exitParagraphCharNoSpace(self)




    def paragraphCharNoSpace(self):

        localctx = RESTParser.ParagraphCharNoSpaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_paragraphCharNoSpace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(RESTParser.PARAGRAPH_CHAR_NOSPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PresepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRESEP(self):
            return self.getToken(RESTParser.PRESEP, 0)

        def getRuleIndex(self):
            return RESTParser.RULE_presep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPresep" ):
                listener.enterPresep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPresep" ):
                listener.exitPresep(self)




    def presep(self):

        localctx = RESTParser.PresepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_presep)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(RESTParser.PRESEP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostsepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSTSEP(self):
            return self.getToken(RESTParser.POSTSEP, 0)

        def getRuleIndex(self):
            return RESTParser.RULE_postsep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostsep" ):
                listener.enterPostsep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostsep" ):
                listener.exitPostsep(self)




    def postsep(self):

        localctx = RESTParser.PostsepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_postsep)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(RESTParser.POSTSEP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RESTParser.ID, 0)

        def getRuleIndex(self):
            return RESTParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)




    def id_(self):

        localctx = RESTParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(RESTParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def digitNonZero(self):
            return self.getTypedRuleContext(RESTParser.DigitNonZeroContext,0)


        def digits(self):
            return self.getTypedRuleContext(RESTParser.DigitsContext,0)


        def digit(self):
            return self.getTypedRuleContext(RESTParser.DigitContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = RESTParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_number)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.digitNonZero()
                self.state = 167
                self.digits()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.digit()
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


    class DigitNonZeroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT_NONZERO(self):
            return self.getToken(RESTParser.DIGIT_NONZERO, 0)

        def getRuleIndex(self):
            return RESTParser.RULE_digitNonZero

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigitNonZero" ):
                listener.enterDigitNonZero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigitNonZero" ):
                listener.exitDigitNonZero(self)




    def digitNonZero(self):

        localctx = RESTParser.DigitNonZeroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_digitNonZero)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(RESTParser.DIGIT_NONZERO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DigitsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def digit(self):
            return self.getTypedRuleContext(RESTParser.DigitContext,0)


        def digits(self):
            return self.getTypedRuleContext(RESTParser.DigitsContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_digits

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigits" ):
                listener.enterDigits(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigits" ):
                listener.exitDigits(self)




    def digits(self):

        localctx = RESTParser.DigitsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_digits)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.digit()
                self.state = 175
                self.digits()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.digit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DigitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(RESTParser.DIGIT, 0)

        def getRuleIndex(self):
            return RESTParser.RULE_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigit" ):
                listener.enterDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigit" ):
                listener.exitDigit(self)




    def digit(self):

        localctx = RESTParser.DigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_digit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(RESTParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NobrStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nobrChar(self):
            return self.getTypedRuleContext(RESTParser.NobrCharContext,0)


        def nobrString(self):
            return self.getTypedRuleContext(RESTParser.NobrStringContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_nobrString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNobrString" ):
                listener.enterNobrString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNobrString" ):
                listener.exitNobrString(self)




    def nobrString(self):

        localctx = RESTParser.NobrStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_nobrString)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.nobrChar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.nobrChar()
                self.state = 184
                self.nobrString()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NobrCharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOBR_CHAR(self):
            return self.getToken(RESTParser.NOBR_CHAR, 0)

        def getRuleIndex(self):
            return RESTParser.RULE_nobrChar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNobrChar" ):
                listener.enterNobrChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNobrChar" ):
                listener.exitNobrChar(self)




    def nobrChar(self):

        localctx = RESTParser.NobrCharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_nobrChar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(RESTParser.NOBR_CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TitleFirstCharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TITLE_FIRST_CHAR(self):
            return self.getToken(RESTParser.TITLE_FIRST_CHAR, 0)

        def getRuleIndex(self):
            return RESTParser.RULE_titleFirstChar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTitleFirstChar" ):
                listener.enterTitleFirstChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTitleFirstChar" ):
                listener.exitTitleFirstChar(self)




    def titleFirstChar(self):

        localctx = RESTParser.TitleFirstCharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_titleFirstChar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(RESTParser.TITLE_FIRST_CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnderlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eqs(self):
            return self.getTypedRuleContext(RESTParser.EqsContext,0)


        def dashes(self):
            return self.getTypedRuleContext(RESTParser.DashesContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_underline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnderline" ):
                listener.enterUnderline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnderline" ):
                listener.exitUnderline(self)




    def underline(self):

        localctx = RESTParser.UnderlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_underline)
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.eqs()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.dashes()
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


    class EqsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_4(self):
            return self.getToken(RESTParser.TERM_4, 0)

        def eqs(self):
            return self.getTypedRuleContext(RESTParser.EqsContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_eqs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqs" ):
                listener.enterEqs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqs" ):
                listener.exitEqs(self)




    def eqs(self):

        localctx = RESTParser.EqsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_eqs)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(RESTParser.TERM_4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.match(RESTParser.TERM_4)
                self.state = 198
                self.eqs()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DashesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_5(self):
            return self.getToken(RESTParser.TERM_5, 0)

        def dashes(self):
            return self.getTypedRuleContext(RESTParser.DashesContext,0)


        def getRuleIndex(self):
            return RESTParser.RULE_dashes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDashes" ):
                listener.enterDashes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDashes" ):
                listener.exitDashes(self)




    def dashes(self):

        localctx = RESTParser.DashesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_dashes)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(RESTParser.TERM_5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.match(RESTParser.TERM_5)
                self.state = 203
                self.dashes()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





