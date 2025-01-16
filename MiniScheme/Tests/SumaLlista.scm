;Aquest test es pot executar des del directori arrel del projecte amb les comandes:

  ;SI VOLEM COMPROVAR EL CORRECTE FUNCIONAMENT DE LA GRAMÀTICA
    ;python3 scheme.py ./Tests/SumaLlista.scm | diff - ./Tests/SumaLlista.out

  ;SI VOLEM VEURE LA SORTIDA PER PANTALLA
    ;python3 scheme.py ./Tests/SumaLlista.scm

;Consisteix en mostrar per pantalla la suma dels nombres de la llista l

(define l '(1 2 3 4 5 6 7 8 9 10))

(define (suma-llista llista)
  (if (null? llista)
      0
      (+ (car llista) (suma-llista (cdr llista)))))


(define (main)
  (display "l: ")
  (display l)
  (newline)

  (display "Suma dels elements d'l: ")
  (display (suma-llista l))
  (newline)
)

