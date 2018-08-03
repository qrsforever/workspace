(defclass DUCK (is-a USER)
 (slot sound)
)

(defrule put-sound-value
   (object (is-a DUCK)
       (sound ?s))
 =>
   (printout t "---> " ?s crlf)
)

(make-instance [d1] of DUCK)

(send [d1] put-sound aa)

(agenda)
(run)

(send [d1] get-sound)
(send [d1] put-sound aa)

(agenda)
(run)

(exit)

