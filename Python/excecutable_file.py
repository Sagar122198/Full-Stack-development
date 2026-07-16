fileName = input("Enter file name : ")
fileContent = input("Write the content : ")
with open(fileName , "a") as file:
    file.write(fileContent)
readFile = input("Type 'Y' to read file and 'N' to exit")
if readFile == 'Y':
    with open(fileName , "r") as file:
        print(file.readlines())
else:
    print("Thank you")