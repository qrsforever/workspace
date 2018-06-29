

(defrule test-time
    ?time <- (time ?year ?month ?day ?hour ?min ?sec)
    (and
        (test (= ?year 2018))
        (test (and (> ?month 0) (<= ?month 12)))
        (test (or (= ?day 11) (= ?day 13) (= ?day 15)))
        (test (= ?hour 0))
        (test (= ?min 0))
        (test (= ?sec 0))
    )
    ; (test (and (= ?year 2018) (= ?month 06)))
=>
    (printout t "time is " ?year "/" ?month "/" ?day " " ?hour ":" ?min ":" ?sec crlf)
)

; not ok
(assert (time 2018 06 20 13 30 0))
(agenda)
(run)

; ok
(assert (time 2018 06 13 0 0 0))
(agenda)
(run)

; not ok
(assert (time 2017 06 13 0 0 0))
(agenda)
(run)

(agenda)
(run)
(exit)
