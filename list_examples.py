# empty list
a = []

b = [1, 2, 3, 4]

c = [9+8, "Noo", "-7", None]

print(a, b, c)

d = [1, 2, [3, 4, [5, 6]]]
print(d, len(d), len(d[2]), len(d[2][2]))

# list operations:
a = [1, 2, 3]
b = ["a", "b", "c"]
c = a + b
print(c)
e = 4*a
print(e)
print(e[1])
e[1] = 7
print(e)
for item in e:
    print(item)