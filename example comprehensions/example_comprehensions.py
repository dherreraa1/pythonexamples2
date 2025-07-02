x = [i for i in range(10)]
print(x)

lst = [[j for j in range(5)] for _ in range(10)]
print(lst)

y = 50
x = [i for i in range(y) if i%2 == 0]
print(x)

options = ["any", "albany", "apple", "world", "hello", ""]
z = [string for string in options if len(string) > 1 and string[0]=="a" and string[-1]=="y"]
print(z)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
flattened = [num for row in matrix for num in row] 
print(flattened)

w = ["Even" if num%2 == 0 else "Odd" for num in range(10)]
print(w)

import pprint

printer = pprint.PrettyPrinter()
lst3d = [[[k for k in range(5)] for _ in range(5)] for _ in range(5)]
printer.pprint(lst3d)

def square(x):
    return x**2

squared_nums = [square(x) for x in range(10)]
print(squared_nums)

pairs = [("a",1), ("b",2), ("c",3)]
my_dict = {k: v for k, v in pairs}
print(my_dict)

my_dict1 = {k: square(v) for k, v in pairs}
print(my_dict1)

nums = [1,2,2,3,3,3,4,4,4,4]
unique_squares = {square(x) for x in nums}
print(unique_squares)

sum_of_squares = sum(x**2 for x in range(1000000))
