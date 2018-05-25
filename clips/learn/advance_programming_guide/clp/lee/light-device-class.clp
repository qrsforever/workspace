;=======================================
; date: 2018-05-24 12:57:39
; title: define light class
;=======================================

(deffacts fact-LIGHT-DEVICE-info
    (device-class-info 
        (devname "LIGHT-DEVICE")
        (version "1.0.0")
    )
)

(defclass LIGHT-DEVICE "a light device"
    (is-a DEVICE) (role concrete) (pattern-match reactive) 

    (slot switch 
        (type SYMBOL) 
        (allowed-symbols ON OFF)
        (default OFF)
    )
)
