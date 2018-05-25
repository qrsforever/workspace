;=======================================
; date: 2018-05-24 14:11:16
; title: define open door rule
; (ppdefrule door_open)
; (undefrule door_open)
;=======================================

(deffacts IOT::fact-rules-info
    (rule-engine-info
        (rulname "door-open")
        (version "1.0.0")
    )
)

;---------------------------------------
; Rule: door-open
;---------------------------------------

(defrule IOT::door-open 
    (declare 
        (salience ?*rule-normal-priority*)
        (auto-focus TRUE)
    )
    (object 
        (is-a DOOR-DEVICE)
        (UUID "111111")
        (switch ON)
    )
    (object
        (is-a DEVICE)
        (UUID "333333")
        (brightness ?brightness &:(< ?brightness 20))
    )
  =>
    (rule-action "222222" "switch" "ON")
)

