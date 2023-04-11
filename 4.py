# tuple
t = (1, 2, 3, 4, 5, 6, 7)

# Length of tuple
print(len(t))

# Converting tuple into list
l = list(t)
print(l)

# Updating tuple by converting into list
l[3] = 6
t = tuple(l)
print(t)

# Appending tuple by converting into list
l.append(0)
t = tuple(l)
print(t)

# Using list() function by converting into list
t = (7, 8)
l = list(t)
print(l)