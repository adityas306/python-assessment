numbers = list(map(int, input("Enter numbers: ").split()))

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Largest number:", largest)
print("Second largest number:", second_largest)