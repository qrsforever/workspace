; clips -f process-moved-infomation.clp

;===================================================================
; Address of Factor
;===================================================================

(deftemplate person
    (slot name)
    (slot address)
)


(deftemplate moved
    (slot name)
    (slot address)
)

(defrule process-moved-information
    ?f1 <- (moved (name ?name) (address ?address))
    ?f2 <- (person (name ?name))
  => 
    (retract ?f1)
    (modify ?f2 (address ?address))
)

(deffacts example
    (person (name "john hill") (address "25 mulberry lane"))
    (moved (name "john hill") (address "37 cherry lane"))
)

(reset)
(facts)
(run)
(facts)

(exit)
