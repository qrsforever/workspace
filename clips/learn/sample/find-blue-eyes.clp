; clips -f find-blue-eyes.clp

(deftemplate person
    (slot name)
    (slot eyes)
    (slot hair)
)

(deffacts people
    (person (name jane) (eyes blue) (hair red))
    (person (name jack) (eyes blue) (hair black))
)

(defrule find-blue-eyes
    (person (name ?name) (eyes blue))
  =>
    (printout t ?name "has blue eyes." crlf)
)
(reset)
(run)
(facts)

;===================================================================
; Variable is very important
;===================================================================

(deftemplate find (slot eyes))

(defrule find-eyes
    (find (eyes ?eyes))
    (person (name ?name) (eyes ?eyes))
  =>
    (printout t ?name "has blue eyes." crlf)
)

(reset)
(assert (find (eyes blue)))
(facts)
(agenda)
(run)

(exit)
