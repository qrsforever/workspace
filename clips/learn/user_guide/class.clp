; instance sample
(clear)

(defclass DUCK (is-a USER)
 (slot sound)
 (slot age)
)

(definstances DUCK_OBJECTS
 (Dorky_Duck of DUCK)
)

(reset)

(send [Dorky_Duck] print)
(send [Dorky_Duck] put-sound quack)
(send [Dorky_Duck] print)

; why age not show out.
(make-instance Dixie_Duck of DUCK
 (sound quack) 
 (age 2)
)

(send [Dixie_Duck] print)

(exit)
