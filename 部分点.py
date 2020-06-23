
str = list(input())
s = int(input())
a = 0

for i in str:
    if i == "R":
        a += 1

if a >= s:
    print("Yes")
else:
    print("No")