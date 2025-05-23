# Generated from /Users/annaellebaiget/Desktop/MS_Thesis/ExplainFuzz/data/intermediate/grammars/final/B/bParser.g4 by ANTLR 4.11.1
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
        4,1,44,677,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,1,0,1,0,1,
        0,1,0,3,0,109,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,129,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,3,3,141,8,3,1,4,1,4,1,4,1,4,1,4,3,4,148,8,4,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,3,6,157,8,6,1,7,1,7,1,7,1,7,1,7,3,7,164,8,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,
        8,181,8,8,1,9,1,9,1,9,1,9,1,9,3,9,188,8,9,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,3,10,200,8,10,1,11,1,11,1,11,1,11,3,
        11,206,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,3,12,272,8,12,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,
        15,1,15,1,15,3,15,285,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,354,8,16,1,17,1,17,1,
        17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,3,19,369,8,
        19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,
        22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,
        25,1,25,3,25,398,8,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,417,8,28,1,29,1,
        29,1,29,1,29,1,29,3,29,424,8,29,1,30,1,30,1,30,1,30,1,31,1,31,1,
        31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,441,8,31,1,32,1,
        32,1,32,1,32,1,32,1,32,1,32,3,32,450,8,32,1,33,1,33,1,33,1,33,1,
        33,1,33,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,490,8,36,1,37,1,37,1,
        37,1,37,1,37,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,3,38,539,8,38,1,39,1,39,1,39,1,40,1,
        40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,
        40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,
        40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,
        40,3,40,585,8,40,1,41,1,41,1,41,1,41,1,41,3,41,592,8,41,1,42,1,42,
        1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,
        1,43,1,43,1,43,1,43,3,43,613,8,43,1,44,1,44,1,45,1,45,1,46,1,46,
        1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,3,47,629,8,47,1,48,1,48,
        1,49,1,49,1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,
        1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,
        1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,
        1,51,1,51,1,51,3,51,675,8,51,1,51,0,0,52,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,
        64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,0,
        5,1,0,20,21,1,0,22,23,3,0,18,18,22,22,24,36,1,0,40,42,1,0,39,42,
        749,0,108,1,0,0,0,2,128,1,0,0,0,4,130,1,0,0,0,6,140,1,0,0,0,8,147,
        1,0,0,0,10,149,1,0,0,0,12,156,1,0,0,0,14,163,1,0,0,0,16,180,1,0,
        0,0,18,187,1,0,0,0,20,199,1,0,0,0,22,205,1,0,0,0,24,271,1,0,0,0,
        26,273,1,0,0,0,28,275,1,0,0,0,30,284,1,0,0,0,32,353,1,0,0,0,34,355,
        1,0,0,0,36,359,1,0,0,0,38,368,1,0,0,0,40,370,1,0,0,0,42,374,1,0,
        0,0,44,378,1,0,0,0,46,384,1,0,0,0,48,387,1,0,0,0,50,397,1,0,0,0,
        52,399,1,0,0,0,54,404,1,0,0,0,56,416,1,0,0,0,58,423,1,0,0,0,60,425,
        1,0,0,0,62,440,1,0,0,0,64,449,1,0,0,0,66,451,1,0,0,0,68,457,1,0,
        0,0,70,461,1,0,0,0,72,489,1,0,0,0,74,491,1,0,0,0,76,538,1,0,0,0,
        78,540,1,0,0,0,80,584,1,0,0,0,82,591,1,0,0,0,84,593,1,0,0,0,86,612,
        1,0,0,0,88,614,1,0,0,0,90,616,1,0,0,0,92,618,1,0,0,0,94,628,1,0,
        0,0,96,630,1,0,0,0,98,632,1,0,0,0,100,634,1,0,0,0,102,674,1,0,0,
        0,104,105,3,2,1,0,105,106,5,0,0,1,106,109,1,0,0,0,107,109,5,0,0,
        1,108,104,1,0,0,0,108,107,1,0,0,0,109,1,1,0,0,0,110,111,3,16,8,0,
        111,112,3,2,1,0,112,129,1,0,0,0,113,114,3,98,49,0,114,115,3,22,11,
        0,115,116,3,20,10,0,116,117,5,2,0,0,117,129,1,0,0,0,118,119,3,98,
        49,0,119,120,5,3,0,0,120,121,3,18,9,0,121,122,5,4,0,0,122,123,3,
        24,12,0,123,129,1,0,0,0,124,125,3,98,49,0,125,126,3,22,11,0,126,
        127,5,2,0,0,127,129,1,0,0,0,128,110,1,0,0,0,128,113,1,0,0,0,128,
        118,1,0,0,0,128,124,1,0,0,0,129,3,1,0,0,0,130,131,5,1,0,0,131,132,
        3,100,50,0,132,5,1,0,0,0,133,134,3,100,50,0,134,135,3,8,4,0,135,
        141,1,0,0,0,136,141,5,40,0,0,137,141,5,41,0,0,138,141,5,42,0,0,139,
        141,5,39,0,0,140,133,1,0,0,0,140,136,1,0,0,0,140,137,1,0,0,0,140,
        138,1,0,0,0,140,139,1,0,0,0,141,7,1,0,0,0,142,143,3,4,2,0,143,144,
        3,8,4,0,144,148,1,0,0,0,145,146,5,1,0,0,146,148,3,100,50,0,147,142,
        1,0,0,0,147,145,1,0,0,0,148,9,1,0,0,0,149,150,5,1,0,0,150,151,3,
        98,49,0,151,11,1,0,0,0,152,153,3,98,49,0,153,154,3,14,7,0,154,157,
        1,0,0,0,155,157,5,39,0,0,156,152,1,0,0,0,156,155,1,0,0,0,157,13,
        1,0,0,0,158,159,3,10,5,0,159,160,3,14,7,0,160,164,1,0,0,0,161,162,
        5,1,0,0,162,164,3,98,49,0,163,158,1,0,0,0,163,161,1,0,0,0,164,15,
        1,0,0,0,165,166,3,98,49,0,166,167,3,22,11,0,167,168,3,20,10,0,168,
        169,5,2,0,0,169,181,1,0,0,0,170,171,3,98,49,0,171,172,5,3,0,0,172,
        173,3,18,9,0,173,174,5,4,0,0,174,175,3,24,12,0,175,181,1,0,0,0,176,
        177,3,98,49,0,177,178,3,22,11,0,178,179,5,2,0,0,179,181,1,0,0,0,
        180,165,1,0,0,0,180,170,1,0,0,0,180,176,1,0,0,0,181,17,1,0,0,0,182,
        188,1,0,0,0,183,184,3,98,49,0,184,185,3,14,7,0,185,188,1,0,0,0,186,
        188,5,39,0,0,187,182,1,0,0,0,187,183,1,0,0,0,187,186,1,0,0,0,188,
        19,1,0,0,0,189,190,3,6,3,0,190,191,3,20,10,0,191,200,1,0,0,0,192,
        193,3,100,50,0,193,194,3,8,4,0,194,200,1,0,0,0,195,200,5,40,0,0,
        196,200,5,41,0,0,197,200,5,42,0,0,198,200,5,39,0,0,199,189,1,0,0,
        0,199,192,1,0,0,0,199,195,1,0,0,0,199,196,1,0,0,0,199,197,1,0,0,
        0,199,198,1,0,0,0,200,21,1,0,0,0,201,206,1,0,0,0,202,206,5,40,0,
        0,203,206,5,41,0,0,204,206,5,42,0,0,205,201,1,0,0,0,205,202,1,0,
        0,0,205,203,1,0,0,0,205,204,1,0,0,0,206,23,1,0,0,0,207,208,3,98,
        49,0,208,209,5,5,0,0,209,210,3,24,12,0,210,272,1,0,0,0,211,212,5,
        15,0,0,212,213,3,98,49,0,213,214,3,58,29,0,214,215,5,2,0,0,215,272,
        1,0,0,0,216,217,5,16,0,0,217,218,3,98,49,0,218,219,3,22,11,0,219,
        220,3,64,32,0,220,221,5,2,0,0,221,272,1,0,0,0,222,223,5,14,0,0,223,
        224,3,96,48,0,224,225,5,5,0,0,225,226,3,24,12,0,226,272,1,0,0,0,
        227,228,5,6,0,0,228,229,3,32,16,0,229,230,5,7,0,0,230,272,1,0,0,
        0,231,232,5,12,0,0,232,233,5,3,0,0,233,234,3,102,51,0,234,235,5,
        4,0,0,235,236,3,24,12,0,236,237,3,50,25,0,237,272,1,0,0,0,238,239,
        5,11,0,0,239,240,5,3,0,0,240,241,3,102,51,0,241,242,5,4,0,0,242,
        243,3,24,12,0,243,272,1,0,0,0,244,245,5,10,0,0,245,246,3,102,51,
        0,246,247,3,24,12,0,247,272,1,0,0,0,248,249,5,9,0,0,249,250,3,102,
        51,0,250,251,5,2,0,0,251,272,1,0,0,0,252,253,5,8,0,0,253,254,3,38,
        19,0,254,255,5,2,0,0,255,272,1,0,0,0,256,257,3,102,51,0,257,258,
        5,2,0,0,258,272,1,0,0,0,259,272,5,2,0,0,260,261,5,6,0,0,261,272,
        5,7,0,0,262,263,5,15,0,0,263,264,3,98,49,0,264,265,5,2,0,0,265,272,
        1,0,0,0,266,267,5,16,0,0,267,268,3,98,49,0,268,269,3,22,11,0,269,
        270,5,2,0,0,270,272,1,0,0,0,271,207,1,0,0,0,271,211,1,0,0,0,271,
        216,1,0,0,0,271,222,1,0,0,0,271,227,1,0,0,0,271,231,1,0,0,0,271,
        238,1,0,0,0,271,244,1,0,0,0,271,248,1,0,0,0,271,252,1,0,0,0,271,
        256,1,0,0,0,271,259,1,0,0,0,271,260,1,0,0,0,271,262,1,0,0,0,271,
        266,1,0,0,0,272,25,1,0,0,0,273,274,5,2,0,0,274,27,1,0,0,0,275,276,
        3,102,51,0,276,277,5,2,0,0,277,29,1,0,0,0,278,279,5,6,0,0,279,280,
        3,32,16,0,280,281,5,7,0,0,281,285,1,0,0,0,282,283,5,6,0,0,283,285,
        5,7,0,0,284,278,1,0,0,0,284,282,1,0,0,0,285,31,1,0,0,0,286,287,3,
        24,12,0,287,288,3,32,16,0,288,354,1,0,0,0,289,290,3,98,49,0,290,
        291,5,5,0,0,291,292,3,24,12,0,292,354,1,0,0,0,293,294,5,15,0,0,294,
        295,3,98,49,0,295,296,3,58,29,0,296,297,5,2,0,0,297,354,1,0,0,0,
        298,299,5,16,0,0,299,300,3,98,49,0,300,301,3,22,11,0,301,302,3,64,
        32,0,302,303,5,2,0,0,303,354,1,0,0,0,304,305,5,14,0,0,305,306,3,
        96,48,0,306,307,5,5,0,0,307,308,3,24,12,0,308,354,1,0,0,0,309,310,
        5,6,0,0,310,311,3,32,16,0,311,312,5,7,0,0,312,354,1,0,0,0,313,314,
        5,12,0,0,314,315,5,3,0,0,315,316,3,102,51,0,316,317,5,4,0,0,317,
        318,3,24,12,0,318,319,3,50,25,0,319,354,1,0,0,0,320,321,5,11,0,0,
        321,322,5,3,0,0,322,323,3,102,51,0,323,324,5,4,0,0,324,325,3,24,
        12,0,325,354,1,0,0,0,326,327,5,10,0,0,327,328,3,102,51,0,328,329,
        3,24,12,0,329,354,1,0,0,0,330,331,5,9,0,0,331,332,3,102,51,0,332,
        333,5,2,0,0,333,354,1,0,0,0,334,335,5,8,0,0,335,336,3,38,19,0,336,
        337,5,2,0,0,337,354,1,0,0,0,338,339,3,102,51,0,339,340,5,2,0,0,340,
        354,1,0,0,0,341,354,5,2,0,0,342,343,5,6,0,0,343,354,5,7,0,0,344,
        345,5,15,0,0,345,346,3,98,49,0,346,347,5,2,0,0,347,354,1,0,0,0,348,
        349,5,16,0,0,349,350,3,98,49,0,350,351,3,22,11,0,351,352,5,2,0,0,
        352,354,1,0,0,0,353,286,1,0,0,0,353,289,1,0,0,0,353,293,1,0,0,0,
        353,298,1,0,0,0,353,304,1,0,0,0,353,309,1,0,0,0,353,313,1,0,0,0,
        353,320,1,0,0,0,353,326,1,0,0,0,353,330,1,0,0,0,353,334,1,0,0,0,
        353,338,1,0,0,0,353,341,1,0,0,0,353,342,1,0,0,0,353,344,1,0,0,0,
        353,348,1,0,0,0,354,33,1,0,0,0,355,356,5,3,0,0,356,357,3,102,51,
        0,357,358,5,4,0,0,358,35,1,0,0,0,359,360,5,8,0,0,360,361,3,38,19,
        0,361,362,5,2,0,0,362,37,1,0,0,0,363,369,1,0,0,0,364,365,5,3,0,0,
        365,366,3,102,51,0,366,367,5,4,0,0,367,369,1,0,0,0,368,363,1,0,0,
        0,368,364,1,0,0,0,369,39,1,0,0,0,370,371,5,9,0,0,371,372,3,102,51,
        0,372,373,5,2,0,0,373,41,1,0,0,0,374,375,5,10,0,0,375,376,3,102,
        51,0,376,377,3,24,12,0,377,43,1,0,0,0,378,379,5,11,0,0,379,380,5,
        3,0,0,380,381,3,102,51,0,381,382,5,4,0,0,382,383,3,24,12,0,383,45,
        1,0,0,0,384,385,5,13,0,0,385,386,3,24,12,0,386,47,1,0,0,0,387,388,
        5,12,0,0,388,389,5,3,0,0,389,390,3,102,51,0,390,391,5,4,0,0,391,
        392,3,24,12,0,392,393,3,50,25,0,393,49,1,0,0,0,394,398,1,0,0,0,395,
        396,5,13,0,0,396,398,3,24,12,0,397,394,1,0,0,0,397,395,1,0,0,0,398,
        51,1,0,0,0,399,400,5,14,0,0,400,401,3,96,48,0,401,402,5,5,0,0,402,
        403,3,24,12,0,403,53,1,0,0,0,404,405,5,1,0,0,405,406,3,98,49,0,406,
        55,1,0,0,0,407,408,5,15,0,0,408,409,3,98,49,0,409,410,3,58,29,0,
        410,411,5,2,0,0,411,417,1,0,0,0,412,413,5,15,0,0,413,414,3,98,49,
        0,414,415,5,2,0,0,415,417,1,0,0,0,416,407,1,0,0,0,416,412,1,0,0,
        0,417,57,1,0,0,0,418,419,3,54,27,0,419,420,3,58,29,0,420,424,1,0,
        0,0,421,422,5,1,0,0,422,424,3,98,49,0,423,418,1,0,0,0,423,421,1,
        0,0,0,424,59,1,0,0,0,425,426,5,1,0,0,426,427,3,98,49,0,427,428,3,
        22,11,0,428,61,1,0,0,0,429,430,5,16,0,0,430,431,3,98,49,0,431,432,
        3,22,11,0,432,433,3,64,32,0,433,434,5,2,0,0,434,441,1,0,0,0,435,
        436,5,16,0,0,436,437,3,98,49,0,437,438,3,22,11,0,438,439,5,2,0,0,
        439,441,1,0,0,0,440,429,1,0,0,0,440,435,1,0,0,0,441,63,1,0,0,0,442,
        443,3,60,30,0,443,444,3,64,32,0,444,450,1,0,0,0,445,446,5,1,0,0,
        446,447,3,98,49,0,447,448,3,22,11,0,448,450,1,0,0,0,449,442,1,0,
        0,0,449,445,1,0,0,0,450,65,1,0,0,0,451,452,3,72,36,0,452,453,5,17,
        0,0,453,454,3,102,51,0,454,455,5,5,0,0,455,456,3,102,51,0,456,67,
        1,0,0,0,457,458,3,72,36,0,458,459,3,92,46,0,459,460,3,102,51,0,460,
        69,1,0,0,0,461,462,3,98,49,0,462,463,3,84,42,0,463,464,3,102,51,
        0,464,71,1,0,0,0,465,466,5,3,0,0,466,467,3,102,51,0,467,468,5,4,
        0,0,468,490,1,0,0,0,469,470,3,88,44,0,470,471,3,98,49,0,471,490,
        1,0,0,0,472,473,3,98,49,0,473,474,3,88,44,0,474,490,1,0,0,0,475,
        476,3,90,45,0,476,477,3,102,51,0,477,490,1,0,0,0,478,479,5,18,0,
        0,479,490,3,98,49,0,480,490,5,39,0,0,481,490,5,40,0,0,482,490,5,
        41,0,0,483,490,5,42,0,0,484,485,3,98,49,0,485,486,5,3,0,0,486,487,
        3,76,38,0,487,488,5,4,0,0,488,490,1,0,0,0,489,465,1,0,0,0,489,469,
        1,0,0,0,489,472,1,0,0,0,489,475,1,0,0,0,489,478,1,0,0,0,489,480,
        1,0,0,0,489,481,1,0,0,0,489,482,1,0,0,0,489,483,1,0,0,0,489,484,
        1,0,0,0,490,73,1,0,0,0,491,492,3,98,49,0,492,493,5,3,0,0,493,494,
        3,76,38,0,494,495,5,4,0,0,495,75,1,0,0,0,496,539,1,0,0,0,497,498,
        3,102,51,0,498,499,3,82,41,0,499,539,1,0,0,0,500,501,5,3,0,0,501,
        502,3,102,51,0,502,503,5,4,0,0,503,539,1,0,0,0,504,505,3,88,44,0,
        505,506,3,98,49,0,506,539,1,0,0,0,507,508,3,98,49,0,508,509,3,88,
        44,0,509,539,1,0,0,0,510,511,3,90,45,0,511,512,3,102,51,0,512,539,
        1,0,0,0,513,514,5,18,0,0,514,539,3,98,49,0,515,516,3,72,36,0,516,
        517,3,92,46,0,517,518,3,102,51,0,518,539,1,0,0,0,519,520,3,72,36,
        0,520,521,5,17,0,0,521,522,3,102,51,0,522,523,5,5,0,0,523,524,3,
        102,51,0,524,539,1,0,0,0,525,526,3,98,49,0,526,527,3,84,42,0,527,
        528,3,102,51,0,528,539,1,0,0,0,529,539,5,39,0,0,530,539,5,40,0,0,
        531,539,5,41,0,0,532,539,5,42,0,0,533,534,3,98,49,0,534,535,5,3,
        0,0,535,536,3,76,38,0,536,537,5,4,0,0,537,539,1,0,0,0,538,496,1,
        0,0,0,538,497,1,0,0,0,538,500,1,0,0,0,538,504,1,0,0,0,538,507,1,
        0,0,0,538,510,1,0,0,0,538,513,1,0,0,0,538,515,1,0,0,0,538,519,1,
        0,0,0,538,525,1,0,0,0,538,529,1,0,0,0,538,530,1,0,0,0,538,531,1,
        0,0,0,538,532,1,0,0,0,538,533,1,0,0,0,539,77,1,0,0,0,540,541,5,1,
        0,0,541,542,3,102,51,0,542,79,1,0,0,0,543,544,3,102,51,0,544,545,
        3,82,41,0,545,585,1,0,0,0,546,547,5,3,0,0,547,548,3,102,51,0,548,
        549,5,4,0,0,549,585,1,0,0,0,550,551,3,88,44,0,551,552,3,98,49,0,
        552,585,1,0,0,0,553,554,3,98,49,0,554,555,3,88,44,0,555,585,1,0,
        0,0,556,557,3,90,45,0,557,558,3,102,51,0,558,585,1,0,0,0,559,560,
        5,18,0,0,560,585,3,98,49,0,561,562,3,72,36,0,562,563,3,92,46,0,563,
        564,3,102,51,0,564,585,1,0,0,0,565,566,3,72,36,0,566,567,5,17,0,
        0,567,568,3,102,51,0,568,569,5,5,0,0,569,570,3,102,51,0,570,585,
        1,0,0,0,571,572,3,98,49,0,572,573,3,84,42,0,573,574,3,102,51,0,574,
        585,1,0,0,0,575,585,5,39,0,0,576,585,5,40,0,0,577,585,5,41,0,0,578,
        585,5,42,0,0,579,580,3,98,49,0,580,581,5,3,0,0,581,582,3,76,38,0,
        582,583,5,4,0,0,583,585,1,0,0,0,584,543,1,0,0,0,584,546,1,0,0,0,
        584,550,1,0,0,0,584,553,1,0,0,0,584,556,1,0,0,0,584,559,1,0,0,0,
        584,561,1,0,0,0,584,565,1,0,0,0,584,571,1,0,0,0,584,575,1,0,0,0,
        584,576,1,0,0,0,584,577,1,0,0,0,584,578,1,0,0,0,584,579,1,0,0,0,
        585,81,1,0,0,0,586,587,3,78,39,0,587,588,3,82,41,0,588,592,1,0,0,
        0,589,590,5,1,0,0,590,592,3,102,51,0,591,586,1,0,0,0,591,589,1,0,
        0,0,592,83,1,0,0,0,593,594,5,19,0,0,594,595,3,86,43,0,595,85,1,0,
        0,0,596,613,1,0,0,0,597,613,5,24,0,0,598,613,5,18,0,0,599,613,5,
        25,0,0,600,613,5,26,0,0,601,613,5,27,0,0,602,613,5,28,0,0,603,613,
        5,29,0,0,604,613,5,30,0,0,605,613,5,31,0,0,606,613,5,32,0,0,607,
        613,5,22,0,0,608,613,5,33,0,0,609,613,5,34,0,0,610,613,5,35,0,0,
        611,613,5,36,0,0,612,596,1,0,0,0,612,597,1,0,0,0,612,598,1,0,0,0,
        612,599,1,0,0,0,612,600,1,0,0,0,612,601,1,0,0,0,612,602,1,0,0,0,
        612,603,1,0,0,0,612,604,1,0,0,0,612,605,1,0,0,0,612,606,1,0,0,0,
        612,607,1,0,0,0,612,608,1,0,0,0,612,609,1,0,0,0,612,610,1,0,0,0,
        612,611,1,0,0,0,613,87,1,0,0,0,614,615,7,0,0,0,615,89,1,0,0,0,616,
        617,7,1,0,0,617,91,1,0,0,0,618,619,7,2,0,0,619,93,1,0,0,0,620,621,
        5,35,0,0,621,629,3,102,51,0,622,623,3,102,51,0,623,624,5,37,0,0,
        624,625,3,102,51,0,625,626,5,38,0,0,626,629,1,0,0,0,627,629,5,39,
        0,0,628,620,1,0,0,0,628,622,1,0,0,0,628,627,1,0,0,0,629,95,1,0,0,
        0,630,631,7,3,0,0,631,97,1,0,0,0,632,633,5,39,0,0,633,99,1,0,0,0,
        634,635,7,4,0,0,635,101,1,0,0,0,636,637,5,3,0,0,637,638,3,102,51,
        0,638,639,5,4,0,0,639,675,1,0,0,0,640,641,3,88,44,0,641,642,3,98,
        49,0,642,675,1,0,0,0,643,644,3,98,49,0,644,645,3,88,44,0,645,675,
        1,0,0,0,646,647,3,90,45,0,647,648,3,102,51,0,648,675,1,0,0,0,649,
        650,5,18,0,0,650,675,3,98,49,0,651,652,3,72,36,0,652,653,3,92,46,
        0,653,654,3,102,51,0,654,675,1,0,0,0,655,656,3,72,36,0,656,657,5,
        17,0,0,657,658,3,102,51,0,658,659,5,5,0,0,659,660,3,102,51,0,660,
        675,1,0,0,0,661,662,3,98,49,0,662,663,3,84,42,0,663,664,3,102,51,
        0,664,675,1,0,0,0,665,675,5,39,0,0,666,675,5,40,0,0,667,675,5,41,
        0,0,668,675,5,42,0,0,669,670,3,98,49,0,670,671,5,3,0,0,671,672,3,
        76,38,0,672,673,5,4,0,0,673,675,1,0,0,0,674,636,1,0,0,0,674,640,
        1,0,0,0,674,643,1,0,0,0,674,646,1,0,0,0,674,649,1,0,0,0,674,651,
        1,0,0,0,674,655,1,0,0,0,674,661,1,0,0,0,674,665,1,0,0,0,674,666,
        1,0,0,0,674,667,1,0,0,0,674,668,1,0,0,0,674,669,1,0,0,0,675,103,
        1,0,0,0,26,108,128,140,147,156,163,180,187,199,205,271,284,353,368,
        397,416,423,440,449,489,538,584,591,612,628,674
    ]

