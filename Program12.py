list1=list(map(int,input("Enter first list:").split()))
list2=list(map(int,input("Enter second list:").split()))


if len(list1)==len(list2):
     print("(a)Lists are of the same length")
else:
     print("(a)Lists are not of the same length")\


if sum(list1)==sum(list2):
     print("(b) Lists sum to the same value")
else:
     print("(b) Lists do not sum to the same value")


if set(list1).intersection(set(list2)):
     print("(c)Both lists contain common values(s)")
else:
     print("(c)No common values")
