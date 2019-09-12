
(defclass DUCK (is-a USER)
 (slot sound)
 (slot age)
)

; 条件重复也没有问题
(defrule repeat
    ?o1 <- (object (is-a DUCK))
    ?o2 <- (object (is-a DUCK))
 =>
    (printout t "111111" crlf)
)

(make-instance [ins1] of DUCK)

(agenda)
(run)


(send [ins1] put-age 30)

(agenda)
(run)
