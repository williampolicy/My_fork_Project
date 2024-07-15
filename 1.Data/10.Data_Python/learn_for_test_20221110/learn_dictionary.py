from collections import defaultdict
animals = {
    'a': ['ant', 'antelope', 'armadillo'],
    'b': ['beetle', 'bear', 'bat'],
    'c': ['cat', 'cougar', 'camel']
}

animals = defaultdict(list, animals)

print(animals['b'])
print(animals['d'])