; ======================================
; date: 2018-05-24 10:08:40
; title: Global definition
; ======================================

;---------------------------------------
;	Global Module
;---------------------------------------

(defmodule IOT (export ?ALL))

;---------------------------------------
;	Global variables
;---------------------------------------

(defglobal 
    ?*VERSION* = "1.0.0"
    ?*DEBUG* = 1

    ?*rule-high-priority* = 100
    ?*rule-normal-priority* = 0
    ?*rule-low-priority* = -100
)


;---------------------------------------
;	Global Template
;---------------------------------------

; (deftemplate attribute
;     (slot name (type STRING))
;     (slot value (type STRING))
; )

(deftemplate IOT::device-class-info 
    (slot devname (type STRING))
    (slot version (type STRING) (default "1.0.0"))
)

(deftemplate IOT::rule-engine-info 
    (slot rulname (type STRING))
    (slot version (type STRING) (default "1.0.0"))
)


;---------------------------------------
;	Global functions
;---------------------------------------

(deffunction IOT::print-args (?a ?b $?c)                                 
    (printout t ?a " " ?b " and " (length$ ?c) " extras: " ?c crlf)
)

(deffunction IOT::rule-action (?did ?pro ?val $?args)
    (if (= (length$ ?args) 0)
        then
            (printout t "DeviceID[" ?did "] set " ?pro " = " ?val crlf)
        else
            (print-args ?did ?pro ?val $?args)
    )
)

(deffunction IOT::show-mem-used ()
    (printout t "Memory Consumption " (/ (mem-used) 131072) " MB" crlf)
)

;---------------------------------------
;	Global Class
;---------------------------------------

; (defclass ATTRIBUTE (is-a USER)
;     (slot n (type STRING))
;     (slot v (type STRING))
; )

(defclass IOT::DEVICE (is-a USER)
    (slot ID     (visibility public) (type SYMBOL))
    (slot Class  (visibility public) (type SYMBOL))
    (slot Parent (visibility public) (default-dynamic nil))
    (slot UUID   (visibility public) (type STRING))

    ; for debug for recording the instances count of all devices
    (slot insCnt (type INTEGER) (storage shared) (default 0))
)
    
(defmessage-handler IOT::DEVICE init after ()
    (bind ?self:ID (instance-name-to-symbol (instance-name ?self)))
    (bind ?self:Class (class ?self))

    ; for debug
    (bind ?self:insCnt (+ ?self:insCnt 1))
)

;---------------------------------------
;	Gloabl Rule
;---------------------------------------

(defrule IOT::show-mem-used
    ?f <- (MEM-USED)
  =>
    (retract ?f)
    (printout t "Memory Consumption " (/ (mem-used) 131072) " MB" crlf)
)
