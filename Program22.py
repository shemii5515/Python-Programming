numbers=list(map(int,input("Enter integres seprated by spaces:").split()))
positive=[n for n in numbers if n>0]
print("Positive numbers:",positive)


n=int(input("Enter No:"))
squares=[i*i for i in range(1,n+1)]
print("Squares:",squares)


word=input("Enter a word:")
vowels=[ch for ch in word if ch.lower() in "aeiou"]
print("Vowels:",vowels)


values=[ord(ch)for ch in word]
print("Ordinal values:",values)

