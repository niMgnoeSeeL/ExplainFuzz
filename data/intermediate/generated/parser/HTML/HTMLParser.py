# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/HTML/HTMLParser.g4 by ANTLR 4.13.0
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
        4,1,23,130,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,3,0,30,8,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,0,3,0,39,8,
        0,1,0,5,0,42,8,0,10,0,12,0,45,9,0,1,0,5,0,48,8,0,10,0,12,0,51,9,
        0,1,0,1,0,1,1,1,1,1,2,5,2,58,8,2,10,2,12,2,61,9,2,1,2,1,2,5,2,65,
        8,2,10,2,12,2,68,9,2,1,3,1,3,1,3,5,3,73,8,3,10,3,12,3,76,9,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,85,8,3,1,3,3,3,88,8,3,1,3,1,3,1,3,3,
        3,93,8,3,1,4,3,4,96,8,4,1,4,1,4,1,4,3,4,101,8,4,1,4,3,4,104,8,4,
        5,4,106,8,4,10,4,12,4,109,9,4,1,5,1,5,1,5,3,5,114,8,5,1,6,1,6,1,
        7,1,7,3,7,120,8,7,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,0,0,11,
        0,2,4,6,8,10,12,14,16,18,20,0,5,1,0,6,7,2,0,7,7,11,11,1,0,1,2,1,
        0,18,19,1,0,20,21,139,0,25,1,0,0,0,2,54,1,0,0,0,4,59,1,0,0,0,6,92,
        1,0,0,0,8,95,1,0,0,0,10,110,1,0,0,0,12,115,1,0,0,0,14,119,1,0,0,
        0,16,121,1,0,0,0,18,123,1,0,0,0,20,126,1,0,0,0,22,24,3,2,1,0,23,
        22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,29,1,0,0,
        0,27,25,1,0,0,0,28,30,5,3,0,0,29,28,1,0,0,0,29,30,1,0,0,0,30,34,
        1,0,0,0,31,33,3,2,1,0,32,31,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,
        34,35,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,37,39,5,5,0,0,38,37,1,
        0,0,0,38,39,1,0,0,0,39,43,1,0,0,0,40,42,3,2,1,0,41,40,1,0,0,0,42,
        45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,49,1,0,0,0,45,43,1,0,0,
        0,46,48,3,4,2,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,
        1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,53,5,0,0,1,53,1,1,0,0,0,54,
        55,7,0,0,0,55,3,1,0,0,0,56,58,3,14,7,0,57,56,1,0,0,0,58,61,1,0,0,
        0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,66,
        3,6,3,0,63,65,3,14,7,0,64,63,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,
        66,67,1,0,0,0,67,5,1,0,0,0,68,66,1,0,0,0,69,70,5,10,0,0,70,74,5,
        16,0,0,71,73,3,10,5,0,72,71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,
        74,75,1,0,0,0,75,87,1,0,0,0,76,74,1,0,0,0,77,84,5,12,0,0,78,79,3,
        8,4,0,79,80,5,10,0,0,80,81,5,14,0,0,81,82,5,16,0,0,82,83,5,12,0,
        0,83,85,1,0,0,0,84,78,1,0,0,0,84,85,1,0,0,0,85,88,1,0,0,0,86,88,
        5,13,0,0,87,77,1,0,0,0,87,86,1,0,0,0,88,93,1,0,0,0,89,93,5,6,0,0,
        90,93,3,18,9,0,91,93,3,20,10,0,92,69,1,0,0,0,92,89,1,0,0,0,92,90,
        1,0,0,0,92,91,1,0,0,0,93,7,1,0,0,0,94,96,3,12,6,0,95,94,1,0,0,0,
        95,96,1,0,0,0,96,107,1,0,0,0,97,101,3,6,3,0,98,101,5,4,0,0,99,101,
        3,16,8,0,100,97,1,0,0,0,100,98,1,0,0,0,100,99,1,0,0,0,101,103,1,
        0,0,0,102,104,3,12,6,0,103,102,1,0,0,0,103,104,1,0,0,0,104,106,1,
        0,0,0,105,100,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,
        0,0,0,108,9,1,0,0,0,109,107,1,0,0,0,110,113,5,16,0,0,111,112,5,15,
        0,0,112,114,5,22,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,11,1,0,
        0,0,115,116,7,1,0,0,116,13,1,0,0,0,117,120,3,16,8,0,118,120,5,7,
        0,0,119,117,1,0,0,0,119,118,1,0,0,0,120,15,1,0,0,0,121,122,7,2,0,
        0,122,17,1,0,0,0,123,124,5,8,0,0,124,125,7,3,0,0,125,19,1,0,0,0,
        126,127,5,9,0,0,127,128,7,4,0,0,128,21,1,0,0,0,18,25,29,34,38,43,
        49,59,66,74,84,87,92,95,100,103,107,113,119
    ]

