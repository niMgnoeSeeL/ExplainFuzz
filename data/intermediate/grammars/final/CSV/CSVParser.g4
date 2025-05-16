parser grammar CSVParser;

options { tokenVocab=CSVLexer;}

csvFile : hdr row_plus EOF ;

row_plus : row row_plus 
| field block_0_star term_1_question TERM_2 
| field term_1_question TERM_2 ;

block_0 : TERM_0 field ;

row : field block_0_star term_1_question TERM_2 
| field term_1_question TERM_2 ;

term_1_question : TERM_1 
|  ;

block_0_star : block_0 block_0_star 
| TERM_0 field ;

field : TEXT 
| STRING 
|  ;

hdr : field block_0_star term_1_question TERM_2 
| field term_1_question TERM_2 ;

