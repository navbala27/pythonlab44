import csv

d = {1:'liverpool', 2:'chelsea',3:'city'}

with open ("sample.csv","w") as f1:
    csvdat = csv.writer(f1)
    
    for item in d.items():
        csvdat.writerow(item)
        
with open("sample.csv","r") as f1:
    csvdat = csv.reader(f1)
    for row in csvdat:
        print(" ".join (row))