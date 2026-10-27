color_list1 = ["Red", "Green", "Blue", "Yellow", "Pink"]
color_list2 = ["Green", "Yellow", "Black"]

print("Colors in color_list1 but not in color_list2:")

for color in color_list1:
    if color not in color_list2:
        print(color)

