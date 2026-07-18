number = []
for i in [1,3,4,5,5,6]:
    number.append(i**2)
print(number)

#comprehension ---->
number = [i**2 for i in [1,3,4,5,5,6]]
print(number)