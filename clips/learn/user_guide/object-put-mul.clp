
(defclass BASE (is-a USER)
)

(defmessage-handler BASE putData (?slot ?value)
    (bind ?old (nth$ 1 (dynamic-get ?slot)))
    (dynamic-put ?slot ?value ?old)
)

(defmessage-handler BASE getData (?slot)
    (return (nth$ 1 (dynamic-get ?slot)))
)

(defclass DUCK (is-a BASE)
     (multislot sound (type NUMBER) (visibility public) (cardinality 2 2))
)


(defrule put-sound-value
   (object (is-a DUCK)
       (sound ?new ?old &:(neq ?new ?old)))
 =>
   (printout t "---> " ?new "  " ?old crlf)
)

(make-instance [d1] of DUCK)

; (send [d1] putData sound 33)
(send [d1] get-sound)
(send [d1] getData sound)

(send [d1] put-sound 11 22)

(agenda)
(run)

(send [d1] get-sound)
(send [d1] put-sound 11 22)

(agenda)
(run)

(agenda)
(run)

(send [d1] putData sound 44)
(send [d1] getData sound)

(agenda)
(run)

(send [d1] putData sound 44)
(send [d1] getData sound)

(agenda)
(run)


(exit)
