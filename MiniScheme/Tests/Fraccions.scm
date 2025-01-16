
    ; TEST INTERACTIU!!! (llegeix de fitxer)
    
;Aquest test es pot executar des del directori arrel del projecte amb les comandes:

  ;SI VOLEM COMPROVAR EL CORRECTE FUNCIONAMENT DE LA GRAMÀTICA
    ;python3 scheme.py ./Tests/Fraccions.scm < ./Tests/Fraccions.inp | diff - ./Tests/Fraccions.out

  ;SI VOLEM VEURE LA SORTIDA PER PANTALLA
    ;python3 scheme.py ./Tests/Fraccions.scm < ./Tests/Fraccions.inp

  ;SI VOLEM ESCRIURE I LLEGIR PEL NOSTRE COMPTE
    ;python3 scheme.py ./Tests/Fraccions.scm


(define x (/ 3 2) )
(display "VARIABLE DEL CODI x = ")
(display x)
(newline)   
(display "x + 1/2 = ")
(display (+ x (/ 1 2))) ; 4/2 = 2
(newline)   
(display "x + 1 = ")
(display (+ x 1)) ; 5/2
(newline)

;Veiem que es puguin llegir fraccions
(define y (read))
(display "VARIABLE D'STDIN y = ")
(display y)
(newline)   
(display "y + 1/2 = ")
(display (+ y (/ 1 2))) ; 4/2 = 2
(newline)   
(display "y + 1 = ")
(display (+ y 1)) ; 5/2
(newline)