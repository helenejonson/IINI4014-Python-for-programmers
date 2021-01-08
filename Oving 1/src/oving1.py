f = input("forname: ")
l = input("lastname: ")
a = f.split()
b = l.split()
tot = ""
for i in range(len(a)):
    s = a[i]
    tot += s[0]
for i in range(len(b)):
    s = b[i]
    tot += s[0]
print("Initials: " + tot)
print("Hi! Welcome to Python programming " + f + " " + l + ".")