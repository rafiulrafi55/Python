s1= input(str("Enter a sentence : "))
s2 = (bool(s1.find("@" or "#" or "$" or "%")))
if s2 == True:
    print("Strong Password")
else:
    print("Weak Password")
