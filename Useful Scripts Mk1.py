import csv
forces=[]
file=csv.reader(open('C:\\Users\\tw15036\\OneDrive - University of Bristol\\Documents\\Year 4\\GIP\\myFile.csv','r'))
forces=[]
for row in file:
    forces.append(row)
