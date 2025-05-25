/*
Copyright(c) Miryung Kim


Modified based on
https://github.com/tunnelvisionlabs/antlr4-grammar-postgresql/blob/master/src/com/tunnelvisionlabs/postgresql/PostgreSqlLexer.g4
*/

/*
 * [The "MIT license"]
 * Copyright (C) 2014 Sam Harwell, Tunnel Vision Laboratories, LLC
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * 1. The above copyright notice and this permission notice shall be included in
 *    all copies or substantial portions of the Software.
 * 2. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 *    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 *    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 *    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 *    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 *    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 *    DEALINGS IN THE SOFTWARE.
 * 3. Except as contained in this notice, the name of Tunnel Vision
 *    Laboratories, LLC. shall not be used in advertising or otherwise to
 *    promote the sale, use or other dealings in this Software without prior
 *    written authorization from Tunnel Vision Laboratories, LLC.
 */

// $antlr-format alignTrailingComments true, columnLimit 150, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine true, allowShortBlocksOnASingleLine true, minEmptyLines 0, alignSemicolons ownLine
// $antlr-format alignColons trailing, singleLineOverrulesHangingColon true, alignLexerCommands true, alignLabels true, alignTrailers true

lexer grammar SQLSimplifiedLexer;
/* Reference:
 * http://www.postgresql.org/docs/9.3/static/sql-syntax-lexical.html
 */

options {
    //superClass = PostgreSQLLexerBase; commented out by Miryung Kim
    caseInsensitive = true;
}
/*
@header {
}
@members { //This field stores the tags which are used to detect the end of a dollar-quoted string literal.
}
*/
//

// SPECIAL CHARACTERS (4.1.4)

//

// Note that Asterisk is a valid operator, but does not have the type Operator due to its syntactic use in locations

// that are not expressions.

OPEN_PAREN: '(';

CLOSE_PAREN: ')';

COMMA: ',';

SEMI: ';';

STAR: '*';

EQUAL: '=';

DOT: '.';

SLASH: '/';

LT: '<';

GT: '>';

PARAM: '$' ([0-9])+;
//

// OPERATORS (4.1.3)

//

// this rule does not allow + or - at the end of a multi-character operator

Operator:
    (
        (
            OperatorCharacter
            | ('+' | '-' )+ (OperatorCharacter | '/' )
            | '/'
        )+
        | // special handling for the single-character operators + and -
        [+-]
    )
    //TODO somehow rewrite this part without using Actions

;
/* This rule handles operators which end with + or -, and sets the token type to Operator. It is comprised of four
 * parts, in order:
 *
 *   1. A prefix, which does not contain a character from the required set which allows + or - to appear at the end of
 *      the operator.
 *   2. A character from the required set which allows + or - to appear at the end of the operator.
 *   3. An optional sub-token which takes the form of an operator which does not include a + or - at the end of the
 *      sub-token.
 *   4. A suffix sequence of + and - characters.
 */

/*OperatorEndingWithPlusMinus:
    (OperatorCharacterNotAllowPlusMinusAtEnd | '-' {checkLA('-')}? | '/' {checkLA('*')}?)* OperatorCharacterAllowPlusMinusAtEnd Operator? (
        '+'
        | '-' {checkLA('-')}?
    )+        -> type (Operator)
;
*/
OperatorEndingWithPlusMinus:
    (OperatorCharacterNotAllowPlusMinusAtEnd | '-'  | '/' )* OperatorCharacterAllowPlusMinusAtEnd Operator? (
        '+'
        | '-'
    )+        -> type (Operator)
;

// Each of the following fragment rules omits the +, -, and / characters, which must always be handled in a special way

// by the operator rules above.

