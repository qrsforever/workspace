; sample test

(clear)
(defclass DUCK (is-a USER)
    (slot age (default 1))
    (multislot sound (default quack quack))
)

(defrule find-sound
    ?duck <- (object
        (is-a DUCK)
        (sound $?find))
  =>
    (printout t "Duck " (instance-name ?duck) " says " ?find crlf)
)

(defrule find-dorky-sound
    (object
        (is-a DUCK)
        (sound $?find)
        (name [Dorky_Duck]))
    =>
    (printout t "[Dorky_Duck] sound" crlf)
)

(make-instance [Dorky_Duck] of DUCK)
(make-instance [Dinky_Duck] of DUCK)

(instances)

(agenda)
(run)

(defrule find-age-over-10
    ?duck <- (object
        (is-a DUCK)
        (age ?age &:(> ?age 10)))
  =>
    (printout t "Duck-1 " (instance-name ?duck) " age " ?age crlf)
)

(defrule find-age-over-20-or-below-10
    ?duck <- (object
        (is-a DUCK)
        (age ?age &:(> ?age 20)|:(< ?age 10)))
  =>
    (printout t "Duck-2 " (instance-name ?duck) " age " ?age crlf)
)

(defrule find-age-over-10-and-below-20
    ?duck <- (object
        (is-a DUCK)
        (age ?age &:(> ?age 10)&:(< ?age 20)))
  =>
    (printout t "Duck-3 " (instance-name ?duck) " age " ?age crlf)
)

(defrule find-name-is-unkown-or-name-is-dinky
    (or
        (object
            (is-a DUCK)
            (age 30)
        )

        (object
            (is-a DUCK)
            (name [Dinky_Duck])
        )
    )
    ?f <- (make-again 1)
  =>
    (retract ?f)
    (printout t "Duck-3 " crlf)
)

; (send [Dinky_Duck] put-age 30)
; (assert (make-again 1))
; (send [Dinky_Duck] print)
;
(instances)

(send [Dinky_Duck] print)
(send [Dorky_Duck] print)
(send [Dinky_Duck] put-age 25)
(send [Dinky_Duck] put-age 15)
(agenda)
(run)

; (agenda)
; (run)
; (agenda)
;
; (assert (make-again 1))
; (facts)
; (instances)
; (agenda)

(exit)
