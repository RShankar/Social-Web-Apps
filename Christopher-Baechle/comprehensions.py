

mylist = [2,4,6,8,10]

for x in mylist:
    print x

[x for x in mylist]

o = [x for x in mylist]
type(o)

[x*3 for x in mylist]

[x*3 for x in mylist if x > 5]

[x*3 for x in mylist if x*3 > 20]

[x*3 for x in mylist if x*3 > 20 and x*3 < 30]

[x for x in [2,4,6]

[x for x in (2,4,6)]

#2-dimensional

mylist1 = [2,4,6,8]
mylist2 = [3,5,7,9]

for x in mylist1:
    for y in mylist2:
        print x*y

[x*y for x in mylist1 for y in mylist2]

[mylist1[i]*mylist2[i] for i in range(0,len(mylist1))]

#Set comprehensions
o = {1,3,5,7}

{x for x in (1,3,5,7) }

{x for x in (1,3,5,7,5,3) }

#Dictionaries
people = ['Tom','Bob','Jeff']
ages = [54,11,22]
zip(people,ages)

dict(zip(people,ages))

{ k:v for (k,v) in zip(people,ages) }

#URL queries
url = '?max_id=12345&q=NCAA&include_entities=1'
url[1:]
url[1:].split('&')
dict ( [ kv.split('=') for kv in url[1:].split('&') ] )






