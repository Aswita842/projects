#when you enter a word this programs shows you how many letters are there in this (in descending order)
import operator
inpword=input('enter a word: ')
a=list(inpword.lower())
sa=sorted(a)

dictem={}

I=0
count=1
while I<(len(sa)-1):
    a1=sa[I]
    a2=sa[I+1]
    if a1==a2:
        count=count+1
        if I+1==len(sa)-1:
            dictem.update({a1:count})
    else:
        dictem.update({a1:count})
        count=1
    I=I+1

sorted_d = dict( sorted(dictem.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_d)
