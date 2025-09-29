parser grammar CSVParser;
options { tokenVocab=CSVLexer; }

csvFile : hdr row+ EOF ; 
hdr : row ; 
row : field ( TERM_0 field )* TERM_1? TERM_2 ; 
field : TEXT | STRING |  ; 