import pandas as pd
import mergeData as merge
import clean_code as cc
import get_safest as safe
import get_br as gbr
import input_logic as log
import decision_tree as tree
# from final_main import main 


def print_outputs(br_budget_df, user_answers):
	if br_budget_df.empty == True:
		print("There were no options that matched your results.\n")
		print("If you would like to try again, please re-run the program.")

	# output city/neighborhood options
	else:
		print("Cool beans. Consider the following locations for your apartment:")
		
		if user_answers["car_in"] == "NO":
			if user_answers["br_in"] == "0":
				br_budget_df = br_budget_df.sort_values(by=["Dist_fm_Brown_Walking"], ascending=True)
				print(br_budget_df[["Neighborhood", "Studio", "Dist_fm_Brown_Walking"]][0:5])
			if user_answers["br_in"] == "1":
				br_budget_df = br_budget_df.sort_values(["Dist_fm_Brown_Walking"], ascending=True)
				print(br_budget_df[["Neighborhood", "1_Bedroom", "Dist_fm_Brown_Walking"]][0:5])
			if user_answers["br_in"] == "2":
				br_budget_df = br_budget_df.sort_values(["Dist_fm_Brown_Walking"], ascending=True)
				print(br_budget_df[["Neighborhood", "2_Bedrooms", "Dist_fm_Brown_Walking"]][0:5])
			if user_answers["br_in"] == "3":
				br_budget_df = br_budget_df.sort_values(["3_Bedrooms"], ascending=True)
				print(br_budget_df[["Neighborhood", "3_Bedrooms", "Dist_fm_Brown_Walking"]])

					
		else:
			if user_answers["br_in"] == "0":
				br_budget_df = br_budget_df.sort_values(by=["Studio"], ascending=True)
				print(br_budget_df[["City", "zip", "Studio", "Distance"]][0:10])
			if user_answers["br_in"] == "1":
				br_budget_df = br_budget_df.sort_values(["1_Bedroom"], ascending=True)
				print(br_budget_df[["City", "zip", "1_Bedroom", "Distance"]][0:10])
			if user_answers["br_in"] == "2":
				br_budget_df = br_budget_df.sort_values(["2_Bedrooms"], ascending=True)
				print(br_budget_df[["City", "zip", "2_Bedrooms", "Distance"]][0:10])
			if user_answers["br_in"] == "3":
				br_budget_df = br_budget_df.sort_values(["3_Bedrooms"], ascending=True)
				print(br_budget_df[["City", "zip", "3_Bedrooms", "Distance"]][0:10])
