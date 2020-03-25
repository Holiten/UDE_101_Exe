nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]

new_list = []

for i in nombres:
    if i not in new_list:
        new_list.append(i)

print(new_list)