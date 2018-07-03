
(clear)

(defrule delete-onerule
    (delete-rule ?name)
 =>
    (undefrule ?name)
    (list-defrules)
)

(defrule onerule
    (exec onerule)
 =>
    (list-defrules)
    ; error, in used, cannot delete
    ; (undefrule onerule)
    (assert (delete-rule onerule))
)

(assert (exec onerule))
(agenda)
(run)

(exit)
