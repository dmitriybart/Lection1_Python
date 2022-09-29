# Использование циклов
original = 25
inverted = 0
while original != 0:
    inverted = inverted*10+(original%10)
    original //= 10
print(inverted)

# использование For
list = [1,2,3,4,5]
for i in list:
    print(i**2)


for i in range(1, 10, 2): #(отб до-1, шаг)
    print(i)