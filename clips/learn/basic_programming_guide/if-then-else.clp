; clips -f if-then-else.clp

(defrule closed-valves
    (temp high)
    (valve ?v closed)
 =>
    (if (= ?v 6)
        then
            (printout t "The special valve " ?v " is closed!" crlf)
            (assert (perform special operation))
        else
            (printout t "Valve " ?v " is normally closed" crlf)
    )
)

; (defrule closed-valves-number-6
;     (temp high)
;     (valve 6 closed)
;  =>
;     (printout t "The special valve " ?v " is closed!" crlf)
;     (assert (perform special operation))
; )

; (defrule closed-valves-number-not-6
;     (temp high)
;     (valve ?v&~6 closed)
;  =>
;     (assert (perform special operation))
; )

(watch all)

(assert (temp high))
(assert (valve 6 closed))

(facts)
(agenda)
(run)

(assert (temp high))
(assert (valve 7 closed))

(facts)
(agenda)
(run)

(exit)

