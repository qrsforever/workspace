(deftemplate strkey
   (slot key (type SYMBOL))
)

(defrule test-lhs-str-index
   (strkey (key ?k &:(= 1 (str-index hh ?k))))
 =>
   (bind ?k "xxxx")
   (printout t "hhhh:" ?k crlf)
   (facts)
)

(str-index hh hhbb)

(assert (strkey (key hh:11)))

(agenda)
(run)

(assert (strkey (key bbhh)))

(agenda)
(run)

(bind ?strstr aa:11)
(bind ?idx (str-index : ?strstr))

(if (and (neq ?idx FALSE) (> ?idx 1))
 then
    (bind ?name (sub-string 1 (- ?idx 1) ?strstr))
    (bind ?skey (sub-string (+ ?idx 1) (str-length ?strstr) ?strstr))
    (printout t "name: " ?name "  skey:" ?skey crlf)
)

(printout t "strstr: " ?strstr crlf)

(exit)
