my_array = [5,1,1,2,2,3,4,5,7,8]
vec1  = []
vec2 = []

if len(my_array) % 2 != 0:
	print("Not possible")
else:
	for i in my_array:
		if i in vec1 or len(vec1) != len(vec2):
			vec2.append(i)
		else:
			vec1.append(i)
if len(vec1) != len(vec2):
	print("Not possible")
else:
    print("Possible")
    print(vec1)
    print(vec2)