grammar REST;
start : bodyElements EOF;
bodyElements
    : bodyElement NEWLINE bodyElements
    | bodyElement
    ;
bodyElement
    : sectionTitle NEWLINE
    | labeledParagraph
    | paragraph
    | enumeration
    ;
sectionTitle
    : titleText NEWLINE underline
    ;
titleText
    : titleFirstChar
    | titleFirstChar nobrString
    ;
paragraph
    : firstParagraphElement paragraphElements NEWLINE
    ;
labeledParagraph
    : label NEWLINE NEWLINE paragraph
    ;
label
    : '.. _' id ':'
    ;
paragraphElements
    : paragraphElement paragraphElements
    | paragraphElement
    ;
firstParagraphElement
    : paragraphCharsNoSpace
    | internalReferenceNoSpace
    ;
paragraphElement
    : paragraphChars
    | internalReference
    ;
internalReference
    : presep id '_' postsep
    ;
internalReferenceNoSpace
    : id '_' postsep
    ;
enumeration
    : enumerationItems NEWLINE
    ;
enumerationItems
    : enumerationItem NEWLINE enumerationItems
    | enumerationItem
    ;
enumerationItem
    : number '. ' nobrString
    ;
paragraphChars
    : paragraphChar paragraphChars
    | paragraphChar
    ;
paragraphCharsNoSpace
    : paragraphCharNoSpace paragraphCharsNoSpace
    | paragraphCharNoSpace
    ;
paragraphChar : PARAGRAPH_CHAR;
paragraphCharNoSpace : PARAGRAPH_CHAR_NOSPACE;
presep : PRESEP;
postsep : POSTSEP;
id : ID;
number
    : digitNonZero digits
    | digit
    ;
digitNonZero : DIGIT_NONZERO;
digits
    : digit digits
    | digit
    ;
digit : DIGIT;
nobrString
    : nobrChar
    | nobrChar nobrString
    ;
nobrChar : NOBR_CHAR;
titleFirstChar : TITLE_FIRST_CHAR;
underline
    : eqs
    | dashes
    ;
eqs
    : '='
    | '=' eqs
    ;
dashes
    : '-'
    | '-' dashes
    ;
// PRINTABLE : [0-9a-zA-Z!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\f];
PARAGRAPH_CHAR : [0-9a-zA-Z!"#$%&'()+,-./:;<=>?@[\]^~ \t\n\r\f];
PARAGRAPH_CHAR_NOSPACE : [0-9a-zA-Z!"#$%&'()+,-./:;<=>?@[\]^~];
PRESEP : [ \t,;()];
POSTSEP : [ \t,.;()];
ID : [a-z];
DIGIT_NONZERO : [1-9];
DIGIT : [0-9];
NOBR_CHAR : [0-9a-zA-Z!"#$%&'()*+,-./:;<=>?@[\]^~ \f];
TITLE_FIRST_CHAR : [0-9a-zA-Z!"#$%&'(),./:;<>?@[\]^~];
NEWLINE : '\n';