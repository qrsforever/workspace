
; if argument is key word, that's ok
(bind ?eqsym eq)
(printout t "equal sym: " ?eqsym crlf)

;
(defglobal
    ?*TEST_CASE* = TRUE
)

; test global variable can be used in if statement directly
(if ?*TEST_CASE*
; (if (eq ?*TEST_CASE* TRUE)
 then
    (printout t "TEST_CASE start..." crlf)
 else
    (printout t "TEST_CASE not start..." crlf)
)

(bind ?b (create$ aa bb ccc))
(printout t (expand$ ?b) crlf)

(bind ?a aaaa)

(bind ?b (format nil "%s" ?a))

(type ?a)
(type ?b)

(if (eq ?a aaaa)
 then
    (printout t "aaaaaaaaaaaaaaaaaaaa" crlf)
)

(format t "aaa%nbbb%n")


(deftemplate timer-event
 (slot id)
 (slot txt)
)

(defrule timer-event
    ?t <- (timer-event (id ?id &:(= ?id 1111)))
  =>
    (printout t "### id " ?id crlf)
)

(assert (timer-event (id 1111)))
(assert (timer-event (id 2222)))

(agenda)
(run)

(defrule test-event
    ?f <- (test-event ?id)
  =>
  (bind ?fact (nth$ 1 (find-fact ((?f timer-event)) (eq ?f:id 1111))))
  (type ?fact)
  (if (neq ?fact nil)
   then
   (retract ?fact)
  )
)

(bind ?fact (nth$ 1 (find-fact ((?f timer-event)) (eq ?f:id 1111))))

(facts)

(type ?fact)

(if (neq ?fact nil)
 then
    (retract ?fact)
)

(facts)

(defclass oic.d.light  (is-a USER)
 (slot a)
 (slot b)
)

(deftemplate mytest
    (slot arg (type INTEGER))
    (multislot args (type INTEGER SYMBOL))
)

(defrule mytest
    (mytest (args $?args))
  =>
    (printout t "---> " (multifieldp $?args) crlf)
)

(assert (mytest (arg 1)))
(assert (mytest (args 1 a)))
(facts)
(deftemplate-slot-types mytest args)

(bind $?values (fact-slot-value 3 args))

(multifieldp $?values)
(nth$ 1 $?values)
(nth$ 2 $?values)

(agenda)
(run)
(exit)
