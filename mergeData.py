#April
#generic function to merge to datasets using two columns from two CSV files

import requests
import pandas as pd

# Create a function that takes in csv 1 filename, csv 2 filename, merges on city, writes merged csv filename?
def masterMerge(csv1Filename, csv2Filename, mergeCol, mergedCsvFilename):
	
	csv_1 = csv1Filename
	csv_2 = csv2Filename

	# 1. Read data from first CSV, use City column
	csv_1 = pd.read_csv(csv_1, dtype={mergeCol: str})
			
	# 2. Read data from first CSV, use City column
	csv_2 = pd.read_csv(csv_2, dtype={mergeCol: str})
	
	# check city data are string/object
	# print(csv_1.dtypes)
	# print(csv_2.dtypes)
	
	# 3. Merge data on city
	mergedData = csv_1.merge(csv_2, on=mergeCol, how="left")
	# print(mergedData)

	# 4. Write out new merged csv with all columns from both CSVs
	# Write separate function to read dataframe with only relevant columns and write that master CSV? Would be three lines of code.
	mergedData.to_csv(mergedCsvFilename, index=False, float_format="%g")

# main()