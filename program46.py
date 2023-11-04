'''Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square. '''


import math
n=int(input("enter a four dgitit number"))
l=[]
if n<=9999:
    for i in range(1000,n+1):
        if math.sqrt(i).is_integer():
            s=str(i)
            
            l.append(i)
print(l)





        
'''s=str(i)
if s[0]%2==0 and s[1]%2==0 and s[2]%2==0 and s[3]%2==0 :'''
