import random
mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))        

print(random.choices(mylist, k=2)) 

print(random.sample(mylist, k=2))   

random.shuffle(mylist)

print(mylist)                   

print(random.randrange(3, 9))      
