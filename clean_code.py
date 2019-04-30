# clean data 
def clean(df, arry_col):
	df[arry_col] = df[arry_col].replace('\$', '', regex=True)
	df[arry_col] = df[arry_col].replace('\,', '', regex=True)
	df[arry_col] = df[arry_col].astype(float)

	return(df)

def clean_pvd(df, arry_col):
	df[arry_col] = df[arry_col].replace('\$', '', regex=True)
	df[arry_col] = df[arry_col].replace('\,', '', regex=True)
	df[arry_col] = df[arry_col].fillna(0).astype(int)

	return(df)

def clean_zip(x):
	return("0" + str(x))
