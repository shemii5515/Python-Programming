def compare(s1, s2, n):
    if s1[:n] == s2[:n]:
        return True
    else:
        return False

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
n = int(input("Enter the number of characters: "))

print(compare(s1, s2, n))

