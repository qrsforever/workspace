(deftemplate sos
  (slot arg1 (type INTEGER))
)

(defrule lhs-cal
    (timedate ?td)
    (sos (arg1 ?a1 &:(> ?a1 (+ ?td 1))))
 =>
    (printout t "-->" ?a1 crlf)
)

(assert (timedate 5))
(assert (sos (arg1 10)))

(agenda)
(run)

(exit)
