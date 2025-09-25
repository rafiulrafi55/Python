s1 = input(str("Enter 1st alphabet : "))
s2 = s1.lower()
s3 = input(str("Enter 2nd alphabet : "))
s4 = s3.lower()

s5 = sorted(s2)
s6 = sorted(s4)

if s5 < s6:
    flag = s6
else:
    flag = s5

print(flag)