import csv

data = []
with open("dwarf_stars.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
star_data = data[1:]

for data_point in star_data:
    data_point[2] = data_point[2].lower()

star_data.sort(key=lambda star_data: star_data[2])

with open ("dwarf.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerow(star_data)