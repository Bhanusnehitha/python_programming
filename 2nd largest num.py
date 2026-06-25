numbers = list(map(int, input("Enter numbers separated by space: ").split()))

unique = list(set(numbers))
unique.sort()

if len(unique) >= 2:
    print("Second largest number:", unique[-2])
else:
    print("Second largest number does not exist.")