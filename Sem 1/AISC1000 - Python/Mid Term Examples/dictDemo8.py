#creating a new dictionary
myDict1 = {}
myDict1['ibm']='12345'
myDict1['ibm-x']='23098'
myDict1['hp']='28764'
myDict1['dell']='09416'
#search = input('enter the server code you search for: ')
keepGoing="y"
while (keepGoing=="y"):
    search = input('enter the server code you search for: ')
    for server, code in myDict1.items():
        if code == search:
            print (server)# you can append the server into a list OR you can delete it
            break
    else:print ('server is not found')#else is executed when the loop does exit normally
    keepGoing= input ("Do you want to continue ?(y/n): ")
print (" thanks for using the app.")
# improve the program so you ask the user if she/he want to continue with the app
# or stop ( "do you want to try again?(y/n): ")
#if entered y, the program keeps going, if entered n, the program does exist.
# use while loop
