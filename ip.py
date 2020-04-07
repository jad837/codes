import csv

with open('latlong.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

#print(data)
pata=[]
the_file = open('list.txt','w')
for i in range(len(data)):
    #print(data[i])
    k=[]
    k.append(data[i][5])
    k.append(data[i][4])
    pata.append(k)
    the_file.write(str(k)+","+"\n")
print(pata)