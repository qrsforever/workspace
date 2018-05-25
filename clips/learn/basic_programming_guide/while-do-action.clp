; clips -f while-do-action.clp

(defrule open-valves
    (valves-open-through ?v)
  =>
    (while (> ?v 0)
        (printout t "Valve " ?v " is open" crlf)
        (bind ?v (- ?v 1))
    )
)

(watch all)
(assert(valves-open-through 10))

(facts)
(agenda)
(run)

(exit)
