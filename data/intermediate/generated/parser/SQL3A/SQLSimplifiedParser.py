# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/SQL3A/SQLSimplifiedParser.g4 by ANTLR 4.13.0
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
        4,1,88,406,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,91,8,1,1,2,1,2,1,2,3,2,96,8,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,126,8,3,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,187,8,4,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,5,6,196,8,6,10,6,12,6,199,9,6,1,7,1,7,1,7,1,7,3,7,
        205,8,7,1,8,1,8,1,8,1,8,3,8,211,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,5,9,221,8,9,10,9,12,9,224,9,9,1,10,1,10,1,10,3,10,229,8,10,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,3,11,246,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,255,
        8,12,1,13,1,13,1,13,1,13,3,13,261,8,13,1,14,1,14,1,14,1,14,1,14,
        1,14,5,14,269,8,14,10,14,12,14,272,9,14,1,15,1,15,1,15,3,15,277,
        8,15,1,16,1,16,1,16,1,16,3,16,283,8,16,1,17,1,17,3,17,287,8,17,1,
        18,1,18,1,18,1,18,1,18,1,18,5,18,295,8,18,10,18,12,18,298,9,18,1,
        19,1,19,1,19,1,19,1,19,3,19,305,8,19,1,20,1,20,1,20,1,20,1,20,1,
        20,5,20,313,8,20,10,20,12,20,316,9,20,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,3,21,325,8,21,1,22,1,22,1,22,1,22,1,22,1,22,3,22,333,8,22,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        3,23,374,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,384,8,
        24,1,25,1,25,1,26,1,26,3,26,390,8,26,1,27,1,27,1,28,1,28,1,29,1,
        29,1,30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,1,33,0,5,12,18,28,36,
        40,34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,66,0,8,2,0,25,25,69,69,4,0,36,
        36,40,40,42,42,47,47,2,0,6,6,9,10,2,0,13,13,27,27,2,0,24,24,38,38,
        2,0,5,5,47,47,1,0,9,10,2,0,15,15,17,17,425,0,68,1,0,0,0,2,90,1,0,
        0,0,4,95,1,0,0,0,6,125,1,0,0,0,8,186,1,0,0,0,10,188,1,0,0,0,12,190,
        1,0,0,0,14,204,1,0,0,0,16,210,1,0,0,0,18,212,1,0,0,0,20,228,1,0,
        0,0,22,245,1,0,0,0,24,254,1,0,0,0,26,260,1,0,0,0,28,262,1,0,0,0,
        30,276,1,0,0,0,32,282,1,0,0,0,34,286,1,0,0,0,36,288,1,0,0,0,38,304,
        1,0,0,0,40,306,1,0,0,0,42,324,1,0,0,0,44,332,1,0,0,0,46,373,1,0,
        0,0,48,383,1,0,0,0,50,385,1,0,0,0,52,389,1,0,0,0,54,391,1,0,0,0,
        56,393,1,0,0,0,58,395,1,0,0,0,60,397,1,0,0,0,62,399,1,0,0,0,64,401,
        1,0,0,0,66,403,1,0,0,0,68,69,3,2,1,0,69,70,5,4,0,0,70,71,5,0,0,1,
        71,1,1,0,0,0,72,73,5,29,0,0,73,74,3,34,17,0,74,75,5,21,0,0,75,76,
        3,42,21,0,76,77,3,22,11,0,77,78,3,20,10,0,78,79,3,26,13,0,79,80,
        3,30,15,0,80,81,3,32,16,0,81,82,3,4,2,0,82,91,1,0,0,0,83,84,5,29,
        0,0,84,85,5,18,0,0,85,86,3,34,17,0,86,87,5,21,0,0,87,88,3,42,21,
        0,88,89,3,32,16,0,89,91,1,0,0,0,90,72,1,0,0,0,90,83,1,0,0,0,91,3,
        1,0,0,0,92,96,1,0,0,0,93,94,5,31,0,0,94,96,3,2,1,0,95,92,1,0,0,0,
        95,93,1,0,0,0,96,5,1,0,0,0,97,126,3,46,23,0,98,99,3,46,23,0,99,100,
        3,18,9,0,100,126,1,0,0,0,101,102,3,58,29,0,102,103,3,6,3,0,103,126,
        1,0,0,0,104,105,3,52,26,0,105,106,3,6,3,0,106,126,1,0,0,0,107,126,
        3,8,4,0,108,109,5,1,0,0,109,110,3,2,1,0,110,111,5,2,0,0,111,126,
        1,0,0,0,112,126,5,5,0,0,113,126,5,69,0,0,114,126,5,71,0,0,115,116,
        5,18,0,0,116,126,3,6,3,0,117,118,5,1,0,0,118,119,3,14,7,0,119,120,
        5,2,0,0,120,126,1,0,0,0,121,122,5,1,0,0,122,123,3,16,8,0,123,124,
        5,2,0,0,124,126,1,0,0,0,125,97,1,0,0,0,125,98,1,0,0,0,125,101,1,
        0,0,0,125,104,1,0,0,0,125,107,1,0,0,0,125,108,1,0,0,0,125,112,1,
        0,0,0,125,113,1,0,0,0,125,114,1,0,0,0,125,115,1,0,0,0,125,117,1,
        0,0,0,125,121,1,0,0,0,126,7,1,0,0,0,127,128,5,47,0,0,128,129,5,1,
        0,0,129,130,3,6,3,0,130,131,5,2,0,0,131,187,1,0,0,0,132,133,5,1,
        0,0,133,134,3,6,3,0,134,135,5,2,0,0,135,187,1,0,0,0,136,137,5,39,
        0,0,137,138,5,1,0,0,138,139,5,37,0,0,139,140,5,21,0,0,140,141,3,
        6,3,0,141,142,5,2,0,0,142,187,1,0,0,0,143,144,5,47,0,0,144,145,5,
        1,0,0,145,146,5,16,0,0,146,147,5,32,0,0,147,148,3,6,3,0,148,149,
        5,30,0,0,149,150,3,6,3,0,150,151,5,19,0,0,151,152,3,10,5,0,152,153,
        5,44,0,0,153,154,5,2,0,0,154,155,3,12,6,0,155,187,1,0,0,0,156,157,
        5,41,0,0,157,158,5,1,0,0,158,159,3,6,3,0,159,160,5,21,0,0,160,161,
        5,69,0,0,161,162,5,20,0,0,162,163,5,69,0,0,163,164,5,2,0,0,164,187,
        1,0,0,0,165,166,5,45,0,0,166,167,5,1,0,0,167,168,3,6,3,0,168,169,
        5,8,0,0,169,170,3,6,3,0,170,171,5,3,0,0,171,172,5,69,0,0,172,173,
        5,2,0,0,173,187,1,0,0,0,174,175,5,1,0,0,175,176,5,16,0,0,176,177,
        5,32,0,0,177,178,3,6,3,0,178,179,5,30,0,0,179,180,3,6,3,0,180,181,
        5,19,0,0,181,182,3,10,5,0,182,183,5,44,0,0,183,184,5,2,0,0,184,185,
        3,12,6,0,185,187,1,0,0,0,186,127,1,0,0,0,186,132,1,0,0,0,186,136,
        1,0,0,0,186,143,1,0,0,0,186,156,1,0,0,0,186,165,1,0,0,0,186,174,
        1,0,0,0,187,9,1,0,0,0,188,189,7,0,0,0,189,11,1,0,0,0,190,197,6,6,
        -1,0,191,192,10,1,0,0,192,193,3,52,26,0,193,194,3,8,4,0,194,196,
        1,0,0,0,195,191,1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,
        1,0,0,0,198,13,1,0,0,0,199,197,1,0,0,0,200,205,5,56,0,0,201,202,
        5,56,0,0,202,203,5,3,0,0,203,205,3,14,7,0,204,200,1,0,0,0,204,201,
        1,0,0,0,205,15,1,0,0,0,206,211,5,69,0,0,207,208,5,69,0,0,208,209,
        5,3,0,0,209,211,3,16,8,0,210,206,1,0,0,0,210,207,1,0,0,0,211,17,
        1,0,0,0,212,213,6,9,-1,0,213,214,3,54,27,0,214,215,3,46,23,0,215,
        222,1,0,0,0,216,217,10,1,0,0,217,218,3,52,26,0,218,219,3,46,23,0,
        219,221,1,0,0,0,220,216,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,
        222,223,1,0,0,0,223,19,1,0,0,0,224,222,1,0,0,0,225,226,5,33,0,0,
        226,229,3,6,3,0,227,229,1,0,0,0,228,225,1,0,0,0,228,227,1,0,0,0,
        229,21,1,0,0,0,230,231,5,34,0,0,231,232,3,48,24,0,232,233,5,26,0,
        0,233,234,3,24,12,0,234,246,1,0,0,0,235,236,5,34,0,0,236,237,5,1,
        0,0,237,238,3,2,1,0,238,239,5,2,0,0,239,240,5,14,0,0,240,241,5,47,
        0,0,241,242,5,26,0,0,242,243,3,24,12,0,243,246,1,0,0,0,244,246,1,
        0,0,0,245,230,1,0,0,0,245,235,1,0,0,0,245,244,1,0,0,0,246,23,1,0,
        0,0,247,248,3,46,23,0,248,249,3,18,9,0,249,255,1,0,0,0,250,251,3,
        58,29,0,251,252,3,46,23,0,252,253,3,18,9,0,253,255,1,0,0,0,254,247,
        1,0,0,0,254,250,1,0,0,0,255,25,1,0,0,0,256,257,5,22,0,0,257,258,
        5,35,0,0,258,261,3,28,14,0,259,261,1,0,0,0,260,256,1,0,0,0,260,259,
        1,0,0,0,261,27,1,0,0,0,262,263,6,14,-1,0,263,264,3,46,23,0,264,270,
        1,0,0,0,265,266,10,1,0,0,266,267,5,3,0,0,267,269,3,46,23,0,268,265,
        1,0,0,0,269,272,1,0,0,0,270,268,1,0,0,0,270,271,1,0,0,0,271,29,1,
        0,0,0,272,270,1,0,0,0,273,274,5,23,0,0,274,277,3,6,3,0,275,277,1,
        0,0,0,276,273,1,0,0,0,276,275,1,0,0,0,277,31,1,0,0,0,278,279,5,28,
        0,0,279,280,5,35,0,0,280,283,3,38,19,0,281,283,1,0,0,0,282,278,1,
        0,0,0,282,281,1,0,0,0,283,33,1,0,0,0,284,287,5,5,0,0,285,287,3,36,
        18,0,286,284,1,0,0,0,286,285,1,0,0,0,287,35,1,0,0,0,288,289,6,18,
        -1,0,289,290,3,46,23,0,290,296,1,0,0,0,291,292,10,1,0,0,292,293,
        5,3,0,0,293,295,3,46,23,0,294,291,1,0,0,0,295,298,1,0,0,0,296,294,
        1,0,0,0,296,297,1,0,0,0,297,37,1,0,0,0,298,296,1,0,0,0,299,305,3,
        44,22,0,300,301,3,44,22,0,301,302,5,3,0,0,302,303,3,38,19,0,303,
        305,1,0,0,0,304,299,1,0,0,0,304,300,1,0,0,0,305,39,1,0,0,0,306,307,
        6,20,-1,0,307,308,3,48,24,0,308,314,1,0,0,0,309,310,10,1,0,0,310,
        311,5,3,0,0,311,313,3,48,24,0,312,309,1,0,0,0,313,316,1,0,0,0,314,
        312,1,0,0,0,314,315,1,0,0,0,315,41,1,0,0,0,316,314,1,0,0,0,317,325,
        3,40,20,0,318,319,5,1,0,0,319,320,3,2,1,0,320,321,5,2,0,0,321,322,
        5,14,0,0,322,323,3,48,24,0,323,325,1,0,0,0,324,317,1,0,0,0,324,318,
        1,0,0,0,325,43,1,0,0,0,326,333,3,46,23,0,327,328,5,47,0,0,328,329,
        5,46,0,0,329,333,3,62,31,0,330,331,5,47,0,0,331,333,3,64,32,0,332,
        326,1,0,0,0,332,327,1,0,0,0,332,330,1,0,0,0,333,45,1,0,0,0,334,374,
        5,47,0,0,335,336,5,47,0,0,336,337,5,14,0,0,337,374,3,66,33,0,338,
        339,3,48,24,0,339,340,5,7,0,0,340,341,3,60,30,0,341,374,1,0,0,0,
        342,343,3,48,24,0,343,344,5,7,0,0,344,345,3,60,30,0,345,346,5,14,
        0,0,346,347,3,66,33,0,347,374,1,0,0,0,348,374,5,69,0,0,349,350,5,
        56,0,0,350,351,5,14,0,0,351,374,3,66,33,0,352,374,5,56,0,0,353,374,
        5,71,0,0,354,355,5,71,0,0,355,356,5,14,0,0,356,374,3,66,33,0,357,
        358,3,50,25,0,358,359,5,56,0,0,359,374,1,0,0,0,360,361,3,50,25,0,
        361,362,5,56,0,0,362,363,3,50,25,0,363,374,1,0,0,0,364,374,3,8,4,
        0,365,366,3,8,4,0,366,367,5,14,0,0,367,368,3,66,33,0,368,374,1,0,
        0,0,369,370,3,8,4,0,370,371,5,14,0,0,371,372,5,43,0,0,372,374,1,
        0,0,0,373,334,1,0,0,0,373,335,1,0,0,0,373,338,1,0,0,0,373,342,1,
        0,0,0,373,348,1,0,0,0,373,349,1,0,0,0,373,352,1,0,0,0,373,353,1,
        0,0,0,373,354,1,0,0,0,373,357,1,0,0,0,373,360,1,0,0,0,373,364,1,
        0,0,0,373,365,1,0,0,0,373,369,1,0,0,0,374,47,1,0,0,0,375,384,5,47,
        0,0,376,377,5,47,0,0,377,378,5,14,0,0,378,384,3,66,33,0,379,380,
        3,8,4,0,380,381,5,14,0,0,381,382,5,47,0,0,382,384,1,0,0,0,383,375,
        1,0,0,0,383,376,1,0,0,0,383,379,1,0,0,0,384,49,1,0,0,0,385,386,7,
        1,0,0,386,51,1,0,0,0,387,390,3,56,28,0,388,390,3,54,27,0,389,387,
        1,0,0,0,389,388,1,0,0,0,390,53,1,0,0,0,391,392,7,2,0,0,392,55,1,
        0,0,0,393,394,7,3,0,0,394,57,1,0,0,0,395,396,7,4,0,0,396,59,1,0,
        0,0,397,398,7,5,0,0,398,61,1,0,0,0,399,400,7,6,0,0,400,63,1,0,0,
        0,401,402,7,7,0,0,402,65,1,0,0,0,403,404,5,47,0,0,404,67,1,0,0,0,
        24,90,95,125,186,197,204,210,222,228,245,254,260,270,276,282,286,
        296,304,314,324,332,373,383,389
    ]

