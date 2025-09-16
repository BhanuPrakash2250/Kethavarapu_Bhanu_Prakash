a = int(input("Enter a number: "))
# If input is even, use previous odd number
if a % 2 == 0:
    a -= 1

# Print odd numbers from 1 to a (inclusive)
for i in range(1, a + 1, 2):
    print(i, end=', ' if i < a else '')
