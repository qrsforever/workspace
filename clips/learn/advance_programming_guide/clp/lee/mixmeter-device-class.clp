;=======================================
; date: 2018-05-24 13:58:15
; title: device_brightness_class
;=======================================

(deffacts fact-MIXMETER-DEVICE-info
    (device-class-info 
        (devname "MIXMETER-DEVICE")
        (version "1.0.0")
    )
)

(defclass MIXMETER-DEVICE "a mix meter device"
    (is-a DEVICE) (role concrete) (pattern-match reactive) 

    (slot brightness
        (type INTEGER) 
        (range 0 100)
        (default 50)
    )

    (slot temprature
        (type FLOAT) 
        (range -50.0 80.0)
        (default 0.0)
    )
)
