; TEST INTERACTIU!!!

  ;Més entretingut que els altres


;Aquest test es pot executar des del directori arrel del projecte amb les comandes:

  ;SI VOLEM COMPROVAR EL CORRECTE FUNCIONAMENT DE LA GRAMÀTICA
    ;python3 scheme.py ./Tests/Read.scm < ./Tests/Read.inp | diff - ./Tests/Read.out

  ;SI VOLEM VEURE LA SORTIDA PER PANTALLA
    ;python3 scheme.py ./Tests/Read.scm < ./Tests/Read.inp

  ;SI VOLEM ESCRIURE I LLEGIR PEL NOSTRE COMPTE
    ;python3 scheme.py ./Tests/Read.scm

;Enters
(define (sumar-dos-valors)
  (display "Introdueix dos valors enters (nombre 1 'intro' nombre 2): ")
  (let ((int1 (read))
        (int2 (read)))
     (display "La suma és: ")
     (display (+ int1 int2))
     (newline)
  )
)

;Booleans
(define (llegeix-dos-bools)
  (display "Introdueix dos valors booleans separats (bool 'intro' bool): ")
  (let ((bool1 (read))
        (bool2 (read)))
      (if (and bool1 #t)
            (display "primer bool Cert!")
            (display "primer bool Fals :("))
      (newline)
      (if (bool2)
            (display "segon bool Cert!")
            (display "segon bool Fals :("))
      (newline)
  )
)

;String
(define (llegeix-string)
  (display "Introdueix una cadena de text: ")
  (let ((s1 (read)))
     (display "Cadena: ")
     (display s1)
     (newline)
  )
)

;Llista Enters
(define (sumar-llista lst)
  (if (null? lst)         
      0                   
      (+ (car lst)        
         (sumar-llista (cdr lst)))
  )
) 

(sumar-dos-valors)
(llegeix-dos-bools)
(llegeix-string)

(display "Introdueix una llista d'enters: ")
(let ((llista (read))
      (suma (sumar-llista llista)))
      (display "La suma de la llista ")
      (display llista)
      (display " es: ")
      (display suma)
      (newline)
)
