
(defclass DEVICE (is-a USER) (role abstract)
    (slot ID     (type SYMBOL))
    (slot Class  (visibility public) (type SYMBOL) (access initialize-only))
    (slot UUID   (visibility public) (type STRING))
    (slot insCnt (type INTEGER) (storage shared) (default 0))
)

(defmessage-handler DEVICE init after ()
    (bind ?self:ID (instance-name-to-symbol (instance-name ?self)))
    (bind ?self:Class (class ?self))
    (bind ?self:insCnt (+ ?self:insCnt 1))
)

(defclass Light
  (is-a DEVICE)
  (role concrete) (pattern-match reactive) 
  (slot OnlineState (type NUMBER) (allowed-numbers 2 1))
  (slot PowerOnOff (type NUMBER) (allowed-numbers 2 1))
  (slot Brightness (type NUMBER) (range 1 7))
)

(defclass Letv
  (is-a DEVICE)
  (role concrete) (pattern-match reactive) 
  (slot OnlineState (type NUMBER) (allowed-numbers 2 1))
  (slot PowerOnOff (type NUMBER) (allowed-numbers 2 1))
)

(defclass LightSensor
  (is-a DEVICE)
  (role concrete) (pattern-match reactive) 
  (slot OnlineState (type NUMBER) (allowed-numbers 2 1))
  (slot Quantity (type NUMBER) (range 0 1000))
  (slot PowerOnOff (type NUMBER) (allowed-numbers 2 1))
)

; ?id1 ?id2 ?id3 ---> not same ?id
(defrule rul-0000000000.000.00001 "tv-light-rule"
  (and
    (object (is-a Light)
      (ID ?id1 &:(eq ?id1 ins-38D269B0EA1801010311))
      (PowerOnOff ?PowerOnOff &:(= ?PowerOnOff 1))
    )
    (object (is-a Letv)
      (ID ?id2 &:(eq ?id2 ins-00000000000000000002))
      (PowerOnOff ?PowerOnOff &:(= ?PowerOnOff 1))
    )
    (object (is-a LightSensor)
      (ID ?id3 &:(eq ?id3 ins-00000000000000000001))
      (Quantity ?Quantity &:(>= ?Quantity 10 )&:(<= ?Quantity 20))
    )
  )
 =>
  (printout t "##############id " ?id1 crlf)
)

(make-instance ins-38D269B0EA1801010311 of Light)
(make-instance ins-00000000000000000002 of Letv)
(make-instance ins-00000000000000000001 of LightSensor)

(send [ins-38D269B0EA1801010311] put-PowerOnOff 1)
(send [ins-00000000000000000002] put-PowerOnOff 1)
(send [ins-00000000000000000001] put-Quantity 15)

(send [ins-38D269B0EA1801010311] print)
(send [ins-00000000000000000002] print)
(send [ins-00000000000000000001] print)

(agenda)
(run)

(exit)
