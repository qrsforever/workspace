
(defclass DEVICE (is-a USER)
    (role abstract)
    (slot ID     (visibility public) (type SYMBOL))
    ; (slot Class  (visibility public) (type SYMBOL) (access read-only))
    (slot Class  (visibility public) (type SYMBOL) (access initialize-only))
    (slot Parent (visibility public) (default-dynamic nil))
    (slot UUID   (visibility public) (type STRING))
    (slot insCnt (type INTEGER) (storage shared) (default 0))
)

(defmessage-handler DEVICE init after ()
    (bind ?self:ID (instance-name-to-symbol (instance-name ?self)))
    (bind ?self:Class (class ?self))
    (bind ?self:insCnt (+ ?self:insCnt 1))
)

(defclass Light (is-a DEVICE) (role concrete) (pattern-match reactive)
    (slot switch)
)

; error if access is read-only: Class write deny.
; success if access is initialize-only
(make-instance light_1 of Light (switch 1))

; error even if access is initialize-only
(send [light_1] put-Class "Light2")

; (make-instance light_1 of Light)
(instances)
(send [light_1] print)
(exit)
