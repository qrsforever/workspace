
(deffunction ret-true ()
    (return false)
)

(deffunction ret-TRUE ()
    (return FALSE)
)

(if (ret-true)
 then
  (printout t "####" crlf)
)

(ret-true)

(if (ret-TRUE)
 then
  (printout t "####" crlf)
)

(ret-TRUE)

(exit)
