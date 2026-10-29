def even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

num = int(input("Enter a number: "))
result = even_odd(num)

print("The number is", result)

