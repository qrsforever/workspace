
(bind ?a "aaa")
(bind ?b "\"bbb\"")

(defmethod escape-quote ((?str STRING))
    (bind ?str-len (str-length ?str))
    (if (bind ?pos (str-index "\"" ?str))
     then
        (str-cat (sub-string 1 (- ?pos 1) ?str)
         "\\\""
         (escape-quote (sub-string (+ ?pos 1) ?str-len ?str))
        )
     else
        (return ?str)
    )
)

(defmethod unescape-quote ((?str STRING))
    (bind ?str-len (str-length ?str))
    (if (bind ?pos (str-index "\\\"" ?str))
     then
        (str-cat (sub-string 1 (- ?pos 1) ?str)
         (unescape-quote (sub-string (+ ?pos 1) ?str-len ?str))
        )
     else
        (return ?str)
    )
)

(bind ?c "aaa \"bb\"")

(printout t ?a crlf)
(printout t ?b crlf)

(printout t (format nil "--> %s" ?b) crlf)
(printout t (format nil "--> \"%s\"" ?b) crlf)

(printout t (implode$ (create$ aaa "bbb" "\"ccc\"")) crlf)
(printout t (escape-quote (implode$ (create$ aaa "bbb"))) crlf)

(bind ?str (escape-quote "\"aaa\" cccc \"bbb\""))
(printout t ?str crlf)

(printout t (unescape-quote ?str) crlf)

(exit)


; (defrule MAIN::_rul-3059
 ; (declare (salience 1000))
 ; (action-response 10000001 success)
 ; =>
 ; (send [rul-001] action-success "\"10000001\" \"tellYou\" \"Girlfriend Birthday\"")
 ; )
