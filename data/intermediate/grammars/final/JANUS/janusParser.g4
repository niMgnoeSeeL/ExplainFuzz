parser grammar janusParser;
options { tokenVocab=janusLexer; }

program : ( IDENT ( TERM_0 NUM TERM_1 )? )* ( TERM_2 IDENT statements )* EOF ; 
statements : statement+ ; 
statement : ifstmt | dostmt | callstmt | readstmt | writestmt | lvalstmt ; 
ifstmt : TERM_3 expression ( TERM_4 statements )? ( TERM_5 statements )? TERM_6 expression ; 
dostmt : TERM_7 expression ( TERM_8 statements )? ( TERM_9 statements )? TERM_10 expression ; 
callstmt : TERM_11 IDENT | TERM_12 IDENT ; 
readstmt : TERM_13 IDENT ; 
writestmt : TERM_14 IDENT ; 
lvalstmt : lvalue modstmt | lvalue swapstmt ; 
modstmt : TERM_15 expression | TERM_16 expression | TERM_17 expression | TERM_18 expression ; 
swapstmt : TERM_19 lvalue ; 
expression : minexp | minexp BINOP expression ; 
minexp : TERM_20 expression TERM_21 | TERM_22 expression | TERM_23 expression | lvalue | constant ; 
lvalue : IDENT | IDENT TERM_0 expression TERM_1 ; 
constant : NUM ; 