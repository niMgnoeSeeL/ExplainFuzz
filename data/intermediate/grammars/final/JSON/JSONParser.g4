parser grammar JSONParser;

options { tokenVocab=JSONLexer;}

json : value EOF ;

block_0 : TERM_1 pair ;

obj : TERM_0 pair block_0_star TERM_2 
| TERM_0 TERM_2 
| TERM_0 pair TERM_2 ;

block_0_star : block_0 block_0_star 
| TERM_1 pair ;

pair : STRING TERM_3 value ;

block_1 : TERM_1 value ;

arr : TERM_4 value block_1_star TERM_5 
| TERM_4 TERM_5 
| TERM_4 value TERM_5 ;

block_1_star : block_1 block_1_star 
| TERM_1 value ;

value : STRING 
| NUMBER 
| TERM_6 
| TERM_7 
| TERM_8 
| TERM_0 pair block_0_star TERM_2 
| TERM_0 TERM_2 
| TERM_4 value block_1_star TERM_5 
| TERM_4 TERM_5 
| TERM_0 pair TERM_2 
| TERM_4 value TERM_5 ;

