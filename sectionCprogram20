arr = list(map(int, input("Enter array elements: ").split()))

duplicates = []

for i in range(len(arr)):
    if arr[i] in arr[:i]:
        if arr[i] not in duplicates:
            duplicates.append(arr[i])

print("Duplicate elements:", duplicates)