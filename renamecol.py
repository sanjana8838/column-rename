import csv
import json
import pandas as pd 

with open('columnnames.json') as json_file:
    data = json.load(json_file)
    
print(data)


df = pd.read_csv('BESS 2 Nov 2023.csv')

for i in df.columns:
    for key in data:
        if i == key:
            print('match')

            df.rename(columns = {str(i):str(data[key])}, inplace=True)
            
df.to_csv('newfile.csv')

            
