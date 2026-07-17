def add(*args):
    print(type(args))
    total = 0 
    for num in args:
        total = total + num
    return total
total = add(1,2,4,52,52,52,64,67,32,6725,256,2,56,2,56,6,256,5,2)
print(total)