//    Exercici1, generar fitxers "antlr4 -Dlanguage=Python3 -no-listener exprs.g4"
//  APUNTS
// * representa 0..*
// + representa 1..*

grammar exprs;

root : expr         // l'etiqueta ja és root
     ;

expr : expr '+' expr                  #suma //son etiquetes, no comentaris
    | expr '-' expr                   #resta
    | expr '*' expr                   #multiplicacio
    | expr '/' expr                   #divisio
    | <assoc=right> expr '^' expr     #potencia // per defecte s'associa per l'esquerra
    | NUM                             #numero
    ;

NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ; //espai, tabulador, enter o retorn de carro