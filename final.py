import csv

data1list = []
data2list = []

with open("data1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data1list.append(row)

with open("dataset_2_sorted.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data2list.append(row)

headers1 = data1list[0]
planetdata1 = data1list[1:]

headers2 = data2list[0]
planetdata2 = data2list[1:]

headers = headers1+headers2
planetdata = []

for index, datarow in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerow(planetdata)