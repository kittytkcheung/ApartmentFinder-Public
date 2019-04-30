import pandas as pd
import mergeData as merge
import clean_code as cc
import get_safest as safe
import get_br as gbr

# How many bedrooms are you looking for?
def input_logic(allData, pvdData):
	input_dict = {}
	br_invalid = True
	while(br_invalid):
		br = input("Are you looking for 0, 1, 2, or 3 bedrooms?\n")
		br = br.strip()

		try:
			numBr = float(br)
			if numBr < 4:
				br_invalid = False

			else:
				br_invalid = True

		except ValueError:
			br_invalid = True

	input_dict["br_in"] = br

	# What is your budget?
	budget_invalid = True
	while(budget_invalid):
		budget = input("What is your monthly budget for rent?\n")
		budget = budget.strip("")
		budget = budget.strip("$")
		budget = budget.replace(",", "")
		
		try:
			budget = float(budget)

			if budget > 680 and budget < 2819:
				budget_invalid = False

			elif budget >= 2819:
				print("I see we're balling out.\n")
				budget_invalid = False

			elif budget <= 680:
				print("Hate to break it to you, but looks like you'll have to live in your parents' basement. All options will be above budget.\n")
				budget_invalid = True

		except ValueError:
			budget_invalid = True

	input_dict["budget_in"] = budget

	# How much do you care about crime?
	crime_invalid = True
	while(crime_invalid):
		crime = input("On a scale of 1-5 (1 = Do not care; 5 = Care a lot), how much do you care about crime where you live?\n")
		crime = crime.strip()

		try:
			crime = int(crime)
			if crime > 0 and crime < 6:
				crime_invalid = False

			else:
				crime_invalid = True

		except ValueError:
			crime_invalid = True

	input_dict["crime_in"] = crime

	# Do you have a car and are willing to commute?
	car_invalid = True
	while(car_invalid):
		car = input("Do you have a car?\n")
		car = car.strip().upper()
	
		if car == "NO":
			car_invalid = False
		
		elif car == "YES":
			car_invalid = False

		else:
			car_invalid = True

	input_dict["car_in"] = car

	return(input_dict)


