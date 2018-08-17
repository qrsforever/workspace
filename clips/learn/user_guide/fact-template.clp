
(deftemplate rule
 (slot ID (default none))
)

(defrule r1
  (rule (ID rul-001))
 =>
  (printout t "rul-001" crlf)
)

(assert (rule))
(facts)

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


(deftemplate foo (slot bar) (multislot yak))

(defrule r3
    ?f <- (foo (bar ?bar) (yak $?yak)) 
    ; ?f <- (foo) 
 =>
    (printout t "foo here" crlf)
    (printout t "names: " (fact-slot-names ?f) crlf)
    (printout t "slot value: " (fact-slot-value ?f yak) crlf)
    (printout t "slot insert1: " (insert$ $?yak 1 x) crlf)
    (bind ?v1 (fact-slot-value ?f yak))
    (printout t "slot insert2: " (insert$ ?v1 1 x) crlf)
    (bind ?v2 (insert$ ?v1 1 x))
    (printout t "member x index: " (member$ x ?v2) crlf)
    (printout t "member x index: " (member$ x ?yak) crlf)
    (printout t "slot delete: " (delete$ ?v2 1 1) crlf)

)
(assert (foo (bar 1)))
; (fact-slot-value 4 yak)
(agenda)
(run)

(modify 4 (yak (insert$ (create$ ) 1 x)))
(facts)

; not modify fact-index
(modify 4 (bar 2))
(facts)
(modify 4 (bar 5))
(facts)
(modify 4 (bar 6))
(facts)
(modify 4 (bar 7))
(facts)


(exit)

