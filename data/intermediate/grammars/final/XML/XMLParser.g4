parser grammar XMLParser;

options { tokenVocab=XMLLexer;}

document : prolog_question misc_star element misc_star EOF 
| prolog_question element misc_star EOF ;

misc_star : misc misc_star 
| COMMENT 
| PI 
| SEA_WS ;

prolog_question :  
| XMLDeclOpen attribute_star SPECIAL_CLOSE 
| XMLDeclOpen SPECIAL_CLOSE 
| XMLDeclOpen SPECIAL_CLOSE ;

prolog : XMLDeclOpen attribute_star SPECIAL_CLOSE 
| XMLDeclOpen SPECIAL_CLOSE 
| XMLDeclOpen SPECIAL_CLOSE ;

attribute_star : attribute attribute_star 
| attribute attribute_star 
| Name EQUALS STRING 
| Name EQUALS STRING ;

block_2 : CDATA 
| PI 
| COMMENT 
| OPEN Name attribute_star CLOSE content OPEN SLASH Name CLOSE 
| OPEN Name attribute_star SLASH_CLOSE 
| EntityRef 
| CharRef 
| OPEN Name SLASH_CLOSE 
| OPEN Name CLOSE content OPEN SLASH Name CLOSE 
| OPEN Name SLASH_CLOSE 
| OPEN Name CLOSE content OPEN SLASH Name CLOSE ;

block_0 : block_2 chardata_question 
| CDATA 
| PI 
| COMMENT 
| OPEN Name attribute_star CLOSE content OPEN SLASH Name CLOSE 
| OPEN Name attribute_star SLASH_CLOSE 
| EntityRef 
| CharRef 
| OPEN Name SLASH_CLOSE 
| OPEN Name CLOSE content OPEN SLASH Name CLOSE 
| OPEN Name SLASH_CLOSE 
| OPEN Name CLOSE content OPEN SLASH Name CLOSE ;

content : chardata_question block_0_star 
| block_0 block_0_star 
|  
| TEXT 
| SEA_WS 
| block_2 chardata_question 
| CDATA 
| PI 
| COMMENT 
| OPEN Name attribute_star CLOSE content OPEN SLASH Name CLOSE 
| OPEN Name attribute_star SLASH_CLOSE 
| EntityRef 
| CharRef 
| OPEN Name SLASH_CLOSE 
| OPEN Name CLOSE content OPEN SLASH Name CLOSE 
| OPEN Name SLASH_CLOSE 
| OPEN Name CLOSE content OPEN SLASH Name CLOSE ;

block_0_star : block_0 block_0_star 
| block_2 chardata_question 
| CDATA 
| PI 
| COMMENT 
| OPEN Name attribute_star CLOSE content OPEN SLASH Name CLOSE 
| OPEN Name attribute_star SLASH_CLOSE 
| EntityRef 
| CharRef 
| OPEN Name SLASH_CLOSE 
| OPEN Name CLOSE content OPEN SLASH Name CLOSE 
| OPEN Name SLASH_CLOSE 
| OPEN Name CLOSE content OPEN SLASH Name CLOSE ;

element : OPEN Name attribute_star CLOSE content OPEN SLASH Name CLOSE 
| OPEN Name attribute_star SLASH_CLOSE 
| OPEN Name CLOSE content OPEN SLASH Name CLOSE 
| OPEN Name SLASH_CLOSE 
| OPEN Name CLOSE content OPEN SLASH Name CLOSE 
| OPEN Name SLASH_CLOSE ;

reference : EntityRef 
| CharRef ;

attribute : Name EQUALS STRING ;

chardata : TEXT 
| SEA_WS ;

misc : COMMENT 
| PI 
| SEA_WS ;

chardata_question : TEXT 
| SEA_WS ;

