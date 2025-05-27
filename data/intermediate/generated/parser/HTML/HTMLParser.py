# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/HTML/HTMLParser.g4 by ANTLR 4.11.1
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
        4,1,23,397,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,3,0,153,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,181,8,1,1,2,1,2,3,2,185,8,2,1,3,1,3,3,3,189,8,3,1,4,1,4,1,4,1,
        4,1,4,3,4,196,8,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,223,8,
        6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,231,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,
        9,1,9,1,9,3,9,242,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,251,
        8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,3,11,266,8,11,1,12,1,12,1,12,1,12,1,12,3,12,273,8,12,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,3,13,291,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,312,8,
        14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,3,15,342,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,3,16,366,8,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,
        19,3,19,377,8,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,
        24,1,24,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,0,0,28,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,
        54,0,6,1,0,6,7,2,0,7,7,11,11,2,0,1,2,7,7,1,0,1,2,1,0,18,19,1,0,20,
        21,450,0,152,1,0,0,0,2,180,1,0,0,0,4,184,1,0,0,0,6,188,1,0,0,0,8,
        195,1,0,0,0,10,197,1,0,0,0,12,222,1,0,0,0,14,230,1,0,0,0,16,232,
        1,0,0,0,18,241,1,0,0,0,20,250,1,0,0,0,22,265,1,0,0,0,24,272,1,0,
        0,0,26,290,1,0,0,0,28,311,1,0,0,0,30,341,1,0,0,0,32,365,1,0,0,0,
        34,367,1,0,0,0,36,370,1,0,0,0,38,376,1,0,0,0,40,378,1,0,0,0,42,380,
        1,0,0,0,44,382,1,0,0,0,46,384,1,0,0,0,48,386,1,0,0,0,50,389,1,0,
        0,0,52,391,1,0,0,0,54,394,1,0,0,0,56,57,3,8,4,0,57,58,3,6,3,0,58,
        59,3,8,4,0,59,60,3,4,2,0,60,61,3,8,4,0,61,62,3,2,1,0,62,63,5,0,0,
        1,63,153,1,0,0,0,64,65,3,8,4,0,65,66,3,6,3,0,66,67,3,8,4,0,67,68,
        3,4,2,0,68,69,3,8,4,0,69,70,5,0,0,1,70,153,1,0,0,0,71,72,3,6,3,0,
        72,73,3,4,2,0,73,74,3,8,4,0,74,75,3,2,1,0,75,76,5,0,0,1,76,153,1,
        0,0,0,77,78,3,8,4,0,78,79,3,6,3,0,79,80,3,4,2,0,80,81,3,2,1,0,81,
        82,5,0,0,1,82,153,1,0,0,0,83,84,3,6,3,0,84,85,3,4,2,0,85,86,3,2,
        1,0,86,87,5,0,0,1,87,153,1,0,0,0,88,89,3,8,4,0,89,90,3,6,3,0,90,
        91,3,4,2,0,91,92,3,8,4,0,92,93,3,2,1,0,93,94,5,0,0,1,94,153,1,0,
        0,0,95,96,3,6,3,0,96,97,3,4,2,0,97,98,3,8,4,0,98,99,5,0,0,1,99,153,
        1,0,0,0,100,101,3,8,4,0,101,102,3,6,3,0,102,103,3,4,2,0,103,104,
        3,8,4,0,104,105,5,0,0,1,105,153,1,0,0,0,106,107,3,6,3,0,107,108,
        3,4,2,0,108,109,5,0,0,1,109,153,1,0,0,0,110,111,3,6,3,0,111,112,
        3,8,4,0,112,113,3,4,2,0,113,114,3,2,1,0,114,115,5,0,0,1,115,153,
        1,0,0,0,116,117,3,8,4,0,117,118,3,6,3,0,118,119,3,8,4,0,119,120,
        3,4,2,0,120,121,3,2,1,0,121,122,5,0,0,1,122,153,1,0,0,0,123,124,
        3,6,3,0,124,125,3,8,4,0,125,126,3,4,2,0,126,127,3,8,4,0,127,128,
        5,0,0,1,128,153,1,0,0,0,129,130,3,8,4,0,130,131,3,6,3,0,131,132,
        3,8,4,0,132,133,3,4,2,0,133,134,5,0,0,1,134,153,1,0,0,0,135,136,
        3,6,3,0,136,137,3,8,4,0,137,138,3,4,2,0,138,139,5,0,0,1,139,153,
        1,0,0,0,140,141,3,6,3,0,141,142,3,8,4,0,142,143,3,4,2,0,143,144,
        3,8,4,0,144,145,3,2,1,0,145,146,5,0,0,1,146,153,1,0,0,0,147,148,
        3,8,4,0,148,149,3,6,3,0,149,150,3,4,2,0,150,151,5,0,0,1,151,153,
        1,0,0,0,152,56,1,0,0,0,152,64,1,0,0,0,152,71,1,0,0,0,152,77,1,0,
        0,0,152,83,1,0,0,0,152,88,1,0,0,0,152,95,1,0,0,0,152,100,1,0,0,0,
        152,106,1,0,0,0,152,110,1,0,0,0,152,116,1,0,0,0,152,123,1,0,0,0,
        152,129,1,0,0,0,152,135,1,0,0,0,152,140,1,0,0,0,152,147,1,0,0,0,
        153,1,1,0,0,0,154,155,3,12,6,0,155,156,3,2,1,0,156,181,1,0,0,0,157,
        158,3,14,7,0,158,159,3,22,11,0,159,160,3,14,7,0,160,181,1,0,0,0,
        161,162,3,14,7,0,162,163,3,22,11,0,163,181,1,0,0,0,164,165,3,22,
        11,0,165,166,3,14,7,0,166,181,1,0,0,0,167,168,5,10,0,0,168,169,5,
        16,0,0,169,170,3,24,12,0,170,171,3,18,9,0,171,181,1,0,0,0,172,181,
        5,6,0,0,173,174,5,8,0,0,174,181,3,46,23,0,175,176,5,9,0,0,176,181,
        3,50,25,0,177,178,5,10,0,0,178,179,5,16,0,0,179,181,3,18,9,0,180,
        154,1,0,0,0,180,157,1,0,0,0,180,161,1,0,0,0,180,164,1,0,0,0,180,
        167,1,0,0,0,180,172,1,0,0,0,180,173,1,0,0,0,180,175,1,0,0,0,180,
        177,1,0,0,0,181,3,1,0,0,0,182,185,5,5,0,0,183,185,1,0,0,0,184,182,
        1,0,0,0,184,183,1,0,0,0,185,5,1,0,0,0,186,189,5,3,0,0,187,189,1,
        0,0,0,188,186,1,0,0,0,188,187,1,0,0,0,189,7,1,0,0,0,190,191,3,10,
        5,0,191,192,3,8,4,0,192,196,1,0,0,0,193,196,5,6,0,0,194,196,5,7,
        0,0,195,190,1,0,0,0,195,193,1,0,0,0,195,194,1,0,0,0,196,9,1,0,0,
        0,197,198,7,0,0,0,198,11,1,0,0,0,199,200,3,14,7,0,200,201,3,22,11,
        0,201,202,3,14,7,0,202,223,1,0,0,0,203,204,3,14,7,0,204,205,3,22,
        11,0,205,223,1,0,0,0,206,207,3,22,11,0,207,208,3,14,7,0,208,223,
        1,0,0,0,209,210,5,10,0,0,210,211,5,16,0,0,211,212,3,24,12,0,212,
        213,3,18,9,0,213,223,1,0,0,0,214,223,5,6,0,0,215,216,5,8,0,0,216,
        223,3,46,23,0,217,218,5,9,0,0,218,223,3,50,25,0,219,220,5,10,0,0,
        220,221,5,16,0,0,221,223,3,18,9,0,222,199,1,0,0,0,222,203,1,0,0,
        0,222,206,1,0,0,0,222,209,1,0,0,0,222,214,1,0,0,0,222,215,1,0,0,
        0,222,217,1,0,0,0,222,219,1,0,0,0,223,13,1,0,0,0,224,225,3,42,21,
        0,225,226,3,14,7,0,226,231,1,0,0,0,227,231,5,7,0,0,228,231,5,1,0,
        0,229,231,5,2,0,0,230,224,1,0,0,0,230,227,1,0,0,0,230,228,1,0,0,
        0,230,229,1,0,0,0,231,15,1,0,0,0,232,233,3,30,15,0,233,234,5,10,
        0,0,234,235,5,14,0,0,235,236,5,16,0,0,236,237,5,12,0,0,237,17,1,
        0,0,0,238,239,5,12,0,0,239,242,3,20,10,0,240,242,5,13,0,0,241,238,
        1,0,0,0,241,240,1,0,0,0,242,19,1,0,0,0,243,251,1,0,0,0,244,245,3,
        30,15,0,245,246,5,10,0,0,246,247,5,14,0,0,247,248,5,16,0,0,248,249,
        5,12,0,0,249,251,1,0,0,0,250,243,1,0,0,0,250,244,1,0,0,0,251,21,
        1,0,0,0,252,253,5,10,0,0,253,254,5,16,0,0,254,255,3,24,12,0,255,
        256,3,18,9,0,256,266,1,0,0,0,257,266,5,6,0,0,258,259,5,8,0,0,259,
        266,3,46,23,0,260,261,5,9,0,0,261,266,3,50,25,0,262,263,5,10,0,0,
        263,264,5,16,0,0,264,266,3,18,9,0,265,252,1,0,0,0,265,257,1,0,0,
        0,265,258,1,0,0,0,265,260,1,0,0,0,265,262,1,0,0,0,266,23,1,0,0,0,
        267,268,3,36,18,0,268,269,3,24,12,0,269,273,1,0,0,0,270,271,5,16,
        0,0,271,273,3,38,19,0,272,267,1,0,0,0,272,270,1,0,0,0,273,25,1,0,
        0,0,274,291,5,4,0,0,275,276,5,10,0,0,276,277,5,16,0,0,277,278,3,
        24,12,0,278,279,3,18,9,0,279,291,1,0,0,0,280,291,5,6,0,0,281,291,
        5,1,0,0,282,291,5,2,0,0,283,284,5,8,0,0,284,291,3,46,23,0,285,286,
        5,9,0,0,286,291,3,50,25,0,287,288,5,10,0,0,288,289,5,16,0,0,289,
        291,3,18,9,0,290,274,1,0,0,0,290,275,1,0,0,0,290,280,1,0,0,0,290,
        281,1,0,0,0,290,282,1,0,0,0,290,283,1,0,0,0,290,285,1,0,0,0,290,
        287,1,0,0,0,291,27,1,0,0,0,292,293,3,26,13,0,293,294,3,54,27,0,294,
        312,1,0,0,0,295,312,5,4,0,0,296,297,5,10,0,0,297,298,5,16,0,0,298,
        299,3,24,12,0,299,300,3,18,9,0,300,312,1,0,0,0,301,312,5,6,0,0,302,
        312,5,1,0,0,303,312,5,2,0,0,304,305,5,8,0,0,305,312,3,46,23,0,306,
        307,5,9,0,0,307,312,3,50,25,0,308,309,5,10,0,0,309,310,5,16,0,0,
        310,312,3,18,9,0,311,292,1,0,0,0,311,295,1,0,0,0,311,296,1,0,0,0,
        311,301,1,0,0,0,311,302,1,0,0,0,311,303,1,0,0,0,311,304,1,0,0,0,
        311,306,1,0,0,0,311,308,1,0,0,0,312,29,1,0,0,0,313,314,3,54,27,0,
        314,315,3,32,16,0,315,342,1,0,0,0,316,317,3,28,14,0,317,318,3,32,
        16,0,318,342,1,0,0,0,319,342,1,0,0,0,320,321,3,26,13,0,321,322,3,
        54,27,0,322,342,1,0,0,0,323,342,5,4,0,0,324,325,5,10,0,0,325,326,
        5,16,0,0,326,327,3,24,12,0,327,328,3,18,9,0,328,342,1,0,0,0,329,
        342,5,6,0,0,330,342,5,1,0,0,331,342,5,2,0,0,332,333,5,8,0,0,333,
        342,3,46,23,0,334,335,5,9,0,0,335,342,3,50,25,0,336,337,5,10,0,0,
        337,338,5,16,0,0,338,342,3,18,9,0,339,342,5,11,0,0,340,342,5,7,0,
        0,341,313,1,0,0,0,341,316,1,0,0,0,341,319,1,0,0,0,341,320,1,0,0,
        0,341,323,1,0,0,0,341,324,1,0,0,0,341,329,1,0,0,0,341,330,1,0,0,
        0,341,331,1,0,0,0,341,332,1,0,0,0,341,334,1,0,0,0,341,336,1,0,0,
        0,341,339,1,0,0,0,341,340,1,0,0,0,342,31,1,0,0,0,343,344,3,28,14,
        0,344,345,3,32,16,0,345,366,1,0,0,0,346,347,3,26,13,0,347,348,3,
        54,27,0,348,366,1,0,0,0,349,366,5,4,0,0,350,351,5,10,0,0,351,352,
        5,16,0,0,352,353,3,24,12,0,353,354,3,18,9,0,354,366,1,0,0,0,355,
        366,5,6,0,0,356,366,5,1,0,0,357,366,5,2,0,0,358,359,5,8,0,0,359,
        366,3,46,23,0,360,361,5,9,0,0,361,366,3,50,25,0,362,363,5,10,0,0,
        363,364,5,16,0,0,364,366,3,18,9,0,365,343,1,0,0,0,365,346,1,0,0,
        0,365,349,1,0,0,0,365,350,1,0,0,0,365,355,1,0,0,0,365,356,1,0,0,
        0,365,357,1,0,0,0,365,358,1,0,0,0,365,360,1,0,0,0,365,362,1,0,0,
        0,366,33,1,0,0,0,367,368,5,15,0,0,368,369,5,22,0,0,369,35,1,0,0,
        0,370,371,5,16,0,0,371,372,3,38,19,0,372,37,1,0,0,0,373,377,1,0,
        0,0,374,375,5,15,0,0,375,377,5,22,0,0,376,373,1,0,0,0,376,374,1,
        0,0,0,377,39,1,0,0,0,378,379,7,1,0,0,379,41,1,0,0,0,380,381,7,2,
        0,0,381,43,1,0,0,0,382,383,7,3,0,0,383,45,1,0,0,0,384,385,7,4,0,
        0,385,47,1,0,0,0,386,387,5,8,0,0,387,388,3,46,23,0,388,49,1,0,0,
        0,389,390,7,5,0,0,390,51,1,0,0,0,391,392,5,9,0,0,392,393,3,50,25,
        0,393,53,1,0,0,0,394,395,7,1,0,0,395,55,1,0,0,0,16,152,180,184,188,
        195,222,230,241,250,265,272,290,311,341,365,376
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
    RULE_htmlelements_star = 1
    RULE_dtd_question = 2
    RULE_xml_question = 3
    RULE_scriptletorseaws_star = 4
    RULE_scriptletOrSeaWs = 5
    RULE_htmlElements = 6
    RULE_htmlmisc_star = 7
    RULE_block_7 = 8
    RULE_block_0 = 9
    RULE_block_7_question = 10
    RULE_htmlElement = 11
    RULE_htmlattribute_star = 12
    RULE_block_8 = 13
    RULE_block_2 = 14
    RULE_htmlContent = 15
    RULE_block_2_star = 16
    RULE_block_4 = 17
    RULE_htmlAttribute = 18
    RULE_block_4_question = 19
    RULE_htmlChardata = 20
    RULE_htmlMisc = 21
    RULE_htmlComment = 22
    RULE_block_5 = 23
    RULE_script = 24
    RULE_block_6 = 25
    RULE_style = 26
    RULE_htmlchardata_question = 27

    ruleNames =  [ "htmlDocument", "htmlelements_star", "dtd_question", 
                   "xml_question", "scriptletorseaws_star", "scriptletOrSeaWs", 
                   "htmlElements", "htmlmisc_star", "block_7", "block_0", 
                   "block_7_question", "htmlElement", "htmlattribute_star", 
                   "block_8", "block_2", "htmlContent", "block_2_star", 
                   "block_4", "htmlAttribute", "block_4_question", "htmlChardata", 
                   "htmlMisc", "htmlComment", "block_5", "script", "block_6", 
                   "style", "htmlchardata_question" ]

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
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class HtmlDocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scriptletorseaws_star(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParser.Scriptletorseaws_starContext)
            else:
                return self.getTypedRuleContext(HTMLParser.Scriptletorseaws_starContext,i)


        def xml_question(self):
            return self.getTypedRuleContext(HTMLParser.Xml_questionContext,0)


        def dtd_question(self):
            return self.getTypedRuleContext(HTMLParser.Dtd_questionContext,0)


        def htmlelements_star(self):
            return self.getTypedRuleContext(HTMLParser.Htmlelements_starContext,0)


        def EOF(self):
            return self.getToken(HTMLParser.EOF, 0)

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
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.scriptletorseaws_star()
                self.state = 57
                self.xml_question()
                self.state = 58
                self.scriptletorseaws_star()
                self.state = 59
                self.dtd_question()
                self.state = 60
                self.scriptletorseaws_star()
                self.state = 61
                self.htmlelements_star()
                self.state = 62
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.scriptletorseaws_star()
                self.state = 65
                self.xml_question()
                self.state = 66
                self.scriptletorseaws_star()
                self.state = 67
                self.dtd_question()
                self.state = 68
                self.scriptletorseaws_star()
                self.state = 69
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.xml_question()
                self.state = 72
                self.dtd_question()
                self.state = 73
                self.scriptletorseaws_star()
                self.state = 74
                self.htmlelements_star()
                self.state = 75
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.scriptletorseaws_star()
                self.state = 78
                self.xml_question()
                self.state = 79
                self.dtd_question()
                self.state = 80
                self.htmlelements_star()
                self.state = 81
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 83
                self.xml_question()
                self.state = 84
                self.dtd_question()
                self.state = 85
                self.htmlelements_star()
                self.state = 86
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.scriptletorseaws_star()
                self.state = 89
                self.xml_question()
                self.state = 90
                self.dtd_question()
                self.state = 91
                self.scriptletorseaws_star()
                self.state = 92
                self.htmlelements_star()
                self.state = 93
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 95
                self.xml_question()
                self.state = 96
                self.dtd_question()
                self.state = 97
                self.scriptletorseaws_star()
                self.state = 98
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 100
                self.scriptletorseaws_star()
                self.state = 101
                self.xml_question()
                self.state = 102
                self.dtd_question()
                self.state = 103
                self.scriptletorseaws_star()
                self.state = 104
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 106
                self.xml_question()
                self.state = 107
                self.dtd_question()
                self.state = 108
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 110
                self.xml_question()
                self.state = 111
                self.scriptletorseaws_star()
                self.state = 112
                self.dtd_question()
                self.state = 113
                self.htmlelements_star()
                self.state = 114
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 116
                self.scriptletorseaws_star()
                self.state = 117
                self.xml_question()
                self.state = 118
                self.scriptletorseaws_star()
                self.state = 119
                self.dtd_question()
                self.state = 120
                self.htmlelements_star()
                self.state = 121
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 123
                self.xml_question()
                self.state = 124
                self.scriptletorseaws_star()
                self.state = 125
                self.dtd_question()
                self.state = 126
                self.scriptletorseaws_star()
                self.state = 127
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 129
                self.scriptletorseaws_star()
                self.state = 130
                self.xml_question()
                self.state = 131
                self.scriptletorseaws_star()
                self.state = 132
                self.dtd_question()
                self.state = 133
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 135
                self.xml_question()
                self.state = 136
                self.scriptletorseaws_star()
                self.state = 137
                self.dtd_question()
                self.state = 138
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 140
                self.xml_question()
                self.state = 141
                self.scriptletorseaws_star()
                self.state = 142
                self.dtd_question()
                self.state = 143
                self.scriptletorseaws_star()
                self.state = 144
                self.htmlelements_star()
                self.state = 145
                self.match(HTMLParser.EOF)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 147
                self.scriptletorseaws_star()
                self.state = 148
                self.xml_question()
                self.state = 149
                self.dtd_question()
                self.state = 150
                self.match(HTMLParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Htmlelements_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def htmlElements(self):
            return self.getTypedRuleContext(HTMLParser.HtmlElementsContext,0)


        def htmlelements_star(self):
            return self.getTypedRuleContext(HTMLParser.Htmlelements_starContext,0)


        def htmlmisc_star(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParser.Htmlmisc_starContext)
            else:
                return self.getTypedRuleContext(HTMLParser.Htmlmisc_starContext,i)


        def htmlElement(self):
            return self.getTypedRuleContext(HTMLParser.HtmlElementContext,0)


        def TAG_OPEN(self):
            return self.getToken(HTMLParser.TAG_OPEN, 0)

        def TAG_NAME(self):
            return self.getToken(HTMLParser.TAG_NAME, 0)

        def htmlattribute_star(self):
            return self.getTypedRuleContext(HTMLParser.Htmlattribute_starContext,0)


        def block_0(self):
            return self.getTypedRuleContext(HTMLParser.Block_0Context,0)


        def SCRIPTLET(self):
            return self.getToken(HTMLParser.SCRIPTLET, 0)

        def SCRIPT_OPEN(self):
            return self.getToken(HTMLParser.SCRIPT_OPEN, 0)

        def block_5(self):
            return self.getTypedRuleContext(HTMLParser.Block_5Context,0)


        def STYLE_OPEN(self):
            return self.getToken(HTMLParser.STYLE_OPEN, 0)

        def block_6(self):
            return self.getTypedRuleContext(HTMLParser.Block_6Context,0)


        def getRuleIndex(self):
            return HTMLParser.RULE_htmlelements_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlelements_star" ):
                listener.enterHtmlelements_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlelements_star" ):
                listener.exitHtmlelements_star(self)




    def htmlelements_star(self):

        localctx = HTMLParser.Htmlelements_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_htmlelements_star)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.htmlElements()
                self.state = 155
                self.htmlelements_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.htmlmisc_star()
                self.state = 158
                self.htmlElement()
                self.state = 159
                self.htmlmisc_star()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.htmlmisc_star()
                self.state = 162
                self.htmlElement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 164
                self.htmlElement()
                self.state = 165
                self.htmlmisc_star()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 167
                self.match(HTMLParser.TAG_OPEN)
                self.state = 168
                self.match(HTMLParser.TAG_NAME)
                self.state = 169
                self.htmlattribute_star()
                self.state = 170
                self.block_0()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 172
                self.match(HTMLParser.SCRIPTLET)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 173
                self.match(HTMLParser.SCRIPT_OPEN)
                self.state = 174
                self.block_5()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 175
                self.match(HTMLParser.STYLE_OPEN)
                self.state = 176
                self.block_6()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 177
                self.match(HTMLParser.TAG_OPEN)
                self.state = 178
                self.match(HTMLParser.TAG_NAME)
                self.state = 179
                self.block_0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dtd_questionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DTD(self):
            return self.getToken(HTMLParser.DTD, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_dtd_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDtd_question" ):
                listener.enterDtd_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDtd_question" ):
                listener.exitDtd_question(self)




    def dtd_question(self):

        localctx = HTMLParser.Dtd_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dtd_question)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(HTMLParser.DTD)
                pass
            elif token in [-1, 1, 2, 6, 7, 8, 9, 10]:
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


    class Xml_questionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XML(self):
            return self.getToken(HTMLParser.XML, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_xml_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXml_question" ):
                listener.enterXml_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXml_question" ):
                listener.exitXml_question(self)




    def xml_question(self):

        localctx = HTMLParser.Xml_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_xml_question)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(HTMLParser.XML)
                pass
            elif token in [-1, 1, 2, 5, 6, 7, 8, 9, 10]:
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


    class Scriptletorseaws_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scriptletOrSeaWs(self):
            return self.getTypedRuleContext(HTMLParser.ScriptletOrSeaWsContext,0)


        def scriptletorseaws_star(self):
            return self.getTypedRuleContext(HTMLParser.Scriptletorseaws_starContext,0)


        def SCRIPTLET(self):
            return self.getToken(HTMLParser.SCRIPTLET, 0)

        def SEA_WS(self):
            return self.getToken(HTMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_scriptletorseaws_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScriptletorseaws_star" ):
                listener.enterScriptletorseaws_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScriptletorseaws_star" ):
                listener.exitScriptletorseaws_star(self)




    def scriptletorseaws_star(self):

        localctx = HTMLParser.Scriptletorseaws_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_scriptletorseaws_star)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.scriptletOrSeaWs()
                self.state = 191
                self.scriptletorseaws_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(HTMLParser.SCRIPTLET)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.match(HTMLParser.SEA_WS)
                pass


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
        self.enterRule(localctx, 10, self.RULE_scriptletOrSeaWs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
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

        def htmlmisc_star(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParser.Htmlmisc_starContext)
            else:
                return self.getTypedRuleContext(HTMLParser.Htmlmisc_starContext,i)


        def htmlElement(self):
            return self.getTypedRuleContext(HTMLParser.HtmlElementContext,0)


        def TAG_OPEN(self):
            return self.getToken(HTMLParser.TAG_OPEN, 0)

        def TAG_NAME(self):
            return self.getToken(HTMLParser.TAG_NAME, 0)

        def htmlattribute_star(self):
            return self.getTypedRuleContext(HTMLParser.Htmlattribute_starContext,0)


        def block_0(self):
            return self.getTypedRuleContext(HTMLParser.Block_0Context,0)


        def SCRIPTLET(self):
            return self.getToken(HTMLParser.SCRIPTLET, 0)

        def SCRIPT_OPEN(self):
            return self.getToken(HTMLParser.SCRIPT_OPEN, 0)

        def block_5(self):
            return self.getTypedRuleContext(HTMLParser.Block_5Context,0)


        def STYLE_OPEN(self):
            return self.getToken(HTMLParser.STYLE_OPEN, 0)

        def block_6(self):
            return self.getTypedRuleContext(HTMLParser.Block_6Context,0)


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
        self.enterRule(localctx, 12, self.RULE_htmlElements)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.htmlmisc_star()
                self.state = 200
                self.htmlElement()
                self.state = 201
                self.htmlmisc_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.htmlmisc_star()
                self.state = 204
                self.htmlElement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 206
                self.htmlElement()
                self.state = 207
                self.htmlmisc_star()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.match(HTMLParser.TAG_OPEN)
                self.state = 210
                self.match(HTMLParser.TAG_NAME)
                self.state = 211
                self.htmlattribute_star()
                self.state = 212
                self.block_0()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 214
                self.match(HTMLParser.SCRIPTLET)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 215
                self.match(HTMLParser.SCRIPT_OPEN)
                self.state = 216
                self.block_5()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 217
                self.match(HTMLParser.STYLE_OPEN)
                self.state = 218
                self.block_6()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 219
                self.match(HTMLParser.TAG_OPEN)
                self.state = 220
                self.match(HTMLParser.TAG_NAME)
                self.state = 221
                self.block_0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Htmlmisc_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def htmlMisc(self):
            return self.getTypedRuleContext(HTMLParser.HtmlMiscContext,0)


        def htmlmisc_star(self):
            return self.getTypedRuleContext(HTMLParser.Htmlmisc_starContext,0)


        def SEA_WS(self):
            return self.getToken(HTMLParser.SEA_WS, 0)

        def HTML_COMMENT(self):
            return self.getToken(HTMLParser.HTML_COMMENT, 0)

        def HTML_CONDITIONAL_COMMENT(self):
            return self.getToken(HTMLParser.HTML_CONDITIONAL_COMMENT, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_htmlmisc_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlmisc_star" ):
                listener.enterHtmlmisc_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlmisc_star" ):
                listener.exitHtmlmisc_star(self)




    def htmlmisc_star(self):

        localctx = HTMLParser.Htmlmisc_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_htmlmisc_star)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.htmlMisc()
                self.state = 225
                self.htmlmisc_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(HTMLParser.SEA_WS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.match(HTMLParser.HTML_COMMENT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 229
                self.match(HTMLParser.HTML_CONDITIONAL_COMMENT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def htmlContent(self):
            return self.getTypedRuleContext(HTMLParser.HtmlContentContext,0)


        def TAG_OPEN(self):
            return self.getToken(HTMLParser.TAG_OPEN, 0)

        def TAG_SLASH(self):
            return self.getToken(HTMLParser.TAG_SLASH, 0)

        def TAG_NAME(self):
            return self.getToken(HTMLParser.TAG_NAME, 0)

        def TAG_CLOSE(self):
            return self.getToken(HTMLParser.TAG_CLOSE, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_block_7

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_7" ):
                listener.enterBlock_7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_7" ):
                listener.exitBlock_7(self)




    def block_7(self):

        localctx = HTMLParser.Block_7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block_7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.htmlContent()
            self.state = 233
            self.match(HTMLParser.TAG_OPEN)
            self.state = 234
            self.match(HTMLParser.TAG_SLASH)
            self.state = 235
            self.match(HTMLParser.TAG_NAME)
            self.state = 236
            self.match(HTMLParser.TAG_CLOSE)
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

        def TAG_CLOSE(self):
            return self.getToken(HTMLParser.TAG_CLOSE, 0)

        def block_7_question(self):
            return self.getTypedRuleContext(HTMLParser.Block_7_questionContext,0)


        def TAG_SLASH_CLOSE(self):
            return self.getToken(HTMLParser.TAG_SLASH_CLOSE, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_block_0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_0" ):
                listener.enterBlock_0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_0" ):
                listener.exitBlock_0(self)




    def block_0(self):

        localctx = HTMLParser.Block_0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block_0)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(HTMLParser.TAG_CLOSE)
                self.state = 239
                self.block_7_question()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(HTMLParser.TAG_SLASH_CLOSE)
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


    class Block_7_questionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def htmlContent(self):
            return self.getTypedRuleContext(HTMLParser.HtmlContentContext,0)


        def TAG_OPEN(self):
            return self.getToken(HTMLParser.TAG_OPEN, 0)

        def TAG_SLASH(self):
            return self.getToken(HTMLParser.TAG_SLASH, 0)

        def TAG_NAME(self):
            return self.getToken(HTMLParser.TAG_NAME, 0)

        def TAG_CLOSE(self):
            return self.getToken(HTMLParser.TAG_CLOSE, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_block_7_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_7_question" ):
                listener.enterBlock_7_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_7_question" ):
                listener.exitBlock_7_question(self)




    def block_7_question(self):

        localctx = HTMLParser.Block_7_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_block_7_question)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.htmlContent()
                self.state = 245
                self.match(HTMLParser.TAG_OPEN)
                self.state = 246
                self.match(HTMLParser.TAG_SLASH)
                self.state = 247
                self.match(HTMLParser.TAG_NAME)
                self.state = 248
                self.match(HTMLParser.TAG_CLOSE)
                pass


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

        def TAG_OPEN(self):
            return self.getToken(HTMLParser.TAG_OPEN, 0)

        def TAG_NAME(self):
            return self.getToken(HTMLParser.TAG_NAME, 0)

        def htmlattribute_star(self):
            return self.getTypedRuleContext(HTMLParser.Htmlattribute_starContext,0)


        def block_0(self):
            return self.getTypedRuleContext(HTMLParser.Block_0Context,0)


        def SCRIPTLET(self):
            return self.getToken(HTMLParser.SCRIPTLET, 0)

        def SCRIPT_OPEN(self):
            return self.getToken(HTMLParser.SCRIPT_OPEN, 0)

        def block_5(self):
            return self.getTypedRuleContext(HTMLParser.Block_5Context,0)


        def STYLE_OPEN(self):
            return self.getToken(HTMLParser.STYLE_OPEN, 0)

        def block_6(self):
            return self.getTypedRuleContext(HTMLParser.Block_6Context,0)


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
        self.enterRule(localctx, 22, self.RULE_htmlElement)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(HTMLParser.TAG_OPEN)
                self.state = 253
                self.match(HTMLParser.TAG_NAME)
                self.state = 254
                self.htmlattribute_star()
                self.state = 255
                self.block_0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(HTMLParser.SCRIPTLET)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.match(HTMLParser.SCRIPT_OPEN)
                self.state = 259
                self.block_5()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 260
                self.match(HTMLParser.STYLE_OPEN)
                self.state = 261
                self.block_6()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 262
                self.match(HTMLParser.TAG_OPEN)
                self.state = 263
                self.match(HTMLParser.TAG_NAME)
                self.state = 264
                self.block_0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Htmlattribute_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def htmlAttribute(self):
            return self.getTypedRuleContext(HTMLParser.HtmlAttributeContext,0)


        def htmlattribute_star(self):
            return self.getTypedRuleContext(HTMLParser.Htmlattribute_starContext,0)


        def TAG_NAME(self):
            return self.getToken(HTMLParser.TAG_NAME, 0)

        def block_4_question(self):
            return self.getTypedRuleContext(HTMLParser.Block_4_questionContext,0)


        def getRuleIndex(self):
            return HTMLParser.RULE_htmlattribute_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlattribute_star" ):
                listener.enterHtmlattribute_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlattribute_star" ):
                listener.exitHtmlattribute_star(self)




    def htmlattribute_star(self):

        localctx = HTMLParser.Htmlattribute_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_htmlattribute_star)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.htmlAttribute()
                self.state = 268
                self.htmlattribute_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.match(HTMLParser.TAG_NAME)
                self.state = 271
                self.block_4_question()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CDATA(self):
            return self.getToken(HTMLParser.CDATA, 0)

        def TAG_OPEN(self):
            return self.getToken(HTMLParser.TAG_OPEN, 0)

        def TAG_NAME(self):
            return self.getToken(HTMLParser.TAG_NAME, 0)

        def htmlattribute_star(self):
            return self.getTypedRuleContext(HTMLParser.Htmlattribute_starContext,0)


        def block_0(self):
            return self.getTypedRuleContext(HTMLParser.Block_0Context,0)


        def SCRIPTLET(self):
            return self.getToken(HTMLParser.SCRIPTLET, 0)

        def HTML_COMMENT(self):
            return self.getToken(HTMLParser.HTML_COMMENT, 0)

        def HTML_CONDITIONAL_COMMENT(self):
            return self.getToken(HTMLParser.HTML_CONDITIONAL_COMMENT, 0)

        def SCRIPT_OPEN(self):
            return self.getToken(HTMLParser.SCRIPT_OPEN, 0)

        def block_5(self):
            return self.getTypedRuleContext(HTMLParser.Block_5Context,0)


        def STYLE_OPEN(self):
            return self.getToken(HTMLParser.STYLE_OPEN, 0)

        def block_6(self):
            return self.getTypedRuleContext(HTMLParser.Block_6Context,0)


        def getRuleIndex(self):
            return HTMLParser.RULE_block_8

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_8" ):
                listener.enterBlock_8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_8" ):
                listener.exitBlock_8(self)




    def block_8(self):

        localctx = HTMLParser.Block_8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block_8)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.match(HTMLParser.CDATA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.match(HTMLParser.TAG_OPEN)
                self.state = 276
                self.match(HTMLParser.TAG_NAME)
                self.state = 277
                self.htmlattribute_star()
                self.state = 278
                self.block_0()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                self.match(HTMLParser.SCRIPTLET)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 281
                self.match(HTMLParser.HTML_COMMENT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 282
                self.match(HTMLParser.HTML_CONDITIONAL_COMMENT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 283
                self.match(HTMLParser.SCRIPT_OPEN)
                self.state = 284
                self.block_5()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 285
                self.match(HTMLParser.STYLE_OPEN)
                self.state = 286
                self.block_6()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 287
                self.match(HTMLParser.TAG_OPEN)
                self.state = 288
                self.match(HTMLParser.TAG_NAME)
                self.state = 289
                self.block_0()
                pass


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

        def block_8(self):
            return self.getTypedRuleContext(HTMLParser.Block_8Context,0)


        def htmlchardata_question(self):
            return self.getTypedRuleContext(HTMLParser.Htmlchardata_questionContext,0)


        def CDATA(self):
            return self.getToken(HTMLParser.CDATA, 0)

        def TAG_OPEN(self):
            return self.getToken(HTMLParser.TAG_OPEN, 0)

        def TAG_NAME(self):
            return self.getToken(HTMLParser.TAG_NAME, 0)

        def htmlattribute_star(self):
            return self.getTypedRuleContext(HTMLParser.Htmlattribute_starContext,0)


        def block_0(self):
            return self.getTypedRuleContext(HTMLParser.Block_0Context,0)


        def SCRIPTLET(self):
            return self.getToken(HTMLParser.SCRIPTLET, 0)

        def HTML_COMMENT(self):
            return self.getToken(HTMLParser.HTML_COMMENT, 0)

        def HTML_CONDITIONAL_COMMENT(self):
            return self.getToken(HTMLParser.HTML_CONDITIONAL_COMMENT, 0)

        def SCRIPT_OPEN(self):
            return self.getToken(HTMLParser.SCRIPT_OPEN, 0)

        def block_5(self):
            return self.getTypedRuleContext(HTMLParser.Block_5Context,0)


        def STYLE_OPEN(self):
            return self.getToken(HTMLParser.STYLE_OPEN, 0)

        def block_6(self):
            return self.getTypedRuleContext(HTMLParser.Block_6Context,0)


        def getRuleIndex(self):
            return HTMLParser.RULE_block_2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_2" ):
                listener.enterBlock_2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_2" ):
                listener.exitBlock_2(self)




    def block_2(self):

        localctx = HTMLParser.Block_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_block_2)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.block_8()
                self.state = 293
                self.htmlchardata_question()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(HTMLParser.CDATA)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.match(HTMLParser.TAG_OPEN)
                self.state = 297
                self.match(HTMLParser.TAG_NAME)
                self.state = 298
                self.htmlattribute_star()
                self.state = 299
                self.block_0()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 301
                self.match(HTMLParser.SCRIPTLET)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 302
                self.match(HTMLParser.HTML_COMMENT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 303
                self.match(HTMLParser.HTML_CONDITIONAL_COMMENT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 304
                self.match(HTMLParser.SCRIPT_OPEN)
                self.state = 305
                self.block_5()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 306
                self.match(HTMLParser.STYLE_OPEN)
                self.state = 307
                self.block_6()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 308
                self.match(HTMLParser.TAG_OPEN)
                self.state = 309
                self.match(HTMLParser.TAG_NAME)
                self.state = 310
                self.block_0()
                pass


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

        def htmlchardata_question(self):
            return self.getTypedRuleContext(HTMLParser.Htmlchardata_questionContext,0)


        def block_2_star(self):
            return self.getTypedRuleContext(HTMLParser.Block_2_starContext,0)


        def block_2(self):
            return self.getTypedRuleContext(HTMLParser.Block_2Context,0)


        def block_8(self):
            return self.getTypedRuleContext(HTMLParser.Block_8Context,0)


        def CDATA(self):
            return self.getToken(HTMLParser.CDATA, 0)

        def TAG_OPEN(self):
            return self.getToken(HTMLParser.TAG_OPEN, 0)

        def TAG_NAME(self):
            return self.getToken(HTMLParser.TAG_NAME, 0)

        def htmlattribute_star(self):
            return self.getTypedRuleContext(HTMLParser.Htmlattribute_starContext,0)


        def block_0(self):
            return self.getTypedRuleContext(HTMLParser.Block_0Context,0)


        def SCRIPTLET(self):
            return self.getToken(HTMLParser.SCRIPTLET, 0)

        def HTML_COMMENT(self):
            return self.getToken(HTMLParser.HTML_COMMENT, 0)

        def HTML_CONDITIONAL_COMMENT(self):
            return self.getToken(HTMLParser.HTML_CONDITIONAL_COMMENT, 0)

        def SCRIPT_OPEN(self):
            return self.getToken(HTMLParser.SCRIPT_OPEN, 0)

        def block_5(self):
            return self.getTypedRuleContext(HTMLParser.Block_5Context,0)


        def STYLE_OPEN(self):
            return self.getToken(HTMLParser.STYLE_OPEN, 0)

        def block_6(self):
            return self.getTypedRuleContext(HTMLParser.Block_6Context,0)


        def HTML_TEXT(self):
            return self.getToken(HTMLParser.HTML_TEXT, 0)

        def SEA_WS(self):
            return self.getToken(HTMLParser.SEA_WS, 0)

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
        self.enterRule(localctx, 30, self.RULE_htmlContent)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.htmlchardata_question()
                self.state = 314
                self.block_2_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.block_2()
                self.state = 317
                self.block_2_star()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 320
                self.block_8()
                self.state = 321
                self.htmlchardata_question()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 323
                self.match(HTMLParser.CDATA)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 324
                self.match(HTMLParser.TAG_OPEN)
                self.state = 325
                self.match(HTMLParser.TAG_NAME)
                self.state = 326
                self.htmlattribute_star()
                self.state = 327
                self.block_0()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 329
                self.match(HTMLParser.SCRIPTLET)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 330
                self.match(HTMLParser.HTML_COMMENT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 331
                self.match(HTMLParser.HTML_CONDITIONAL_COMMENT)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 332
                self.match(HTMLParser.SCRIPT_OPEN)
                self.state = 333
                self.block_5()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 334
                self.match(HTMLParser.STYLE_OPEN)
                self.state = 335
                self.block_6()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 336
                self.match(HTMLParser.TAG_OPEN)
                self.state = 337
                self.match(HTMLParser.TAG_NAME)
                self.state = 338
                self.block_0()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 339
                self.match(HTMLParser.HTML_TEXT)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 340
                self.match(HTMLParser.SEA_WS)
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
            return self.getTypedRuleContext(HTMLParser.Block_2Context,0)


        def block_2_star(self):
            return self.getTypedRuleContext(HTMLParser.Block_2_starContext,0)


        def block_8(self):
            return self.getTypedRuleContext(HTMLParser.Block_8Context,0)


        def htmlchardata_question(self):
            return self.getTypedRuleContext(HTMLParser.Htmlchardata_questionContext,0)


        def CDATA(self):
            return self.getToken(HTMLParser.CDATA, 0)

        def TAG_OPEN(self):
            return self.getToken(HTMLParser.TAG_OPEN, 0)

        def TAG_NAME(self):
            return self.getToken(HTMLParser.TAG_NAME, 0)

        def htmlattribute_star(self):
            return self.getTypedRuleContext(HTMLParser.Htmlattribute_starContext,0)


        def block_0(self):
            return self.getTypedRuleContext(HTMLParser.Block_0Context,0)


        def SCRIPTLET(self):
            return self.getToken(HTMLParser.SCRIPTLET, 0)

        def HTML_COMMENT(self):
            return self.getToken(HTMLParser.HTML_COMMENT, 0)

        def HTML_CONDITIONAL_COMMENT(self):
            return self.getToken(HTMLParser.HTML_CONDITIONAL_COMMENT, 0)

        def SCRIPT_OPEN(self):
            return self.getToken(HTMLParser.SCRIPT_OPEN, 0)

        def block_5(self):
            return self.getTypedRuleContext(HTMLParser.Block_5Context,0)


        def STYLE_OPEN(self):
            return self.getToken(HTMLParser.STYLE_OPEN, 0)

        def block_6(self):
            return self.getTypedRuleContext(HTMLParser.Block_6Context,0)


        def getRuleIndex(self):
            return HTMLParser.RULE_block_2_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_2_star" ):
                listener.enterBlock_2_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_2_star" ):
                listener.exitBlock_2_star(self)




    def block_2_star(self):

        localctx = HTMLParser.Block_2_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_block_2_star)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.block_2()
                self.state = 344
                self.block_2_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.block_8()
                self.state = 347
                self.htmlchardata_question()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 349
                self.match(HTMLParser.CDATA)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 350
                self.match(HTMLParser.TAG_OPEN)
                self.state = 351
                self.match(HTMLParser.TAG_NAME)
                self.state = 352
                self.htmlattribute_star()
                self.state = 353
                self.block_0()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 355
                self.match(HTMLParser.SCRIPTLET)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 356
                self.match(HTMLParser.HTML_COMMENT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 357
                self.match(HTMLParser.HTML_CONDITIONAL_COMMENT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 358
                self.match(HTMLParser.SCRIPT_OPEN)
                self.state = 359
                self.block_5()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 360
                self.match(HTMLParser.STYLE_OPEN)
                self.state = 361
                self.block_6()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 362
                self.match(HTMLParser.TAG_OPEN)
                self.state = 363
                self.match(HTMLParser.TAG_NAME)
                self.state = 364
                self.block_0()
                pass


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

        def TAG_EQUALS(self):
            return self.getToken(HTMLParser.TAG_EQUALS, 0)

        def ATTVALUE_VALUE(self):
            return self.getToken(HTMLParser.ATTVALUE_VALUE, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_block_4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_4" ):
                listener.enterBlock_4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_4" ):
                listener.exitBlock_4(self)




    def block_4(self):

        localctx = HTMLParser.Block_4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block_4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(HTMLParser.TAG_EQUALS)
            self.state = 368
            self.match(HTMLParser.ATTVALUE_VALUE)
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

        def block_4_question(self):
            return self.getTypedRuleContext(HTMLParser.Block_4_questionContext,0)


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
        self.enterRule(localctx, 36, self.RULE_htmlAttribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(HTMLParser.TAG_NAME)
            self.state = 371
            self.block_4_question()
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

        def TAG_EQUALS(self):
            return self.getToken(HTMLParser.TAG_EQUALS, 0)

        def ATTVALUE_VALUE(self):
            return self.getToken(HTMLParser.ATTVALUE_VALUE, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_block_4_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_4_question" ):
                listener.enterBlock_4_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_4_question" ):
                listener.exitBlock_4_question(self)




    def block_4_question(self):

        localctx = HTMLParser.Block_4_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_block_4_question)
        try:
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 16]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.match(HTMLParser.TAG_EQUALS)
                self.state = 375
                self.match(HTMLParser.ATTVALUE_VALUE)
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
        self.enterRule(localctx, 40, self.RULE_htmlChardata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
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

        def SEA_WS(self):
            return self.getToken(HTMLParser.SEA_WS, 0)

        def HTML_COMMENT(self):
            return self.getToken(HTMLParser.HTML_COMMENT, 0)

        def HTML_CONDITIONAL_COMMENT(self):
            return self.getToken(HTMLParser.HTML_CONDITIONAL_COMMENT, 0)

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
        self.enterRule(localctx, 42, self.RULE_htmlMisc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 134) != 0):
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
        self.enterRule(localctx, 44, self.RULE_htmlComment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
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


    class Block_5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCRIPT_BODY(self):
            return self.getToken(HTMLParser.SCRIPT_BODY, 0)

        def SCRIPT_SHORT_BODY(self):
            return self.getToken(HTMLParser.SCRIPT_SHORT_BODY, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_block_5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_5" ):
                listener.enterBlock_5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_5" ):
                listener.exitBlock_5(self)




    def block_5(self):

        localctx = HTMLParser.Block_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_block_5)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
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


    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCRIPT_OPEN(self):
            return self.getToken(HTMLParser.SCRIPT_OPEN, 0)

        def block_5(self):
            return self.getTypedRuleContext(HTMLParser.Block_5Context,0)


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
        self.enterRule(localctx, 48, self.RULE_script)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(HTMLParser.SCRIPT_OPEN)
            self.state = 387
            self.block_5()
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

        def STYLE_BODY(self):
            return self.getToken(HTMLParser.STYLE_BODY, 0)

        def STYLE_SHORT_BODY(self):
            return self.getToken(HTMLParser.STYLE_SHORT_BODY, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_block_6

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_6" ):
                listener.enterBlock_6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_6" ):
                listener.exitBlock_6(self)




    def block_6(self):

        localctx = HTMLParser.Block_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_block_6)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
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


    class StyleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STYLE_OPEN(self):
            return self.getToken(HTMLParser.STYLE_OPEN, 0)

        def block_6(self):
            return self.getTypedRuleContext(HTMLParser.Block_6Context,0)


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
        self.enterRule(localctx, 52, self.RULE_style)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(HTMLParser.STYLE_OPEN)
            self.state = 392
            self.block_6()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Htmlchardata_questionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HTML_TEXT(self):
            return self.getToken(HTMLParser.HTML_TEXT, 0)

        def SEA_WS(self):
            return self.getToken(HTMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_htmlchardata_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlchardata_question" ):
                listener.enterHtmlchardata_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlchardata_question" ):
                listener.exitHtmlchardata_question(self)




    def htmlchardata_question(self):

        localctx = HTMLParser.Htmlchardata_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_htmlchardata_question)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
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





