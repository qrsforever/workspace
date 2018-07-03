
(deffunction test(?a ?b ?c)
    ; (return (str-cat ?a ?b ?c))
    ; (if FALSE
    (if TRUE
     then
        (return "(defrule ruleid \
        ?f <- (init) \
         => \
         (retract ?f) \
         (printout t \"1111\" crlf)\
        )")
     else
        (return FALSE)
    )
)

(bind ?gen-rule (test a b cd))
(printout t ?gen-rule crlf)
(build ?gen-rule)

(assert (init))

(agenda)
(run)

(exit)

