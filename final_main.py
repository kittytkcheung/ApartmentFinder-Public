# Kitty Cheung, Izabela Tyszka, Erin Wurtumberger, April Yee
import pandas as pd
import mergeData as merge
import clean_code as cc
import get_safest as safe
import get_br as gbr
import input_logic as log
import decision_tree as tree
import output as out
import distance_calc as dist


def main():

	# Merge zip code and crime data by city
	merge.masterMerge("City_Crime_Data.csv", "City_zipcodes_data.csv", "City", "RI_city_zip_crime.csv")

	# Merge zip/crime with apartment data by city
	merge.masterMerge("RI_city_zip_crime.csv", "city_apartment_data.csv", "City", "RI_crime_housing.csv")	

	# Merge zip/crime/housing with latitude/longitude data by zip code
	merge.masterMerge("RI_crime_housing.csv", "us_zip_lat_long.csv", "zip", "RI_crime_housing_lat_lng.csv")

	# Read CSV using pandas using only relevant columns
	allData = "RI_crime_housing_lat_lng.csv"
	allData = pd.read_csv(allData, usecols=["City", "Crime_Occurances", "Percent_of_Population", "Crime_Rating", "zip", "Studio", "1_Bedroom", "2_Bedrooms", "3_Bedrooms", "LAT", "LNG"])
	
	#Add distance column calculated from lat & long colums
	allData = dist.add_dist(allData)

	# Write Master RI CSV file 
	allData.to_csv("Master_RI_data.csv", index=False, float_format="%g")

	# Use Master_RI_data.csv and Master_Providence_Neighborhood_Data.csv 

	# Read Providence neighborhood master data
	pvdData = "Master_Providence_Neighborhood_Data.csv"
	pvdData = pd.read_csv(pvdData)


	# Clean data
	br_col = ["Studio", "1_Bedroom", "2_Bedrooms", "3_Bedrooms"]
	allData = cc.clean(allData, br_col)
	pvdData = cc.clean_pvd(pvdData, br_col)

	pvdData["Dist_fm_Brown_Walking"] = pvdData["Dist_fm_Brown_Walking"].fillna(0).astype(int)

	allData["zip"] = allData["zip"].apply(cc.clean_zip)

	# Greet user
	print("\nHello scholar! Looking for a new home to optimize your collegiate experience?")
	print("Look no further - this botty bot has got your back!\n")

	# Returns user inputs as a dictionary and calls on helper functions to find cheapest and safest options
	user_answers = log.input_logic(allData, pvdData)

	crime_df = tree.dec_tree(user_answers, allData, pvdData)

	# Outputs
	br_budget_df = gbr.get_br(crime_df, user_answers["br_in"], user_answers["budget_in"])
	out.print_outputs(br_budget_df, user_answers)	


main()

