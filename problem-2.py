a = int(input("Enter a number: "))
for i in range(1, 2 * a, 2):
    print(i, end=', ' if i < 2 * a - 1 else '')
