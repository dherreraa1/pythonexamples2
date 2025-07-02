from itertools import batched, zip_longest, product, starmap, groupby

numbers: list[int] = [1,2,3,4,5,6,7]
my_batch: batched = batched(numbers, n=4)
print(next(my_batch))
print(next(my_batch))

names: list[str] = ['Bob', 'Joe', 'Jam']
numbers: list[int] = [1,2,3,4,5]
symbols: list[str] = ['#','$','%','?']

zipped: zip_longest = zip_longest(names, numbers, symbols)
zipped1: zip = zip(names, numbers, symbols)
print(list(zipped))
print(list(zipped1))

elements: list[str] = ['A','B','C']
my_product: product = product(elements, repeat=2)
for t in my_product:
    print(''.join(t))

def get_sum(a:int, b:int, c:int) -> int:
    return sum((a,b,c))

def get_sum1(*args) -> int:
    return sum(args)

data: list[tuple[int,int,int]] = [(1,2,3),(4,5,6)]
sums: starmap = starmap(get_sum,data)
print(list(sums))
sums1: starmap = starmap(get_sum1,data)
print(list(sums1))

data1: list[tuple[int,int]] = [(2,4),(3,3),(4,2)]
powers: starmap = starmap(pow,data1)
print(list(powers))

def count_vowels(word: str) -> int:
    counter: int = 0
    for letter in word:
       if letter in 'aeiouAEIOU':
        counter += 1
    return counter

words: list[int] = ['cat', 'dog', 'mood', 'banana', 'red']
sorted_words: list[str] = sorted(words, key=count_vowels)
grouped: groupby = groupby(sorted_words, key=count_vowels)

print(sorted_words)
for vowels, grouped_words in grouped:
    print(f'{ vowels=} {list(grouped_words)}')