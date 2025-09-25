s1 = input(str("Enter 1st a word : "))
s2 = s1.lower()
s3 = input(str("Enter 1st a word : "))
s4 = s3.lower()

s5 = sorted(s2)
s6 = sorted(s4)

if s5 == s6:
  print("The words are anagrams")
else:
  print("The words are not anagrams")