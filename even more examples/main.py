condition = False
x = 1 if condition else 0
print(x)

num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2 
print(f'{total:,}')

names = ['a','b','c','d']
for index, item in enumerate(names, start = 1):
    print(index, item)

codes = ['01','02','03','04']
universes = ['la','ny', 'sd', 'ch']
for item1, item2, item3 in zip(names,codes,universes):
    print(f'{item1} {item2} {item3}')

class Person():
    pass

person = Person()
person_info = {'first': 'Corey', 'last':'Schafer'}
for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))

from getpass import getpass

username = input("Username: ")
password = getpass("Password: ")
print("Loggin In...")

from datetime import datetime

print(datetime.today())