class SQLSimplifiedParser ( Parser ):

    grammarFileName = "SQLSimplifiedParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "';'", "'*'", "'='", 
                     "'.'", "'/'", "'<'", "'>'", "<INVALID>", "<INVALID>", 
                     "'AND'", "'AS'", "'ASC'", "'CASE'", "'DESC'", "'DISTINCT'", 
                     "'ELSE'", "'FOR'", "'FROM'", "'GROUP'", "'HAVING'", 
                     "'NOT'", "'NULL'", "'ON'", "'OR'", "'ORDER'", "'SELECT'", 
                     "'THEN'", "'UNION'", "'WHEN'", "'WHERE'", "'JOIN'", 
                     "'BY'", "'DAY'", "'YEAR'", "'EXISTS'", "'EXTRACT'", 
                     "'INTERVAL'", "'SUBSTRING'", "'TIME'", "'VALUE'", "'END'", 
                     "'ROUND'", "'USING'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\\\'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'''" ]

    symbolicNames = [ "<INVALID>", "OPEN_PAREN", "CLOSE_PAREN", "COMMA", 
                      "SEMI", "STAR", "EQUAL", "DOT", "SLASH", "LT", "GT", 
                      "PARAM", "Operator", "AND", "AS", "ASC", "CASE", "DESC", 
                      "DISTINCT", "ELSE", "FOR", "FROM", "GROUP_P", "HAVING", 
                      "NOT", "NULL_P", "ON", "OR", "ORDER", "SELECT", "THEN", 
                      "UNION", "WHEN", "WHERE", "JOIN", "BY", "DAY_P", "YEAR_P", 
                      "EXISTS", "EXTRACT", "INTERVAL", "SUBSTRING", "TIME", 
                      "VALUE_P", "END_P", "ROUND", "USING", "Identifier", 
                      "QuotedIdentifier", "UnterminatedQuotedIdentifier", 
                      "InvalidQuotedIdentifier", "InvalidUnterminatedQuotedIdentifier", 
                      "UnicodeQuotedIdentifier", "UnterminatedUnicodeQuotedIdentifier", 
                      "InvalidUnicodeQuotedIdentifier", "InvalidUnterminatedUnicodeQuotedIdentifier", 
                      "StringConstant", "UnterminatedStringConstant", "UnicodeEscapeStringConstant", 
                      "UnterminatedUnicodeEscapeStringConstant", "BeginDollarStringConstant", 
                      "BinaryStringConstant", "UnterminatedBinaryStringConstant", 
                      "InvalidBinaryStringConstant", "InvalidUnterminatedBinaryStringConstant", 
                      "HexadecimalStringConstant", "UnterminatedHexadecimalStringConstant", 
                      "InvalidHexadecimalStringConstant", "InvalidUnterminatedHexadecimalStringConstant", 
                      "Integral", "NumericFail", "Numeric", "PLSQLVARIABLENAME", 
                      "PLSQLIDENTIFIER", "Whitespace", "Newline", "LineComment", 
                      "BlockComment", "UnterminatedBlockComment", "MetaCommand", 
                      "EndMetaCommand", "ErrorCharacter", "EscapeStringConstant", 
                      "UnterminatedEscapeStringConstant", "InvalidEscapeStringConstant", 
                      "InvalidUnterminatedEscapeStringConstant", "DollarText", 
                      "EndDollarStringConstant", "AfterEscapeStringConstantWithNewlineMode_Continued" ]

    RULE_start = 0
    RULE_select_statement = 1
    RULE_union_list = 2
    RULE_c_expr = 3
    RULE_f_expr = 4
    RULE_integral_or_null = 5
    RULE_binary_op_fexpr_list = 6
    RULE_string_list = 7
    RULE_integral_list = 8
    RULE_binary_op_columnref_list = 9
    RULE_where_clause = 10
    RULE_join_clause = 11
    RULE_on_clause = 12
    RULE_group_clause = 13
    RULE_group_by_list = 14
    RULE_having_clause = 15
    RULE_sort_clause = 16
    RULE_column_list_or_star = 17
    RULE_column_list = 18
    RULE_sortby_list = 19
    RULE_from_list = 20
    RULE_from_clause = 21
    RULE_sortby = 22
    RULE_columnref = 23
    RULE_table_ref = 24
    RULE_typeidentifier = 25
    RULE_binary_op = 26
    RULE_math_op = 27
    RULE_logic_op = 28
    RULE_unary_op = 29
    RULE_identifier_or_star = 30
    RULE_gt_lt = 31
    RULE_asc_desc = 32
    RULE_collabel = 33

    ruleNames =  [ "start", "select_statement", "union_list", "c_expr", 
                   "f_expr", "integral_or_null", "binary_op_fexpr_list", 
                   "string_list", "integral_list", "binary_op_columnref_list", 
                   "where_clause", "join_clause", "on_clause", "group_clause", 
                   "group_by_list", "having_clause", "sort_clause", "column_list_or_star", 
                   "column_list", "sortby_list", "from_list", "from_clause", 
                   "sortby", "columnref", "table_ref", "typeidentifier", 
                   "binary_op", "math_op", "logic_op", "unary_op", "identifier_or_star", 
                   "gt_lt", "asc_desc", "collabel" ]

    EOF = Token.EOF
    OPEN_PAREN=1
    CLOSE_PAREN=2
    COMMA=3
    SEMI=4
    STAR=5
    EQUAL=6
    DOT=7
    SLASH=8
    LT=9
    GT=10
    PARAM=11
    Operator=12
    AND=13
    AS=14
    ASC=15
    CASE=16
    DESC=17
    DISTINCT=18
    ELSE=19
    FOR=20
    FROM=21
    GROUP_P=22
    HAVING=23
    NOT=24
    NULL_P=25
    ON=26
    OR=27
    ORDER=28
    SELECT=29
    THEN=30
    UNION=31
    WHEN=32
    WHERE=33
    JOIN=34
    BY=35
    DAY_P=36
    YEAR_P=37
    EXISTS=38
    EXTRACT=39
    INTERVAL=40
    SUBSTRING=41
    TIME=42
    VALUE_P=43
    END_P=44
    ROUND=45
    USING=46
    Identifier=47
    QuotedIdentifier=48
    UnterminatedQuotedIdentifier=49
    InvalidQuotedIdentifier=50
    InvalidUnterminatedQuotedIdentifier=51
    UnicodeQuotedIdentifier=52
    UnterminatedUnicodeQuotedIdentifier=53
    InvalidUnicodeQuotedIdentifier=54
    InvalidUnterminatedUnicodeQuotedIdentifier=55
    StringConstant=56
    UnterminatedStringConstant=57
    UnicodeEscapeStringConstant=58
    UnterminatedUnicodeEscapeStringConstant=59
    BeginDollarStringConstant=60
    BinaryStringConstant=61
    UnterminatedBinaryStringConstant=62
    InvalidBinaryStringConstant=63
    InvalidUnterminatedBinaryStringConstant=64
    HexadecimalStringConstant=65
    UnterminatedHexadecimalStringConstant=66
    InvalidHexadecimalStringConstant=67
    InvalidUnterminatedHexadecimalStringConstant=68
    Integral=69
    NumericFail=70
    Numeric=71
    PLSQLVARIABLENAME=72
    PLSQLIDENTIFIER=73
    Whitespace=74
    Newline=75
    LineComment=76
    BlockComment=77
    UnterminatedBlockComment=78
    MetaCommand=79
    EndMetaCommand=80
    ErrorCharacter=81
    EscapeStringConstant=82
    UnterminatedEscapeStringConstant=83
    InvalidEscapeStringConstant=84
    InvalidUnterminatedEscapeStringConstant=85
    DollarText=86
    EndDollarStringConstant=87
    AfterEscapeStringConstantWithNewlineMode_Continued=88

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

        def select_statement(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Select_statementContext,0)


        def SEMI(self):
            return self.getToken(SQLSimplifiedParser.SEMI, 0)

        def EOF(self):
            return self.getToken(SQLSimplifiedParser.EOF, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = SQLSimplifiedParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.select_statement()
            self.state = 69
            self.match(SQLSimplifiedParser.SEMI)
            self.state = 70
            self.match(SQLSimplifiedParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(SQLSimplifiedParser.SELECT, 0)

        def column_list_or_star(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Column_list_or_starContext,0)


        def FROM(self):
            return self.getToken(SQLSimplifiedParser.FROM, 0)

        def from_clause(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.From_clauseContext,0)


        def join_clause(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Join_clauseContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Where_clauseContext,0)


        def group_clause(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Group_clauseContext,0)


        def having_clause(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Having_clauseContext,0)


        def sort_clause(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Sort_clauseContext,0)


        def union_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Union_listContext,0)


        def DISTINCT(self):
            return self.getToken(SQLSimplifiedParser.DISTINCT, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_select_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_statement" ):
                listener.enterSelect_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_statement" ):
                listener.exitSelect_statement(self)




    def select_statement(self):

        localctx = SQLSimplifiedParser.Select_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_select_statement)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(SQLSimplifiedParser.SELECT)
                self.state = 73
                self.column_list_or_star()
                self.state = 74
                self.match(SQLSimplifiedParser.FROM)
                self.state = 75
                self.from_clause()
                self.state = 76
                self.join_clause()
                self.state = 77
                self.where_clause()
                self.state = 78
                self.group_clause()
                self.state = 79
                self.having_clause()
                self.state = 80
                self.sort_clause()
                self.state = 81
                self.union_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.match(SQLSimplifiedParser.SELECT)
                self.state = 84
                self.match(SQLSimplifiedParser.DISTINCT)
                self.state = 85
                self.column_list_or_star()
                self.state = 86
                self.match(SQLSimplifiedParser.FROM)
                self.state = 87
                self.from_clause()
                self.state = 88
                self.sort_clause()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Union_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNION(self):
            return self.getToken(SQLSimplifiedParser.UNION, 0)

        def select_statement(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Select_statementContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_union_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion_list" ):
                listener.enterUnion_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion_list" ):
                listener.exitUnion_list(self)




    def union_list(self):

        localctx = SQLSimplifiedParser.Union_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_union_list)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 4]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(SQLSimplifiedParser.UNION)
                self.state = 94
                self.select_statement()
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


    class C_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnref(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.ColumnrefContext,0)


        def binary_op_columnref_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Binary_op_columnref_listContext,0)


        def unary_op(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Unary_opContext,0)


        def c_expr(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.C_exprContext,0)


        def binary_op(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Binary_opContext,0)


        def f_expr(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.F_exprContext,0)


        def OPEN_PAREN(self):
            return self.getToken(SQLSimplifiedParser.OPEN_PAREN, 0)

        def select_statement(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Select_statementContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(SQLSimplifiedParser.CLOSE_PAREN, 0)

        def STAR(self):
            return self.getToken(SQLSimplifiedParser.STAR, 0)

        def Integral(self):
            return self.getToken(SQLSimplifiedParser.Integral, 0)

        def Numeric(self):
            return self.getToken(SQLSimplifiedParser.Numeric, 0)

        def DISTINCT(self):
            return self.getToken(SQLSimplifiedParser.DISTINCT, 0)

        def string_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.String_listContext,0)


        def integral_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Integral_listContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_c_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterC_expr" ):
                listener.enterC_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitC_expr" ):
                listener.exitC_expr(self)




    def c_expr(self):

        localctx = SQLSimplifiedParser.C_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_c_expr)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.columnref()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.columnref()
                self.state = 99
                self.binary_op_columnref_list(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.unary_op()
                self.state = 102
                self.c_expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.binary_op()
                self.state = 105
                self.c_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 107
                self.f_expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 108
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 109
                self.select_statement()
                self.state = 110
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 112
                self.match(SQLSimplifiedParser.STAR)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 113
                self.match(SQLSimplifiedParser.Integral)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 114
                self.match(SQLSimplifiedParser.Numeric)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 115
                self.match(SQLSimplifiedParser.DISTINCT)
                self.state = 116
                self.c_expr()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 117
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 118
                self.string_list()
                self.state = 119
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 121
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 122
                self.integral_list()
                self.state = 123
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SQLSimplifiedParser.Identifier, 0)

        def OPEN_PAREN(self):
            return self.getToken(SQLSimplifiedParser.OPEN_PAREN, 0)

        def c_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLSimplifiedParser.C_exprContext)
            else:
                return self.getTypedRuleContext(SQLSimplifiedParser.C_exprContext,i)


        def CLOSE_PAREN(self):
            return self.getToken(SQLSimplifiedParser.CLOSE_PAREN, 0)

        def EXTRACT(self):
            return self.getToken(SQLSimplifiedParser.EXTRACT, 0)

        def YEAR_P(self):
            return self.getToken(SQLSimplifiedParser.YEAR_P, 0)

        def FROM(self):
            return self.getToken(SQLSimplifiedParser.FROM, 0)

        def CASE(self):
            return self.getToken(SQLSimplifiedParser.CASE, 0)

        def WHEN(self):
            return self.getToken(SQLSimplifiedParser.WHEN, 0)

        def THEN(self):
            return self.getToken(SQLSimplifiedParser.THEN, 0)

        def ELSE(self):
            return self.getToken(SQLSimplifiedParser.ELSE, 0)

        def integral_or_null(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Integral_or_nullContext,0)


        def END_P(self):
            return self.getToken(SQLSimplifiedParser.END_P, 0)

        def binary_op_fexpr_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Binary_op_fexpr_listContext,0)


        def SUBSTRING(self):
            return self.getToken(SQLSimplifiedParser.SUBSTRING, 0)

        def Integral(self, i:int=None):
            if i is None:
                return self.getTokens(SQLSimplifiedParser.Integral)
            else:
                return self.getToken(SQLSimplifiedParser.Integral, i)

        def FOR(self):
            return self.getToken(SQLSimplifiedParser.FOR, 0)

        def ROUND(self):
            return self.getToken(SQLSimplifiedParser.ROUND, 0)

        def SLASH(self):
            return self.getToken(SQLSimplifiedParser.SLASH, 0)

        def COMMA(self):
            return self.getToken(SQLSimplifiedParser.COMMA, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_f_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_expr" ):
                listener.enterF_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_expr" ):
                listener.exitF_expr(self)




    def f_expr(self):

        localctx = SQLSimplifiedParser.F_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_f_expr)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(SQLSimplifiedParser.Identifier)
                self.state = 128
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 129
                self.c_expr()
                self.state = 130
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 133
                self.c_expr()
                self.state = 134
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.match(SQLSimplifiedParser.EXTRACT)
                self.state = 137
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 138
                self.match(SQLSimplifiedParser.YEAR_P)
                self.state = 139
                self.match(SQLSimplifiedParser.FROM)
                self.state = 140
                self.c_expr()
                self.state = 141
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.match(SQLSimplifiedParser.Identifier)
                self.state = 144
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 145
                self.match(SQLSimplifiedParser.CASE)
                self.state = 146
                self.match(SQLSimplifiedParser.WHEN)
                self.state = 147
                self.c_expr()
                self.state = 148
                self.match(SQLSimplifiedParser.THEN)
                self.state = 149
                self.c_expr()
                self.state = 150
                self.match(SQLSimplifiedParser.ELSE)
                self.state = 151
                self.integral_or_null()
                self.state = 152
                self.match(SQLSimplifiedParser.END_P)
                self.state = 153
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                self.state = 154
                self.binary_op_fexpr_list(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 156
                self.match(SQLSimplifiedParser.SUBSTRING)
                self.state = 157
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 158
                self.c_expr()
                self.state = 159
                self.match(SQLSimplifiedParser.FROM)
                self.state = 160
                self.match(SQLSimplifiedParser.Integral)
                self.state = 161
                self.match(SQLSimplifiedParser.FOR)
                self.state = 162
                self.match(SQLSimplifiedParser.Integral)
                self.state = 163
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 165
                self.match(SQLSimplifiedParser.ROUND)
                self.state = 166
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 167
                self.c_expr()
                self.state = 168
                self.match(SQLSimplifiedParser.SLASH)
                self.state = 169
                self.c_expr()
                self.state = 170
                self.match(SQLSimplifiedParser.COMMA)
                self.state = 171
                self.match(SQLSimplifiedParser.Integral)
                self.state = 172
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 174
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 175
                self.match(SQLSimplifiedParser.CASE)
                self.state = 176
                self.match(SQLSimplifiedParser.WHEN)
                self.state = 177
                self.c_expr()
                self.state = 178
                self.match(SQLSimplifiedParser.THEN)
                self.state = 179
                self.c_expr()
                self.state = 180
                self.match(SQLSimplifiedParser.ELSE)
                self.state = 181
                self.integral_or_null()
                self.state = 182
                self.match(SQLSimplifiedParser.END_P)
                self.state = 183
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                self.state = 184
                self.binary_op_fexpr_list(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Integral_or_nullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integral(self):
            return self.getToken(SQLSimplifiedParser.Integral, 0)

        def NULL_P(self):
            return self.getToken(SQLSimplifiedParser.NULL_P, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_integral_or_null

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegral_or_null" ):
                listener.enterIntegral_or_null(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegral_or_null" ):
                listener.exitIntegral_or_null(self)




    def integral_or_null(self):

        localctx = SQLSimplifiedParser.Integral_or_nullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_integral_or_null)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            _la = self._input.LA(1)
            if not(_la==25 or _la==69):
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


    class Binary_op_fexpr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def binary_op_fexpr_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Binary_op_fexpr_listContext,0)


        def binary_op(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Binary_opContext,0)


        def f_expr(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.F_exprContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_binary_op_fexpr_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_op_fexpr_list" ):
                listener.enterBinary_op_fexpr_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_op_fexpr_list" ):
                listener.exitBinary_op_fexpr_list(self)



    def binary_op_fexpr_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SQLSimplifiedParser.Binary_op_fexpr_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_binary_op_fexpr_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SQLSimplifiedParser.Binary_op_fexpr_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_binary_op_fexpr_list)
                    self.state = 191
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 192
                    self.binary_op()
                    self.state = 193
                    self.f_expr() 
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class String_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringConstant(self):
            return self.getToken(SQLSimplifiedParser.StringConstant, 0)

        def COMMA(self):
            return self.getToken(SQLSimplifiedParser.COMMA, 0)

        def string_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.String_listContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_string_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_list" ):
                listener.enterString_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_list" ):
                listener.exitString_list(self)




    def string_list(self):

        localctx = SQLSimplifiedParser.String_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_string_list)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(SQLSimplifiedParser.StringConstant)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(SQLSimplifiedParser.StringConstant)
                self.state = 202
                self.match(SQLSimplifiedParser.COMMA)
                self.state = 203
                self.string_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Integral_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integral(self):
            return self.getToken(SQLSimplifiedParser.Integral, 0)

        def COMMA(self):
            return self.getToken(SQLSimplifiedParser.COMMA, 0)

        def integral_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Integral_listContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_integral_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegral_list" ):
                listener.enterIntegral_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegral_list" ):
                listener.exitIntegral_list(self)




    def integral_list(self):

        localctx = SQLSimplifiedParser.Integral_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_integral_list)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(SQLSimplifiedParser.Integral)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(SQLSimplifiedParser.Integral)
                self.state = 208
                self.match(SQLSimplifiedParser.COMMA)
                self.state = 209
                self.integral_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Binary_op_columnref_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def math_op(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Math_opContext,0)


        def columnref(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.ColumnrefContext,0)


        def binary_op_columnref_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Binary_op_columnref_listContext,0)


        def binary_op(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Binary_opContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_binary_op_columnref_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_op_columnref_list" ):
                listener.enterBinary_op_columnref_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_op_columnref_list" ):
                listener.exitBinary_op_columnref_list(self)



    def binary_op_columnref_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SQLSimplifiedParser.Binary_op_columnref_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_binary_op_columnref_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.math_op()
            self.state = 214
            self.columnref()
            self._ctx.stop = self._input.LT(-1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SQLSimplifiedParser.Binary_op_columnref_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_binary_op_columnref_list)
                    self.state = 216
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 217
                    self.binary_op()
                    self.state = 218
                    self.columnref() 
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Where_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(SQLSimplifiedParser.WHERE, 0)

        def c_expr(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.C_exprContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_where_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_clause" ):
                listener.enterWhere_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_clause" ):
                listener.exitWhere_clause(self)




    def where_clause(self):

        localctx = SQLSimplifiedParser.Where_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_where_clause)
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(SQLSimplifiedParser.WHERE)
                self.state = 226
                self.c_expr()
                pass
            elif token in [2, 4, 22, 23, 28, 31]:
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


    class Join_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JOIN(self):
            return self.getToken(SQLSimplifiedParser.JOIN, 0)

        def table_ref(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Table_refContext,0)


        def ON(self):
            return self.getToken(SQLSimplifiedParser.ON, 0)

        def on_clause(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.On_clauseContext,0)


        def OPEN_PAREN(self):
            return self.getToken(SQLSimplifiedParser.OPEN_PAREN, 0)

        def select_statement(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Select_statementContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(SQLSimplifiedParser.CLOSE_PAREN, 0)

        def AS(self):
            return self.getToken(SQLSimplifiedParser.AS, 0)

        def Identifier(self):
            return self.getToken(SQLSimplifiedParser.Identifier, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_join_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoin_clause" ):
                listener.enterJoin_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoin_clause" ):
                listener.exitJoin_clause(self)




    def join_clause(self):

        localctx = SQLSimplifiedParser.Join_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_join_clause)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(SQLSimplifiedParser.JOIN)
                self.state = 231
                self.table_ref()
                self.state = 232
                self.match(SQLSimplifiedParser.ON)
                self.state = 233
                self.on_clause()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(SQLSimplifiedParser.JOIN)
                self.state = 236
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 237
                self.select_statement()
                self.state = 238
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                self.state = 239
                self.match(SQLSimplifiedParser.AS)
                self.state = 240
                self.match(SQLSimplifiedParser.Identifier)
                self.state = 241
                self.match(SQLSimplifiedParser.ON)
                self.state = 242
                self.on_clause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class On_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnref(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.ColumnrefContext,0)


        def binary_op_columnref_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Binary_op_columnref_listContext,0)


        def unary_op(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Unary_opContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_on_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOn_clause" ):
                listener.enterOn_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOn_clause" ):
                listener.exitOn_clause(self)




    def on_clause(self):

        localctx = SQLSimplifiedParser.On_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_on_clause)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 36, 39, 40, 41, 42, 45, 47, 56, 69, 71]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.columnref()
                self.state = 248
                self.binary_op_columnref_list(0)
                pass
            elif token in [24, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.unary_op()
                self.state = 251
                self.columnref()
                self.state = 252
                self.binary_op_columnref_list(0)
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


    class Group_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP_P(self):
            return self.getToken(SQLSimplifiedParser.GROUP_P, 0)

        def BY(self):
            return self.getToken(SQLSimplifiedParser.BY, 0)

        def group_by_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Group_by_listContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_group_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup_clause" ):
                listener.enterGroup_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup_clause" ):
                listener.exitGroup_clause(self)




    def group_clause(self):

        localctx = SQLSimplifiedParser.Group_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_group_clause)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(SQLSimplifiedParser.GROUP_P)
                self.state = 257
                self.match(SQLSimplifiedParser.BY)
                self.state = 258
                self.group_by_list(0)
                pass
            elif token in [2, 4, 23, 28, 31]:
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


    class Group_by_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnref(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.ColumnrefContext,0)


        def group_by_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Group_by_listContext,0)


        def COMMA(self):
            return self.getToken(SQLSimplifiedParser.COMMA, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_group_by_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup_by_list" ):
                listener.enterGroup_by_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup_by_list" ):
                listener.exitGroup_by_list(self)



    def group_by_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SQLSimplifiedParser.Group_by_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_group_by_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.columnref()
            self._ctx.stop = self._input.LT(-1)
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SQLSimplifiedParser.Group_by_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_group_by_list)
                    self.state = 265
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 266
                    self.match(SQLSimplifiedParser.COMMA)
                    self.state = 267
                    self.columnref() 
                self.state = 272
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Having_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HAVING(self):
            return self.getToken(SQLSimplifiedParser.HAVING, 0)

        def c_expr(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.C_exprContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_having_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHaving_clause" ):
                listener.enterHaving_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHaving_clause" ):
                listener.exitHaving_clause(self)




    def having_clause(self):

        localctx = SQLSimplifiedParser.Having_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_having_clause)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(SQLSimplifiedParser.HAVING)
                self.state = 274
                self.c_expr()
                pass
            elif token in [2, 4, 28, 31]:
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


    class Sort_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDER(self):
            return self.getToken(SQLSimplifiedParser.ORDER, 0)

        def BY(self):
            return self.getToken(SQLSimplifiedParser.BY, 0)

        def sortby_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Sortby_listContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_sort_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSort_clause" ):
                listener.enterSort_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSort_clause" ):
                listener.exitSort_clause(self)




    def sort_clause(self):

        localctx = SQLSimplifiedParser.Sort_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_sort_clause)
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(SQLSimplifiedParser.ORDER)
                self.state = 279
                self.match(SQLSimplifiedParser.BY)
                self.state = 280
                self.sortby_list()
                pass
            elif token in [2, 4, 31]:
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


    class Column_list_or_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(SQLSimplifiedParser.STAR, 0)

        def column_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Column_listContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_column_list_or_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_list_or_star" ):
                listener.enterColumn_list_or_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_list_or_star" ):
                listener.exitColumn_list_or_star(self)




    def column_list_or_star(self):

        localctx = SQLSimplifiedParser.Column_list_or_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_column_list_or_star)
        try:
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.match(SQLSimplifiedParser.STAR)
                pass
            elif token in [1, 36, 39, 40, 41, 42, 45, 47, 56, 69, 71]:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.column_list(0)
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


    class Column_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnref(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.ColumnrefContext,0)


        def column_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Column_listContext,0)


        def COMMA(self):
            return self.getToken(SQLSimplifiedParser.COMMA, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_column_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_list" ):
                listener.enterColumn_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_list" ):
                listener.exitColumn_list(self)



    def column_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SQLSimplifiedParser.Column_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_column_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.columnref()
            self._ctx.stop = self._input.LT(-1)
            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SQLSimplifiedParser.Column_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_column_list)
                    self.state = 291
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 292
                    self.match(SQLSimplifiedParser.COMMA)
                    self.state = 293
                    self.columnref() 
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Sortby_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sortby(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.SortbyContext,0)


        def COMMA(self):
            return self.getToken(SQLSimplifiedParser.COMMA, 0)

        def sortby_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Sortby_listContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_sortby_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSortby_list" ):
                listener.enterSortby_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSortby_list" ):
                listener.exitSortby_list(self)




    def sortby_list(self):

        localctx = SQLSimplifiedParser.Sortby_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_sortby_list)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.sortby()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.sortby()
                self.state = 301
                self.match(SQLSimplifiedParser.COMMA)
                self.state = 302
                self.sortby_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class From_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_ref(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Table_refContext,0)


        def from_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.From_listContext,0)


        def COMMA(self):
            return self.getToken(SQLSimplifiedParser.COMMA, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_from_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom_list" ):
                listener.enterFrom_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom_list" ):
                listener.exitFrom_list(self)



    def from_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SQLSimplifiedParser.From_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_from_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.table_ref()
            self._ctx.stop = self._input.LT(-1)
            self.state = 314
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SQLSimplifiedParser.From_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_from_list)
                    self.state = 309
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 310
                    self.match(SQLSimplifiedParser.COMMA)
                    self.state = 311
                    self.table_ref() 
                self.state = 316
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class From_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def from_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.From_listContext,0)


        def OPEN_PAREN(self):
            return self.getToken(SQLSimplifiedParser.OPEN_PAREN, 0)

        def select_statement(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Select_statementContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(SQLSimplifiedParser.CLOSE_PAREN, 0)

        def AS(self):
            return self.getToken(SQLSimplifiedParser.AS, 0)

        def table_ref(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Table_refContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_from_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom_clause" ):
                listener.enterFrom_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom_clause" ):
                listener.exitFrom_clause(self)




    def from_clause(self):

        localctx = SQLSimplifiedParser.From_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_from_clause)
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.from_list(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 319
                self.select_statement()
                self.state = 320
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                self.state = 321
                self.match(SQLSimplifiedParser.AS)
                self.state = 322
                self.table_ref()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SortbyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnref(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.ColumnrefContext,0)


        def Identifier(self):
            return self.getToken(SQLSimplifiedParser.Identifier, 0)

        def USING(self):
            return self.getToken(SQLSimplifiedParser.USING, 0)

        def gt_lt(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Gt_ltContext,0)


        def asc_desc(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Asc_descContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_sortby

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSortby" ):
                listener.enterSortby(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSortby" ):
                listener.exitSortby(self)




    def sortby(self):

        localctx = SQLSimplifiedParser.SortbyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_sortby)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.columnref()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.match(SQLSimplifiedParser.Identifier)
                self.state = 328
                self.match(SQLSimplifiedParser.USING)
                self.state = 329
                self.gt_lt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 330
                self.match(SQLSimplifiedParser.Identifier)
                self.state = 331
                self.asc_desc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnrefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SQLSimplifiedParser.Identifier, 0)

        def AS(self):
            return self.getToken(SQLSimplifiedParser.AS, 0)

        def collabel(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.CollabelContext,0)


        def table_ref(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Table_refContext,0)


        def DOT(self):
            return self.getToken(SQLSimplifiedParser.DOT, 0)

        def identifier_or_star(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Identifier_or_starContext,0)


        def Integral(self):
            return self.getToken(SQLSimplifiedParser.Integral, 0)

        def StringConstant(self):
            return self.getToken(SQLSimplifiedParser.StringConstant, 0)

        def Numeric(self):
            return self.getToken(SQLSimplifiedParser.Numeric, 0)

        def typeidentifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLSimplifiedParser.TypeidentifierContext)
            else:
                return self.getTypedRuleContext(SQLSimplifiedParser.TypeidentifierContext,i)


        def f_expr(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.F_exprContext,0)


        def VALUE_P(self):
            return self.getToken(SQLSimplifiedParser.VALUE_P, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_columnref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnref" ):
                listener.enterColumnref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnref" ):
                listener.exitColumnref(self)




    def columnref(self):

        localctx = SQLSimplifiedParser.ColumnrefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_columnref)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(SQLSimplifiedParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.match(SQLSimplifiedParser.Identifier)
                self.state = 336
                self.match(SQLSimplifiedParser.AS)
                self.state = 337
                self.collabel()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 338
                self.table_ref()
                self.state = 339
                self.match(SQLSimplifiedParser.DOT)
                self.state = 340
                self.identifier_or_star()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 342
                self.table_ref()
                self.state = 343
                self.match(SQLSimplifiedParser.DOT)
                self.state = 344
                self.identifier_or_star()
                self.state = 345
                self.match(SQLSimplifiedParser.AS)
                self.state = 346
                self.collabel()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 348
                self.match(SQLSimplifiedParser.Integral)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 349
                self.match(SQLSimplifiedParser.StringConstant)
                self.state = 350
                self.match(SQLSimplifiedParser.AS)
                self.state = 351
                self.collabel()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 352
                self.match(SQLSimplifiedParser.StringConstant)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 353
                self.match(SQLSimplifiedParser.Numeric)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 354
                self.match(SQLSimplifiedParser.Numeric)
                self.state = 355
                self.match(SQLSimplifiedParser.AS)
                self.state = 356
                self.collabel()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 357
                self.typeidentifier()
                self.state = 358
                self.match(SQLSimplifiedParser.StringConstant)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 360
                self.typeidentifier()
                self.state = 361
                self.match(SQLSimplifiedParser.StringConstant)
                self.state = 362
                self.typeidentifier()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 364
                self.f_expr()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 365
                self.f_expr()
                self.state = 366
                self.match(SQLSimplifiedParser.AS)
                self.state = 367
                self.collabel()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 369
                self.f_expr()
                self.state = 370
                self.match(SQLSimplifiedParser.AS)
                self.state = 371
                self.match(SQLSimplifiedParser.VALUE_P)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_refContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SQLSimplifiedParser.Identifier, 0)

        def AS(self):
            return self.getToken(SQLSimplifiedParser.AS, 0)

        def collabel(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.CollabelContext,0)


        def f_expr(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.F_exprContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_table_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_ref" ):
                listener.enterTable_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_ref" ):
                listener.exitTable_ref(self)




    def table_ref(self):

        localctx = SQLSimplifiedParser.Table_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_table_ref)
        try:
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.match(SQLSimplifiedParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.match(SQLSimplifiedParser.Identifier)
                self.state = 377
                self.match(SQLSimplifiedParser.AS)
                self.state = 378
                self.collabel()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 379
                self.f_expr()
                self.state = 380
                self.match(SQLSimplifiedParser.AS)
                self.state = 381
                self.match(SQLSimplifiedParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeidentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SQLSimplifiedParser.Identifier, 0)

        def TIME(self):
            return self.getToken(SQLSimplifiedParser.TIME, 0)

        def INTERVAL(self):
            return self.getToken(SQLSimplifiedParser.INTERVAL, 0)

        def DAY_P(self):
            return self.getToken(SQLSimplifiedParser.DAY_P, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_typeidentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeidentifier" ):
                listener.enterTypeidentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeidentifier" ):
                listener.exitTypeidentifier(self)




    def typeidentifier(self):

        localctx = SQLSimplifiedParser.TypeidentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_typeidentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 146303765970944) != 0)):
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


    class Binary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_op(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Logic_opContext,0)


        def math_op(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Math_opContext,0)


        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_binary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_op" ):
                listener.enterBinary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_op" ):
                listener.exitBinary_op(self)




    def binary_op(self):

        localctx = SQLSimplifiedParser.Binary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_binary_op)
        try:
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.logic_op()
                pass
            elif token in [6, 9, 10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.math_op()
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


    class Math_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(SQLSimplifiedParser.LT, 0)

        def GT(self):
            return self.getToken(SQLSimplifiedParser.GT, 0)

        def EQUAL(self):
            return self.getToken(SQLSimplifiedParser.EQUAL, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_math_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_op" ):
                listener.enterMath_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_op" ):
                listener.exitMath_op(self)




    def math_op(self):

        localctx = SQLSimplifiedParser.Math_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_math_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1600) != 0)):
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


    class Logic_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(SQLSimplifiedParser.AND, 0)

        def OR(self):
            return self.getToken(SQLSimplifiedParser.OR, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_logic_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_op" ):
                listener.enterLogic_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_op" ):
                listener.exitLogic_op(self)




    def logic_op(self):

        localctx = SQLSimplifiedParser.Logic_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_logic_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            _la = self._input.LA(1)
            if not(_la==13 or _la==27):
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


    class Unary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(SQLSimplifiedParser.NOT, 0)

        def EXISTS(self):
            return self.getToken(SQLSimplifiedParser.EXISTS, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_unary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_op" ):
                listener.enterUnary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_op" ):
                listener.exitUnary_op(self)




    def unary_op(self):

        localctx = SQLSimplifiedParser.Unary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_unary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            _la = self._input.LA(1)
            if not(_la==24 or _la==38):
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


    class Identifier_or_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SQLSimplifiedParser.Identifier, 0)

        def STAR(self):
            return self.getToken(SQLSimplifiedParser.STAR, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_identifier_or_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier_or_star" ):
                listener.enterIdentifier_or_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier_or_star" ):
                listener.exitIdentifier_or_star(self)




    def identifier_or_star(self):

        localctx = SQLSimplifiedParser.Identifier_or_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_identifier_or_star)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            _la = self._input.LA(1)
            if not(_la==5 or _la==47):
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


    class Gt_ltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(SQLSimplifiedParser.GT, 0)

        def LT(self):
            return self.getToken(SQLSimplifiedParser.LT, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_gt_lt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGt_lt" ):
                listener.enterGt_lt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGt_lt" ):
                listener.exitGt_lt(self)




    def gt_lt(self):

        localctx = SQLSimplifiedParser.Gt_ltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_gt_lt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
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


    class Asc_descContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASC(self):
            return self.getToken(SQLSimplifiedParser.ASC, 0)

        def DESC(self):
            return self.getToken(SQLSimplifiedParser.DESC, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_asc_desc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsc_desc" ):
                listener.enterAsc_desc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsc_desc" ):
                listener.exitAsc_desc(self)




    def asc_desc(self):

        localctx = SQLSimplifiedParser.Asc_descContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_asc_desc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            _la = self._input.LA(1)
            if not(_la==15 or _la==17):
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


    class CollabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SQLSimplifiedParser.Identifier, 0)

        def getRuleIndex(self):
            return SQLSimplifiedParser.RULE_collabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCollabel" ):
                listener.enterCollabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCollabel" ):
                listener.exitCollabel(self)




    def collabel(self):

        localctx = SQLSimplifiedParser.CollabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_collabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(SQLSimplifiedParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.binary_op_fexpr_list_sempred
        self._predicates[9] = self.binary_op_columnref_list_sempred
        self._predicates[14] = self.group_by_list_sempred
        self._predicates[18] = self.column_list_sempred
        self._predicates[20] = self.from_list_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def binary_op_fexpr_list_sempred(self, localctx:Binary_op_fexpr_listContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def binary_op_columnref_list_sempred(self, localctx:Binary_op_columnref_listContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def group_by_list_sempred(self, localctx:Group_by_listContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def column_list_sempred(self, localctx:Column_listContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def from_list_sempred(self, localctx:From_listContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




