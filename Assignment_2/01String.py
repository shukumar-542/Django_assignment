string = input("enter the string: ")

firstString = ""
lastString = ""

if len(string)<2:
    print("empty string")
else:
    firstString = string[0 : 2]
    lastString = string[-2:]

    result = firstString + lastString
    print(result)