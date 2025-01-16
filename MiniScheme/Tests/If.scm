;Aquest test es pot executar des del directori arrel del projecte amb les comandes=

  ;SI VOLEM   COMPROVAR EL CORRECTE FUNCIONAMENT DE LA GRAMÀTICA
    ;python3 scheme.py ./Tests/If.scm | diff - ./Tests/If.out

  ;SI VOLEM VEURE LA SORTIDA PER PANTALLA
    ;python3 scheme.py ./Tests/If.scm


(define x #t)
(define y #f)

(define (main)
  (display "x: ") (display x)(newline)

  (display "y: ") (display y)(newline)

  ;Sortida esperada Cert!
  (display "or x y: ")
    (display
      (if (or x y)
      "Cert!"     
      "Fals"))
    (newline)

  ;Sortida esperada Fals
  (display "and x y: ")
    (display
      (if (and x y)
      "Cert!"
      "Fals"))  
    (newline)

  ;Sortida esperada Fals
  (display "not x: ")
    (display
      (if (not x)
      "Cert!"
      "Fals"))
    (newline)
    
  ;Sortida esperada Cert!
  (display "not y: ")
    (display
      (if (not y)
      "Cert!"
      "Fals"))
    (newline)
)
