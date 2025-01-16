;Aquest test es pot executar des del directori arrel del projecte amb les comandes:

  ;SI VOLEM COMPROVAR EL CORRECTE FUNCIONAMENT DE LA GRAMÀTICA
    ;python3 scheme.py ./Tests/DefineVariables.scm | diff - ./Tests/DefineVariables.out

  ;SI VOLEM VEURE LA SORTIDA PER PANTALLA
    ;python3 scheme.py ./Tests/DefineVariables.scm

(define x (+ 1 3)) ; 4
(define y (mod 18 6)) ; 0
(define s1 "pepa")
(define s2 "josep")
(define b1 #t)
(define b2 (> 1 2)) ;Valor esperat #f
(define b3 (not b1)) ;Valor esperat #f

(define (main) 
;Enters
  (display "x té valor: ")
  (display x) 
  (newline)
  (display "y té valor: ")
  (display y) 
  (newline)ç
;String
  (display "s1 té valor: ") ; pepa
  (display s1) 
  (newline)
  (display "s2 té valor: ") ; josep
  (display s2) 
  (newline)
;Booleans
  (display "b1 té valor: ")
  (display b1) ;#t
  (newline)
  (display "b2 té valor: ")
  (display b2) ;#f
  (newline)
  (display "b3 té valor: ")
  (display b3) ;#f 
  (newline)


)
