# Store 15 values in a list
numbers = []

print("Enter 15 numbers:")

for i in range(15):
    num = int(input(f"Enter value {i+1}: "))
    numbers.append(num)

# Get target value
target = int(input("Enter the target value to search: "))

# Search for the target
found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Target found at index:", i)
        found = True
        break

if not found:
    print("Target not found.")