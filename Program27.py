n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    x = int(input("Enter an element: "))
    lst.append(x)

print("Sum =", sum(lst))

