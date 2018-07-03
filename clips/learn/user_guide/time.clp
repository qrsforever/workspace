
; 如果是or, 此场景必须套个and, 否则提示?Y未定义
(defrule test
    (or (and
         ?f <- (time ?Y ?M ?D ?h ?m ?s)
         (test (= ?Y 2018))
        )
    )
  =>
    (printout t ?Y "/" ?M "/" ?D " " ?h ":" ?m ":" ?s crlf)
)

(assert (time 2018 06 20 21 55 00))

(agenda)
(run)

(deffunction create-clock()
    (return (time))
)

(deftemplate datetime
    (slot year (type INTEGER))
    (slot month (type INTEGER))
    (slot day (type INTEGER))
    (slot hour (type INTEGER))
    (slot minute (type INTEGER))
    (slot second (type INTEGER))
    (slot clock (type INTEGER) (default-dynamic (create-clock)))
)

(defrule test2
    (declare (salience 200))
    ?f <- (datetime
            (year ?year &:(= ?year 2018))
            (month ?month &:(> ?month 7))
            (minute ?minute &:(= ?minute 22))
        )
 =>
    (retract ?f)
    (printout t "okkkkkkkko" crlf)
)

(defrule test3
    (declare (salience -200))
    ?f <- (datetime (month ?month &:(= ?month 8)))
  =>
    (retract ?f)
    (printout t "--->found " ?f crlf)
)

(assert (datetime (year 2018) (month 8) (minute 22)))
; not retract
(assert (datetime (year 2019) (month 8) (minute 22)))
(assert (datetime (year 2021) (month 8) (minute 22)))
(assert (datetime (year 2022) (month 8) (minute 22)))
(assert (datetime (year 2023) (month 8) (minute 22)))

(facts)

(agenda)
(run)

(facts)
(exit)
