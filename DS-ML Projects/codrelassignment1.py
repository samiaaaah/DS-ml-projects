#1
name= "samiya"
age=19
height=5
print("my name is:{}.".format(name))
print ( "my age is:{}.".format(age))
print("my height is:{}.".format(height))

#2
a=6.0879
print(type(a))
a=int(a)
print(type(a))
print(a)





#3)list
months=["january","february","march","april","may","june","July","august","September","October","november","december"]
print(months[0],months[2],months[4],months[6],months[8],months[10])
print(months[1],months[3],months[5],months[7],months[9],months[11])

#4,5
odd=["january","march","may","july","september","november"]
even=["february","april","june","august","october","december"]
print(odd[4])
print(even[3])
print(even[1:6])

#6)adddays
week=["monday","tuesday","wednesday","thursday","friday","saturday"]
even1=even+week
print(even1)

#functions
odd=["january","march","may","july","september","november"]
print(len(odd))
print(type(odd))
del(odd[5])
print(odd)
odd[2]="saturday"
print(odd)
