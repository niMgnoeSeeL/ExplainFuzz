parser grammar bParser;

options { tokenVocab=bLexer;}

program : definition_star EOF 
| EOF ;

definition_star : definition definition_star 
| name constant_question block_0_star TERM_1 
| name TERM_2 block_2_question TERM_3 statement 
| name constant_question TERM_1 ;

block_9 : TERM_0 ival ;

block_0 : ival block_9_star 
| INT 
| STRING1 
| STRING2 
| NAME ;

block_9_star : block_9 block_9_star 
| TERM_0 ival ;

block_10 : TERM_0 name ;

block_2 : name block_10_star 
| NAME ;

block_10_star : block_10 block_10_star 
| TERM_0 name ;

definition : name constant_question block_0_star TERM_1 
| name TERM_2 block_2_question TERM_3 statement 
| name constant_question TERM_1 ;

block_2_question :  
| name block_10_star 
| NAME ;

block_0_star : block_0 block_0_star 
| ival block_9_star 
| INT 
| STRING1 
| STRING2 
| NAME ;

constant_question :  
| INT 
| STRING1 
| STRING2 ;

statement : name TERM_4 statement 
| TERM_14 name block_6_star TERM_1 
| TERM_15 name constant_question block_7_star TERM_1 
| TERM_13 constant TERM_4 statement 
| TERM_5 statement_star TERM_6 
| TERM_11 TERM_2 rvalue TERM_3 statement block_5_question 
| TERM_10 TERM_2 rvalue TERM_3 statement 
| TERM_9 rvalue statement 
| TERM_8 rvalue TERM_1 
| TERM_7 block_4_question TERM_1 
| rvalue TERM_1 
| TERM_1 
| TERM_5 TERM_6 
| TERM_14 name TERM_1 
| TERM_15 name constant_question TERM_1 ;

nullstmt : TERM_1 ;

expressionstmt : rvalue TERM_1 ;

blockstmt : TERM_5 statement_star TERM_6 
| TERM_5 TERM_6 ;

statement_star : statement statement_star 
| name TERM_4 statement 
| TERM_14 name block_6_star TERM_1 
| TERM_15 name constant_question block_7_star TERM_1 
| TERM_13 constant TERM_4 statement 
| TERM_5 statement_star TERM_6 
| TERM_11 TERM_2 rvalue TERM_3 statement block_5_question 
| TERM_10 TERM_2 rvalue TERM_3 statement 
| TERM_9 rvalue statement 
| TERM_8 rvalue TERM_1 
| TERM_7 block_4_question TERM_1 
| rvalue TERM_1 
| TERM_1 
| TERM_5 TERM_6 
| TERM_14 name TERM_1 
| TERM_15 name constant_question TERM_1 ;

block_4 : TERM_2 rvalue TERM_3 ;

returnstmt : TERM_7 block_4_question TERM_1 ;

block_4_question :  
| TERM_2 rvalue TERM_3 ;

gotostmt : TERM_8 rvalue TERM_1 ;

switchstmt : TERM_9 rvalue statement ;

whilestmt : TERM_10 TERM_2 rvalue TERM_3 statement ;

block_5 : TERM_12 statement ;

ifstmt : TERM_11 TERM_2 rvalue TERM_3 statement block_5_question ;

block_5_question :  
| TERM_12 statement ;

casestmt : TERM_13 constant TERM_4 statement ;

block_6 : TERM_0 name ;

externsmt : TERM_14 name block_6_star TERM_1 
| TERM_14 name TERM_1 ;

block_6_star : block_6 block_6_star 
| TERM_0 name ;

block_7 : TERM_0 name constant_question ;

autosmt : TERM_15 name constant_question block_7_star TERM_1 
| TERM_15 name constant_question TERM_1 ;

block_7_star : block_7 block_7_star 
| TERM_0 name constant_question ;

ternary : expression TERM_16 rvalue TERM_4 rvalue ;

comparison : expression binary rvalue ;

assignment : name assign rvalue ;

expression : TERM_2 rvalue TERM_3 
| incdec name 
| name incdec 
| unary rvalue 
| TERM_17 name 
| NAME 
| INT 
| STRING1 
| STRING2 
| name TERM_2 functionparameters_question TERM_3 ;

functioninvocation : name TERM_2 functionparameters_question TERM_3 ;

functionparameters_question :  
| rvalue block_8_star 
| TERM_2 rvalue TERM_3 
| incdec name 
| name incdec 
| unary rvalue 
| TERM_17 name 
| expression binary rvalue 
| expression TERM_16 rvalue TERM_4 rvalue 
| name assign rvalue 
| NAME 
| INT 
| STRING1 
| STRING2 
| name TERM_2 functionparameters_question TERM_3 ;

block_8 : TERM_0 rvalue ;

functionparameters : rvalue block_8_star 
| TERM_2 rvalue TERM_3 
| incdec name 
| name incdec 
| unary rvalue 
| TERM_17 name 
| expression binary rvalue 
| expression TERM_16 rvalue TERM_4 rvalue 
| name assign rvalue 
| NAME 
| INT 
| STRING1 
| STRING2 
| name TERM_2 functionparameters_question TERM_3 ;

block_8_star : block_8 block_8_star 
| TERM_0 rvalue ;

assign : TERM_18 binary_question ;

binary_question :  
| TERM_23 
| TERM_17 
| TERM_24 
| TERM_25 
| TERM_26 
| TERM_27 
| TERM_28 
| TERM_29 
| TERM_30 
| TERM_31 
| TERM_21 
| TERM_32 
| TERM_33 
| TERM_34 
| TERM_35 ;

incdec : TERM_19 
| TERM_20 ;

unary : TERM_21 
| TERM_22 ;

binary : TERM_23 
| TERM_17 
| TERM_24 
| TERM_25 
| TERM_26 
| TERM_27 
| TERM_28 
| TERM_29 
| TERM_30 
| TERM_31 
| TERM_21 
| TERM_32 
| TERM_33 
| TERM_34 
| TERM_35 ;

lvalue : TERM_34 rvalue 
| rvalue TERM_36 rvalue TERM_37 
| NAME ;

constant : INT 
| STRING1 
| STRING2 ;

name : NAME ;

ival : INT 
| STRING1 
| STRING2 
| NAME ;

rvalue : TERM_2 rvalue TERM_3 
| incdec name 
| name incdec 
| unary rvalue 
| TERM_17 name 
| expression binary rvalue 
| expression TERM_16 rvalue TERM_4 rvalue 
| name assign rvalue 
| NAME 
| INT 
| STRING1 
| STRING2 
| name TERM_2 functionparameters_question TERM_3 ;

