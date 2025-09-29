grammar XML;
start
    : xml_tree
    ;
xml_tree
    : xml_open_tag inner_xml_tree xml_close_tag
    | xml_openclose_tag
    ;
inner_xml_tree
    : xml_tree inner_xml_tree
    | xml_tree
    | text
    ;
xml_open_tag
    : '<' id ' ' xml_attribute '>'
    | '<' id '>'
    ;
xml_openclose_tag
    : '<' id ' ' xml_attribute '/>'
    | '<' id '/>'
    ;
xml_close_tag
    : '</' id '>'
    ;
xml_attribute
    : xml_attribute ' ' xml_attribute
    | id '=' '"' text '"'
    ;
id: id_with_prefix
    | id_no_prefix
    ;
id_no_prefix
    : id_start_char id_chars
    | id_start_char
    ;
id_with_prefix: id_no_prefix ':' id_no_prefix;
id_start_char
    : ID_START_CHAR
    ;
id_chars
    : id_char id_chars
    | id_char
    ;
id_char
    : ID_START_CHAR
    | OTHER_ID_CHAR
    ;
text
    : TEXT_CHAR text
    | TEXT_CHAR
    ;
ID_START_CHAR
    : [a-zA-Z_]
    ;
OTHER_ID_CHAR
    : [0-9.-]
    ;
TEXT_CHAR
    : [a-zA-Z0-9. \t/?,=:+-]
    | '&quot;'
    | '&#x27;'
    ;