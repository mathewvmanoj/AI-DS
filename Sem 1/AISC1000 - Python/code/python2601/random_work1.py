import random
print(random.random()) #returns 0 to 1 float
t1 = (10, 20, 30, 40, 50)# a tuple
l1 = [10, 20, 30, 40, 50]# a list
print()
print (random.choice(t1))#randomly selects one element from t1
print()
print (random.uniform(3, 8)) #randomly selects one float between 3 and 8
print()
print (random.randint(3, 8))#randomly selects one integer between 3 and 8
print()
'''l2=[]
random.shuffle(l1)
l2=l1
print(l2)
print(l1)'''
#how we shuffle tuple?
