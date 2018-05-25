;=======================================
; date: 2018-05-24 10:33:45
; title: main
;=======================================

(clear)

; (watch all)
; (watch compilations)
; (watch statistics)
; (watch focus)
; (watch messages)
; (watch deffunctions)
; (watch globals)
; (watch rules)
; (watch activations)
; (watch facts)
; (watch instances)
; (watch slots)
; (watch message-handlers)
; (watch generic-functions)
; (watch methods)

(load iot-global.clp)
(load iot-devices.clp)
(load iot-rules.clp)

(reset)
(facts)

(set-current-module IOT)
(get-current-module)
(focus IOT)
(list-focus-stack)

; (describe-class DOOR-DEVICE)
; (describe-class DEVICE_LIGTH)
; (describe-class MIXMETER-DEVICE)
; show tree inherit
; (browse-classes)
; (get-defclass-list)

(make-instance d_111111 of DOOR-DEVICE 
    (UUID "111111")
)

(make-instance d_222222 of LIGHT-DEVICE
    (UUID "222222")
)

(make-instance d_333333 of MIXMETER-DEVICE
    (UUID "333333")
)

;---------------------------------------
; test unmake-instance to call message-handler
;---------------------------------------
; (get-defmessage-handler-list DOOR-DEVICE)
; (make-instance d_444444 of DOOR-DEVICE
;     (UUID "444444")
;     (dname "door2")
; )
; (facts)
; (unmake-instance [d_444444])

(facts)

; fail for initialize-only
; (send [d_111111] put-dname "door2")

(send [d_111111] print)
(send [d_222222] print)
(send [d_333333] print)

(list-defrules)
(show-mem-used)

; Simulate event to trigger door_open_rule.
(send [d_111111] put-switch ON)
(send [d_333333] put-brightness 10)

; (make-instance (gensym) of ATTRIBUTE 
;     (name "a1")
;     (value "v1")
; )

(agenda IOT)

; (focus IOT)
(run)
(list-focus-stack)

(exit)
