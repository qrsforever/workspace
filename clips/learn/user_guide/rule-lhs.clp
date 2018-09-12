(deftemplate sos
  (slot arg1 (type INTEGER))
  (slot arg2 (type INTEGER))
)

(defrule lhs-cal
    (timedate ?td)
    (sos (arg1 ?a1 &:(> ?a1 (+ ?td 1))))
 =>
    (printout t "-->" ?a1 crlf)
)

(assert (timedate 5))
(assert (sos (arg1 10)))
; not trigger
; (assert (sos (arg2 10)))

(agenda)
(run)

(defclass message (is-a USER)
    (slot arg1 (type INTEGER))
    (slot arg2 (type INTEGER))
)

(defrule message-one-slot
    ?ins <- (object
        (is-a message)
        (arg1 ?a1)
        )
 =>
    (printout t "-->" ?a1 crlf)
)

(make-instance [m1] of message)

(agenda)
(run)

(send [m1] put-arg1 10)
; not trigger
(send [m1] put-arg2 10)
(agenda)
(run)

(exit)
