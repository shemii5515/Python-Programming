names=input("Enter first names seprated by space:").split()
count=0
for name in names:
    count += name.lower().count('a')
print("Number of occurrences of 'a':",count)

