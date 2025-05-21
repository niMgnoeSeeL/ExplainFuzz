parser grammar janusParser;

options { tokenVocab=janusLexer;}

block_7 : TERM_0 NUM TERM_1 ;

block_0 : IDENT block_7_question ;

block_7_question :  
| TERM_0 NUM TERM_1 ;

block_2 : TERM_2 IDENT statements ;

program : block_0_star block_2_star EOF 
| block_0_star EOF 
| EOF 
| block_2_star EOF ;

block_2_star : block_2 block_2_star 
| TERM_2 IDENT statements ;

block_0_star : block_0 block_0_star 
| IDENT block_7_question ;

statement_plus : statement statement_plus 
| TERM_3 expression block_3_question block_4_question TERM_6 expression 
| TERM_7 expression block_5_question block_6_question TERM_10 expression 
| TERM_11 IDENT 
| TERM_12 IDENT 
| TERM_13 IDENT 
| TERM_14 IDENT 
| lvalue modstmt 
| lvalue swapstmt ;

block_3 : TERM_4 statements ;

block_4 : TERM_5 statements ;

ifstmt : TERM_3 expression block_3_question block_4_question TERM_6 expression ;

block_4_question :  
| TERM_5 statements ;

block_3_question :  
| TERM_4 statements ;

block_5 : TERM_8 statements ;

block_6 : TERM_9 statements ;

dostmt : TERM_7 expression block_5_question block_6_question TERM_10 expression ;

block_6_question :  
| TERM_9 statements ;

block_5_question :  
| TERM_8 statements ;

callstmt : TERM_11 IDENT 
| TERM_12 IDENT ;

readstmt : TERM_13 IDENT ;

writestmt : TERM_14 IDENT ;

lvalstmt : lvalue modstmt 
| lvalue swapstmt ;

modstmt : TERM_15 expression 
| TERM_16 expression 
| TERM_17 expression 
| TERM_18 expression ;

swapstmt : TERM_19 lvalue ;

expression : minexp BINOP expression 
| TERM_20 expression TERM_21 
| BINOP expression 
| TERM_22 expression 
| IDENT 
| IDENT TERM_0 expression TERM_1 
| NUM ;

minexp : TERM_20 expression TERM_21 
| BINOP expression 
| TERM_22 expression 
| IDENT 
| IDENT TERM_0 expression TERM_1 
| NUM ;

lvalue : IDENT 
| IDENT TERM_0 expression TERM_1 ;

constant : NUM ;

statements : statement statement_plus 
| TERM_3 expression block_3_question block_4_question TERM_6 expression 
| TERM_7 expression block_5_question block_6_question TERM_10 expression 
| TERM_11 IDENT 
| TERM_12 IDENT 
| TERM_13 IDENT 
| TERM_14 IDENT 
| lvalue modstmt 
| lvalue swapstmt ;

statement : TERM_3 expression block_3_question block_4_question TERM_6 expression 
| TERM_7 expression block_5_question block_6_question TERM_10 expression 
| TERM_11 IDENT 
| TERM_12 IDENT 
| TERM_13 IDENT 
| TERM_14 IDENT 
| lvalue modstmt 
| lvalue swapstmt ;

