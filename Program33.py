n = int(input("Enter a number:"))
temp = n
s = 0
power = len(str(n))

while temp > 0:
    digit = temp % 10
    s = s + digit ** power
    temp = temp // 10

if s == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

