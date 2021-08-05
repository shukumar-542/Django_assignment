#create file

file = open("file.txt", 'r')

# file.write("this is write file")

for i in file.readline():
    print(i, end="")
file.close()