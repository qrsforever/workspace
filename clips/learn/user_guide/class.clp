; instance sample
(clear)

(defclass DUCK (is-a USER)
 (slot sound)
 (slot age)
)

(browse-classes USER)
(class-superclasses DUCK)
(class-subclasses USER)

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

(clear)

(defclass A (is-a USER)
    (slot x (default 7) (range 1 8))
    (slot y (allowed-integers 2 3) (allowed-symbols foo bar))
)

(describe-class A)

(slot-default-value A x)
(slot-range A x)
(slot-allowed-values A y)

(defclass B (is-a USER) (slot x))
(defclass C (is-a USER)
    (slot y (allowed-classes A B))
)

(slot-allowed-classes B x)
(slot-allowed-classes C y)

; but not check
(make-instance Test_C of C
    (y "aaa")
)
(send [Test_C] print)

(defclass D (is-a USER)
    (slot x (type INTEGER) (default 7) (range 1 8))
)

; return not used, must have delete
; (defmessage-handler D delete ()
(defmessage-handler D delete before ()
    (return TRUE)
)

; check send wrong type ????? why ???
(make-instance Test_D of D
    (x 10)
)
(send [Test_D] put-y "20")
(send [Test_D] print)
(class [Test_D])
(instance-name [Test_D])

(instance-existp Test_D)
(instance-existp [Test_D])

(instance-existp Test_G)
(instance-existp [Test_G])


(lexemep "aaaa  bbb")
(lexemep aaaa)

(if (not (lexemep aaaa))
 then
    (printout t "YYYYY" crlf)
  else
    (printout t "NNNNN" crlf)
)

(instances)
(unmake-instance [Test_D])
(bind ?res (unmake-instance [Test_D]))
(if (eq ?res TRUE)
 then
     (printout t "unmake-instance:" ?res crlf)
)
(undefclass D)
(list-defclasses)

(symbol-to-instance-name Test_D)
(exit)
