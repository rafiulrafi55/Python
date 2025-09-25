s1 = input(str("Enter 1st word : "))
s2 = s1.lower()
s3 = input(str("Enter word : "))
s4 = s3.lower()

if s2.__eq__(s4):
    print("The words are anagrams")
else:
    print("The words are not anagrams")