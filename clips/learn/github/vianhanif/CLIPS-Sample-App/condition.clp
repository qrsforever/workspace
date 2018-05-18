(defrule app_condition
	(check_daily yes)
	(user_gender female)
	=>
	(section)
	(print "1. Pregnant")
	(print "2. Breastfeed")
	(print "3. Normal")
	(ask_condition "How is your condition ? ")
)