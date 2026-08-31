num = int(input("Enter a number: "))

original = num
num = abs(num)

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if abs(original) == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")