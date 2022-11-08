import random
m=int(input("Wprowadz liczbe"))
zestaw_1=[]
while n>0:
    zestaw_1.append(random.randrange(0,11))
    n+=1
print(zestaw_1)
zestaw_2=[]
n=int(input("Wproeadz liczbe"))
for i in range(m):
    zestaw_2.append(random.randrange(5, 16))
print(zestaw_2)
if t in zestaw_1:
    print("Liczba z zestawu 1")
if t in zestaw_2:
    print("Liczba z zestawu 2")
else:
    print("Niema takiej liczbe w obu zestawach")
zestaw_1_2=[]
zestaw_1_2=zestaw_1+zestaw_2
print(zestaw_1_2)
