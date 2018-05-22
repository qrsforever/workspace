(clear)

(deftemplate oav
 (slot object)
 (slot attribute)
 (slot value))

(deffacts startup "冰箱柜 状态"
 (oav 
  (object refrigerator)
  (attribute light)
  (value on))
 (oav 
  (object refrigerator)
  (attribute door)
  (value open))
 (oav 
  (object refrigerator)
  (attribute temp)
  (value 40))
 )

(deftemplate person
 (slot name)
 (multislot attrs)
)

(deffacts startup2 "冰箱柜2 状态"
 ( aaa)
 )

(facts)
(reset)
(facts)

(exit)
