#Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64
#Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3]
n1=int(input('enter the length of first list: '))
a=[]
a1=[]
for i in range(0, n1):
    ele1=int(input('enter the element (click enter after entering the number):'))
 
    a.append(ele1)

for i in a:
    if i>0:
        a1.append(i)
print('output for list 1: ',a1)
    
n2=int(input('enter the length of second list: '))
b=[]
b1=[]
for i in range(0, n2):
    ele2=int(input('enter the element (click enter after entering the number):'))
 
    b.append(ele2)

for j in b:
    if j>0:
        b1.append(j)
print('output for list 2: ',b1)
    
