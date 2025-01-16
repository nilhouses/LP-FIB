grammar scheme;

root : expr+;

expr : '(' expr* ')'                                             #evaluate
     | '\'' '(' expr* ')'                                        #list
     | OP                                                        #op
     | ID                                                        #ID 
     | NUM                                                       #number
     | BOOL                                                      #boolean
     | STRING                                                    #string
     ;

OP : '+' | '-' | '*' | '/' | 'mod' | '<' | '<=' | '>' | '>=' | '=' | '<>' | 'and' | 'or' | 'not';

BOOL : '#t'|'#f';
NUM : '-'?[0-9]+;
ID : [a-zA-Z][?a-zA-Z0-9_-]*;
STRING : '"' (~["])* '"';

COMMENT : ';' ~[\r\n]* -> skip ; // comentari (;) 
WS  : [ \t\n\r]+ -> skip ;  // Espai, tabulador, enter(<-|) o retorn de carro