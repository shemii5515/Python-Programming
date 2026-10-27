n = int(input("Enter number of items: "))
d = {}

for i in range(n):
    key = (input("Enter key: "))
    value = int(input("Enter value: "))
    d[key] = value

print("Ascending order:", dict(sorted(d.items(),key=lambda x: x[1])))
print("Descending order:", dict(sorted(d.items(),key=lambda x: x[1],reverse=True)))

