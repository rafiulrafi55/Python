s1  = input(str("Enter a word : "))
s = s1.lower()
s3 = s[::-1]
if s == s3:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")

