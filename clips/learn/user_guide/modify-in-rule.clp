(deftemplate foo (slot bar) (slot switch))

(defrule rutest
    ?f <- (foo (bar ?b) (switch ?sw &: (eq ?sw on)))
  => 
    (printout t "---> fact: " ?f crlf)
    (modify ?f (switch off) (bar 1))
    (printout t "---> fact: " (facts) crlf)
    (modify ?f (bar 2))
    (printout t "---> fact: " (facts) crlf)
    (modify ?f (bar 3))
    (printout t "---> fact: " (facts) crlf)
    (modify ?f (bar 4))
    
)

(assert (foo (bar 0) (switch on)))
