tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

product = tuple(x * y for x, y in zip(tup1, tup2))

print(f"The tuples are {tup1} and {tup2}.")
print(f"The product of those tuples is {product}")