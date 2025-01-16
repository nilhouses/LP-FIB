grammar exprs;

root : expr         // l'etiqueta ja és root
     ;

expr : <assoc=right> expr '^' expr    #potencia // per defecte s'associa per l'esquerra
    | expr '*' expr                   #multiplicacio
    | expr '/' expr                   #divisio
    | expr '+' expr                   #suma //son etiquetes, no comentaris
    | expr '-' expr                   #resta
    | NUM                             #numero
    ;

NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ; //espai, tabulador, enter o retorn de carro