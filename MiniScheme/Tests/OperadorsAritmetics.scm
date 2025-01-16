;Aquest test es pot executar des del directori arrel del projecte amb les comandes:

  ;SI VOLEM   COMPROVAR EL CORRECTE FUNCIONAMENT DE LA GRAMÀTICA
    ;python3 scheme.py ./Tests/OperadorsAritmetics.scm | diff - ./Tests/OperadorsAritmetics.out

  ;SI VOLEM VEURE LA SORTIDA PER PANTALLA
    ;python3 scheme.py ./Tests/OperadorsAritmetics.scm

(define x 0)
(define y (/ 3 2))

;Suma amb resultat positiu
  (display "x + 3 = ") ; 0 + 3 = 3 
  (display (+ x 3))
  (newline)

;Suma amb resultat negatiu
  (display "2 - 33 = ") ; 2 - 33 = - 31 
  (display (+ 2 -33))
  (newline)

;Resta amb resultat positiu
  (display "x - 3 = ") ; 0 - 3 = -3 
  (display (- x 3))
  (newline)

;Resta amb resultat negatiu
  (display "3 - 0 = ") ; 3 - 0 = 3 
  (display (- 3 x))
  (newline)

;Multiplicacio
  (display "2 * 3 = ") ; 2 * 3 = 6 
  (display (* 2 3))
  (newline)

;Divisió entera
  (display "8 / 2 = ") ; 8 / 2 = 4 
  (display (/ 8 2))
  (newline)

;Divisions amb residu
  (display "3 / 2 = ")
  (display (/ 3 2)) ; 3/2 Format fraccionari
  (newline)
  (display "y = ")
  (display y);1
  (newline)

;Mòdul
  (display "3 % 2 = ")  ; 3 % 2 = 1
  (display (mod 3 2))
  (newline)

;Operacions combinades
  (display "(+ (* 2 3) 5) = ")
  (display (+ (* 2 3) 5)) ; 11
  (newline)

