
(bind ?a "aaa")
(bind ?b "\"bbb\"")

(printout t ?a crlf)
(printout t ?b crlf)

(printout t (format nil "--> %s" ?b) crlf)
(printout t (format nil "--> \"%s\"" ?b) crlf)

(exit)