class bParser ( Parser ):

    grammarFileName = "bParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "';'", "'('", "')'", "':'", "'{'", 
                     "'}'", "'return'", "'goto'", "'switch'", "'while'", 
                     "'if'", "'else'", "'case'", "'extrn'", "'auto'", "'?'", 
                     "'&'", "'='", "'++'", "'--'", "'-'", "'!'", "'|'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'<<'", 
                     "'>>'", "'+'", "'%'", "'*'", "'/'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "TERM_0", "TERM_1", "TERM_2", "TERM_3", 
                      "TERM_4", "TERM_5", "TERM_6", "TERM_7", "TERM_8", 
                      "TERM_9", "TERM_10", "TERM_11", "TERM_12", "TERM_13", 
                      "TERM_14", "TERM_15", "TERM_16", "TERM_17", "TERM_18", 
                      "TERM_19", "TERM_20", "TERM_21", "TERM_22", "TERM_23", 
                      "TERM_24", "TERM_25", "TERM_26", "TERM_27", "TERM_28", 
                      "TERM_29", "TERM_30", "TERM_31", "TERM_32", "TERM_33", 
                      "TERM_34", "TERM_35", "TERM_36", "TERM_37", "NAME", 
                      "INT", "STRING1", "STRING2", "BLOCKCOMMENT", "WS" ]

    RULE_program = 0
    RULE_definition_star = 1
    RULE_block_9 = 2
    RULE_block_0 = 3
    RULE_block_9_star = 4
    RULE_block_10 = 5
    RULE_block_2 = 6
    RULE_block_10_star = 7
    RULE_definition = 8
    RULE_block_2_question = 9
    RULE_block_0_star = 10
    RULE_constant_question = 11
    RULE_statement = 12
    RULE_nullstmt = 13
    RULE_expressionstmt = 14
    RULE_blockstmt = 15
    RULE_statement_star = 16
    RULE_block_4 = 17
    RULE_returnstmt = 18
    RULE_block_4_question = 19
    RULE_gotostmt = 20
    RULE_switchstmt = 21
    RULE_whilestmt = 22
    RULE_block_5 = 23
    RULE_ifstmt = 24
    RULE_block_5_question = 25
    RULE_casestmt = 26
    RULE_block_6 = 27
    RULE_externsmt = 28
    RULE_block_6_star = 29
    RULE_block_7 = 30
    RULE_autosmt = 31
    RULE_block_7_star = 32
    RULE_ternary = 33
    RULE_comparison = 34
    RULE_assignment = 35
    RULE_expression = 36
    RULE_functioninvocation = 37
    RULE_functionparameters_question = 38
    RULE_block_8 = 39
    RULE_functionparameters = 40
    RULE_block_8_star = 41
    RULE_assign = 42
    RULE_binary_question = 43
    RULE_incdec = 44
    RULE_unary = 45
    RULE_binary = 46
    RULE_lvalue = 47
    RULE_constant = 48
    RULE_name = 49
    RULE_ival = 50
    RULE_rvalue = 51

    ruleNames =  [ "program", "definition_star", "block_9", "block_0", "block_9_star", 
                   "block_10", "block_2", "block_10_star", "definition", 
                   "block_2_question", "block_0_star", "constant_question", 
                   "statement", "nullstmt", "expressionstmt", "blockstmt", 
                   "statement_star", "block_4", "returnstmt", "block_4_question", 
                   "gotostmt", "switchstmt", "whilestmt", "block_5", "ifstmt", 
                   "block_5_question", "casestmt", "block_6", "externsmt", 
                   "block_6_star", "block_7", "autosmt", "block_7_star", 
                   "ternary", "comparison", "assignment", "expression", 
                   "functioninvocation", "functionparameters_question", 
                   "block_8", "functionparameters", "block_8_star", "assign", 
                   "binary_question", "incdec", "unary", "binary", "lvalue", 
                   "constant", "name", "ival", "rvalue" ]

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
    TERM_24=25
    TERM_25=26
    TERM_26=27
    TERM_27=28
    TERM_28=29
    TERM_29=30
    TERM_30=31
    TERM_31=32
    TERM_32=33
    TERM_33=34
    TERM_34=35
    TERM_35=36
    TERM_36=37
    TERM_37=38
    NAME=39
    INT=40
    STRING1=41
    STRING2=42
    BLOCKCOMMENT=43
    WS=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definition_star(self):
            return self.getTypedRuleContext(bParser.Definition_starContext,0)


        def EOF(self):
            return self.getToken(bParser.EOF, 0)

        def getRuleIndex(self):
            return bParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = bParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.definition_star()
                self.state = 105
                self.match(bParser.EOF)
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(bParser.EOF)
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


    class Definition_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definition(self):
            return self.getTypedRuleContext(bParser.DefinitionContext,0)


        def definition_star(self):
            return self.getTypedRuleContext(bParser.Definition_starContext,0)


        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def constant_question(self):
            return self.getTypedRuleContext(bParser.Constant_questionContext,0)


        def block_0_star(self):
            return self.getTypedRuleContext(bParser.Block_0_starContext,0)


        def TERM_1(self):
            return self.getToken(bParser.TERM_1, 0)

        def TERM_2(self):
            return self.getToken(bParser.TERM_2, 0)

        def block_2_question(self):
            return self.getTypedRuleContext(bParser.Block_2_questionContext,0)


        def TERM_3(self):
            return self.getToken(bParser.TERM_3, 0)

        def statement(self):
            return self.getTypedRuleContext(bParser.StatementContext,0)


        def getRuleIndex(self):
            return bParser.RULE_definition_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition_star" ):
                listener.enterDefinition_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition_star" ):
                listener.exitDefinition_star(self)




    def definition_star(self):

        localctx = bParser.Definition_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_definition_star)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.definition()
                self.state = 111
                self.definition_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.name()
                self.state = 114
                self.constant_question()
                self.state = 115
                self.block_0_star()
                self.state = 116
                self.match(bParser.TERM_1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.name()
                self.state = 119
                self.match(bParser.TERM_2)
                self.state = 120
                self.block_2_question()
                self.state = 121
                self.match(bParser.TERM_3)
                self.state = 122
                self.statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 124
                self.name()
                self.state = 125
                self.constant_question()
                self.state = 126
                self.match(bParser.TERM_1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_0(self):
            return self.getToken(bParser.TERM_0, 0)

        def ival(self):
            return self.getTypedRuleContext(bParser.IvalContext,0)


        def getRuleIndex(self):
            return bParser.RULE_block_9

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_9" ):
                listener.enterBlock_9(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_9" ):
                listener.exitBlock_9(self)




    def block_9(self):

        localctx = bParser.Block_9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block_9)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(bParser.TERM_0)
            self.state = 131
            self.ival()
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

        def ival(self):
            return self.getTypedRuleContext(bParser.IvalContext,0)


        def block_9_star(self):
            return self.getTypedRuleContext(bParser.Block_9_starContext,0)


        def INT(self):
            return self.getToken(bParser.INT, 0)

        def STRING1(self):
            return self.getToken(bParser.STRING1, 0)

        def STRING2(self):
            return self.getToken(bParser.STRING2, 0)

        def NAME(self):
            return self.getToken(bParser.NAME, 0)

        def getRuleIndex(self):
            return bParser.RULE_block_0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_0" ):
                listener.enterBlock_0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_0" ):
                listener.exitBlock_0(self)




    def block_0(self):

        localctx = bParser.Block_0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block_0)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.ival()
                self.state = 134
                self.block_9_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(bParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.match(bParser.STRING1)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.match(bParser.STRING2)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 139
                self.match(bParser.NAME)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_9_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_9(self):
            return self.getTypedRuleContext(bParser.Block_9Context,0)


        def block_9_star(self):
            return self.getTypedRuleContext(bParser.Block_9_starContext,0)


        def TERM_0(self):
            return self.getToken(bParser.TERM_0, 0)

        def ival(self):
            return self.getTypedRuleContext(bParser.IvalContext,0)


        def getRuleIndex(self):
            return bParser.RULE_block_9_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_9_star" ):
                listener.enterBlock_9_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_9_star" ):
                listener.exitBlock_9_star(self)




    def block_9_star(self):

        localctx = bParser.Block_9_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block_9_star)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.block_9()
                self.state = 143
                self.block_9_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(bParser.TERM_0)
                self.state = 146
                self.ival()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_0(self):
            return self.getToken(bParser.TERM_0, 0)

        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def getRuleIndex(self):
            return bParser.RULE_block_10

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_10" ):
                listener.enterBlock_10(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_10" ):
                listener.exitBlock_10(self)




    def block_10(self):

        localctx = bParser.Block_10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block_10)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(bParser.TERM_0)
            self.state = 150
            self.name()
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

        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def block_10_star(self):
            return self.getTypedRuleContext(bParser.Block_10_starContext,0)


        def NAME(self):
            return self.getToken(bParser.NAME, 0)

        def getRuleIndex(self):
            return bParser.RULE_block_2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_2" ):
                listener.enterBlock_2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_2" ):
                listener.exitBlock_2(self)




    def block_2(self):

        localctx = bParser.Block_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block_2)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.name()
                self.state = 153
                self.block_10_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(bParser.NAME)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_10_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_10(self):
            return self.getTypedRuleContext(bParser.Block_10Context,0)


        def block_10_star(self):
            return self.getTypedRuleContext(bParser.Block_10_starContext,0)


        def TERM_0(self):
            return self.getToken(bParser.TERM_0, 0)

        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def getRuleIndex(self):
            return bParser.RULE_block_10_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_10_star" ):
                listener.enterBlock_10_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_10_star" ):
                listener.exitBlock_10_star(self)




    def block_10_star(self):

        localctx = bParser.Block_10_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block_10_star)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.block_10()
                self.state = 159
                self.block_10_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(bParser.TERM_0)
                self.state = 162
                self.name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def constant_question(self):
            return self.getTypedRuleContext(bParser.Constant_questionContext,0)


        def block_0_star(self):
            return self.getTypedRuleContext(bParser.Block_0_starContext,0)


        def TERM_1(self):
            return self.getToken(bParser.TERM_1, 0)

        def TERM_2(self):
            return self.getToken(bParser.TERM_2, 0)

        def block_2_question(self):
            return self.getTypedRuleContext(bParser.Block_2_questionContext,0)


        def TERM_3(self):
            return self.getToken(bParser.TERM_3, 0)

        def statement(self):
            return self.getTypedRuleContext(bParser.StatementContext,0)


        def getRuleIndex(self):
            return bParser.RULE_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)




    def definition(self):

        localctx = bParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_definition)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.name()
                self.state = 166
                self.constant_question()
                self.state = 167
                self.block_0_star()
                self.state = 168
                self.match(bParser.TERM_1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.name()
                self.state = 171
                self.match(bParser.TERM_2)
                self.state = 172
                self.block_2_question()
                self.state = 173
                self.match(bParser.TERM_3)
                self.state = 174
                self.statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.name()
                self.state = 177
                self.constant_question()
                self.state = 178
                self.match(bParser.TERM_1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_2_questionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def block_10_star(self):
            return self.getTypedRuleContext(bParser.Block_10_starContext,0)


        def NAME(self):
            return self.getToken(bParser.NAME, 0)

        def getRuleIndex(self):
            return bParser.RULE_block_2_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_2_question" ):
                listener.enterBlock_2_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_2_question" ):
                listener.exitBlock_2_question(self)




    def block_2_question(self):

        localctx = bParser.Block_2_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block_2_question)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.name()
                self.state = 184
                self.block_10_star()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
                self.match(bParser.NAME)
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
            return self.getTypedRuleContext(bParser.Block_0Context,0)


        def block_0_star(self):
            return self.getTypedRuleContext(bParser.Block_0_starContext,0)


        def ival(self):
            return self.getTypedRuleContext(bParser.IvalContext,0)


        def block_9_star(self):
            return self.getTypedRuleContext(bParser.Block_9_starContext,0)


        def INT(self):
            return self.getToken(bParser.INT, 0)

        def STRING1(self):
            return self.getToken(bParser.STRING1, 0)

        def STRING2(self):
            return self.getToken(bParser.STRING2, 0)

        def NAME(self):
            return self.getToken(bParser.NAME, 0)

        def getRuleIndex(self):
            return bParser.RULE_block_0_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_0_star" ):
                listener.enterBlock_0_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_0_star" ):
                listener.exitBlock_0_star(self)




    def block_0_star(self):

        localctx = bParser.Block_0_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_block_0_star)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.block_0()
                self.state = 190
                self.block_0_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.ival()
                self.state = 193
                self.block_9_star()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.match(bParser.INT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.match(bParser.STRING1)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 197
                self.match(bParser.STRING2)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 198
                self.match(bParser.NAME)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_questionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(bParser.INT, 0)

        def STRING1(self):
            return self.getToken(bParser.STRING1, 0)

        def STRING2(self):
            return self.getToken(bParser.STRING2, 0)

        def getRuleIndex(self):
            return bParser.RULE_constant_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant_question" ):
                listener.enterConstant_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant_question" ):
                listener.exitConstant_question(self)




    def constant_question(self):

        localctx = bParser.Constant_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_constant_question)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.match(bParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.match(bParser.STRING1)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.match(bParser.STRING2)
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

        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def TERM_4(self):
            return self.getToken(bParser.TERM_4, 0)

        def statement(self):
            return self.getTypedRuleContext(bParser.StatementContext,0)


        def TERM_14(self):
            return self.getToken(bParser.TERM_14, 0)

        def block_6_star(self):
            return self.getTypedRuleContext(bParser.Block_6_starContext,0)


        def TERM_1(self):
            return self.getToken(bParser.TERM_1, 0)

        def TERM_15(self):
            return self.getToken(bParser.TERM_15, 0)

        def constant_question(self):
            return self.getTypedRuleContext(bParser.Constant_questionContext,0)


        def block_7_star(self):
            return self.getTypedRuleContext(bParser.Block_7_starContext,0)


        def TERM_13(self):
            return self.getToken(bParser.TERM_13, 0)

        def constant(self):
            return self.getTypedRuleContext(bParser.ConstantContext,0)


        def TERM_5(self):
            return self.getToken(bParser.TERM_5, 0)

        def statement_star(self):
            return self.getTypedRuleContext(bParser.Statement_starContext,0)


        def TERM_6(self):
            return self.getToken(bParser.TERM_6, 0)

        def TERM_11(self):
            return self.getToken(bParser.TERM_11, 0)

        def TERM_2(self):
            return self.getToken(bParser.TERM_2, 0)

        def rvalue(self):
            return self.getTypedRuleContext(bParser.RvalueContext,0)


        def TERM_3(self):
            return self.getToken(bParser.TERM_3, 0)

        def block_5_question(self):
            return self.getTypedRuleContext(bParser.Block_5_questionContext,0)


        def TERM_10(self):
            return self.getToken(bParser.TERM_10, 0)

        def TERM_9(self):
            return self.getToken(bParser.TERM_9, 0)

        def TERM_8(self):
            return self.getToken(bParser.TERM_8, 0)

        def TERM_7(self):
            return self.getToken(bParser.TERM_7, 0)

        def block_4_question(self):
            return self.getTypedRuleContext(bParser.Block_4_questionContext,0)


        def getRuleIndex(self):
            return bParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = bParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statement)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.name()
                self.state = 208
                self.match(bParser.TERM_4)
                self.state = 209
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(bParser.TERM_14)
                self.state = 212
                self.name()
                self.state = 213
                self.block_6_star()
                self.state = 214
                self.match(bParser.TERM_1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.match(bParser.TERM_15)
                self.state = 217
                self.name()
                self.state = 218
                self.constant_question()
                self.state = 219
                self.block_7_star()
                self.state = 220
                self.match(bParser.TERM_1)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                self.match(bParser.TERM_13)
                self.state = 223
                self.constant()
                self.state = 224
                self.match(bParser.TERM_4)
                self.state = 225
                self.statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 227
                self.match(bParser.TERM_5)
                self.state = 228
                self.statement_star()
                self.state = 229
                self.match(bParser.TERM_6)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 231
                self.match(bParser.TERM_11)
                self.state = 232
                self.match(bParser.TERM_2)
                self.state = 233
                self.rvalue()
                self.state = 234
                self.match(bParser.TERM_3)
                self.state = 235
                self.statement()
                self.state = 236
                self.block_5_question()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 238
                self.match(bParser.TERM_10)
                self.state = 239
                self.match(bParser.TERM_2)
                self.state = 240
                self.rvalue()
                self.state = 241
                self.match(bParser.TERM_3)
                self.state = 242
                self.statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 244
                self.match(bParser.TERM_9)
                self.state = 245
                self.rvalue()
                self.state = 246
                self.statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 248
                self.match(bParser.TERM_8)
                self.state = 249
                self.rvalue()
                self.state = 250
                self.match(bParser.TERM_1)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 252
                self.match(bParser.TERM_7)
                self.state = 253
                self.block_4_question()
                self.state = 254
                self.match(bParser.TERM_1)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 256
                self.rvalue()
                self.state = 257
                self.match(bParser.TERM_1)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 259
                self.match(bParser.TERM_1)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 260
                self.match(bParser.TERM_5)
                self.state = 261
                self.match(bParser.TERM_6)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 262
                self.match(bParser.TERM_14)
                self.state = 263
                self.name()
                self.state = 264
                self.match(bParser.TERM_1)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 266
                self.match(bParser.TERM_15)
                self.state = 267
                self.name()
                self.state = 268
                self.constant_question()
                self.state = 269
                self.match(bParser.TERM_1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_1(self):
            return self.getToken(bParser.TERM_1, 0)

        def getRuleIndex(self):
            return bParser.RULE_nullstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullstmt" ):
                listener.enterNullstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullstmt" ):
                listener.exitNullstmt(self)




    def nullstmt(self):

        localctx = bParser.NullstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_nullstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(bParser.TERM_1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvalue(self):
            return self.getTypedRuleContext(bParser.RvalueContext,0)


        def TERM_1(self):
            return self.getToken(bParser.TERM_1, 0)

        def getRuleIndex(self):
            return bParser.RULE_expressionstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionstmt" ):
                listener.enterExpressionstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionstmt" ):
                listener.exitExpressionstmt(self)




    def expressionstmt(self):

        localctx = bParser.ExpressionstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expressionstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.rvalue()
            self.state = 276
            self.match(bParser.TERM_1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_5(self):
            return self.getToken(bParser.TERM_5, 0)

        def statement_star(self):
            return self.getTypedRuleContext(bParser.Statement_starContext,0)


        def TERM_6(self):
            return self.getToken(bParser.TERM_6, 0)

        def getRuleIndex(self):
            return bParser.RULE_blockstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockstmt" ):
                listener.enterBlockstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockstmt" ):
                listener.exitBlockstmt(self)




    def blockstmt(self):

        localctx = bParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_blockstmt)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(bParser.TERM_5)
                self.state = 279
                self.statement_star()
                self.state = 280
                self.match(bParser.TERM_6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(bParser.TERM_5)
                self.state = 283
                self.match(bParser.TERM_6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(bParser.StatementContext,0)


        def statement_star(self):
            return self.getTypedRuleContext(bParser.Statement_starContext,0)


        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def TERM_4(self):
            return self.getToken(bParser.TERM_4, 0)

        def TERM_14(self):
            return self.getToken(bParser.TERM_14, 0)

        def block_6_star(self):
            return self.getTypedRuleContext(bParser.Block_6_starContext,0)


        def TERM_1(self):
            return self.getToken(bParser.TERM_1, 0)

        def TERM_15(self):
            return self.getToken(bParser.TERM_15, 0)

        def constant_question(self):
            return self.getTypedRuleContext(bParser.Constant_questionContext,0)


        def block_7_star(self):
            return self.getTypedRuleContext(bParser.Block_7_starContext,0)


        def TERM_13(self):
            return self.getToken(bParser.TERM_13, 0)

        def constant(self):
            return self.getTypedRuleContext(bParser.ConstantContext,0)


        def TERM_5(self):
            return self.getToken(bParser.TERM_5, 0)

        def TERM_6(self):
            return self.getToken(bParser.TERM_6, 0)

        def TERM_11(self):
            return self.getToken(bParser.TERM_11, 0)

        def TERM_2(self):
            return self.getToken(bParser.TERM_2, 0)

        def rvalue(self):
            return self.getTypedRuleContext(bParser.RvalueContext,0)


        def TERM_3(self):
            return self.getToken(bParser.TERM_3, 0)

        def block_5_question(self):
            return self.getTypedRuleContext(bParser.Block_5_questionContext,0)


        def TERM_10(self):
            return self.getToken(bParser.TERM_10, 0)

        def TERM_9(self):
            return self.getToken(bParser.TERM_9, 0)

        def TERM_8(self):
            return self.getToken(bParser.TERM_8, 0)

        def TERM_7(self):
            return self.getToken(bParser.TERM_7, 0)

        def block_4_question(self):
            return self.getTypedRuleContext(bParser.Block_4_questionContext,0)


        def getRuleIndex(self):
            return bParser.RULE_statement_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_star" ):
                listener.enterStatement_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_star" ):
                listener.exitStatement_star(self)




    def statement_star(self):

        localctx = bParser.Statement_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_statement_star)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.statement()
                self.state = 287
                self.statement_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.name()
                self.state = 290
                self.match(bParser.TERM_4)
                self.state = 291
                self.statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 293
                self.match(bParser.TERM_14)
                self.state = 294
                self.name()
                self.state = 295
                self.block_6_star()
                self.state = 296
                self.match(bParser.TERM_1)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 298
                self.match(bParser.TERM_15)
                self.state = 299
                self.name()
                self.state = 300
                self.constant_question()
                self.state = 301
                self.block_7_star()
                self.state = 302
                self.match(bParser.TERM_1)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 304
                self.match(bParser.TERM_13)
                self.state = 305
                self.constant()
                self.state = 306
                self.match(bParser.TERM_4)
                self.state = 307
                self.statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 309
                self.match(bParser.TERM_5)
                self.state = 310
                self.statement_star()
                self.state = 311
                self.match(bParser.TERM_6)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 313
                self.match(bParser.TERM_11)
                self.state = 314
                self.match(bParser.TERM_2)
                self.state = 315
                self.rvalue()
                self.state = 316
                self.match(bParser.TERM_3)
                self.state = 317
                self.statement()
                self.state = 318
                self.block_5_question()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 320
                self.match(bParser.TERM_10)
                self.state = 321
                self.match(bParser.TERM_2)
                self.state = 322
                self.rvalue()
                self.state = 323
                self.match(bParser.TERM_3)
                self.state = 324
                self.statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 326
                self.match(bParser.TERM_9)
                self.state = 327
                self.rvalue()
                self.state = 328
                self.statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 330
                self.match(bParser.TERM_8)
                self.state = 331
                self.rvalue()
                self.state = 332
                self.match(bParser.TERM_1)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 334
                self.match(bParser.TERM_7)
                self.state = 335
                self.block_4_question()
                self.state = 336
                self.match(bParser.TERM_1)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 338
                self.rvalue()
                self.state = 339
                self.match(bParser.TERM_1)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 341
                self.match(bParser.TERM_1)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 342
                self.match(bParser.TERM_5)
                self.state = 343
                self.match(bParser.TERM_6)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 344
                self.match(bParser.TERM_14)
                self.state = 345
                self.name()
                self.state = 346
                self.match(bParser.TERM_1)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 348
                self.match(bParser.TERM_15)
                self.state = 349
                self.name()
                self.state = 350
                self.constant_question()
                self.state = 351
                self.match(bParser.TERM_1)
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

        def TERM_2(self):
            return self.getToken(bParser.TERM_2, 0)

        def rvalue(self):
            return self.getTypedRuleContext(bParser.RvalueContext,0)


        def TERM_3(self):
            return self.getToken(bParser.TERM_3, 0)

        def getRuleIndex(self):
            return bParser.RULE_block_4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_4" ):
                listener.enterBlock_4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_4" ):
                listener.exitBlock_4(self)




    def block_4(self):

        localctx = bParser.Block_4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block_4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(bParser.TERM_2)
            self.state = 356
            self.rvalue()
            self.state = 357
            self.match(bParser.TERM_3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_7(self):
            return self.getToken(bParser.TERM_7, 0)

        def block_4_question(self):
            return self.getTypedRuleContext(bParser.Block_4_questionContext,0)


        def TERM_1(self):
            return self.getToken(bParser.TERM_1, 0)

        def getRuleIndex(self):
            return bParser.RULE_returnstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnstmt" ):
                listener.enterReturnstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnstmt" ):
                listener.exitReturnstmt(self)




    def returnstmt(self):

        localctx = bParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(bParser.TERM_7)
            self.state = 360
            self.block_4_question()
            self.state = 361
            self.match(bParser.TERM_1)
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

        def TERM_2(self):
            return self.getToken(bParser.TERM_2, 0)

        def rvalue(self):
            return self.getTypedRuleContext(bParser.RvalueContext,0)


        def TERM_3(self):
            return self.getToken(bParser.TERM_3, 0)

        def getRuleIndex(self):
            return bParser.RULE_block_4_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_4_question" ):
                listener.enterBlock_4_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_4_question" ):
                listener.exitBlock_4_question(self)




    def block_4_question(self):

        localctx = bParser.Block_4_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_block_4_question)
        try:
            self.state = 368
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.match(bParser.TERM_2)
                self.state = 365
                self.rvalue()
                self.state = 366
                self.match(bParser.TERM_3)
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


    class GotostmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_8(self):
            return self.getToken(bParser.TERM_8, 0)

        def rvalue(self):
            return self.getTypedRuleContext(bParser.RvalueContext,0)


        def TERM_1(self):
            return self.getToken(bParser.TERM_1, 0)

        def getRuleIndex(self):
            return bParser.RULE_gotostmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotostmt" ):
                listener.enterGotostmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotostmt" ):
                listener.exitGotostmt(self)




    def gotostmt(self):

        localctx = bParser.GotostmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_gotostmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(bParser.TERM_8)
            self.state = 371
            self.rvalue()
            self.state = 372
            self.match(bParser.TERM_1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_9(self):
            return self.getToken(bParser.TERM_9, 0)

        def rvalue(self):
            return self.getTypedRuleContext(bParser.RvalueContext,0)


        def statement(self):
            return self.getTypedRuleContext(bParser.StatementContext,0)


        def getRuleIndex(self):
            return bParser.RULE_switchstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchstmt" ):
                listener.enterSwitchstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchstmt" ):
                listener.exitSwitchstmt(self)




    def switchstmt(self):

        localctx = bParser.SwitchstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_switchstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(bParser.TERM_9)
            self.state = 375
            self.rvalue()
            self.state = 376
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_10(self):
            return self.getToken(bParser.TERM_10, 0)

        def TERM_2(self):
            return self.getToken(bParser.TERM_2, 0)

        def rvalue(self):
            return self.getTypedRuleContext(bParser.RvalueContext,0)


        def TERM_3(self):
            return self.getToken(bParser.TERM_3, 0)

        def statement(self):
            return self.getTypedRuleContext(bParser.StatementContext,0)


        def getRuleIndex(self):
            return bParser.RULE_whilestmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhilestmt" ):
                listener.enterWhilestmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhilestmt" ):
                listener.exitWhilestmt(self)




    def whilestmt(self):

        localctx = bParser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(bParser.TERM_10)
            self.state = 379
            self.match(bParser.TERM_2)
            self.state = 380
            self.rvalue()
            self.state = 381
            self.match(bParser.TERM_3)
            self.state = 382
            self.statement()
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

        def TERM_12(self):
            return self.getToken(bParser.TERM_12, 0)

        def statement(self):
            return self.getTypedRuleContext(bParser.StatementContext,0)


        def getRuleIndex(self):
            return bParser.RULE_block_5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_5" ):
                listener.enterBlock_5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_5" ):
                listener.exitBlock_5(self)




    def block_5(self):

        localctx = bParser.Block_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_block_5)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(bParser.TERM_12)
            self.state = 385
            self.statement()
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

        def TERM_11(self):
            return self.getToken(bParser.TERM_11, 0)

        def TERM_2(self):
            return self.getToken(bParser.TERM_2, 0)

        def rvalue(self):
            return self.getTypedRuleContext(bParser.RvalueContext,0)


        def TERM_3(self):
            return self.getToken(bParser.TERM_3, 0)

        def statement(self):
            return self.getTypedRuleContext(bParser.StatementContext,0)


        def block_5_question(self):
            return self.getTypedRuleContext(bParser.Block_5_questionContext,0)


        def getRuleIndex(self):
            return bParser.RULE_ifstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstmt" ):
                listener.enterIfstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstmt" ):
                listener.exitIfstmt(self)




    def ifstmt(self):

        localctx = bParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(bParser.TERM_11)
            self.state = 388
            self.match(bParser.TERM_2)
            self.state = 389
            self.rvalue()
            self.state = 390
            self.match(bParser.TERM_3)
            self.state = 391
            self.statement()
            self.state = 392
            self.block_5_question()
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

        def TERM_12(self):
            return self.getToken(bParser.TERM_12, 0)

        def statement(self):
            return self.getTypedRuleContext(bParser.StatementContext,0)


        def getRuleIndex(self):
            return bParser.RULE_block_5_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_5_question" ):
                listener.enterBlock_5_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_5_question" ):
                listener.exitBlock_5_question(self)




    def block_5_question(self):

        localctx = bParser.Block_5_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_block_5_question)
        try:
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(bParser.TERM_12)
                self.state = 396
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_13(self):
            return self.getToken(bParser.TERM_13, 0)

        def constant(self):
            return self.getTypedRuleContext(bParser.ConstantContext,0)


        def TERM_4(self):
            return self.getToken(bParser.TERM_4, 0)

        def statement(self):
            return self.getTypedRuleContext(bParser.StatementContext,0)


        def getRuleIndex(self):
            return bParser.RULE_casestmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCasestmt" ):
                listener.enterCasestmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCasestmt" ):
                listener.exitCasestmt(self)




    def casestmt(self):

        localctx = bParser.CasestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_casestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(bParser.TERM_13)
            self.state = 400
            self.constant()
            self.state = 401
            self.match(bParser.TERM_4)
            self.state = 402
            self.statement()
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

        def TERM_0(self):
            return self.getToken(bParser.TERM_0, 0)

        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def getRuleIndex(self):
            return bParser.RULE_block_6

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_6" ):
                listener.enterBlock_6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_6" ):
                listener.exitBlock_6(self)




    def block_6(self):

        localctx = bParser.Block_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_block_6)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(bParser.TERM_0)
            self.state = 405
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExternsmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_14(self):
            return self.getToken(bParser.TERM_14, 0)

        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def block_6_star(self):
            return self.getTypedRuleContext(bParser.Block_6_starContext,0)


        def TERM_1(self):
            return self.getToken(bParser.TERM_1, 0)

        def getRuleIndex(self):
            return bParser.RULE_externsmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExternsmt" ):
                listener.enterExternsmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExternsmt" ):
                listener.exitExternsmt(self)




    def externsmt(self):

        localctx = bParser.ExternsmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_externsmt)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(bParser.TERM_14)
                self.state = 408
                self.name()
                self.state = 409
                self.block_6_star()
                self.state = 410
                self.match(bParser.TERM_1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.match(bParser.TERM_14)
                self.state = 413
                self.name()
                self.state = 414
                self.match(bParser.TERM_1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_6_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_6(self):
            return self.getTypedRuleContext(bParser.Block_6Context,0)


        def block_6_star(self):
            return self.getTypedRuleContext(bParser.Block_6_starContext,0)


        def TERM_0(self):
            return self.getToken(bParser.TERM_0, 0)

        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def getRuleIndex(self):
            return bParser.RULE_block_6_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_6_star" ):
                listener.enterBlock_6_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_6_star" ):
                listener.exitBlock_6_star(self)




    def block_6_star(self):

        localctx = bParser.Block_6_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_block_6_star)
        try:
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.block_6()
                self.state = 419
                self.block_6_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.match(bParser.TERM_0)
                self.state = 422
                self.name()
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

        def TERM_0(self):
            return self.getToken(bParser.TERM_0, 0)

        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def constant_question(self):
            return self.getTypedRuleContext(bParser.Constant_questionContext,0)


        def getRuleIndex(self):
            return bParser.RULE_block_7

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_7" ):
                listener.enterBlock_7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_7" ):
                listener.exitBlock_7(self)




    def block_7(self):

        localctx = bParser.Block_7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_block_7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(bParser.TERM_0)
            self.state = 426
            self.name()
            self.state = 427
            self.constant_question()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AutosmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_15(self):
            return self.getToken(bParser.TERM_15, 0)

        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def constant_question(self):
            return self.getTypedRuleContext(bParser.Constant_questionContext,0)


        def block_7_star(self):
            return self.getTypedRuleContext(bParser.Block_7_starContext,0)


        def TERM_1(self):
            return self.getToken(bParser.TERM_1, 0)

        def getRuleIndex(self):
            return bParser.RULE_autosmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAutosmt" ):
                listener.enterAutosmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAutosmt" ):
                listener.exitAutosmt(self)




    def autosmt(self):

        localctx = bParser.AutosmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_autosmt)
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(bParser.TERM_15)
                self.state = 430
                self.name()
                self.state = 431
                self.constant_question()
                self.state = 432
                self.block_7_star()
                self.state = 433
                self.match(bParser.TERM_1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.match(bParser.TERM_15)
                self.state = 436
                self.name()
                self.state = 437
                self.constant_question()
                self.state = 438
                self.match(bParser.TERM_1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_7_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_7(self):
            return self.getTypedRuleContext(bParser.Block_7Context,0)


        def block_7_star(self):
            return self.getTypedRuleContext(bParser.Block_7_starContext,0)


        def TERM_0(self):
            return self.getToken(bParser.TERM_0, 0)

        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def constant_question(self):
            return self.getTypedRuleContext(bParser.Constant_questionContext,0)


        def getRuleIndex(self):
            return bParser.RULE_block_7_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_7_star" ):
                listener.enterBlock_7_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_7_star" ):
                listener.exitBlock_7_star(self)




    def block_7_star(self):

        localctx = bParser.Block_7_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_block_7_star)
        try:
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.block_7()
                self.state = 443
                self.block_7_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.match(bParser.TERM_0)
                self.state = 446
                self.name()
                self.state = 447
                self.constant_question()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TernaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(bParser.ExpressionContext,0)


        def TERM_16(self):
            return self.getToken(bParser.TERM_16, 0)

        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bParser.RvalueContext)
            else:
                return self.getTypedRuleContext(bParser.RvalueContext,i)


        def TERM_4(self):
            return self.getToken(bParser.TERM_4, 0)

        def getRuleIndex(self):
            return bParser.RULE_ternary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernary" ):
                listener.enterTernary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernary" ):
                listener.exitTernary(self)




    def ternary(self):

        localctx = bParser.TernaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ternary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.expression()
            self.state = 452
            self.match(bParser.TERM_16)
            self.state = 453
            self.rvalue()
            self.state = 454
            self.match(bParser.TERM_4)
            self.state = 455
            self.rvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(bParser.ExpressionContext,0)


        def binary(self):
            return self.getTypedRuleContext(bParser.BinaryContext,0)


        def rvalue(self):
            return self.getTypedRuleContext(bParser.RvalueContext,0)


        def getRuleIndex(self):
            return bParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = bParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.expression()
            self.state = 458
            self.binary()
            self.state = 459
            self.rvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def assign(self):
            return self.getTypedRuleContext(bParser.AssignContext,0)


        def rvalue(self):
            return self.getTypedRuleContext(bParser.RvalueContext,0)


        def getRuleIndex(self):
            return bParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = bParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.name()
            self.state = 462
            self.assign()
            self.state = 463
            self.rvalue()
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

        def TERM_2(self):
            return self.getToken(bParser.TERM_2, 0)

        def rvalue(self):
            return self.getTypedRuleContext(bParser.RvalueContext,0)


        def TERM_3(self):
            return self.getToken(bParser.TERM_3, 0)

        def incdec(self):
            return self.getTypedRuleContext(bParser.IncdecContext,0)


        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def unary(self):
            return self.getTypedRuleContext(bParser.UnaryContext,0)


        def TERM_17(self):
            return self.getToken(bParser.TERM_17, 0)

        def NAME(self):
            return self.getToken(bParser.NAME, 0)

        def INT(self):
            return self.getToken(bParser.INT, 0)

        def STRING1(self):
            return self.getToken(bParser.STRING1, 0)

        def STRING2(self):
            return self.getToken(bParser.STRING2, 0)

        def functionparameters_question(self):
            return self.getTypedRuleContext(bParser.Functionparameters_questionContext,0)


        def getRuleIndex(self):
            return bParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = bParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expression)
        try:
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.match(bParser.TERM_2)
                self.state = 466
                self.rvalue()
                self.state = 467
                self.match(bParser.TERM_3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 469
                self.incdec()
                self.state = 470
                self.name()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 472
                self.name()
                self.state = 473
                self.incdec()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 475
                self.unary()
                self.state = 476
                self.rvalue()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 478
                self.match(bParser.TERM_17)
                self.state = 479
                self.name()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 480
                self.match(bParser.NAME)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 481
                self.match(bParser.INT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 482
                self.match(bParser.STRING1)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 483
                self.match(bParser.STRING2)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 484
                self.name()
                self.state = 485
                self.match(bParser.TERM_2)
                self.state = 486
                self.functionparameters_question()
                self.state = 487
                self.match(bParser.TERM_3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioninvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def TERM_2(self):
            return self.getToken(bParser.TERM_2, 0)

        def functionparameters_question(self):
            return self.getTypedRuleContext(bParser.Functionparameters_questionContext,0)


        def TERM_3(self):
            return self.getToken(bParser.TERM_3, 0)

        def getRuleIndex(self):
            return bParser.RULE_functioninvocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioninvocation" ):
                listener.enterFunctioninvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioninvocation" ):
                listener.exitFunctioninvocation(self)




    def functioninvocation(self):

        localctx = bParser.FunctioninvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_functioninvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.name()
            self.state = 492
            self.match(bParser.TERM_2)
            self.state = 493
            self.functionparameters_question()
            self.state = 494
            self.match(bParser.TERM_3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Functionparameters_questionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bParser.RvalueContext)
            else:
                return self.getTypedRuleContext(bParser.RvalueContext,i)


        def block_8_star(self):
            return self.getTypedRuleContext(bParser.Block_8_starContext,0)


        def TERM_2(self):
            return self.getToken(bParser.TERM_2, 0)

        def TERM_3(self):
            return self.getToken(bParser.TERM_3, 0)

        def incdec(self):
            return self.getTypedRuleContext(bParser.IncdecContext,0)


        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def unary(self):
            return self.getTypedRuleContext(bParser.UnaryContext,0)


        def TERM_17(self):
            return self.getToken(bParser.TERM_17, 0)

        def expression(self):
            return self.getTypedRuleContext(bParser.ExpressionContext,0)


        def binary(self):
            return self.getTypedRuleContext(bParser.BinaryContext,0)


        def TERM_16(self):
            return self.getToken(bParser.TERM_16, 0)

        def TERM_4(self):
            return self.getToken(bParser.TERM_4, 0)

        def assign(self):
            return self.getTypedRuleContext(bParser.AssignContext,0)


        def NAME(self):
            return self.getToken(bParser.NAME, 0)

        def INT(self):
            return self.getToken(bParser.INT, 0)

        def STRING1(self):
            return self.getToken(bParser.STRING1, 0)

        def STRING2(self):
            return self.getToken(bParser.STRING2, 0)

        def functionparameters_question(self):
            return self.getTypedRuleContext(bParser.Functionparameters_questionContext,0)


        def getRuleIndex(self):
            return bParser.RULE_functionparameters_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionparameters_question" ):
                listener.enterFunctionparameters_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionparameters_question" ):
                listener.exitFunctionparameters_question(self)




    def functionparameters_question(self):

        localctx = bParser.Functionparameters_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_functionparameters_question)
        try:
            self.state = 538
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
                self.rvalue()
                self.state = 498
                self.block_8_star()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 500
                self.match(bParser.TERM_2)
                self.state = 501
                self.rvalue()
                self.state = 502
                self.match(bParser.TERM_3)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 504
                self.incdec()
                self.state = 505
                self.name()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 507
                self.name()
                self.state = 508
                self.incdec()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 510
                self.unary()
                self.state = 511
                self.rvalue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 513
                self.match(bParser.TERM_17)
                self.state = 514
                self.name()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 515
                self.expression()
                self.state = 516
                self.binary()
                self.state = 517
                self.rvalue()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 519
                self.expression()
                self.state = 520
                self.match(bParser.TERM_16)
                self.state = 521
                self.rvalue()
                self.state = 522
                self.match(bParser.TERM_4)
                self.state = 523
                self.rvalue()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 525
                self.name()
                self.state = 526
                self.assign()
                self.state = 527
                self.rvalue()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 529
                self.match(bParser.NAME)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 530
                self.match(bParser.INT)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 531
                self.match(bParser.STRING1)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 532
                self.match(bParser.STRING2)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 533
                self.name()
                self.state = 534
                self.match(bParser.TERM_2)
                self.state = 535
                self.functionparameters_question()
                self.state = 536
                self.match(bParser.TERM_3)
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

        def TERM_0(self):
            return self.getToken(bParser.TERM_0, 0)

        def rvalue(self):
            return self.getTypedRuleContext(bParser.RvalueContext,0)


        def getRuleIndex(self):
            return bParser.RULE_block_8

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_8" ):
                listener.enterBlock_8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_8" ):
                listener.exitBlock_8(self)




    def block_8(self):

        localctx = bParser.Block_8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_block_8)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(bParser.TERM_0)
            self.state = 541
            self.rvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionparametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bParser.RvalueContext)
            else:
                return self.getTypedRuleContext(bParser.RvalueContext,i)


        def block_8_star(self):
            return self.getTypedRuleContext(bParser.Block_8_starContext,0)


        def TERM_2(self):
            return self.getToken(bParser.TERM_2, 0)

        def TERM_3(self):
            return self.getToken(bParser.TERM_3, 0)

        def incdec(self):
            return self.getTypedRuleContext(bParser.IncdecContext,0)


        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def unary(self):
            return self.getTypedRuleContext(bParser.UnaryContext,0)


        def TERM_17(self):
            return self.getToken(bParser.TERM_17, 0)

        def expression(self):
            return self.getTypedRuleContext(bParser.ExpressionContext,0)


        def binary(self):
            return self.getTypedRuleContext(bParser.BinaryContext,0)


        def TERM_16(self):
            return self.getToken(bParser.TERM_16, 0)

        def TERM_4(self):
            return self.getToken(bParser.TERM_4, 0)

        def assign(self):
            return self.getTypedRuleContext(bParser.AssignContext,0)


        def NAME(self):
            return self.getToken(bParser.NAME, 0)

        def INT(self):
            return self.getToken(bParser.INT, 0)

        def STRING1(self):
            return self.getToken(bParser.STRING1, 0)

        def STRING2(self):
            return self.getToken(bParser.STRING2, 0)

        def functionparameters_question(self):
            return self.getTypedRuleContext(bParser.Functionparameters_questionContext,0)


        def getRuleIndex(self):
            return bParser.RULE_functionparameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionparameters" ):
                listener.enterFunctionparameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionparameters" ):
                listener.exitFunctionparameters(self)




    def functionparameters(self):

        localctx = bParser.FunctionparametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_functionparameters)
        try:
            self.state = 584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 543
                self.rvalue()
                self.state = 544
                self.block_8_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 546
                self.match(bParser.TERM_2)
                self.state = 547
                self.rvalue()
                self.state = 548
                self.match(bParser.TERM_3)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 550
                self.incdec()
                self.state = 551
                self.name()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 553
                self.name()
                self.state = 554
                self.incdec()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 556
                self.unary()
                self.state = 557
                self.rvalue()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 559
                self.match(bParser.TERM_17)
                self.state = 560
                self.name()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 561
                self.expression()
                self.state = 562
                self.binary()
                self.state = 563
                self.rvalue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 565
                self.expression()
                self.state = 566
                self.match(bParser.TERM_16)
                self.state = 567
                self.rvalue()
                self.state = 568
                self.match(bParser.TERM_4)
                self.state = 569
                self.rvalue()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 571
                self.name()
                self.state = 572
                self.assign()
                self.state = 573
                self.rvalue()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 575
                self.match(bParser.NAME)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 576
                self.match(bParser.INT)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 577
                self.match(bParser.STRING1)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 578
                self.match(bParser.STRING2)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 579
                self.name()
                self.state = 580
                self.match(bParser.TERM_2)
                self.state = 581
                self.functionparameters_question()
                self.state = 582
                self.match(bParser.TERM_3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_8_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_8(self):
            return self.getTypedRuleContext(bParser.Block_8Context,0)


        def block_8_star(self):
            return self.getTypedRuleContext(bParser.Block_8_starContext,0)


        def TERM_0(self):
            return self.getToken(bParser.TERM_0, 0)

        def rvalue(self):
            return self.getTypedRuleContext(bParser.RvalueContext,0)


        def getRuleIndex(self):
            return bParser.RULE_block_8_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_8_star" ):
                listener.enterBlock_8_star(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_8_star" ):
                listener.exitBlock_8_star(self)




    def block_8_star(self):

        localctx = bParser.Block_8_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_block_8_star)
        try:
            self.state = 591
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 586
                self.block_8()
                self.state = 587
                self.block_8_star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 589
                self.match(bParser.TERM_0)
                self.state = 590
                self.rvalue()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_18(self):
            return self.getToken(bParser.TERM_18, 0)

        def binary_question(self):
            return self.getTypedRuleContext(bParser.Binary_questionContext,0)


        def getRuleIndex(self):
            return bParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = bParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.match(bParser.TERM_18)
            self.state = 594
            self.binary_question()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Binary_questionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_23(self):
            return self.getToken(bParser.TERM_23, 0)

        def TERM_17(self):
            return self.getToken(bParser.TERM_17, 0)

        def TERM_24(self):
            return self.getToken(bParser.TERM_24, 0)

        def TERM_25(self):
            return self.getToken(bParser.TERM_25, 0)

        def TERM_26(self):
            return self.getToken(bParser.TERM_26, 0)

        def TERM_27(self):
            return self.getToken(bParser.TERM_27, 0)

        def TERM_28(self):
            return self.getToken(bParser.TERM_28, 0)

        def TERM_29(self):
            return self.getToken(bParser.TERM_29, 0)

        def TERM_30(self):
            return self.getToken(bParser.TERM_30, 0)

        def TERM_31(self):
            return self.getToken(bParser.TERM_31, 0)

        def TERM_21(self):
            return self.getToken(bParser.TERM_21, 0)

        def TERM_32(self):
            return self.getToken(bParser.TERM_32, 0)

        def TERM_33(self):
            return self.getToken(bParser.TERM_33, 0)

        def TERM_34(self):
            return self.getToken(bParser.TERM_34, 0)

        def TERM_35(self):
            return self.getToken(bParser.TERM_35, 0)

        def getRuleIndex(self):
            return bParser.RULE_binary_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_question" ):
                listener.enterBinary_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_question" ):
                listener.exitBinary_question(self)




    def binary_question(self):

        localctx = bParser.Binary_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_binary_question)
        try:
            self.state = 612
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 597
                self.match(bParser.TERM_23)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 598
                self.match(bParser.TERM_17)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 599
                self.match(bParser.TERM_24)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 600
                self.match(bParser.TERM_25)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 601
                self.match(bParser.TERM_26)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 602
                self.match(bParser.TERM_27)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 603
                self.match(bParser.TERM_28)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 604
                self.match(bParser.TERM_29)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 605
                self.match(bParser.TERM_30)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 606
                self.match(bParser.TERM_31)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 607
                self.match(bParser.TERM_21)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 608
                self.match(bParser.TERM_32)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 609
                self.match(bParser.TERM_33)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 610
                self.match(bParser.TERM_34)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 611
                self.match(bParser.TERM_35)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncdecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_19(self):
            return self.getToken(bParser.TERM_19, 0)

        def TERM_20(self):
            return self.getToken(bParser.TERM_20, 0)

        def getRuleIndex(self):
            return bParser.RULE_incdec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncdec" ):
                listener.enterIncdec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncdec" ):
                listener.exitIncdec(self)




    def incdec(self):

        localctx = bParser.IncdecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_incdec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
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


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_21(self):
            return self.getToken(bParser.TERM_21, 0)

        def TERM_22(self):
            return self.getToken(bParser.TERM_22, 0)

        def getRuleIndex(self):
            return bParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)




    def unary(self):

        localctx = bParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 616
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
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


    class BinaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_23(self):
            return self.getToken(bParser.TERM_23, 0)

        def TERM_17(self):
            return self.getToken(bParser.TERM_17, 0)

        def TERM_24(self):
            return self.getToken(bParser.TERM_24, 0)

        def TERM_25(self):
            return self.getToken(bParser.TERM_25, 0)

        def TERM_26(self):
            return self.getToken(bParser.TERM_26, 0)

        def TERM_27(self):
            return self.getToken(bParser.TERM_27, 0)

        def TERM_28(self):
            return self.getToken(bParser.TERM_28, 0)

        def TERM_29(self):
            return self.getToken(bParser.TERM_29, 0)

        def TERM_30(self):
            return self.getToken(bParser.TERM_30, 0)

        def TERM_31(self):
            return self.getToken(bParser.TERM_31, 0)

        def TERM_21(self):
            return self.getToken(bParser.TERM_21, 0)

        def TERM_32(self):
            return self.getToken(bParser.TERM_32, 0)

        def TERM_33(self):
            return self.getToken(bParser.TERM_33, 0)

        def TERM_34(self):
            return self.getToken(bParser.TERM_34, 0)

        def TERM_35(self):
            return self.getToken(bParser.TERM_35, 0)

        def getRuleIndex(self):
            return bParser.RULE_binary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary" ):
                listener.enterBinary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary" ):
                listener.exitBinary(self)




    def binary(self):

        localctx = bParser.BinaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_binary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 137426632704) != 0):
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


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_34(self):
            return self.getToken(bParser.TERM_34, 0)

        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bParser.RvalueContext)
            else:
                return self.getTypedRuleContext(bParser.RvalueContext,i)


        def TERM_36(self):
            return self.getToken(bParser.TERM_36, 0)

        def TERM_37(self):
            return self.getToken(bParser.TERM_37, 0)

        def NAME(self):
            return self.getToken(bParser.NAME, 0)

        def getRuleIndex(self):
            return bParser.RULE_lvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvalue" ):
                listener.enterLvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvalue" ):
                listener.exitLvalue(self)




    def lvalue(self):

        localctx = bParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_lvalue)
        try:
            self.state = 628
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 620
                self.match(bParser.TERM_34)
                self.state = 621
                self.rvalue()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 622
                self.rvalue()
                self.state = 623
                self.match(bParser.TERM_36)
                self.state = 624
                self.rvalue()
                self.state = 625
                self.match(bParser.TERM_37)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 627
                self.match(bParser.NAME)
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

        def INT(self):
            return self.getToken(bParser.INT, 0)

        def STRING1(self):
            return self.getToken(bParser.STRING1, 0)

        def STRING2(self):
            return self.getToken(bParser.STRING2, 0)

        def getRuleIndex(self):
            return bParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = bParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 630
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 7696581394432) != 0):
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


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(bParser.NAME, 0)

        def getRuleIndex(self):
            return bParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = bParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.match(bParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(bParser.INT, 0)

        def STRING1(self):
            return self.getToken(bParser.STRING1, 0)

        def STRING2(self):
            return self.getToken(bParser.STRING2, 0)

        def NAME(self):
            return self.getToken(bParser.NAME, 0)

        def getRuleIndex(self):
            return bParser.RULE_ival

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIval" ):
                listener.enterIval(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIval" ):
                listener.exitIval(self)




    def ival(self):

        localctx = bParser.IvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_ival)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 8246337208320) != 0):
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


    class RvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM_2(self):
            return self.getToken(bParser.TERM_2, 0)

        def rvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bParser.RvalueContext)
            else:
                return self.getTypedRuleContext(bParser.RvalueContext,i)


        def TERM_3(self):
            return self.getToken(bParser.TERM_3, 0)

        def incdec(self):
            return self.getTypedRuleContext(bParser.IncdecContext,0)


        def name(self):
            return self.getTypedRuleContext(bParser.NameContext,0)


        def unary(self):
            return self.getTypedRuleContext(bParser.UnaryContext,0)


        def TERM_17(self):
            return self.getToken(bParser.TERM_17, 0)

        def expression(self):
            return self.getTypedRuleContext(bParser.ExpressionContext,0)


        def binary(self):
            return self.getTypedRuleContext(bParser.BinaryContext,0)


        def TERM_16(self):
            return self.getToken(bParser.TERM_16, 0)

        def TERM_4(self):
            return self.getToken(bParser.TERM_4, 0)

        def assign(self):
            return self.getTypedRuleContext(bParser.AssignContext,0)


        def NAME(self):
            return self.getToken(bParser.NAME, 0)

        def INT(self):
            return self.getToken(bParser.INT, 0)

        def STRING1(self):
            return self.getToken(bParser.STRING1, 0)

        def STRING2(self):
            return self.getToken(bParser.STRING2, 0)

        def functionparameters_question(self):
            return self.getTypedRuleContext(bParser.Functionparameters_questionContext,0)


        def getRuleIndex(self):
            return bParser.RULE_rvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRvalue" ):
                listener.enterRvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRvalue" ):
                listener.exitRvalue(self)




    def rvalue(self):

        localctx = bParser.RvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_rvalue)
        try:
            self.state = 674
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 636
                self.match(bParser.TERM_2)
                self.state = 637
                self.rvalue()
                self.state = 638
                self.match(bParser.TERM_3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 640
                self.incdec()
                self.state = 641
                self.name()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 643
                self.name()
                self.state = 644
                self.incdec()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 646
                self.unary()
                self.state = 647
                self.rvalue()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 649
                self.match(bParser.TERM_17)
                self.state = 650
                self.name()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 651
                self.expression()
                self.state = 652
                self.binary()
                self.state = 653
                self.rvalue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 655
                self.expression()
                self.state = 656
                self.match(bParser.TERM_16)
                self.state = 657
                self.rvalue()
                self.state = 658
                self.match(bParser.TERM_4)
                self.state = 659
                self.rvalue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 661
                self.name()
                self.state = 662
                self.assign()
                self.state = 663
                self.rvalue()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 665
                self.match(bParser.NAME)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 666
                self.match(bParser.INT)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 667
                self.match(bParser.STRING1)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 668
                self.match(bParser.STRING2)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 669
                self.name()
                self.state = 670
                self.match(bParser.TERM_2)
                self.state = 671
                self.functionparameters_question()
                self.state = 672
                self.match(bParser.TERM_3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





