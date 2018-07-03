
(deffunction mytest (?arg)
    (switch ?arg
        (case 1
         then
            (printout t "case run" crlf)
        )
        (default
            (printout t "case defaut run" crlf)
            (return)
        )
        ; error
        ; (printout t "case end" crlf)
    )
    ; ok
    (printout t "switch end" crlf)
)

(mytest 1)

(exit)
