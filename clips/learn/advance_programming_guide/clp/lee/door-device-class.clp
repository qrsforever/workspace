;=======================================
; date: 2018-05-24 10:24:42
; title: define door class
;=======================================

(deffacts fact-DOOR-DEVICE-info
    (device-class-info 
        (devname "DOOR-DEVICE")
        (version "1.0.0")
    )
)

(defclass DOOR-DEVICE "a door device"
    (is-a DEVICE) (role concrete) (pattern-match reactive) 

    ;(slot dname 
    ;    (type STRING) 
    ;    (default "mixmeter") 
    ;    (access initialize-only)
    ;)

    (slot switch 
        (type SYMBOL) 
        (allowed-symbols ON OFF)
        (default OFF)
    )

    (slot level
        (type INTEGER) 
        (range 1 5)
        (default 1)
    )
)

; (defmessage-handler DOOR-DEVICE init before ()
    ; (assert (device-class-info (devname "DOOR-DEVICE") (version "1.0.0")))
; )

; (defmessage-handler DOOR-DEVICE delete after ()
    ; (foreach ?f (find-fact ((?d device-class-info)) (eq ?d:devname "DOOR-DEVICE"))
        ; (retract ?f)
    ; )
; )
