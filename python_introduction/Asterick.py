rows = 5
i = 1

while i <= rows:
    j = 1
    while j <= rows - i:
        print(" ", end="")
        j = j + 1

k = 1
while k <= (2 * i - 1):
    print("*", end="")
    k = k + 1
print()
i = i + 1