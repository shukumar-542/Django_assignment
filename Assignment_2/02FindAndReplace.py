str = "the srting is not that poor"

notindex= str.find("not")
poorindex= str.find("poor")

if notindex < poorindex and notindex > 0 and poorindex > 0 :
    str = ''.join((str[:notindex],"good"))
print(str)