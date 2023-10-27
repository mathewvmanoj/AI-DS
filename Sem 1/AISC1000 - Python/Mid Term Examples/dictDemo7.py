myDict1 = {}
myDict1['ibm']='12345'
myDict1['ibm-x']='23098'
myDict1['hp']='28764'
myDict1['dell']='09416'
myDict1['asus']='99880'
print (len(myDict1))
print ('get (key) works the same as myDict1[\'key\']',myDict1.get('ibm'))
print()
print (myDict1.get('ibm-y'))
#print (myDict1['ibm-y'])
print ("myDict1 keys are: ",myDict1.keys())# retrieves all keys
print ("myDict1 values are: ",myDict1.values())# retrieves all values
print ("myDict1 entries are: ",myDict1.items())# retrieves all entries
myDict1.popitem()# removes the last entry
print (myDict1)
print(myDict1.pop('dell'))
print (myDict1)
print(myDict1.pop('asus',' it does not exist'))
#del myDict1['asus']