arr = list(map(int, input("Enter array elements: ").split()))

maximum = arr[0]
minimum = arr[0]

for num in arr:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("Maximum element:", maximum)
print("Minimum element:", minimum)