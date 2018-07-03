
(defrule or-test
    (or
        (and
            ?a <- (message a)
            ?b <- (message b)
        )
        ?c <- (message c)
    )
 =>
    ; error not define ?c
    (printout t "---------" ?c crlf)
)

(assert (message c))
; (assert (message a))
; (assert (message b))


(agenda)
(run)

(exit)
