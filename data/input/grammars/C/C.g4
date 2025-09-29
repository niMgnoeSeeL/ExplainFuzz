grammar C;

start: statement+ EOF;

statement
    : block
    | 'if' '(' expr ')' statement ('else' statement)?
    | 'while' '(' expr ')' statement
    | 'do' statement 'while' '(' expr ')' ';'
    | declaration
    | expr ';'
    | ';'
    ;

block: '{' statement* '}';

declaration
    : 'int' ID '=' expr ';'
    | 'int' ID ';'
    ;

expr
    : expr '=' expr              
    | expr '==' expr             
    | expr '<' expr              
    | expr '+' expr              
    | expr '-' expr             
    | expr '*' expr              
    | expr '&&' expr             
    | expr '||' expr            
    | '(' expr ')'               
    | ID                         
    | INT                        
    ;

ID  : [a-z];
INT : [0-9]+;
WS  : [ \t\r\n]+ -> skip;
