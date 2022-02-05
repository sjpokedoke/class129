import csv

data = []

with open("data2.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
planetdata = data[1:]

for datapoint in planetdata:
    datapoint[0] = datapoint[0].lower()

planetdata.sort(key=lambda planetdata:planetdata[0])

with open("data2sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerow(planetdata)