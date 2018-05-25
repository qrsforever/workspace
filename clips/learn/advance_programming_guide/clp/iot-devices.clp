;=======================================
; date: 2018-05-25 17:46:29
; title: define devices
;=======================================

;---------------------------------------
;	Init device facts
;---------------------------------------
(deffacts IOT::fact-devices-info

    (device-class-info 
        (devname "DOOR-DEVICE")
        (version "1.0.0")
    )

    (device-class-info 
        (devname "LIGHT-DEVICE")
        (version "1.0.0")
    )

    (device-class-info 
        (devname "MIXMETER-DEVICE")
        (version "1.0.0")
    )
)

;---------------------------------------
;	DOOR-DEVICE
;---------------------------------------

(defclass IOT::DOOR-DEVICE "a door device"
    (is-a DEVICE) (role concrete) (pattern-match reactive) 

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

;---------------------------------------
;	LIGHT-DEVICE
;---------------------------------------

(defclass IOT::LIGHT-DEVICE "a light device"
    (is-a DEVICE) (role concrete) (pattern-match reactive) 

    (slot switch 
        (type SYMBOL) 
        (allowed-symbols ON OFF)
        (default OFF)
    )
)

;---------------------------------------
; MIXMETER-DEVICE	
;---------------------------------------

(defclass IOT::MIXMETER-DEVICE "a mix meter device"
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
