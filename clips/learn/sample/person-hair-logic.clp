; clips -f person-hair-logic.clp

;===================================================================
; Field constraint (~ | &)
;===================================================================

(deftemplate person
    (slot name)
    (slot eyes)
    (slot hair)
)

(deffacts people
    (person (name jane) (eyes blue) (hair red))
    (person (name jack) (eyes blue) (hair black))
    (person (name dong) (eyes blue) (hair brown))
)

;===================================================================
; ~
;===================================================================

(defrule person-without-brown-hair
    (person (name ?name) (hair ~brown))
  =>
    (printout t ?name " does not have brown hair" crlf)
)


;===================================================================
; |
;===================================================================

(defrule black-or-brown-hair
    (person (name ?name) (hair brown | black))
  =>
    (printout t ?name " does not have brown or black hair" crlf)
)

;===================================================================
; & ?????
;===================================================================

(defrule back-and-brown-hair
    (person (name ?name) (hair ?color&brown|black))
  =>
    (printout t ?name " has " ?color " hair" crlf)
)

(reset)
(facts)
(run)
(exit)

