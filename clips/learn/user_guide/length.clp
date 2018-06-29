
(bind ?file "11111")
(printout t "file " ?file crlf)

(length$ (create$ a b c d e f g))

; error
; (length ?file)

(length$ ?file)
(str-length ?file)

(exit)
