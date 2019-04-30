import get_safest as safe
import get_br as gbr

def dec_tree(user_answers, allData, pvdData):
# Depending on whether they want to live in Pvd or outside of Pvd, access one of two datasets
	if user_answers["car_in"] == "NO":
		# max_walk = input("max walking time? ")
		df = safe.get_safest_pvd(pvdData, user_answers["crime_in"])
	
	elif user_answers["car_in"] == "YES":
		# Filter cities that match crime input
		df = safe.get_safest(allData,  user_answers["crime_in"])

	return(df)