;=================================================================
; date: 2018-06-04 20:21:39
; title: Unit Test
;=================================================================

(defmodule TEST (export ?ALL))

(defglobal
    ?*CLIPS_DIRS* = (get-clips-dirs)
    ?*DEBUG* = 2
    ?*CONFIG_PREFIXES* = (create$ "res/")
    ?*START-TIME* = (now)
)

(deffunction resolve-file (?file)
    (foreach ?d ?*CLIPS_DIRS*
        (bind ?fn (str-cat ?d ?file))
        (if (open ?fn fd) then
            (close fd)
            (return ?fn)
        )
    )
    (return FALSE)
)

; (load* (resolve-file utils.clp))

(deftemplate confval
    (slot path (type STRING))
    (slot type (type SYMBOL) (allowed-values FLOAT UINT INT BOOL STRING))
    (slot value)
    (slot is-list (type SYMBOL) (allowed-values TRUE FALSE) (default FALSE))
    (multislot list-value)
)

(defrule print-confval
    (confval (path ?p) (type ?t) (value ?v) (is-list ?is-list) (list-value $?lv))
  =>
    (printout t "confval path: " ?p "  type: " ?t
     "  value: " (if (eq ?is-list TRUE) then ?lv else ?v) crlf)
)
