print(9/4)
print(9//4)

for i in range(10, -5, -2):
    print(i)
print(list(range(10, -5, -2)), end = " ")

x = [1,4,9,2]
print(x)
print(*x)

number: int = 10; 
print("Even" if number%2 == 0 else "Odd")

def my_sqr(a):
    return a**2

powers = map(my_sqr, x)
print(list(powers))
powers1 = map(lambda a: a**2, x)
print(list(powers1))

def longer_than_3(str):
    return len(str) > 3

strings = ["hi","hello","dot"]
filtered = filter(longer_than_3, strings)
print(list(filtered))
filtered1 = filter(lambda str: len(str) > 3, strings)
print(list(filtered1))

print(sum(x))
print(sorted(x))
print(x[-3:-1])
x.sort()
print(x)

matrix = [4*[0] for i in range(4)]
print(matrix)

matrix1=[4*[0] for i in range(4)]
for i in range(4):
    for j in range(4):
        if i==j:
            matrix1[i][j]=1

print(matrix1)

matrix2 = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
print(matrix2)

import numpy as np
y = [1,4,9,2]
z = np.array(y)
print(y)
print(z)
print(z[-3:])
print(z[:-3])

"""
from skimage import io
photo = io.imread('image.jpg')
import matplotlib.pyplot as plt
plt.imshow(photo)
plt.show()
"""

target = 18
q_target = []
q = [2,7,11,15]
# sol 1
for i in range(len(q)):
    for j in range(i,len(q)):
        if(q[i]+q[j]==target):
            q_target.append(q[i])
            q_target.append(q[j])
print(q_target)

# sol 2
q_target1 = []
my_dict = dict(zip(q,range(len(q))))
for i in my_dict:
    desired = target-i
    if desired in q and my_dict[desired] != i:
        q_target1.append(i)
print(q_target1)