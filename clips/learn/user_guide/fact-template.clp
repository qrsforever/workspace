
(deftemplate rule
 (slot ID)
)

(defrule r1
  (rule (ID rul-001))
 =>
  (printout t "rul-001" crlf)
)

(assert (rule (ID rul-001)))

(facts)
(agenda)
(run)
(assert (rule (ID rul-001)))
(bind ?fs (facts))
(printout t "####" ?fs crlf)
(agenda)
(run)

(defrule r2
  (r2)
 =>
  (bind ?f (nth$ 1 (find-fact ((?ru rule)) (neq ?ru:ID nil))))
  (if (neq ?f nil)
   then
    (bind ?id (fact-slot-value ?f ID))
    (printout t "#####" ?id crlf)
  )
)

(assert (r2))
(agenda)
(run)



(exit)

