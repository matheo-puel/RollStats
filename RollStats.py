import random
import sys

X = 100000
Float = 2

liste1 = []
liste2 = []
liste3 = []
liste4 = []
liste5 = []
liste6 = []

for i in range(X):
    R = random.randint(1,6)
    Loading = (i/X)*100
    print(round(Loading, 2), "%")
    sys.stdout.write("\033[F")
    if(R == 1): liste1.append(R) 
    elif(R==2): liste2.append(R)
    elif(R==3): liste3.append(R)
    elif(R==4): liste4.append(R)
    elif(R==5): liste5.append(R)
    elif(R==6): liste6.append(R)

l1 = len(liste1)
l2 = len(liste2)
l3 = len(liste3)
l4 = len(liste4)
l5 = len(liste5)
l6 = len(liste6)

p1 = (l1 / X) * 100
p2 = (l2 / X) * 100
p3 = (l3 / X) * 100
p4 = (l4 / X) * 100
p5 = (l5 / X) * 100
p6 = (l6 / X) * 100
total = p1+p2+p3+p4+p5+p6
print("1: ", round(p1, Float), "%")
print("2: ", round(p2, Float), "%")
print("3: ", round(p3, Float), "%")
print("4: ", round(p4, Float), "%")
print("5: ", round(p5, Float), "%")
print("6: ", round(p6, Float), "%")
print("Total: ", round(total, Float) , "%")
