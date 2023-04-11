my_list=[12,25,55,65,57,4]
print(f"My mixed list :{my_list}")
my_even = []
my_odd = []
for num in my_list:
    if num % 2 == 0:
        my_even.append(num)
    else:
        my_odd.append(num)
print(f"My even list :{my_even}")
print(f"My even list :{my_odd}")