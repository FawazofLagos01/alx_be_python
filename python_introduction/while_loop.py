outer_count = 5
inner_count = 1
while outer_count > 0:
    while inner_count <= outer_count:
        print(inner_count, end="")
        inner_count = inner_count + 1
    print()
    outer_count = outer_count - 1