my_list = [1,0,2,0,4,6]

for i in my_list:
    if i == 0:
        my_list.remove(i)
        my_list.append(i)

print(my_list)