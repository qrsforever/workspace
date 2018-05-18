(defrule app_weight
	(check_daily yes)
	=>
	(section)
	(ask_weight "How much do you weight (kg) ? ")
)