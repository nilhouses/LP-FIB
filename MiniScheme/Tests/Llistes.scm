; Test bàsic de llistes i les seves funcions bàsiques (A Read.scm hi ha més operacions amb llistes)

;Es pot executar des del directori arrel del projecte amb les comandes:

  ;SI VOLEM COMPROVAR EL CORRECTE FUNCIONAMENT DE LA GRAMÀTICA
    ;python3 scheme.py ./Tests/Llistes.scm | diff - ./Tests/Llistes.out

  ;SI VOLEM ESCRIURE I LLEGIR PEL NOSTRE COMPTE
    ;python3 scheme.py ./Tests/Llistes.scm


(define l '("pepa" 1 #f))
(define x (+ 5 4))


(define (main)
  (display "l: ")
  (display l)
  (newline)

  (display "Primer element: ")
  (display (car l))
  (newline)

  (display "Resta dels elements: ")
  (display (cdr l))
  (newline)

  (display "Element x ")
  (display x)
  (newline)

  (display "Afegim l'element x davant de la llista l: ")
  (display (cons x l))
  (newline)

  (display "Creem la llista '(1,2,3) a partir de cons annidats: ")
  (display (cons 1 (cons 2 (cons 3 '()))))
  (newline)

  (display "La llista l es buida? ")
  (display (if (null? l)
            "si"
            "no"
           ))(newline)
  
  (display "La llista '() es buida? ")
  (display (if (null? '())
            "si"
            "no"
           ))(newline)
)

