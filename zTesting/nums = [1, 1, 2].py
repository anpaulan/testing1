nums = [1, 1, 2, 2 , 3, 4, 4, 45]
counts = dict()
for x in nums:
    if x not in counts:
        counts[x] = 1
    else: 
        counts[x] = counts[x] + 1
unique = counts.keys()
list = []
for i in unique:
    list.append(i)


print(len(list))