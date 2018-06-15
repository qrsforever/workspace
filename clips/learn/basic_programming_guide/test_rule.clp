(clear)

(deftemplate oav
 (slot object)
 (slot attribute)
 (slot value))

(defrule example-rule "简单例子"
 (oav 
  (object refrigerator)
  (attribute light)
  (value on))
 (oav
  (object refrigerator)
  (attribute door)
  (value open))
 =>
 (assert 
  (oav 
   (object refrigerator)
   (attribute food)
   (value spoiled))
  )
 )

(defrule example-rule1 "简单例子"
 (oav 
  (object refrigerator)
  (attribute light)
  (value on))
 (oav
  (object refrigerator)
  (attribute door)
  (value open))
 =>
 (assert
  (oav
   (object refrigerator)
   (attribute food)
   (value spoiled))
  )
 )

(facts)

(assert
 (oav 
  (object refrigerator)
  (attribute light)
  (value on))
 )

(facts)

(agenda)

(assert
 (oav
  (object refrigerator)
  (attribute door)
  (value open))
 )

(facts)

(agenda)

(run)

(facts)

(agenda)

(exit)
