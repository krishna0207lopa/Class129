import csv
import pandas as pd

file1 = 'dwarf_stars.csv'
file2 = 'Stars_data.csv'

dataset1 = []
dataset2 = []
with open("dwarf_stars.csv") as data1:
    csv_reader =csv.reader(data1)
    
    for i in csv_reader:
        dataset1.append(i)
        
with open("Stars_data.csv",'r') as data2:
    csv_reader = csv.reader(data2)
    
    for i in csv_reader:
        dataset2.append(i)

headers1 = dataset1[0]
headers2 = dataset2[0]

stars_dataset_1 = dataset1[1:]
stars_dataset_2 = dataset2[1:]

h = headers1+headers2

stars_data =[]

for ds in stars_dataset_1:
    stars_data.append(ds)
for st in stars_dataset_2:
    stars_data.append(st)

with open("Stars.csv",'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(stars_data)
    
df = pd.read_csv('Stars.csv')
