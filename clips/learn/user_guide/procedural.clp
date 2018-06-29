
(deffunction test ( ?a $?b)
 (if (eq ?a array)
   then
    (printout t "yes" crlf)
 )
)

(test array 11 22)

(exit)
