#Import libraries
import csv
import json
import pandas as pd 

#Load json file as a dictionary
with open('columnnames.json') as json_file:
    data = json.load(json_file)

#Load csv to pandas dataframe
df = pd.read_csv('BESSdata.csv')

#Find if column names match dictionary
for i in df.columns:
    for key in data:
        if i == key:
            df.rename(columns = {str(i):str(data[key])}, inplace=True)

#Save modified dataframe to new csv file
df.to_csv('newfile.csv')

            
