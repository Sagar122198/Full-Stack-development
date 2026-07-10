container = [1,2,3,4,5,6,7]
for i in container:
    if i==3 or i == 5:
        continue
    print(i)
for i in container:
    if i==4:
        break
    print(i)

num = 0
while num <=10:
    num+= 1
    if num % 2 == 0:
        continue
    print(num)

while num <= 10000:
    num+=1
    if num == 10:
        break
    print(num)