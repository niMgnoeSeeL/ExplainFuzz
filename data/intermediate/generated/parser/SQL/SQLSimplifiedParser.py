# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/SQL/SQLSimplifiedParser.g4 by ANTLR 4.13.0
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
        4,1,88,382,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,85,8,1,1,2,1,2,1,2,3,2,90,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,3,3,117,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,
        4,178,8,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,5,6,187,8,6,10,6,12,6,190,
        9,6,1,7,1,7,1,7,1,7,3,7,196,8,7,1,8,1,8,1,8,1,8,3,8,202,8,8,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,212,8,9,10,9,12,9,215,9,9,1,10,1,
        10,1,10,3,10,220,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,237,8,11,1,12,1,12,1,12,1,
        12,3,12,243,8,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,251,8,13,10,
        13,12,13,254,9,13,1,14,1,14,1,14,3,14,259,8,14,1,15,1,15,1,15,1,
        15,3,15,265,8,15,1,16,1,16,3,16,269,8,16,1,17,1,17,1,17,1,17,1,17,
        1,17,5,17,277,8,17,10,17,12,17,280,9,17,1,18,1,18,1,18,1,18,1,18,
        3,18,287,8,18,1,19,1,19,1,19,1,19,1,19,1,19,5,19,295,8,19,10,19,
        12,19,298,9,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,307,8,20,
        1,21,1,21,1,21,1,21,1,21,1,21,3,21,315,8,21,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,356,8,22,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,366,8,23,1,24,1,24,1,25,
        1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,30,0,5,
        12,18,26,34,38,31,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,54,56,58,60,0,7,2,0,25,25,69,69,4,
        0,36,36,40,40,42,42,47,47,4,0,6,6,9,10,13,13,27,27,2,0,24,24,38,
        38,2,0,5,5,47,47,1,0,9,10,2,0,15,15,17,17,401,0,62,1,0,0,0,2,84,
        1,0,0,0,4,89,1,0,0,0,6,116,1,0,0,0,8,177,1,0,0,0,10,179,1,0,0,0,
        12,181,1,0,0,0,14,195,1,0,0,0,16,201,1,0,0,0,18,203,1,0,0,0,20,219,
        1,0,0,0,22,236,1,0,0,0,24,242,1,0,0,0,26,244,1,0,0,0,28,258,1,0,
        0,0,30,264,1,0,0,0,32,268,1,0,0,0,34,270,1,0,0,0,36,286,1,0,0,0,
        38,288,1,0,0,0,40,306,1,0,0,0,42,314,1,0,0,0,44,355,1,0,0,0,46,365,
        1,0,0,0,48,367,1,0,0,0,50,369,1,0,0,0,52,371,1,0,0,0,54,373,1,0,
        0,0,56,375,1,0,0,0,58,377,1,0,0,0,60,379,1,0,0,0,62,63,3,2,1,0,63,
        64,5,4,0,0,64,65,5,0,0,1,65,1,1,0,0,0,66,67,5,29,0,0,67,68,3,32,
        16,0,68,69,5,21,0,0,69,70,3,40,20,0,70,71,3,22,11,0,71,72,3,20,10,
        0,72,73,3,24,12,0,73,74,3,28,14,0,74,75,3,30,15,0,75,76,3,4,2,0,
        76,85,1,0,0,0,77,78,5,29,0,0,78,79,5,18,0,0,79,80,3,32,16,0,80,81,
        5,21,0,0,81,82,3,40,20,0,82,83,3,30,15,0,83,85,1,0,0,0,84,66,1,0,
        0,0,84,77,1,0,0,0,85,3,1,0,0,0,86,90,1,0,0,0,87,88,5,31,0,0,88,90,
        3,2,1,0,89,86,1,0,0,0,89,87,1,0,0,0,90,5,1,0,0,0,91,117,3,44,22,
        0,92,93,3,44,22,0,93,94,3,18,9,0,94,117,1,0,0,0,95,96,3,52,26,0,
        96,97,3,6,3,0,97,117,1,0,0,0,98,117,3,8,4,0,99,100,5,1,0,0,100,101,
        3,2,1,0,101,102,5,2,0,0,102,117,1,0,0,0,103,117,5,5,0,0,104,117,
        5,69,0,0,105,117,5,71,0,0,106,107,5,18,0,0,107,117,3,6,3,0,108,109,
        5,1,0,0,109,110,3,14,7,0,110,111,5,2,0,0,111,117,1,0,0,0,112,113,
        5,1,0,0,113,114,3,16,8,0,114,115,5,2,0,0,115,117,1,0,0,0,116,91,
        1,0,0,0,116,92,1,0,0,0,116,95,1,0,0,0,116,98,1,0,0,0,116,99,1,0,
        0,0,116,103,1,0,0,0,116,104,1,0,0,0,116,105,1,0,0,0,116,106,1,0,
        0,0,116,108,1,0,0,0,116,112,1,0,0,0,117,7,1,0,0,0,118,119,5,47,0,
        0,119,120,5,1,0,0,120,121,3,6,3,0,121,122,5,2,0,0,122,178,1,0,0,
        0,123,124,5,1,0,0,124,125,3,6,3,0,125,126,5,2,0,0,126,178,1,0,0,
        0,127,128,5,39,0,0,128,129,5,1,0,0,129,130,5,37,0,0,130,131,5,21,
        0,0,131,132,3,6,3,0,132,133,5,2,0,0,133,178,1,0,0,0,134,135,5,47,
        0,0,135,136,5,1,0,0,136,137,5,16,0,0,137,138,5,32,0,0,138,139,3,
        6,3,0,139,140,5,30,0,0,140,141,3,6,3,0,141,142,5,19,0,0,142,143,
        3,10,5,0,143,144,5,44,0,0,144,145,5,2,0,0,145,146,3,12,6,0,146,178,
        1,0,0,0,147,148,5,41,0,0,148,149,5,1,0,0,149,150,3,6,3,0,150,151,
        5,21,0,0,151,152,5,69,0,0,152,153,5,20,0,0,153,154,5,69,0,0,154,
        155,5,2,0,0,155,178,1,0,0,0,156,157,5,45,0,0,157,158,5,1,0,0,158,
        159,3,6,3,0,159,160,5,8,0,0,160,161,3,6,3,0,161,162,5,3,0,0,162,
        163,5,69,0,0,163,164,5,2,0,0,164,178,1,0,0,0,165,166,5,1,0,0,166,
        167,5,16,0,0,167,168,5,32,0,0,168,169,3,6,3,0,169,170,5,30,0,0,170,
        171,3,6,3,0,171,172,5,19,0,0,172,173,3,10,5,0,173,174,5,44,0,0,174,
        175,5,2,0,0,175,176,3,12,6,0,176,178,1,0,0,0,177,118,1,0,0,0,177,
        123,1,0,0,0,177,127,1,0,0,0,177,134,1,0,0,0,177,147,1,0,0,0,177,
        156,1,0,0,0,177,165,1,0,0,0,178,9,1,0,0,0,179,180,7,0,0,0,180,11,
        1,0,0,0,181,188,6,6,-1,0,182,183,10,1,0,0,183,184,3,50,25,0,184,
        185,3,8,4,0,185,187,1,0,0,0,186,182,1,0,0,0,187,190,1,0,0,0,188,
        186,1,0,0,0,188,189,1,0,0,0,189,13,1,0,0,0,190,188,1,0,0,0,191,196,
        5,56,0,0,192,193,5,56,0,0,193,194,5,3,0,0,194,196,3,14,7,0,195,191,
        1,0,0,0,195,192,1,0,0,0,196,15,1,0,0,0,197,202,5,69,0,0,198,199,
        5,69,0,0,199,200,5,3,0,0,200,202,3,16,8,0,201,197,1,0,0,0,201,198,
        1,0,0,0,202,17,1,0,0,0,203,204,6,9,-1,0,204,205,3,50,25,0,205,206,
        3,44,22,0,206,213,1,0,0,0,207,208,10,1,0,0,208,209,3,50,25,0,209,
        210,3,44,22,0,210,212,1,0,0,0,211,207,1,0,0,0,212,215,1,0,0,0,213,
        211,1,0,0,0,213,214,1,0,0,0,214,19,1,0,0,0,215,213,1,0,0,0,216,217,
        5,33,0,0,217,220,3,6,3,0,218,220,1,0,0,0,219,216,1,0,0,0,219,218,
        1,0,0,0,220,21,1,0,0,0,221,222,5,34,0,0,222,223,3,44,22,0,223,224,
        5,26,0,0,224,225,3,6,3,0,225,237,1,0,0,0,226,227,5,34,0,0,227,228,
        5,1,0,0,228,229,3,2,1,0,229,230,5,2,0,0,230,231,5,14,0,0,231,232,
        3,46,23,0,232,233,5,26,0,0,233,234,3,6,3,0,234,237,1,0,0,0,235,237,
        1,0,0,0,236,221,1,0,0,0,236,226,1,0,0,0,236,235,1,0,0,0,237,23,1,
        0,0,0,238,239,5,22,0,0,239,240,5,35,0,0,240,243,3,26,13,0,241,243,
        1,0,0,0,242,238,1,0,0,0,242,241,1,0,0,0,243,25,1,0,0,0,244,245,6,
        13,-1,0,245,246,3,44,22,0,246,252,1,0,0,0,247,248,10,1,0,0,248,249,
        5,3,0,0,249,251,3,44,22,0,250,247,1,0,0,0,251,254,1,0,0,0,252,250,
        1,0,0,0,252,253,1,0,0,0,253,27,1,0,0,0,254,252,1,0,0,0,255,256,5,
        23,0,0,256,259,3,6,3,0,257,259,1,0,0,0,258,255,1,0,0,0,258,257,1,
        0,0,0,259,29,1,0,0,0,260,261,5,28,0,0,261,262,5,35,0,0,262,265,3,
        36,18,0,263,265,1,0,0,0,264,260,1,0,0,0,264,263,1,0,0,0,265,31,1,
        0,0,0,266,269,5,5,0,0,267,269,3,34,17,0,268,266,1,0,0,0,268,267,
        1,0,0,0,269,33,1,0,0,0,270,271,6,17,-1,0,271,272,3,44,22,0,272,278,
        1,0,0,0,273,274,10,1,0,0,274,275,5,3,0,0,275,277,3,44,22,0,276,273,
        1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,279,1,0,0,0,279,35,1,
        0,0,0,280,278,1,0,0,0,281,287,3,42,21,0,282,283,3,42,21,0,283,284,
        5,3,0,0,284,285,3,36,18,0,285,287,1,0,0,0,286,281,1,0,0,0,286,282,
        1,0,0,0,287,37,1,0,0,0,288,289,6,19,-1,0,289,290,3,46,23,0,290,296,
        1,0,0,0,291,292,10,1,0,0,292,293,5,3,0,0,293,295,3,46,23,0,294,291,
        1,0,0,0,295,298,1,0,0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,39,1,
        0,0,0,298,296,1,0,0,0,299,307,3,38,19,0,300,301,5,1,0,0,301,302,
        3,2,1,0,302,303,5,2,0,0,303,304,5,14,0,0,304,305,3,46,23,0,305,307,
        1,0,0,0,306,299,1,0,0,0,306,300,1,0,0,0,307,41,1,0,0,0,308,315,3,
        44,22,0,309,310,5,47,0,0,310,311,5,46,0,0,311,315,3,56,28,0,312,
        313,5,47,0,0,313,315,3,58,29,0,314,308,1,0,0,0,314,309,1,0,0,0,314,
        312,1,0,0,0,315,43,1,0,0,0,316,356,5,47,0,0,317,318,5,47,0,0,318,
        319,5,14,0,0,319,356,3,60,30,0,320,321,3,46,23,0,321,322,5,7,0,0,
        322,323,3,54,27,0,323,356,1,0,0,0,324,325,3,46,23,0,325,326,5,7,
        0,0,326,327,3,54,27,0,327,328,5,14,0,0,328,329,3,60,30,0,329,356,
        1,0,0,0,330,356,5,69,0,0,331,332,5,56,0,0,332,333,5,14,0,0,333,356,
        3,60,30,0,334,356,5,56,0,0,335,356,5,71,0,0,336,337,5,71,0,0,337,
        338,5,14,0,0,338,356,3,60,30,0,339,340,3,48,24,0,340,341,5,56,0,
        0,341,356,1,0,0,0,342,343,3,48,24,0,343,344,5,56,0,0,344,345,3,48,
        24,0,345,356,1,0,0,0,346,356,3,8,4,0,347,348,3,8,4,0,348,349,5,14,
        0,0,349,350,3,60,30,0,350,356,1,0,0,0,351,352,3,8,4,0,352,353,5,
        14,0,0,353,354,5,43,0,0,354,356,1,0,0,0,355,316,1,0,0,0,355,317,
        1,0,0,0,355,320,1,0,0,0,355,324,1,0,0,0,355,330,1,0,0,0,355,331,
        1,0,0,0,355,334,1,0,0,0,355,335,1,0,0,0,355,336,1,0,0,0,355,339,
        1,0,0,0,355,342,1,0,0,0,355,346,1,0,0,0,355,347,1,0,0,0,355,351,
        1,0,0,0,356,45,1,0,0,0,357,366,5,47,0,0,358,359,5,47,0,0,359,360,
        5,14,0,0,360,366,5,47,0,0,361,362,3,8,4,0,362,363,5,14,0,0,363,364,
        5,47,0,0,364,366,1,0,0,0,365,357,1,0,0,0,365,358,1,0,0,0,365,361,
        1,0,0,0,366,47,1,0,0,0,367,368,7,1,0,0,368,49,1,0,0,0,369,370,7,
        2,0,0,370,51,1,0,0,0,371,372,7,3,0,0,372,53,1,0,0,0,373,374,7,4,
        0,0,374,55,1,0,0,0,375,376,7,5,0,0,376,57,1,0,0,0,377,378,7,6,0,
        0,378,59,1,0,0,0,379,380,5,47,0,0,380,61,1,0,0,0,22,84,89,116,177,
        188,195,201,213,219,236,242,252,258,264,268,278,286,296,306,314,
        355,365
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
    RULE_group_clause = 12
    RULE_group_by_list = 13
    RULE_having_clause = 14
    RULE_sort_clause = 15
    RULE_column_list_or_star = 16
    RULE_column_list = 17
    RULE_sortby_list = 18
    RULE_from_list = 19
    RULE_from_clause = 20
    RULE_sortby = 21
    RULE_columnref = 22
    RULE_table_ref = 23
    RULE_typeidentifier = 24
    RULE_binary_op = 25
    RULE_unary_op = 26
    RULE_identifier_or_star = 27
    RULE_gt_lt = 28
    RULE_asc_desc = 29
    RULE_collabel = 30

    ruleNames =  [ "start", "select_statement", "union_list", "c_expr", 
                   "f_expr", "integral_or_null", "binary_op_fexpr_list", 
                   "string_list", "integral_list", "binary_op_columnref_list", 
                   "where_clause", "join_clause", "group_clause", "group_by_list", 
                   "having_clause", "sort_clause", "column_list_or_star", 
                   "column_list", "sortby_list", "from_list", "from_clause", 
                   "sortby", "columnref", "table_ref", "typeidentifier", 
                   "binary_op", "unary_op", "identifier_or_star", "gt_lt", 
                   "asc_desc", "collabel" ]

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
            self.state = 62
            self.select_statement()
            self.state = 63
            self.match(SQLSimplifiedParser.SEMI)
            self.state = 64
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
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(SQLSimplifiedParser.SELECT)
                self.state = 67
                self.column_list_or_star()
                self.state = 68
                self.match(SQLSimplifiedParser.FROM)
                self.state = 69
                self.from_clause()
                self.state = 70
                self.join_clause()
                self.state = 71
                self.where_clause()
                self.state = 72
                self.group_clause()
                self.state = 73
                self.having_clause()
                self.state = 74
                self.sort_clause()
                self.state = 75
                self.union_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(SQLSimplifiedParser.SELECT)
                self.state = 78
                self.match(SQLSimplifiedParser.DISTINCT)
                self.state = 79
                self.column_list_or_star()
                self.state = 80
                self.match(SQLSimplifiedParser.FROM)
                self.state = 81
                self.from_clause()
                self.state = 82
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
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 4]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(SQLSimplifiedParser.UNION)
                self.state = 88
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
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.columnref()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.columnref()
                self.state = 93
                self.binary_op_columnref_list(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.unary_op()
                self.state = 96
                self.c_expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.f_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 99
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 100
                self.select_statement()
                self.state = 101
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 103
                self.match(SQLSimplifiedParser.STAR)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 104
                self.match(SQLSimplifiedParser.Integral)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 105
                self.match(SQLSimplifiedParser.Numeric)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 106
                self.match(SQLSimplifiedParser.DISTINCT)
                self.state = 107
                self.c_expr()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 108
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 109
                self.string_list()
                self.state = 110
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 112
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 113
                self.integral_list()
                self.state = 114
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
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(SQLSimplifiedParser.Identifier)
                self.state = 119
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 120
                self.c_expr()
                self.state = 121
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 124
                self.c_expr()
                self.state = 125
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.match(SQLSimplifiedParser.EXTRACT)
                self.state = 128
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 129
                self.match(SQLSimplifiedParser.YEAR_P)
                self.state = 130
                self.match(SQLSimplifiedParser.FROM)
                self.state = 131
                self.c_expr()
                self.state = 132
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 134
                self.match(SQLSimplifiedParser.Identifier)
                self.state = 135
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 136
                self.match(SQLSimplifiedParser.CASE)
                self.state = 137
                self.match(SQLSimplifiedParser.WHEN)
                self.state = 138
                self.c_expr()
                self.state = 139
                self.match(SQLSimplifiedParser.THEN)
                self.state = 140
                self.c_expr()
                self.state = 141
                self.match(SQLSimplifiedParser.ELSE)
                self.state = 142
                self.integral_or_null()
                self.state = 143
                self.match(SQLSimplifiedParser.END_P)
                self.state = 144
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                self.state = 145
                self.binary_op_fexpr_list(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 147
                self.match(SQLSimplifiedParser.SUBSTRING)
                self.state = 148
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 149
                self.c_expr()
                self.state = 150
                self.match(SQLSimplifiedParser.FROM)
                self.state = 151
                self.match(SQLSimplifiedParser.Integral)
                self.state = 152
                self.match(SQLSimplifiedParser.FOR)
                self.state = 153
                self.match(SQLSimplifiedParser.Integral)
                self.state = 154
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 156
                self.match(SQLSimplifiedParser.ROUND)
                self.state = 157
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 158
                self.c_expr()
                self.state = 159
                self.match(SQLSimplifiedParser.SLASH)
                self.state = 160
                self.c_expr()
                self.state = 161
                self.match(SQLSimplifiedParser.COMMA)
                self.state = 162
                self.match(SQLSimplifiedParser.Integral)
                self.state = 163
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 165
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 166
                self.match(SQLSimplifiedParser.CASE)
                self.state = 167
                self.match(SQLSimplifiedParser.WHEN)
                self.state = 168
                self.c_expr()
                self.state = 169
                self.match(SQLSimplifiedParser.THEN)
                self.state = 170
                self.c_expr()
                self.state = 171
                self.match(SQLSimplifiedParser.ELSE)
                self.state = 172
                self.integral_or_null()
                self.state = 173
                self.match(SQLSimplifiedParser.END_P)
                self.state = 174
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                self.state = 175
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
            self.state = 179
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
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SQLSimplifiedParser.Binary_op_fexpr_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_binary_op_fexpr_list)
                    self.state = 182
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 183
                    self.binary_op()
                    self.state = 184
                    self.f_expr() 
                self.state = 190
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
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(SQLSimplifiedParser.StringConstant)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(SQLSimplifiedParser.StringConstant)
                self.state = 193
                self.match(SQLSimplifiedParser.COMMA)
                self.state = 194
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
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(SQLSimplifiedParser.Integral)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.match(SQLSimplifiedParser.Integral)
                self.state = 199
                self.match(SQLSimplifiedParser.COMMA)
                self.state = 200
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

        def binary_op(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Binary_opContext,0)


        def columnref(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.ColumnrefContext,0)


        def binary_op_columnref_list(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.Binary_op_columnref_listContext,0)


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
            self.state = 204
            self.binary_op()
            self.state = 205
            self.columnref()
            self._ctx.stop = self._input.LT(-1)
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SQLSimplifiedParser.Binary_op_columnref_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_binary_op_columnref_list)
                    self.state = 207
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 208
                    self.binary_op()
                    self.state = 209
                    self.columnref() 
                self.state = 215
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
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(SQLSimplifiedParser.WHERE)
                self.state = 217
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

        def columnref(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.ColumnrefContext,0)


        def ON(self):
            return self.getToken(SQLSimplifiedParser.ON, 0)

        def c_expr(self):
            return self.getTypedRuleContext(SQLSimplifiedParser.C_exprContext,0)


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
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(SQLSimplifiedParser.JOIN)
                self.state = 222
                self.columnref()
                self.state = 223
                self.match(SQLSimplifiedParser.ON)
                self.state = 224
                self.c_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(SQLSimplifiedParser.JOIN)
                self.state = 227
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 228
                self.select_statement()
                self.state = 229
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                self.state = 230
                self.match(SQLSimplifiedParser.AS)
                self.state = 231
                self.table_ref()
                self.state = 232
                self.match(SQLSimplifiedParser.ON)
                self.state = 233
                self.c_expr()
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
        self.enterRule(localctx, 24, self.RULE_group_clause)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(SQLSimplifiedParser.GROUP_P)
                self.state = 239
                self.match(SQLSimplifiedParser.BY)
                self.state = 240
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_group_by_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.columnref()
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SQLSimplifiedParser.Group_by_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_group_by_list)
                    self.state = 247
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 248
                    self.match(SQLSimplifiedParser.COMMA)
                    self.state = 249
                    self.columnref() 
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_having_clause)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(SQLSimplifiedParser.HAVING)
                self.state = 256
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
        self.enterRule(localctx, 30, self.RULE_sort_clause)
        try:
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(SQLSimplifiedParser.ORDER)
                self.state = 261
                self.match(SQLSimplifiedParser.BY)
                self.state = 262
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
        self.enterRule(localctx, 32, self.RULE_column_list_or_star)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(SQLSimplifiedParser.STAR)
                pass
            elif token in [1, 36, 39, 40, 41, 42, 45, 47, 56, 69, 71]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_column_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.columnref()
            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SQLSimplifiedParser.Column_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_column_list)
                    self.state = 273
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 274
                    self.match(SQLSimplifiedParser.COMMA)
                    self.state = 275
                    self.columnref() 
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self.enterRule(localctx, 36, self.RULE_sortby_list)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.sortby()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.sortby()
                self.state = 283
                self.match(SQLSimplifiedParser.COMMA)
                self.state = 284
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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_from_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.table_ref()
            self._ctx.stop = self._input.LT(-1)
            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SQLSimplifiedParser.From_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_from_list)
                    self.state = 291
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 292
                    self.match(SQLSimplifiedParser.COMMA)
                    self.state = 293
                    self.table_ref() 
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self.enterRule(localctx, 40, self.RULE_from_clause)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.from_list(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.match(SQLSimplifiedParser.OPEN_PAREN)
                self.state = 301
                self.select_statement()
                self.state = 302
                self.match(SQLSimplifiedParser.CLOSE_PAREN)
                self.state = 303
                self.match(SQLSimplifiedParser.AS)
                self.state = 304
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
        self.enterRule(localctx, 42, self.RULE_sortby)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.columnref()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.match(SQLSimplifiedParser.Identifier)
                self.state = 310
                self.match(SQLSimplifiedParser.USING)
                self.state = 311
                self.gt_lt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.match(SQLSimplifiedParser.Identifier)
                self.state = 313
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
        self.enterRule(localctx, 44, self.RULE_columnref)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(SQLSimplifiedParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.match(SQLSimplifiedParser.Identifier)
                self.state = 318
                self.match(SQLSimplifiedParser.AS)
                self.state = 319
                self.collabel()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 320
                self.table_ref()
                self.state = 321
                self.match(SQLSimplifiedParser.DOT)
                self.state = 322
                self.identifier_or_star()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 324
                self.table_ref()
                self.state = 325
                self.match(SQLSimplifiedParser.DOT)
                self.state = 326
                self.identifier_or_star()
                self.state = 327
                self.match(SQLSimplifiedParser.AS)
                self.state = 328
                self.collabel()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 330
                self.match(SQLSimplifiedParser.Integral)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 331
                self.match(SQLSimplifiedParser.StringConstant)
                self.state = 332
                self.match(SQLSimplifiedParser.AS)
                self.state = 333
                self.collabel()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 334
                self.match(SQLSimplifiedParser.StringConstant)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 335
                self.match(SQLSimplifiedParser.Numeric)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 336
                self.match(SQLSimplifiedParser.Numeric)
                self.state = 337
                self.match(SQLSimplifiedParser.AS)
                self.state = 338
                self.collabel()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 339
                self.typeidentifier()
                self.state = 340
                self.match(SQLSimplifiedParser.StringConstant)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 342
                self.typeidentifier()
                self.state = 343
                self.match(SQLSimplifiedParser.StringConstant)
                self.state = 344
                self.typeidentifier()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 346
                self.f_expr()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 347
                self.f_expr()
                self.state = 348
                self.match(SQLSimplifiedParser.AS)
                self.state = 349
                self.collabel()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 351
                self.f_expr()
                self.state = 352
                self.match(SQLSimplifiedParser.AS)
                self.state = 353
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

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(SQLSimplifiedParser.Identifier)
            else:
                return self.getToken(SQLSimplifiedParser.Identifier, i)

        def AS(self):
            return self.getToken(SQLSimplifiedParser.AS, 0)

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
        self.enterRule(localctx, 46, self.RULE_table_ref)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(SQLSimplifiedParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.match(SQLSimplifiedParser.Identifier)
                self.state = 359
                self.match(SQLSimplifiedParser.AS)
                self.state = 360
                self.match(SQLSimplifiedParser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 361
                self.f_expr()
                self.state = 362
                self.match(SQLSimplifiedParser.AS)
                self.state = 363
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
        self.enterRule(localctx, 48, self.RULE_typeidentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
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

        def AND(self):
            return self.getToken(SQLSimplifiedParser.AND, 0)

        def OR(self):
            return self.getToken(SQLSimplifiedParser.OR, 0)

        def LT(self):
            return self.getToken(SQLSimplifiedParser.LT, 0)

        def GT(self):
            return self.getToken(SQLSimplifiedParser.GT, 0)

        def EQUAL(self):
            return self.getToken(SQLSimplifiedParser.EQUAL, 0)

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
        self.enterRule(localctx, 50, self.RULE_binary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 134227520) != 0)):
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
        self.enterRule(localctx, 52, self.RULE_unary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
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
        self.enterRule(localctx, 54, self.RULE_identifier_or_star)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
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
        self.enterRule(localctx, 56, self.RULE_gt_lt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
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
        self.enterRule(localctx, 58, self.RULE_asc_desc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
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
        self.enterRule(localctx, 60, self.RULE_collabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
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
        self._predicates[13] = self.group_by_list_sempred
        self._predicates[17] = self.column_list_sempred
        self._predicates[19] = self.from_list_sempred
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
         




