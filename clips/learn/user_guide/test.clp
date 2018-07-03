
(defclass Device (is-a USER)
    (slot a (type INTEGER))
    (slot b (type INTEGER))
)

(defrule test-or
    (or
        (and
         ?f <- (mytest 1)
         ?obj <- (object (is-a Device) (a ?a &:(> ?a 10)))
         ; (test (bind ?res TRUE))
        )
        (and
         ?f <- (mytest 2)
         ?obj <- (object (is-a Device) (b ?b &:(< ?b 10)))
         ; (test (bind ?res FALSE))
        )
    )
 =>
    ; res error
    ; (printout t "obj:" ?obj " fact:" ?f " res " ?res crlf)
    (printout t "obj:" ?obj " fact:" ?f crlf)
)

(make-instance d1 of Device (a 12))
(make-instance d2 of Device (b 1))
(assert (mytest 1))

(instances)
(agenda)
(run)

(defclass Context (is-a USER)
    (slot a (type INTEGER))
)

; Rule Context
(defclass RuleContext (is-a Context)
 (role concrete)
 (slot rule-id (type STRING))
 (slot timeout-ms (type INTEGER) (default 5000))
 (slot start-time (type INTEGER) (default 1111))
 (slot act-all-count (type INTEGER) (access initialize-only))
 (slot success-count (type INTEGER) (default 0))
)

(defrule check-rule-response
    ?obj <- (object (is-a RuleContext) (rule-id ?rule-id))
 =>
)


(exit)
