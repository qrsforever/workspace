; rules sample

(clear)
(defrule duck
 (animal-is duck)
 =>
 (assert (sound-is quack))
)

(watch facts)
(watch activations)

(assert (animal-is duck))

; Sample assert can not trigger twice action
(assert (animal-is duck))

(agenda)
(run)

(facts)

; The rule already fired on this fact, Cann't gen the agenda again.
(assert (animal-is duck))

(rules)
