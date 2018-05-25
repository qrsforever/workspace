;=======================================
; date: 2018-05-24 13:58:15
; title: device_brightness_class
;=======================================

(deffacts fact-SUPER-DEVICE-info
    (device-class-info 
        (devname "SUPER-DEVICE")
        (version "1.0.0")
    )
)

(defclass SUPER-DEVICE "a super device"
    (is-a DEVICE) (role concrete) (pattern-match reactive) 

    (slot dname 
        (type STRING) 
        (default "super") 
        (access initialize-only)
    )
    ; (multislot attrs)
)
