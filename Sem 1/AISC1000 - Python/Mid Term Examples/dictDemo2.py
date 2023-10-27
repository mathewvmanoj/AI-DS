#myDict2 = {('empName1','empName2'): ['Simon','Jack'], 'title': 'Director', 'yOfEmp':9}
myDict2 = {'empName1': ['Simon','Jack'], 'title': 'Director', ('yOfEmp1','yOfEmp2'):[9,10]}

print(myDict2['empName1'])
print(myDict2['title'])
print(myDict2[('yOfEmp1','yOfEmp2')])
print(myDict2)
#myDict2.pop(0)
myDict2.pop('empName1')
print(myDict2)
print(myDict2.items())

