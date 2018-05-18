(defrule app_gender
	(check_daily yes)
	=>
	(section)
	(ask_gender "What is your gender [male / female] ? ")
)