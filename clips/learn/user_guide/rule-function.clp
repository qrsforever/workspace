(defrule foo => )
(defrule bar => )
(defrule rule-111.222.333 => )

(get-defrule-list)

(if (defrule-module bar)
  then
    (printout t "bar:Yes" crlf)
  else
    (printout t "bar:No" crlf)
)

(if (defrule-module nnn)
  then
    (printout t "nnn:Yes" crlf)
  else
    (printout t "nnn:No" crlf)
)

(exit)
