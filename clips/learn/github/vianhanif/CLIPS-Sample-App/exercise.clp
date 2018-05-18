(defrule app_exercise
	(check_daily yes)
	=>
	(section)
	(ask_exercise "Do you usually exercise [yes / no]? ")
)