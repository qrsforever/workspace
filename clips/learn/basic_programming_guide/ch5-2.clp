(clear)

(deffacts color-facts "ordered"
 (colors rgb primary red green blue)
 (colors rgb secondary cyan yellow magenta)
 (colors ryb primary red yellow blue)
 (colors ryb secondary purple orange green)
 )
   
(deftemplate person
 (multislot name)
 (slot age)
 )

(deffacts person-facts "unordered using deftemplate"
 (person (name Joe Bob Green) (age 20))
 (person (name Martin Brown) (age 20))
 (person (name Frank Martin) (age 34))
 (person (name Ann Green) (age 34))
 (person (name Sue Ann Brown) (age 20))
 )

; Literal Constraints
(defrule Find-Joe-Bob
 (person (name Joe Bob Green) (age 20))
 =>
 )

(defrule Find-Ann
 (person (age 34) (name Ann Green))
 =>
 )

(reset)
(agenda)
(facts)

; Wildcards: ? 匹配一个 $? 匹配0或者多个

(defrule find-green
 (colors ? ? $? green $?)
 =>
 )

(reset)
(agenda)

(defrule match-all-persons
 (person)
 =>
 )

(reset)
(agenda)

(clear)

(assert 
 (data 1 blue)
 (data 1 blue red)
 (data 1 blue red 6.9)
 )

(facts)

; 单/多匹配
(defrule find-data-1
 (data ?x $?y ?z)
 =>
 (print 
  "?x = " ?x crlf
  "?y = " ?y crlf
  "?z = " ?z crlf
  "--------" crlf
 )
)

(run)

(exit)
