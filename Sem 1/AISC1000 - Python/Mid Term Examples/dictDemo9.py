myDict1 = {}
myDict1['ibm']='12345'
myDict1['ibm-x']='23098'
myDict1['hp']='28764'
myDict1['dell']='09416'
server_list2=[] # initilizing a new list
for key,value in myDict1.items():
    #print (type(key))
    print(value)
    if (key == 'ibm') or (key == 'hp'):
        server_list2.append (value)
print(server_list2)