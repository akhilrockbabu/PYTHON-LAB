#porgram to read and write in csv dict

import csv


f=open('prgrm72.csv','w+')
fields=['name','age','gender']
insert=csv.DictWriter(f,fieldnames=fields)
insert.writeheader()
rows=[{'name':'akhil','age':'21','gender':'male'},{'name':'dona','age':'20','gender':'female'}] 
insert.writerows(rows)

read=csv.DictReader(f)
for lines in read:
    if lines:
        print(lines[name],'\t',lines[age],'\t',lines[gender])

f.close()
