# Dict , TC = O(n)


arr = [1,2,3,4,5,1,2,3,4,5,6,6,6]

count_dict = {}

for num in arr:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

for key in count_dict:
    print(key, "->", count_dict[key])



# Inbuilt Counter , TC - O(n)


from collections import Counter

arr = [1,2,3,4,5,1,2,3,4,5,6,6,6]

count = Counter(arr)

print(count)




# Nested loop , TC = O(n^2)


arr = [1,2,3,4,5,1,2,3,4,5,6,6,6]

visited = []

for i in range(len(arr)):

    if arr[i] in visited:
        continue

    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    print(arr[i], "->", count)

    visited.append(arr[i])