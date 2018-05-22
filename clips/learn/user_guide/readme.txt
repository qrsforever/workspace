

The CLIPS shell provides the basic elements of an expert system:
 1. fact-list, and instance-list: Global memory for data
 2. knowledge-base: Contains all the rules, the rule-base
 3. inference engine: Controls overall execution of rules

事实 + 认知 + 推理
factor + knowledge + inference


before version6.0 the capabilities: facts --> rules --> inference
after version6.0  the capabilities: facts and objects --> rules --> inference


(watch facts)
(watch instances)
(watch slots)
(watch rules)
(watch activations)
(watch messages)
(watch message-handlers)
(watch generic-functions)
(watch methods)
(watch deffunctions)
(watch compilations)
(watch statistics)
(watch globals)
(watch focus)
(watch all)


(defrule rule_name "comment"
 (pattern_1) ; Left-Hand Side
 (pattern_2) ; Left-Hand Side
 (pattern_3) ; Left-Hand Side
=>
 (action_1) ; Right-Hand Side
 (action_2) ; Right-Hand Side
 (action_3) ; Right-Hand Side
)


rule-based  VS  object-oriented


CLIPS provides three paradigms: rules, objects, and procedures.

CLIPS Object-Oriented Language (COOL)
