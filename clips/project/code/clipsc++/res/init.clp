;=================================================================
; date: 2018-06-04 20:21:39
; title: Unit Test
;=================================================================

(defglobal
    ?*CLIPS_DIRS* = (get-clips-dirs)
    ?*DEBUG* = 2
    ?*CONFIG_PREFIXES* = (create$ "res/")
    ?*START-TIME* = (now)
)

(deffunction resolve-file (?file)
    (foreach ?d ?*CLIPS_DIRS*
        (bind ?fn (str-cat ?d ?file))
        (if (open ?fn file-clips-tmp)
            then
                (close file-clips-tmp)
                (return ?fn)
        )
    )
    (return FALSE)
)

(load* (resolve-file utils.clp))
