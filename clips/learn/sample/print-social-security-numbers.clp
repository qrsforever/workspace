; clips -f print-social-security-numbers.clp

;===================================================================
; Single field wildcard  (?var)
;===================================================================

(deftemplate person
    (multislot name)
    (slot social-security-number)
)

(deffacts some-people
    (person 
        (name john Q. public)
        (social-security-number 483-98-9083)
    )

    (person
        (name jack R. public)
        (social-security-number 483-98-9084)
    )
)

(defrule print-social-security-numbers
    (print-ss-numbers-for ?last-name)
    (person 
        (name ?first-name ?middle-name ?last-name)
        (social-security-number ?ss-number)
     )
  =>
    (printout t ?ss-number crlf)
)

(reset)
(assert (print-ss-numbers-for public))
(facts)
(run)

;===================================================================
; Multiple field wildcard  ($?) 配置0个或多个字段
;===================================================================

(defrule print-social-security-numbers-2
    (print-ss-numbers-for ?last-name)
    (person 
        (name $? ?last-name)
        (social-security-number ?ss-number)
     )
  =>
    (printout t ?ss-number crlf)
)

(reset)
(assert (print-ss-numbers-for public))
(facts)
(run)

(exit)
