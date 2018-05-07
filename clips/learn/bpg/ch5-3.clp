; predicate constraints

(clear)

(deftemplate person
 (slot name)
 (multislot attrs)
)

(defrule not-tall
 (person (attrs $?a&~: (member$ tall ?a)))
 =>
)

(assert 
 (person (name John) (attrs tall thin)); f-1
 (person (name Greg) (attrs short stout)) ; f-2
 (person (name Jill) (attrs young tall)) ; f-3
)

(agenda)


(exit)
