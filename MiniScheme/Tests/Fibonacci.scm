;Aquest test es pot executar des del directori arrel del projecte amb les comandes:

  ;SI VOLEM COMPROVAR EL CORRECTE FUNCIONAMENT DE LA GRAMÀTICA
    ;python3 scheme.py ./Tests/Fibonacci.scm | diff - ./Tests/Fibonacci.out

  ;SI VOLEM VEURE LA SORTIDA PER PANTALLA
    ;python3 scheme.py ./Tests/Fibonacci.scm

;Consisteix en mostrar per pantalla els nombres de la seqüència de fibonacci (fins al nombre 25) 
(define n '( 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25))

(define (fib n)
  (if (= n 0)
      0
      (if (= n 1)
          1
          (+ (fib (- n 1)) (fib (- n 2)))
      )
  )
)

(define (imprimeix-fib llista)
  (if (null? llista)
      '()
      (let ((fib-n (fib (car llista)))) ; Fib del primer element
        (display fib-n) ; mostra'l
        (newline)
        (imprimeix-fib (cdr llista))))) ; Continua

(imprimeix-fib n)