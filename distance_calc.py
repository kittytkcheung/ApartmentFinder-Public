from math import sin, cos, sqrt, atan2, radians


def add_dist(df):
	df["Distance"] = df[["LAT", "LNG"]].apply(dist_calc, axis = 1)
	return(df)

# Calculate given distance to Brown and add to dataframe
def dist_calc(df):

	# approximate radius of earth in km
	R = 6373.0

	lat1 = df["LAT"]
	lon1 = df["LNG"]

	lat1 = radians(lat1)
	lon1 = radians(lon1)

	# Brown's coordinates
	lat2 = radians(41.826815)
	lon2 = radians(-71.402544)

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = (R * c) * .6214

	return(distance)