fragment OperatorCharacter: [*<>=~!@%^&|`?#];
// these are the operator characters that don't count towards one ending with + or -

fragment OperatorCharacterNotAllowPlusMinusAtEnd: [*<>=+];
// an operator may end with + or - if it contains one of these characters

fragment OperatorCharacterAllowPlusMinusAtEnd: [~!@%^&|`?#];
//

// KEYWORDS (Appendix C)

//

//

// reserved keywords

//

AND: 'AND';

AS: 'AS';

ASC: 'ASC';

CASE: 'CASE';

DESC: 'DESC';

DISTINCT: 'DISTINCT';

ELSE: 'ELSE';

FOR: 'FOR';

FROM: 'FROM';

GROUP_P: 'GROUP';

HAVING: 'HAVING';

NOT: 'NOT';

NULL_P: 'NULL';

ON: 'ON';

OR: 'OR';

ORDER: 'ORDER';

SELECT: 'SELECT';

THEN: 'THEN';

UNION: 'UNION';

WHEN: 'WHEN';

WHERE: 'WHERE';

JOIN: 'JOIN';

BY: 'BY';

DAY_P: 'DAY';

YEAR_P: 'YEAR';

EXISTS: 'EXISTS';

EXTRACT: 'EXTRACT';

INTERVAL: 'INTERVAL';

SUBSTRING: 'SUBSTRING';

TIME: 'TIME';

VALUE_P: 'VALUE';

END_P: 'END';

ROUND: 'ROUND';

USING: 'USING';

Identifier: IdentifierStartChar IdentifierChar*;

fragment IdentifierStartChar options {
    caseInsensitive = false;
}: // these are the valid identifier start characters below 0x7F
    [a-zA-Z_]
//    | // these are the valid characters from 0x80 to 0xFF
//    [\u00AA\u00B5\u00BA\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u00FF]
//    |                               // these are the letters above 0xFF which only need a single UTF-16 code unit
//    [\u0100-\uD7FF\uE000-\uFFFF]
//    |                               // letters which require multiple UTF-16 code units
//    [\uD800-\uDBFF] [\uDC00-\uDFFF]
;

fragment IdentifierChar: StrictIdentifierChar | '$';

fragment StrictIdentifierChar: IdentifierStartChar | [0-9];
/* Quoted Identifiers
 *
 *   These are divided into four separate tokens, allowing distinction of valid quoted identifiers from invalid quoted
 *   identifiers without sacrificing the ability of the lexer to reliably recover from lexical errors in the input.
 */

QuotedIdentifier: UnterminatedQuotedIdentifier '"';
// This is a quoted identifier which only contains valid characters but is not terminated

UnterminatedQuotedIdentifier: '"' ('""' | ~ [\u0000"])*;
// This is a quoted identifier which is terminated but contains a \u0000 character

InvalidQuotedIdentifier: InvalidUnterminatedQuotedIdentifier '"';
// This is a quoted identifier which is unterminated and contains a \u0000 character

InvalidUnterminatedQuotedIdentifier: '"' ('""' | ~ '"')*;
/* Unicode Quoted Identifiers
 *
 *   These are divided into four separate tokens, allowing distinction of valid Unicode quoted identifiers from invalid
 *   Unicode quoted identifiers without sacrificing the ability of the lexer to reliably recover from lexical errors in
 *   the input. Note that escape sequences are never checked as part of this determination due to the ability of users
 *   to change the escape character with a UESCAPE clause following the Unicode quoted identifier.
 *
 * TODO: these rules assume "" is still a valid escape sequence within a Unicode quoted identifier.
 */

UnicodeQuotedIdentifier: 'U' '&' QuotedIdentifier;
// This is a Unicode quoted identifier which only contains valid characters but is not terminated

UnterminatedUnicodeQuotedIdentifier: 'U' '&' UnterminatedQuotedIdentifier;
// This is a Unicode quoted identifier which is terminated but contains a \u0000 character

InvalidUnicodeQuotedIdentifier: 'U' '&' InvalidQuotedIdentifier;
// This is a Unicode quoted identifier which is unterminated and contains a \u0000 character

InvalidUnterminatedUnicodeQuotedIdentifier: 'U' '&' InvalidUnterminatedQuotedIdentifier;
//

// CONSTANTS (4.1.2)

//

// String Constants (4.1.2.1)

StringConstant: UnterminatedStringConstant '\'';

UnterminatedStringConstant: '\'' ('\'\'' | ~ '\'')*;
// String Constants with C-style Escapes (4.1.2.2)

BeginEscapeStringConstant: 'E' '\'' -> more, pushMode (EscapeStringConstantMode);
// String Constants with Unicode Escapes (4.1.2.3)

//

//   Note that escape sequences are never checked as part of this token due to the ability of users to change the escape

//   character with a UESCAPE clause following the Unicode string constant.

//

// TODO: these rules assume '' is still a valid escape sequence within a Unicode string constant.

UnicodeEscapeStringConstant: UnterminatedUnicodeEscapeStringConstant '\'';

UnterminatedUnicodeEscapeStringConstant: 'U' '&' UnterminatedStringConstant;
// Dollar-quoted String Constants (4.1.2.4)

BeginDollarStringConstant: '$' Tag? '$' -> pushMode (DollarQuotedStringMode);
/* "The tag, if any, of a dollar-quoted string follows the same rules as an
 * unquoted identifier, except that it cannot contain a dollar sign."
 */

fragment Tag: IdentifierStartChar StrictIdentifierChar*;
// Bit-strings Constants (4.1.2.5)

BinaryStringConstant: UnterminatedBinaryStringConstant '\'';

UnterminatedBinaryStringConstant: 'B' '\'' [01]*;

InvalidBinaryStringConstant: InvalidUnterminatedBinaryStringConstant '\'';

InvalidUnterminatedBinaryStringConstant: 'B' UnterminatedStringConstant;

HexadecimalStringConstant: UnterminatedHexadecimalStringConstant '\'';

UnterminatedHexadecimalStringConstant: 'X' '\'' [0-9A-F]*;

InvalidHexadecimalStringConstant: InvalidUnterminatedHexadecimalStringConstant '\'';

InvalidUnterminatedHexadecimalStringConstant: 'X' UnterminatedStringConstant;
// Numeric Constants (4.1.2.6)

Integral: Digits;

NumericFail: Digits '..' ;

Numeric:
    Digits '.' Digits? /*? replaced with + to solve problem with DOT_DOT .. but this surely must be rewriten */ (
        'E' [+-]? Digits
    )?
    | '.' Digits ('E' [+-]? Digits)?
    | Digits 'E' [+-]? Digits
;

fragment Digits: [0-9]+;

PLSQLVARIABLENAME: ':' [A-Z_] [A-Z_0-9$]*;

PLSQLIDENTIFIER: ':"' ('\\' . | '""' | ~ ('"' | '\\'))* '"';
//

// WHITESPACE (4.1)

//

Whitespace: [ \t]+ -> channel (HIDDEN);

Newline: ('\r' '\n'? | '\n') -> channel (HIDDEN);
//

// COMMENTS (4.1.5)

//

LineComment: '--' ~ [\r\n]* -> channel (HIDDEN);

BlockComment:
    ('/*' ('/'* BlockComment | ~ [/*] | '/'+ ~ [/*] | '*'+ ~ [/*])* '*'* '*/') -> channel (HIDDEN)
;

UnterminatedBlockComment:
    '/*' (
        '/'* BlockComment
        | // these characters are not part of special sequences in a block comment
        ~ [/*]
        | // handle / or * characters which are not part of /* or */ and do not appear at the end of the file
        ('/'+ ~ [/*] | '*'+ ~ [/*])
    )*
    // Handle the case of / or * characters at the end of the file, or a nested unterminated block comment
    ('/'+ | '*'+ | '/'* UnterminatedBlockComment)?
    // Optional assertion to make sure this rule is working as intended

;
//

// META-COMMANDS

//

// http://www.postgresql.org/docs/9.3/static/app-psql.html

MetaCommand: '\\' (~ [\r\n\\"] | '"' ~ [\r\n"]* '"')* ('"' ~ [\r\n"]*)?;

EndMetaCommand: '\\\\';
//

// ERROR

//

// Any character which does not match one of the above rules will appear in the token stream as an ErrorCharacter token.

// This ensures the lexer itself will never encounter a syntax error, so all error handling may be performed by the

// parser.

ErrorCharacter: .;

mode EscapeStringConstantMode;
EscapeStringConstant: EscapeStringText '\'' -> mode (AfterEscapeStringConstantMode);

UnterminatedEscapeStringConstant:
    EscapeStringText
    // Handle a final unmatched \ character appearing at the end of the file
    '\\'? EOF
;

fragment EscapeStringText options {
    caseInsensitive = false;
}:
    (
        '\'\''
        | '\\' (
            // two-digit hex escapes are still valid when treated as single-digit escapes
            'x' [0-9a-fA-F]
            | 'u' [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F]
            | 'U' [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F] [0-9a-fA-F]
            | // Any character other than the Unicode escapes can follow a backslash. Some have special meaning,
            // but that doesn't affect the syntax.
            ~ [xuU]
        )
        | ~ ['\\]
    )*
;

InvalidEscapeStringConstant: InvalidEscapeStringText '\'' -> mode (AfterEscapeStringConstantMode);

InvalidUnterminatedEscapeStringConstant:
    InvalidEscapeStringText
    // Handle a final unmatched \ character appearing at the end of the file
    '\\'? EOF
;

fragment InvalidEscapeStringText: ('\'\'' | '\\' . | ~ ['\\])*;

mode AfterEscapeStringConstantMode;

AfterEscapeStringConstantMode_Whitespace: Whitespace -> type (Whitespace), channel (HIDDEN);
AfterEscapeStringConstantMode_Newline:
    Newline -> type (Newline), channel (HIDDEN), mode (AfterEscapeStringConstantWithNewlineMode)
;
/*

AfterEscapeStringConstantMode_NotContinued:
     {} // intentionally empty
     -> skip, popMode
;
*/

mode AfterEscapeStringConstantWithNewlineMode;
AfterEscapeStringConstantWithNewlineMode_Whitespace:
    Whitespace -> type (Whitespace), channel (HIDDEN)
;

AfterEscapeStringConstantWithNewlineMode_Newline: Newline -> type (Newline), channel (HIDDEN);

AfterEscapeStringConstantWithNewlineMode_Continued:
    '\'' -> more, mode (EscapeStringConstantMode)
;

/*
AfterEscapeStringConstantWithNewlineMode_NotContinued:
     {} // intentionally empty
     -> skip, popMode
;
*/

mode DollarQuotedStringMode;
DollarText:
    ~ '$'+
    //| '$'([0-9])+
    | // this alternative improves the efficiency of handling $ characters within a dollar-quoted string which are

    // not part of the ending tag.
    '$' ~ '$'*
;

// EndDollarStringConstant: ('$' Tag? '$') {isTag()}? {popTag();} -> popMode;

EndDollarStringConstant: ('$' Tag? '$')  -> popMode;