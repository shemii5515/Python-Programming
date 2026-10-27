import math

start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

lst = []

for n in range(max(start, 1000), min(end, 9999) + 1):
    root = math.isqrt(n)

    if root * root == n and all(int(digit) % 2 == 0 for digit in str(n)):
        lst.append(n)

print("The numbers are:", lst)

