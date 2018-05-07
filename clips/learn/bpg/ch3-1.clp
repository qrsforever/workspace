(clear)

(deftemplate point
  (slot x (default ?NONE))
  (slot y (type INTEGER) (default ?DERIVE))
  (slot id (default (gensym*)))
  (slot uid (default-dynamic (gensym*))))

; error: x 必须初始化 
(assert (point))

(assert (point (x 3)))
(assert (point (x 4)))
(facts)

(exit)
