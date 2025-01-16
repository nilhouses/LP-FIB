# Pràctica LP (2024-2025 Q1)
Aquesta pràctica consisteix en implementar un mini intèrpret de [Scheme](https://docs.scheme.org/) amb moltes simplificacions. Admet els tipus simples següents:
- `Enters` (Que si s'operen entre ells poden retornar fraccions)
- `Booleans`
- `Strings`

També s'admeten llistes, que poden ser mixtes, és a dir, poden tenir enters, booleans, strings o fins i tot altres llistes simultàniament. 

Les operacions que ha d'admetre l'intèrpret venen donades a l'[enunciat](https://github.com/jordi-petit/lp-mini-scheme) de la pràctica.

## Instal·lació
Aquest projecte usa Python 3 i [ANTLR4](https://www.antlr.org/about.html), pel que cal:
- Obtenir [python3](https://www.python.org/)

Un cop s'hagi instalat python3, cal obtenir ANTLR4 executant:
```bash
    pip install antlr4-tools
    antlr4
    pip install antlr4-python3-runtime
```
## Usage (Ús)
Per executar l'intèrpret per primera vegada cal que ANTLR generi varis fitxers. La comanda usada serà:   
```bash
    make
```
Una vegada s'hagi executat l'ordre, des del directori arrel del projecte cal executar:
```bash
    python3 scheme.py $PATH/programa.scm
```
on $PATH és el path relatiu del fitxer programa.scm a interpretar. A l'últim apartat de jocs de proves d'aquest document s'indiquen les instruccions concretes per executar un programa dels jocs de proves.

# Codi
## Funcionament
El codi implementa un intèrpret de Scheme amb ANTLR4. Es divideix en tres fitxers principals, la gramàtica (`scheme.g4`), la classe que implementa els visitadors de cada regla (`EvalVisitor.py`) i el driver (`scheme.py`) que interpreta el codi usant els fitxers generats per ANTLR.
Els fitxers disponibles al desplegar el projecte són:
- `./Tests`: Directori que conté els fitxers necessaris per executar els jocs de proves.
- `./Tests/*.scm`: Fitxers font per executar els jocs de proves.
- `./Tests/*.inp`: Fitxers amb l'entrada d'un jocs de proves (si en té).
- `./Tests/*.out`: Fitxers amb la sortida dels jocs de proves.
- `EvalVisitor.py`: Classe que implementa els visitadors de cada regla de la gramàtica.
- `ex.py`: Aquesta classe mostra els errors personalitzats  que he decidit mostrar des d'EvalVisitor.py en format d'excepcions.
- `Makefile`: Fitxer que genera els fitxers necessaris per ANTLR. Pot generar fitxers o eliminar-los, amb les comandes:
```bash
    make
    make clean
```
respectivament.
- `MyErrorListener.py`: Classe que implementa un listener per facilitar l'ubicació dels errors sintàctics.
- `README.md`: Fitxer que documenta el projecte.
- `scheme.g4`: Gramàtica de Scheme implementada amb ANTLR4.
- `scheme.py`: Driver que interpreta el codi.

### Gramàtica
La gramàtica (`scheme.g4`) està formada únicament per expressions. L'implementació ha seguit aquesta línea buscant simplificar-la. Una expressió pot ser un dels següents tipus simples:
- `'(' expr* ')'` Norma d'avaluar una expressió
- `'\'' '(' expr* ')'` Sintaxi d'una lista
- `OP` Operand, pot ser qualsevol valor dels següents ( `+`,`-` , `*` , `/` , `mod` , `<` , `<=` , `>` , `>=` , `=` , `<>` , `and` , `or` o `not`)
- `ID` Identificador que pot representar una llista, string, boolea, enter o funció.                                              
- `NUM` Valor enter.
- `BOOL`  Valor boolea.
- `STRING` Valor string.
A més l'interpret també pot usar `;comentaris`

### Visitador
La el fitxer de la classe visitadora (`EvalVisitor.py`) disposa dels següents atributs globals:

- `GlobalSymbols`: Diccionari que conté les variables globals.
- `LocalSymbols`: Pila que conté les variables amb visibilitat local.
- `OpDICT`: Diccionari que conté les variables globals.
- `prohibitedID`: Llista dels noms que no poden tenir les variables i/o funcions.

La classe com a tal, conté els mètodes següents:
- `VisitRoot`: Avalua les expressions del codi en ordre.
- `VisitNumber`: Avalua un nombre enter retornant el seu valor.
- `VisitBoolean`: Avalua un boolea retornant el seu valor.
- `VisitString`: Avalua una cadena de text retornant el seu valor.
- `VisitList`: Avalua una llista literal (`'\'' '(' expr* ')'`) retornant el seu valor.
- `VisitID`: Avalua un Identificardor (`ID`) retornant el valor que té assignat aquell element (En cas que ens situem a un let, ens interessa buscar el valor de la variable en el context local, en primer lloc, i , si no s'ha trobat ja el buscarem al context global).
- `VisitEvaluate`: Avalua una expressió, aquesta expressió avaluada pot ser:
    - **`OP`** (Operador) amb dos arguments. Exemple:
        ```Scheme
        (* 2 6) ;12
        ```
    - **`if`** (condició única) amb dues expressions (per si s'avalua cert o fals el condicional, respectivament). Exemple:
        ```Scheme
        (if (> 7 4)
            "sí"
            "no")  ; Resultat: "sí"
        ```
    - **`cond`** (condició multiple) amb varies expressions, una per cada condició si s'avalua certa. Exemple:
        ```Scheme
        (cond
        ((> 4 7) "major")
        ((< 4 7) "menor")
        (#t "igual")) ; Resultat: "menor"
        ```
    - **`display`** Mostra el paràmetre passat a través d'stdout Exemple:
        ```Scheme
        (display "val2: ") ; Mostra "val2: " sense cometes
        (display val2) ; Mostra el valor que tingui la variable val2
        ```
    - **`newline`** Mostra un salt de línea Exemple:
        ```Scheme
        (newline)
        ```
    - **`read`** Llegeix d'stdin Exemple:
        ```Scheme
        (var (read)) ; Llegeix un valor i l'assigna a la variable var
        ```
    - **`car`** Retorna el primer element d'una llista. Exemple:
        ```Scheme
        (car '(1 2 3 4)) ; Retorna: 1
        ```
    - **`cdr`** Retorna la cua d'una llista. Exemple:
        ```Scheme
        (cdr '(1 2 3 4)) ; Retorna: (2 3 4)
        ```
    - **`cons`** Afegeix un element al principi d'una llista. Exemple:
        ```Scheme
        (cons 0 '(1 2 3)) ; Retorna: (0 1 2 3)
        ```
    - **`null`** Comprova si una llista és buida. Exemple:
        ```Scheme
        (null? '(1 2 3)) ; Retorna: #f
        (null? '())      ; Retorna: #t
        ```
    - **`let`** Permet definir variables locals dins d'una expressió. Exemple:
        ```Scheme
        (let ((x 7)
            (y 2))
        (- x y))  ; Resultat: 5
        ```
    - **`define`** Permet definir variables globals. Exemple:
        ```Scheme
        (define x 5)                                      ;Enter
        (define b #f)                                     ;Booleà
        (define str "Pepa")                               ;String
        (define exemple '( 1 #t "Pere" '(1 2 3) '()))     ;Llista
        (define(suma-una-unitat x) (+ x 1))               ;Funcio, retorna el paràmetre rebut amb un increment d'una unitat
        ```
    - **`ID expr*`** Permet cridar una funció amb uns parametres passats com a argument. Exemple:
        ```Scheme
        (suma-una-unitat 4) ; Retorna 5, ja que és el comportamant que se li ha assignat a la funció suma una unitat al define anterior.
        ```
- `parseRead` i `parsePrint`: Mètodes auxiliars per parsejar valors de variables i llistes.

### Driver
El driver (`scheme.py`) llegeix el fitxer d’entrada amb extensió `.scm` i el converteix en un "Filestream" que s'envia al lexer `schemeLexer.py`, que transforma el codi en tokens.
Aquest format en tokens és processat pel parser (schemeParser), que crea un arbre sintàctic que posteriorment s'avalua pel fitxer que conté les funcions visitadores (`EvalVisitor.py`). Tant el  lexer com el parser usen MyErrorListener per informar sobre errors sintàctics.

## Gestió d'Errors
A l'[enunciat](https://github.com/jordi-petit/lp-mini-scheme?tab=readme-ov-file) de la pràctica es demana que es reportin els errors sintàctics, mencionant que es suposa, per senzillesa, que no es dónen mai errors semàntics, de tipus o d'execució. En aquests últims casos l'efecte del programa serà indefinit.

Com a programador, he considerat interessant controlar alguns errors per millorar la robustesa del projecte. És per això que el meu projecte té un comportament assignat en alguns dels errors semàntics, de tipus o d'execució. En cas d'error es poden ignorar aquestes excepcions, ja que aquest control dels casos innecessaris no modifica el comportament dels errors sintàctics. 

## Jocs de proves
Els jocs de proves d'aquesta pràctica consisteixen en codis font de scheme (fitxers.scm) que s'executen amb l'intèrpret. Hi ha fitxers que es poden usar per comparar la sortida amb la sortida esperada.

En cas que el programa usi el mètode `read`, cal executar :
```bash
    python3 scheme.py ./Test/test.scm < ./Tests/test.inp | diff - ./Tests/test.out
```
On el fitxer d'entrada és `test.inp`, s'executa i es compara la sortida amb `test.out`.

En cas que només disposem d'un fitxer de sortida, es pot comparar la sortida obtinguda amb la del fitxer `test.out` així:
```bash
    python3 scheme.py ./Tests/test.scm | diff - ./Tests/test.out
```
### Exemple d'ús d'un joc de proves
Si volem provar d'executar el test d'un codi que mostra els nombres de fibonacci dels naturals fins el 25 (programat a `Fibonacci.scm` ), podem executar una de les següents comandes, depenent del nostre objectiu:

Observar la sortida del programa pel terminal:
```bash
    python3 scheme.py ./Tests/Fibonacci.scm
```
Comprovar la correctesa de la sortida comparant-la amb la desitjada:
```bash
    python3 scheme.py ./Tests/Fibonacci.scm | diff - ./Tests/Fibonacci.out
```
De totes maneres, cada test té comentades les comandes a usar per executar-lo en format de comentari al fitxer `.scm`.

## A tenir en compte 
De la mateixa manera que ho implementa scheme, l'intèrpret retorna nombes en format de fracció quan aquests no són enters. És a dir:
```Scheme
    ;ús correcte
    (define x (/ 3 2)) 
    (display x) ; 3/2
    (display (+ x 1)) ; 5/2
```
En cas que el nombre es llegeixi per teclat, el codi permetrà escriure numerador/denominador. El que `No es pot fer` es:
```Scheme
    ;ús incorrecte
    (define x 3/2) 
```
Ja que he considerat que s'hauria de fer `(define x (/ 3 2))` alternativament.

## Autor i suport
En cas d'algun dubte o problema amb la instal·lació i ús del projecte, es pot contactar amb l'autor del projecte
Nil Casas Duatis  
Email: [nil.casas.duatis@estudiantat.upc.edu](mailto:nil.casas.duatis@estudiantat.upc.edu)

## GNU GENERAL PUBLIC LICENSE
Version 3, 29 de juny de 2007

Copyright (c) 2024 Nil Casas Duatis

Aquest programari és un programari lliure; pots redistribuir-lo i/o modificar-lo sota els termes de la Llicència Pública General de GNU, tal com es publica per la Free Software Foundation, ja sigui de la versió 3 de la llicència, o (segons la teva elecció) qualsevol versió posterior.

Aquest programari es distribueix amb l'esperança de ser útil, però SENSE CAP GARANTIA; ni expressa ni implícita, incloent però no limitat a les garanties implicades de COMERÇABILITAT o ADEQUACIÓ A UN FI PARTICULAR. Vegeu la Llicència Pública General de GNU per als detalls.

Pots obtenir una còpia de la Llicència Pública General de GNU a: https://www.gnu.org/licenses/gpl-3.0.html

Si modifiques aquest programari i el distribueixes, has d'incloure una declaració que indiqui que has realitzat canvis, i no pots ocultar que el programari ha estat modificat.