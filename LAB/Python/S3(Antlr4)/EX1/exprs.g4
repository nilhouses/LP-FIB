grammar exprs;

root : expr 
     ;

expr : expr '+' expr                  #suma
    | expr '-' expr                   #resta
    | expr '*' expr                   #multiplicacio
    | expr '/' expr                   #divisio
    | <assoc=right> expr '^' expr     #potencia  
    | NUM                             #numero
    ;

NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ; 