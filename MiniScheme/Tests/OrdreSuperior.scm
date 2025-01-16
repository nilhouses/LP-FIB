;Aquest test es pot executar des del directori arrel del projecte amb les comandes:

  ;SI VOLEM COMPROVAR EL CORRECTE FUNCIONAMENT DE LA GRAMÀTICA
    ;python3 scheme.py ./Tests/OrdreSuperior.scm | diff - ./Tests/OrdreSuperior.out

  ;SI VOLEM VEURE LA SORTIDA PER PANTALLA
    ;python3 scheme.py ./Tests/OrdreSuperior.scm

;Consisteix en mostrar per pantalla la suma dels nombres de la llista l

(define l '( 1 2 3 4 5 6 7 8 9 10))

;FUNCIONS AUXILIARS
(define (dobla x) (* x 2))
(define (parell? x) (= (mod x 2) 0))

;1)FUNCIÓ ORDRE SUPERIOR 1 (APLICA-DOS-COPS)
  
  (define (aplica-dos-cops f x)
      (f (f x)))

  ;ÚS
  (display "aplica-dos-cops dobla 50 = ")
  (display (aplica-dos-cops dobla 50))
  (newline)

;2)FUNCIÓ ORDRE SUPERIOR 2 (MAP)

  (define (map func llista)
    (cond
      ((null? llista) '())
      (else (cons (func (car llista)) (map func (cdr llista))))))

  ;ÚS
  (display "map dobla '( 1 2 3 4 5 6 7 8 9 10) = ")
  (display (map dobla l))  ; Retorna (2 4 6 8)
  (newline)

;3)FUNCIÓ ORDRE SUPERIOR 3 (FILTER)

  (define (filter predicat llista)
    (cond
      ((null? llista) '())  ;
      ((predicat (car llista))
      (cons (car llista) (filter predicat (cdr llista))))
      (#t (filter predicat (cdr llista)))))  


  ;ÚS
  (display "Filtrem els elements parells de la llista '(-4 -3 -2 -1 0 1 2 3 4) = ")
  (display (filter parell? '(-4 -3 -2 -1 0 1 2 3 4)))  ; Retorna (2 4)
  (newline)