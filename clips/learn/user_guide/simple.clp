
; if argument is key word, that's ok
(bind ?eqsym eq)
(printout t "equal sym: " ?eqsym crlf)

;
(defglobal
    ?*TEST_CASE* = TRUE
)

; test global variable can be used in if statement directly
(if ?*TEST_CASE*
; (if (eq ?*TEST_CASE* TRUE)
 then
    (printout t "TEST_CASE start..." crlf)
 else
    (printout t "TEST_CASE not start..." crlf)
)

(bind ?b (create$ aa bb ccc))
(printout t (expand$ ?b) crlf)


(exit)
