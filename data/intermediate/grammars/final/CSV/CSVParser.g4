parser grammar CSVParser;

options { tokenVocab=CSVLexer;}

csvFile : hdr row_plus EOF ;

row_plus : row row_plus 
| field block_0_star TERMINAL1_question TERMINAL2 
| field TERMINAL1_question TERMINAL2 ;

block_0 : TERMINAL0 field ;

row : field block_0_star TERMINAL1_question TERMINAL2 
| field TERMINAL1_question TERMINAL2 ;

block_0_star : block_0 block_0_star 
| TERMINAL0 field ;

field : TEXT 
| STRING 
|  ;

hdr : field block_0_star TERMINAL1_question TERMINAL2 
| field TERMINAL1_question TERMINAL2 ;

