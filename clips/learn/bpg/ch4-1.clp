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

(facts)
(reset)
(facts)

(exit)
