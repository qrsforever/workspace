;=================================================================
; date: 2018-05-25 13:54:22
; title: procedural
;=================================================================


;-----------------------------------------------------------------
; (progn$ <list-spec> <expression>*)
;       <list-spec> ::= <multifield-expression> |
;       (<list-variable> <multifield-expression>)
; 遍历多域值, 进行处理
;-----------------------------------------------------------------

(progn$ 
    (?lv (create$ a b c d))
    (printout t "list-variable: " ?lv ", index: " ?lv-index crlf)
)

;-----------------------------------------------------------------
; (member$ <expression> <multifield-expression>)
; 单域值是否被多域值所包含, 返回index or FALSE
;-----------------------------------------------------------------

(member$ a (create$ c a b))
(member$ d (create$ c a b))





(exit)

