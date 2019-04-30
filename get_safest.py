# filter cities that match crime input
def get_safest(df, crime):
	safest = [4,5]
	average = [3, 4, 5]

	if (crime == 4) or (crime == 5):
		return(df[df.Crime_Rating.isin(safest)])
	elif crime == 3:
		return(df[df.Crime_Rating.isin(average)])
	else:
		return(df)

# filter cities that match crime input
def get_safest_pvd(df, crime):
	safest = [4,5]
	average = [3, 4, 5]

	if (crime == 4) or (crime == 5):
		df = (df[df.Crime_Rates.isin(safest)])
		return(df[df["Dist_fm_Brown_Walking"] <= 45])
	elif crime == 3:
		df = df[df.Crime_Rates.isin(average)]
		return(df[df["Dist_fm_Brown_Walking"] <= 45])
	else:
		return(df[df["Dist_fm_Brown_Walking"] <= 45])

