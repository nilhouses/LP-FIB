grammar exprs;//Nova gramàtica

root : statements         // root guarda los valores
     ;

statements : statement*
           ;

statement : VAR ':=' expr  #asignar       
        | 'write' VAR      #imprimir
        | 'if' expr cosIf  #condicional    //cosIf sera 'then' statement 'end'
        ;

cosIf : 'then' statement+ 'end'
    ;

expr : <assoc=right> expr '^' expr                                      #opArit
    | expr (MUL|DIV) expr                                               #opArit
    | expr (SUM|RES) expr                                               #opArit
    | expr (MENOR|MENORIGUAL|MAJOR|MAJORIGUAL|IGUAL|DIFERENT) expr      #opLogic
    | NUM                                                               #numero
    | VAR                                                               #variable  
    ;


//OPERANDS
DIV : '/';
MUL : '*';
SUM : '+';
RES : '-';
//COMPARADORS
MENOR : '<';
MENORIGUAL : '<=';
MAJOR : '>';
MAJORIGUAL : '>=';
IGUAL : '=';
DIFERENT : '<>';
//TIPUS SIMPLES
NUM : [0-9]+; 
VAR : [a-zA-Z]+;
//BAJANADES
WS  : [ \t\n\r]+ -> skip ; //espai, tabulador, enter o retorn de carro