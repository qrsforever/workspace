
(deftemplate micro-service
    (slot name)
    (slot state)
)

(defrule _sos-micro-service-start
    ?f <- (start-service ?name ?state)
  =>
    (retract ?f)
    ; (printout t (get-deftemplate-list) crlf)
    ; (bind ?service (deftemplate-module ?name))
    ; (printout t "--->" ?service crlf)
    ; (printout t (find-fact ((?sn ?name)) TRUE) crlf)
    (bind ?ms (nth$ 1 (find-fact ((?sn micro-service)) (and (eq ?sn:name ?name) (neq ?sn:state start)))))
    (if (neq ?ms nil)
     then
        ; (printout t "1---->" ?ms:name crlf) ; error using: (fact-slot-value ?ms name)
        (printout t "2---->" ?name crlf)
        (modify ?ms (state ?state))
        (facts)
    )
)

(assert (micro-service (name sos) (state start)))

(assert (start-service sos start))

(agenda)
(run)

(facts)

(exit)
