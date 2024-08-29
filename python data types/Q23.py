listt = [2, 3, 5, 6, 7,88,2,4, 66,43, 53,78,9,43,22]
list2 = []
for item in listt:
    if item not in list2:
        list2.append(item)
print(list2)