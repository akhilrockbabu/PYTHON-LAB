'''Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square. '''

import math
def sqrt_even_num(n):
    l=[]
    if n<=9999 and n>999:
        for i in range(1000,n+1):
            if math.sqrt(i).is_integer():
                s=str(i)
                if s[0]!='0' and s[1]!='0' and s[2]!='0' and s[3]!='0':
                    if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0:
                        l.append(s)
    else:
        print('please enter a four digit number')
    return l


n=int(input("enter a four dgitit number"))
print(sqrt_even_num(n))


'''enter a four dgitit number9999
['4624', '8464']'''
    
