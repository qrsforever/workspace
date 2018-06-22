
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

(deftemplate datetime
    (slot year (type INTEGER))
    (slot month (type INTEGER))
    (slot day (type INTEGER))
    (slot hour (type INTEGER))
    (slot minute (type INTEGER))
    (slot second (type INTEGER))
)

(defrule test2
    ?f <- (datetime 
            (year ?year &:(= ?year 2018))
            (month ?month &:(> ?month 7))
            (minute ?minute &:(= ?minute 22))
        )
 =>
    (printout t "okkkkkkkko" crlf)
)

(assert (datetime (year 2018) (month 8) (minute 22)))

(agenda)
(run)

(exit)
