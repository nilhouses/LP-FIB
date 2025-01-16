;Aquest test es pot executar des del directori arrel del projecte amb les comandes:

  ;SI VOLEM COMPROVAR EL CORRECTE FUNCIONAMENT DE LA GRAMÀTICA
    ;python3 scheme.py ./Tests/Factorial.scm | diff - ./Tests/Factorial.out

  ;SI VOLEM VEURE LA SORTIDA PER PANTALLA
    ;python3 scheme.py ./Tests/Factorial.scm

;Consisteix en mostrar per pantalla el factorial dels nombres de l'intèrval [0,25]
 
(define n '( 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25))

(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))

(define (imprimeix-fact llista)
  (if (null? llista)
      '()
      (let ((fact-n (factorial (car llista)))) ; Fib del primer element
        (display fact-n) ; mostra'l
        (newline)
        (imprimeix-fact (cdr llista))))) ; Continua

(imprimeix-fact n)



