;Aquest test es pot executar des del directori arrel del projecte amb les comandes:

  ;SI VOLEM   COMPROVAR EL CORRECTE FUNCIONAMENT DE LA GRAMÀTICA
    ;python3 scheme.py ./Tests/OperadorsBool.scm | diff - ./Tests/OperadorsBool.out

  ;SI VOLEM VEURE LA SORTIDA PER PANTALLA
    ;python3 scheme.py ./Tests/OperadorsBool.scm

(define fals #f)

(define (main)
;NOT
    (display "NOT #t: ")
    (display (not (> 3 2))) ; not #t : #f 
    (newline)
    (display "NOT #f: ")
    (display (not (< 3 2))) ; not #f : #t 
    (newline)
;AND
    (display "AND #t #t: ")
    (display (and (> 3 2) (< 5 10)) ) ; and #t #t : #t
    (newline)
    (display "AND #f #t: ")
    (display (and (< 3 2) (< 5 10)) ) ; and #f #t : #f
    (newline)
    (display "AND #t #f: ")
    (display (and (<> 3 2) (> 5 10)) ) ; and #t #f : #f
    (newline)
;OR
    (display "OR #t #t: ")
    (display(or (>= 3 2) #t)) ; or #t #t : #t
    (newline)
    (display "OR #t #f: ")
    (display(or #t fals)) ; or #t #f : #t
    (newline)
    (display "OR #f #f: ")
    (display(or (<= 3 2) (= 1 0))) ; or #f #f : #f
    (newline)
;=
    (display "#t = #t: ")
    (display(= #t (> 3 2))) ; = #t #t : #t
    (newline)
    (display "#f = #f: ")
    (display(= #f (< 3 2))) ; = #f #f : #t
    (newline)
    (display "#f = #t: ")
    (display(= fals (> 3 2))) ; = #f #t : #f
    (newline)
    (display "#t = #f: ")
    (display(= #t (= 3 2))) ; = #t #f : #f
    (newline)
; <>
    (display "#t <> #t: ")
    (display(<> #t (> 3 2))) ; <> #t #t : #f
    (newline)
    (display "#f <> #f: ")
    (display(<> #f (< 3 2))) ; <> #f #f : #f
    (newline)
    (display "#f <> #t: ")
    (display(<> fals (> 3 2))) ; <> #f #t : #t
    (newline)
    (display "#t <> #f: ")
    (display(<> #t (= 3 2))) ; <> #t #f : #t
    (newline)
)