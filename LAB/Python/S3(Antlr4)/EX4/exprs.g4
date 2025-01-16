grammar exprs;//Nova gramàtica

root : statements         // root guarda los valores
     ;

statements : statement*
           ;

statement : VAR ':=' expr    #asignar       
        | 'write' VAR        #imprimir
        ;

expr : <assoc=right> expr '^' expr    #potencia // per defecte s'associa per l'esquerra
    | expr '*' expr                   #multiplicacio
    | expr '/' expr                   #divisio
    | expr '+' expr                   #suma //son etiquetes, no comentaris
    | expr '-' expr                   #resta
    | NUM                             #numero
    | VAR                             #variable
    ;

NUM : [0-9]+; 
VAR : [a-zA-Z]+;

WS  : [ \t\n\r]+ -> skip ; //espai, tabulador, enter o retorn de carro