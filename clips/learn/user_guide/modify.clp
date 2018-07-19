
(deftemplate scene-mode
    (slot zone)
    (slot from (type SYMBOL) (default none))
    (slot to (type SYMBOL) (default none))
)

; trigger scene enter
(defrule trigger-scene-enter
    (declare (salience -1000))
    ?enter <- (scene-enter ?zone ?mode)
    ?scene <- (scene-mode (zone ?zone) (to ?to))
  =>
    (retract ?enter)
    (printout t "scene-enter: " ?zone " " ?mode crlf)
    (modify ?scene (state entering) (from ?to) (to ?mode))
)

(defrule room1-none
    ?f <- (scene-mode (zone room1) (to none))
   =>
    (printout t "room1-none mode" crlf)
)

(defrule room1-sleeping
    ?f <- (scene-mode (zone room1) (to sleeping))
  =>
    (printout t "room1 enter sleepping mode" crlf)
)

(defrule room1-getup
    ?f <- (scene-mode (zone room1) (to getup))
  =>
    (printout t "room1 enter getup mode" crlf)
)

(defrule tv-is-on
    (tv-is-on)
  =>
    (assert (scene-enter room1 video))
)

(defrule tv-is-off
    (tv-is-off)
    ?scene <- (scene-mode (zone room1) (from ?from) (to ?to))
    (test (eq ?to video))
  =>
    (printout t "-----> tv-is-off :" ?from " " ?to crlf)
    (modify ?scene (from ?to) (to ?from))
)

(defrule room1-video
    ?f <- (scene-mode (zone room1) (to video))
  =>
    (printout t "----> room1-video" crlf)
)

(assert (scene-mode (zone room1)))
(facts)
(agenda)
(run)

(assert (tv-is-on))
(facts)
(agenda)
(run)

(assert (scene-enter room1 sleeping))
(facts)
(agenda)
(run)

(assert (tv-is-off))
(facts)
(agenda)
(run)

(assert (scene-enter room1 getup))
(facts)
(agenda)
(run)

(exit)

