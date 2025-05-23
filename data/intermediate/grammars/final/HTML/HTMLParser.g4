parser grammar HTMLParser;

options { tokenVocab=HTMLLexer;}

htmlDocument : scriptletorseaws_star xml_question scriptletorseaws_star dtd_question scriptletorseaws_star htmlelements_star EOF 
| scriptletorseaws_star xml_question scriptletorseaws_star dtd_question scriptletorseaws_star EOF 
| scriptletorseaws_star xml_question dtd_question scriptletorseaws_star EOF 
| scriptletorseaws_star xml_question scriptletorseaws_star dtd_question htmlelements_star EOF 
| xml_question scriptletorseaws_star dtd_question EOF 
| xml_question dtd_question scriptletorseaws_star htmlelements_star EOF 
| scriptletorseaws_star xml_question dtd_question htmlelements_star EOF 
| scriptletorseaws_star xml_question scriptletorseaws_star dtd_question EOF 
| xml_question scriptletorseaws_star dtd_question htmlelements_star EOF 
| xml_question dtd_question htmlelements_star EOF 
| scriptletorseaws_star xml_question dtd_question EOF 
| xml_question dtd_question EOF 
| xml_question scriptletorseaws_star dtd_question scriptletorseaws_star EOF 
| xml_question scriptletorseaws_star dtd_question scriptletorseaws_star htmlelements_star EOF 
| xml_question dtd_question scriptletorseaws_star EOF 
| scriptletorseaws_star xml_question dtd_question scriptletorseaws_star htmlelements_star EOF ;

htmlelements_star : htmlElements htmlelements_star 
| htmlmisc_star htmlElement htmlmisc_star 
| htmlElement htmlmisc_star 
| htmlmisc_star htmlElement 
| TAG_OPEN TAG_NAME htmlattribute_star block_0 
| SCRIPTLET 
| SCRIPT_OPEN block_5 
| STYLE_OPEN block_6 
| TAG_OPEN TAG_NAME block_0 ;

dtd_question : DTD 
|  ;

xml_question : XML 
|  ;

scriptletorseaws_star : scriptletOrSeaWs scriptletorseaws_star 
| SCRIPTLET 
| SEA_WS ;

scriptletOrSeaWs : SCRIPTLET 
| SEA_WS ;

htmlElements : htmlmisc_star htmlElement htmlmisc_star 
| htmlmisc_star htmlElement 
| htmlElement htmlmisc_star 
| TAG_OPEN TAG_NAME htmlattribute_star block_0 
| SCRIPTLET 
| SCRIPT_OPEN block_5 
| STYLE_OPEN block_6 
| TAG_OPEN TAG_NAME block_0 ;

htmlmisc_star : htmlMisc htmlmisc_star 
| SEA_WS 
| HTML_COMMENT 
| HTML_CONDITIONAL_COMMENT ;

block_7 : htmlContent TAG_OPEN TAG_SLASH TAG_NAME TAG_CLOSE ;

block_0 : TAG_CLOSE block_7_question 
| TAG_SLASH_CLOSE ;

block_7_question :  
| htmlContent TAG_OPEN TAG_SLASH TAG_NAME TAG_CLOSE ;

htmlElement : TAG_OPEN TAG_NAME htmlattribute_star block_0 
| SCRIPTLET 
| SCRIPT_OPEN block_5 
| STYLE_OPEN block_6 
| TAG_OPEN TAG_NAME block_0 ;

htmlattribute_star : htmlAttribute htmlattribute_star 
| TAG_NAME block_4_question ;

block_8 : CDATA 
| TAG_OPEN TAG_NAME htmlattribute_star block_0 
| SCRIPTLET 
| HTML_COMMENT 
| HTML_CONDITIONAL_COMMENT 
| SCRIPT_OPEN block_5 
| STYLE_OPEN block_6 
| TAG_OPEN TAG_NAME block_0 ;

block_2 : block_8 htmlchardata_question 
| CDATA 
| TAG_OPEN TAG_NAME htmlattribute_star block_0 
| SCRIPTLET 
| HTML_COMMENT 
| HTML_CONDITIONAL_COMMENT 
| SCRIPT_OPEN block_5 
| STYLE_OPEN block_6 
| TAG_OPEN TAG_NAME block_0 ;

htmlContent : htmlchardata_question block_2_star 
| block_2 block_2_star 
|  
| HTML_TEXT 
| SEA_WS 
| block_8 htmlchardata_question 
| CDATA 
| TAG_OPEN TAG_NAME htmlattribute_star block_0 
| SCRIPTLET 
| HTML_COMMENT 
| HTML_CONDITIONAL_COMMENT 
| SCRIPT_OPEN block_5 
| STYLE_OPEN block_6 
| TAG_OPEN TAG_NAME block_0 ;

block_2_star : block_2 block_2_star 
| block_8 htmlchardata_question 
| CDATA 
| TAG_OPEN TAG_NAME htmlattribute_star block_0 
| SCRIPTLET 
| HTML_COMMENT 
| HTML_CONDITIONAL_COMMENT 
| SCRIPT_OPEN block_5 
| STYLE_OPEN block_6 
| TAG_OPEN TAG_NAME block_0 ;

block_4 : TAG_EQUALS ATTVALUE_VALUE ;

htmlAttribute : TAG_NAME block_4_question ;

block_4_question :  
| TAG_EQUALS ATTVALUE_VALUE ;

htmlChardata : HTML_TEXT 
| SEA_WS ;

htmlMisc : SEA_WS 
| HTML_COMMENT 
| HTML_CONDITIONAL_COMMENT ;

htmlComment : HTML_COMMENT 
| HTML_CONDITIONAL_COMMENT ;

block_5 : SCRIPT_BODY 
| SCRIPT_SHORT_BODY ;

script : SCRIPT_OPEN block_5 ;

block_6 : STYLE_BODY 
| STYLE_SHORT_BODY ;

style : STYLE_OPEN block_6 ;

htmlchardata_question : HTML_TEXT 
| SEA_WS ;