class HTMLParser ( Parser ):

    grammarFileName = "HTMLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<'", "<INVALID>", "'>'", 
                     "'/>'", "'/'", "'='" ]

    symbolicNames = [ "<INVALID>", "HTML_COMMENT", "HTML_CONDITIONAL_COMMENT", 
                      "XML", "CDATA", "DTD", "SCRIPTLET", "SEA_WS", "SCRIPT_OPEN", 
                      "STYLE_OPEN", "TAG_OPEN", "HTML_TEXT", "TAG_CLOSE", 
                      "TAG_SLASH_CLOSE", "TAG_SLASH", "TAG_EQUALS", "TAG_NAME", 
                      "TAG_WHITESPACE", "SCRIPT_BODY", "SCRIPT_SHORT_BODY", 
                      "STYLE_BODY", "STYLE_SHORT_BODY", "ATTVALUE_VALUE", 
                      "ATTRIBUTE" ]

    RULE_htmlDocument = 0
    RULE_scriptletOrSeaWs = 1
    RULE_htmlElements = 2
    RULE_htmlElement = 3
    RULE_htmlContent = 4
    RULE_htmlAttribute = 5
    RULE_htmlChardata = 6
    RULE_htmlMisc = 7
    RULE_htmlComment = 8
    RULE_script = 9
    RULE_style = 10

    ruleNames =  [ "htmlDocument", "scriptletOrSeaWs", "htmlElements", "htmlElement", 
                   "htmlContent", "htmlAttribute", "htmlChardata", "htmlMisc", 
                   "htmlComment", "script", "style" ]

    EOF = Token.EOF
    HTML_COMMENT=1
    HTML_CONDITIONAL_COMMENT=2
    XML=3
    CDATA=4
    DTD=5
    SCRIPTLET=6
    SEA_WS=7
    SCRIPT_OPEN=8
    STYLE_OPEN=9
    TAG_OPEN=10
    HTML_TEXT=11
    TAG_CLOSE=12
    TAG_SLASH_CLOSE=13
    TAG_SLASH=14
    TAG_EQUALS=15
    TAG_NAME=16
    TAG_WHITESPACE=17
    SCRIPT_BODY=18
    SCRIPT_SHORT_BODY=19
    STYLE_BODY=20
    STYLE_SHORT_BODY=21
    ATTVALUE_VALUE=22
    ATTRIBUTE=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class HtmlDocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(HTMLParser.EOF, 0)

        def scriptletOrSeaWs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParser.ScriptletOrSeaWsContext)
            else:
                return self.getTypedRuleContext(HTMLParser.ScriptletOrSeaWsContext,i)


        def XML(self):
            return self.getToken(HTMLParser.XML, 0)

        def DTD(self):
            return self.getToken(HTMLParser.DTD, 0)

        def htmlElements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParser.HtmlElementsContext)
            else:
                return self.getTypedRuleContext(HTMLParser.HtmlElementsContext,i)


        def getRuleIndex(self):
            return HTMLParser.RULE_htmlDocument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlDocument" ):
                listener.enterHtmlDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlDocument" ):
                listener.exitHtmlDocument(self)




    def htmlDocument(self):

        localctx = HTMLParser.HtmlDocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_htmlDocument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 22
                    self.scriptletOrSeaWs() 
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 28
                self.match(HTMLParser.XML)


            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 31
                    self.scriptletOrSeaWs() 
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 37
                self.match(HTMLParser.DTD)


            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 40
                    self.scriptletOrSeaWs() 
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1990) != 0):
                self.state = 46
                self.htmlElements()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(HTMLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScriptletOrSeaWsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCRIPTLET(self):
            return self.getToken(HTMLParser.SCRIPTLET, 0)

        def SEA_WS(self):
            return self.getToken(HTMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_scriptletOrSeaWs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScriptletOrSeaWs" ):
                listener.enterScriptletOrSeaWs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScriptletOrSeaWs" ):
                listener.exitScriptletOrSeaWs(self)




    def scriptletOrSeaWs(self):

        localctx = HTMLParser.ScriptletOrSeaWsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_scriptletOrSeaWs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HtmlElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def htmlElement(self):
            return self.getTypedRuleContext(HTMLParser.HtmlElementContext,0)


        def htmlMisc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParser.HtmlMiscContext)
            else:
                return self.getTypedRuleContext(HTMLParser.HtmlMiscContext,i)


        def getRuleIndex(self):
            return HTMLParser.RULE_htmlElements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlElements" ):
                listener.enterHtmlElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlElements" ):
                listener.exitHtmlElements(self)




    def htmlElements(self):

        localctx = HTMLParser.HtmlElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_htmlElements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134) != 0):
                self.state = 56
                self.htmlMisc()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.htmlElement()
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 63
                    self.htmlMisc() 
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HtmlElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAG_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLParser.TAG_OPEN)
            else:
                return self.getToken(HTMLParser.TAG_OPEN, i)

        def TAG_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLParser.TAG_NAME)
            else:
                return self.getToken(HTMLParser.TAG_NAME, i)

        def TAG_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLParser.TAG_CLOSE)
            else:
                return self.getToken(HTMLParser.TAG_CLOSE, i)

        def TAG_SLASH_CLOSE(self):
            return self.getToken(HTMLParser.TAG_SLASH_CLOSE, 0)

        def htmlAttribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParser.HtmlAttributeContext)
            else:
                return self.getTypedRuleContext(HTMLParser.HtmlAttributeContext,i)


        def htmlContent(self):
            return self.getTypedRuleContext(HTMLParser.HtmlContentContext,0)


        def TAG_SLASH(self):
            return self.getToken(HTMLParser.TAG_SLASH, 0)

        def SCRIPTLET(self):
            return self.getToken(HTMLParser.SCRIPTLET, 0)

        def script(self):
            return self.getTypedRuleContext(HTMLParser.ScriptContext,0)


        def style(self):
            return self.getTypedRuleContext(HTMLParser.StyleContext,0)


        def getRuleIndex(self):
            return HTMLParser.RULE_htmlElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlElement" ):
                listener.enterHtmlElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlElement" ):
                listener.exitHtmlElement(self)




    def htmlElement(self):

        localctx = HTMLParser.HtmlElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_htmlElement)
        self._la = 0 # Token type
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(HTMLParser.TAG_OPEN)
                self.state = 70
                self.match(HTMLParser.TAG_NAME)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 71
                    self.htmlAttribute()
                    self.state = 76
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 87
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12]:
                    self.state = 77
                    self.match(HTMLParser.TAG_CLOSE)
                    self.state = 84
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        self.state = 78
                        self.htmlContent()
                        self.state = 79
                        self.match(HTMLParser.TAG_OPEN)
                        self.state = 80
                        self.match(HTMLParser.TAG_SLASH)
                        self.state = 81
                        self.match(HTMLParser.TAG_NAME)
                        self.state = 82
                        self.match(HTMLParser.TAG_CLOSE)


                    pass
                elif token in [13]:
                    self.state = 86
                    self.match(HTMLParser.TAG_SLASH_CLOSE)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.match(HTMLParser.SCRIPTLET)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.script()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.style()
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


    class HtmlContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def htmlChardata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParser.HtmlChardataContext)
            else:
                return self.getTypedRuleContext(HTMLParser.HtmlChardataContext,i)


        def htmlElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParser.HtmlElementContext)
            else:
                return self.getTypedRuleContext(HTMLParser.HtmlElementContext,i)


        def CDATA(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLParser.CDATA)
            else:
                return self.getToken(HTMLParser.CDATA, i)

        def htmlComment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParser.HtmlCommentContext)
            else:
                return self.getTypedRuleContext(HTMLParser.HtmlCommentContext,i)


        def getRuleIndex(self):
            return HTMLParser.RULE_htmlContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlContent" ):
                listener.enterHtmlContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlContent" ):
                listener.exitHtmlContent(self)




    def htmlContent(self):

        localctx = HTMLParser.HtmlContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_htmlContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==11:
                self.state = 94
                self.htmlChardata()


            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 100
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [6, 8, 9, 10]:
                        self.state = 97
                        self.htmlElement()
                        pass
                    elif token in [4]:
                        self.state = 98
                        self.match(HTMLParser.CDATA)
                        pass
                    elif token in [1, 2]:
                        self.state = 99
                        self.htmlComment()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 103
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==7 or _la==11:
                        self.state = 102
                        self.htmlChardata()

             
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HtmlAttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAG_NAME(self):
            return self.getToken(HTMLParser.TAG_NAME, 0)

        def TAG_EQUALS(self):
            return self.getToken(HTMLParser.TAG_EQUALS, 0)

        def ATTVALUE_VALUE(self):
            return self.getToken(HTMLParser.ATTVALUE_VALUE, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_htmlAttribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlAttribute" ):
                listener.enterHtmlAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlAttribute" ):
                listener.exitHtmlAttribute(self)




    def htmlAttribute(self):

        localctx = HTMLParser.HtmlAttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_htmlAttribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(HTMLParser.TAG_NAME)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 111
                self.match(HTMLParser.TAG_EQUALS)
                self.state = 112
                self.match(HTMLParser.ATTVALUE_VALUE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HtmlChardataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HTML_TEXT(self):
            return self.getToken(HTMLParser.HTML_TEXT, 0)

        def SEA_WS(self):
            return self.getToken(HTMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_htmlChardata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlChardata" ):
                listener.enterHtmlChardata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlChardata" ):
                listener.exitHtmlChardata(self)




    def htmlChardata(self):

        localctx = HTMLParser.HtmlChardataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_htmlChardata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not(_la==7 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HtmlMiscContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def htmlComment(self):
            return self.getTypedRuleContext(HTMLParser.HtmlCommentContext,0)


        def SEA_WS(self):
            return self.getToken(HTMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_htmlMisc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlMisc" ):
                listener.enterHtmlMisc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlMisc" ):
                listener.exitHtmlMisc(self)




    def htmlMisc(self):

        localctx = HTMLParser.HtmlMiscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_htmlMisc)
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.htmlComment()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(HTMLParser.SEA_WS)
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


    class HtmlCommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HTML_COMMENT(self):
            return self.getToken(HTMLParser.HTML_COMMENT, 0)

        def HTML_CONDITIONAL_COMMENT(self):
            return self.getToken(HTMLParser.HTML_CONDITIONAL_COMMENT, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_htmlComment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlComment" ):
                listener.enterHtmlComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlComment" ):
                listener.exitHtmlComment(self)




    def htmlComment(self):

        localctx = HTMLParser.HtmlCommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_htmlComment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCRIPT_OPEN(self):
            return self.getToken(HTMLParser.SCRIPT_OPEN, 0)

        def SCRIPT_BODY(self):
            return self.getToken(HTMLParser.SCRIPT_BODY, 0)

        def SCRIPT_SHORT_BODY(self):
            return self.getToken(HTMLParser.SCRIPT_SHORT_BODY, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)




    def script(self):

        localctx = HTMLParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(HTMLParser.SCRIPT_OPEN)
            self.state = 124
            _la = self._input.LA(1)
            if not(_la==18 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StyleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STYLE_OPEN(self):
            return self.getToken(HTMLParser.STYLE_OPEN, 0)

        def STYLE_BODY(self):
            return self.getToken(HTMLParser.STYLE_BODY, 0)

        def STYLE_SHORT_BODY(self):
            return self.getToken(HTMLParser.STYLE_SHORT_BODY, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_style

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStyle" ):
                listener.enterStyle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStyle" ):
                listener.exitStyle(self)




    def style(self):

        localctx = HTMLParser.StyleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_style)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(HTMLParser.STYLE_OPEN)
            self.state = 127
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





