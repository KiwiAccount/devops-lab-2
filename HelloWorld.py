# This used to print hello world using python but oops

for i in range(1, 11):
    print(i)

# New string

print("This is a new string")

# Oh its saying something again

print("Welcome!`")

# Average

numbers = {1, 2, 3, 4, 5}
total = sum(numbers)
average = total / len(numbers)

# this part was added by a colleague

numbers = []

while True:
    try:
        num = float(input("Enter a number, any non num value will quit): "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("No valid numbers entered")
 
# second update to try again

print("HELLO")
