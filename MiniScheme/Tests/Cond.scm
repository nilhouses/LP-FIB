;Aquest test es pot executar des del directori arrel del projecte amb les comandes:

  ;SI VOLEM   COMPROVAR EL CORRECTE FUNCIONAMENT DE LA GRAMÀTICA
    ;python3 scheme.py ./Tests/Cond.scm | diff - ./Tests/Cond.out

  ;SI VOLEM VEURE LA SORTIDA PER PANTALLA
    ;python3 scheme.py ./Tests/Cond.scm


(define x 3)
(define y 5)
(define true #t)

(define (main)
  (display "Comprovem que un cond funcioni correctament en 3 casos")
  (display "3 es ___ que 5: ")
  (newline)
  (display
      (cond
        ((> 3 5) "major")
        (true "menor")
        (#t "igual"))
    )
  (newline)
  (display
    (cond
      ((> 3 5) "major")
      ((= 3 5) "igual")
      (else "menor"))
  )
  (newline)
  (display
      (cond
        ((< x y) "menor")
        ((= x y) "igual")
        (true "major"))
    )
  (newline)
)
