
(deffunction test-args (?a ?b $?flag)
    (bind ?f (nth$ 1 $?flag))
    (if (eq ?f 1)
     then
     (printout t "--->" ?a "---" ?b "---" ?f crlf)
    )
    (printout t "end" crlf)
)

(test-args a b)
(test-args a b 1)
(test-args a b 2)

(exit)
