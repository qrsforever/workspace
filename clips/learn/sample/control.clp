; clips -f control.clp

;===================================================================
; and or integerp , : =
;===================================================================

(and (> 4 3) (> 4 5))
(or (> 4 3) (> 4 5) (> 1 3))
(integerp 3)
(integerp 3.0)

; (test (size > 1))
; (pile-size ?size &:(> ?size 1))
; (data ?item ~:(integerp ?item))


(exit)

