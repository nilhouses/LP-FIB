;Aquest test es pot executar des del directori arrel del projecte amb les comandes:

  ;SI VOLEM   COMPROVAR EL CORRECTE FUNCIONAMENT DE LA GRAMÀTICA
    ;python3 scheme.py ./Tests/Let.scm | diff - ./Tests/Let.out

  ;SI VOLEM VEURE LA SORTIDA PER PANTALLA
    ;python3 scheme.py ./Tests/Let.scm

(define x 5)

  (display "Primer test: Comprova la no-col·lisio d'una variable definida al let amb una altra global (x)")
  (newline)
  (newline)
  ;Consulta variable global
  (display "Valor inicial de la constant x: ")
  (display x)
  (newline)
  
  ;Locals
  (display "LLISTA: ")
  (display
    (let (
        (x (+ 5 3))    ; x = 8
        (y (+ x 2)))   ; y = 8 + 2
    (display '(x y)))  ; Resultat: ( 8 10 )
  )
  (newline)

  ;Comprovem que la variable global es mantingui igual
  (display "La variable global x: ")
  (display x)
  (display " conserva el seu valor")
  (newline)
  (newline)

  (display "Segon test: comprova el correcte funcionament de variables globals i locals en lets superposats")
  (newline)
  (newline)
  (display "x LOCAL primera prova: ")
  (display
      (let (
          (x 10))  ; let extern
          (let ((x (+ 10 x)))  ; let intern que redefineix x = 10 + 10 = 20
              (+ x 5)) ; retorna x + 5 = 20 + 5
      ) 
  )
  (newline)

  ; un sol let 
  (display "x LOCAL segona prova: ")
  (display
  (let (
      (x (+ 5 3))) ; 
      x)  
  )
  (newline)
  (display "La variable global x: ")
  (display x)
  (display " conserva el seu valor")
  (newline)
