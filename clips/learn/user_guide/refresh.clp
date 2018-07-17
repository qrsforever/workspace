
(clear)
(defclass Duck (is-a USER)
 (slot ID)
)

(defrule test-refresh
 (object (is-a Duck) (ID ?ID &:(eq ?ID aaa)))
=>
 (printout t "refresh ok" crlf)
)

; (make-instance d1 of Duck (ID bbb))
(make-instance d1 of Duck (ID aaa))

(agenda)
(run)

(refresh test-refresh)
(agenda)
(run)

(exit)
