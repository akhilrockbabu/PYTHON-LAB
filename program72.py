#porgram to read and write in csv dict

import csv


f=open('prgrm72.csv','w+')
fields=['name','age','gender']
insert=csv.DictWriter(f,fieldnames=fields)
insert.writeheader()
rows=[{'name':'akhil','age':'21','gender':'male'},{'name':'dona','age':'20','gender':'female'}] 
insert.writerows(rows)

f1=open('prgrm72.csv',mode='r')
readit=csv.DictReader(f1)
for lines in readit:
    if readit:
        print(lines[0],'\t',lines[1],'\t',lines[2])
f1.close()
f.close()
