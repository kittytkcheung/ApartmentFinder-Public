# return cheapest cities given number of bedrooms
def get_br(df, br, budget):
	if br == "0":
		br = "Studio"
	if br == "1": 
		br = "1_Bedroom"
	if br == "2": 
		br = "2_Bedrooms"
	if br == "3": 
		br = "3_Bedrooms"

	return(df[df[br] <= budget])