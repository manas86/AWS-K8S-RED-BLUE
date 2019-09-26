a = [[1,8], [2,8]]
b = [[3,16], [4,16], [7,5]]
final = 20
arr = []

for x in a:
    for y in b:
        print([[x[0],y[0]], x[1]+y[1], x[1]+y[1] - final])
        arr.append([[x[0],y[0]], x[1]+y[1], x[1]+y[1] - final])

# arr = [[[1, 4], 10, 0], [[1, 5], 10, 0], [[3, 2], 9, -1], [[3, 4], 15, 5], [[3, 5], 15, 5]]

final_list = sorted(arr, key=lambda x: x[2])
print(final_list)


maxitem = max(final_list, key=lambda x: x[2])
maxitem_Index = final_list.index(maxitem)
print(maxitem_Index)
print(final_list[:maxitem_Index])
print(max(final_list[:maxitem_Index],key=lambda x: x[2]))
print(final_list[maxitem_Index:])
print(max(final_list[maxitem_Index+1:], key=lambda x: x[2]))
secondmaxitem = max(max(final_list[:maxitem_Index]), max(final_list[maxitem_Index+1:]))

print(maxitem, secondmaxitem)