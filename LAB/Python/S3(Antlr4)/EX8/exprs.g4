grammar exprs;//Nova gramàtica

root : functionDeclaration* main;

//Data
//Per les funcions cal que hi hagi almenys 1 return
functionDeclaration : 'function' VAR '(' paramList ')' statements 'end';


paramList : (VAR (',' VAR)*)?;

//Main
main : 'main' statements 'end';

//Statements
statements : statement*;

statement : VAR ':=' expr           #asignar
        | 'write' expr              #write
        | 'if' expr cosIf           #condicional    //cosIf sera 'then' statement 'end'
        | 'while' expr cosWhile     #condwhile
        | 'return' expr             #return
        ;

cosIf : 'then' statements 'end';

cosWhile : 'do' statements 'end';
        
//Expressions

expr : <assoc=right> expr '^' expr                                      #opArit
    | expr (MUL|DIV) expr                                               #opArit
    | expr (SUM|RES) expr                                               #opArit
    | expr (MENOR|MENORIGUAL|MAJOR|MAJORIGUAL|IGUAL|DIFERENT) expr      #opLogic
    | NUM                                                               #numero
    | VAR                                                               #variable
    | VAR '(' (expr (',' expr)*)? ')'                                   #funcCall
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
//TIPUS
NUM : [0-9]+; 
VAR : [a-zA-Z][a-zA-Z]*;      // Representa variables o funcions
//BAJANADES
WS  : [ \t\n\r]+ -> skip ; //espai, tabulador, enter o retorn de carro
