parser grammar SCXMLParser;

options {
    tokenVocab = SCXMLLexer;
}

scxmlDocument
    : prolog? misc* scxmlElement misc* EOF
    ;

prolog
    : XMLDeclOpen attribute* SPECIAL_CLOSE
    ;

scxmlElement
    : '<' SCXML attribute* '>' scxmlContent* '<' '/' SCXML '>'
    ;

scxmlContent
    : stateElement
    | transitionElement
    | finalElement
    | parallelElement
    | historyElement
    | invokeElement
    | scriptElement
    | dataElement
    | onEntryElement
    | onExitElement
    | anyElement
    ;

stateElement
    : '<' STATE attribute* '>' scxmlContent* '<' '/' STATE '>'
    | '<' STATE attribute* '/>'
    ;

transitionElement
    : '<' TRANSITION attribute* '/>'
    | '<' TRANSITION attribute* '>' scxmlContent* '<' '/' TRANSITION '>'
    ;

finalElement
    : '<' FINAL attribute* '>' scxmlContent* '<' '/' FINAL '>'
    | '<' FINAL attribute* '/>'
    ;

parallelElement
    : '<' PARALLEL attribute* '>' scxmlContent* '<' '/' PARALLEL '>'
    | '<' PARALLEL attribute* '/>'
    ;

historyElement
    : '<' HISTORY attribute* '>' scxmlContent* '<' '/' HISTORY '>'
    | '<' HISTORY attribute* '/>'
    ;

invokeElement
    : '<' INVOKE attribute* '>' scxmlContent* '<' '/' INVOKE '>'
    | '<' INVOKE attribute* '/>'
    ;

scriptElement
    : '<' SCRIPT attribute* '>' content? '<' '/' SCRIPT '>'
    | '<' SCRIPT attribute* '/>'
    ;

dataElement
    : '<' DATA attribute* '/>'
    ;

onEntryElement
    : '<' ONENTRY attribute* '>' scxmlContent* '<' '/' ONENTRY '>'
    | '<' ONENTRY attribute* '/>'
    ;

onExitElement
    : '<' ONEXIT attribute* '>' scxmlContent* '<' '/' ONEXIT '>'
    | '<' ONEXIT attribute* '/>'
    ;

anyElement
    : element
    ;

element
    : '<' Name attribute* '>' content? '<' '/' Name '>'
    | '<' Name attribute* '/>'
    ;

content
    : chardata? ((element | reference | CDATA | PI | COMMENT) chardata?)*
    ;

reference
    : EntityRef
    | CharRef
    ;

attribute
    : Name '=' STRING
    ;

chardata
    : TEXT
    | SEA_WS
    ;

misc
    : COMMENT
    | PI
    | SEA_WS
    ;
