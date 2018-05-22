;==================================================
; Module Define
;==================================================

(defmodule MAIN "like namespace"
 (export ?ALL)
)


;==================================================
; Global Variables
;==================================================

(deftemplate MAIN::EventOutput
 (slot speed (type INTEGER) (default 0))
 (slot accel (type INTEGER)) 
 (slot accelOpen (type INTEGER))
 (slot distance (type INTEGER))
)

(defglobal MAIN
 ?*list* = (assert (EventOutput))
)
; (get-defglobal-list MAIN)

;==================================================
; Templete
;==================================================

; event list
(deftemplate MAIN::EventSpeedList
 (slot from (default entryPoint))
 (slot name (default "Receiving Data Stream"))

 ; time type speed
 (multislot speedList)
 )

(deftemplate MAIN::EventAccelOpenList
 (slot from (default entryPoint))
 (slot name (default "Receiving Data Stream"))

 ; time type accelOpen
 (multislot accelOpenList)
 )

(deftemplate MAIN::EventDistanceList
 (slot from (default entryPoint))
 (slot name (default "Receiving Data Stream"))

 ; time type distance
 (multislot distanceList)
 )

; events
(deftemplate MAIN::EventSpeed
 (slot from (default entryPoint))
 (slot name)

 (slot speed (type FLOAT) (default 0.0))
 (slot type (type SYMBOL) (allowed-values VEHICLE_SPEED_SP1) (default VEHICLE_SPEED_SP1))
 (slot time (type FLOAT) (default-dynamic (time)))
)

(deftemplate MAIN::EventAccelOpen
 (slot from (default entryPoint))
 (slot name)

 (slot accelOpen (type FLOAT) (default 0.0))
 (slot type (type SYMBOL) (allowed-values ACCEL_OPEN) (default ACCEL_OPEN))
 (slot time (type FLOAT) (default-dynamic (time)))
)

(deftemplate MAIN::EventDistance
 (slot from (default entryPoint))
 (slot name)

 (slot distance (type FLOAT) (default 255.0))
 (slot type (type SYMBOL) (allowed-values VEHICLE_FOLLOWING_DISTANCE) (default VEHICLE_FOLLOWING_DISTANCE))
 (slot time (type FLOAT) (default-dynamic (time)))
)

; facts
(deftemplate MAIN::EventAcceleration
 (slot from (default entryPoint))
 (slot name)

 (slot acceleration (type FLOAT))
 (slot time (type FLOAT) (default-dynamic (time)))
)

(deftemplate MAIN::EventDriveScene
 (slot from (default entryPoint))
 (slot name)

 (slot driveScene (type SYMBOL) (allowed-values REVERSE STOP START RUNNING ACCEL REDUCE) (default STOP))
 (slot value1 (type FLOAT) (default 0.0))
 (slot value2 (type FLOAT) (default 0.0))
 (slot value3 (type FLOAT) (default 0.0))
 (slot beforeDriveScene (type SYMBOL) (allowed-values REVERSE STOP START RUNNING ACCEL REDUCE))
 (slot time (type FLOAT) (default-dynamic (time)))
 (slot accelAccelerationCount (type INTEGER) (default 0))
 (slot runningAccelerationCount (type INTEGER) (default 0))
)


;==================================================
; Function
;==================================================

(deffunction MAIN::brmsPower(?x ?y)
 (printout qt "**** MAIN::brmsPower ****" crlf)
 (if (and (= ?x 0) (<= ?y 0)) then
  (return 0.0)
  else
  (return (** ?x ?y))
 )
)

;Sqrt
(deffunction MAIN::brmsSqrt(?x)
 (printout qt "**** MAIN::brmsSqrt ****" crlf)
 (return (sqrt (abs ?x)))
)

