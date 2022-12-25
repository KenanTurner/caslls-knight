# returns the logical and function
def func_and(*fs):
    return lambda *args, **kwargs: all(map(lambda f: f(*args, **kwargs), fs))
# returns the logical or function
def func_or(*fs):
    return lambda *args, **kwargs: any(map(lambda f: f(*args, **kwargs), fs))

# Goal: functional regular expressions
# Syntax:
#  is_one = lambda x: x == 1
#  is_two = lambda x: x == 2
#  is_three = lambda x: x == 3
#  is_four = lambda x: x == 4
#  is_three_or_four = func_or(is_three, is_four)
#  pattern = [is_one, is_two, is_three_or_four]
#  search(pattern, [1,2,3]) == [(0,is_one),(1,is_two),(2,is_three_or_four)]
#  search(pattern, [1,2,4]) == [(0,is_one),(1,is_two),(2,is_three_or_four)]
#  search(pattern, [0,0,0,0,1,2,3]) == [(3,is_one),(4,is_two),(5,is_three_or_four)]
#  search(pattern, [0,0,0]) == []
#  search(pattern, [1,0,0,2,0,0,3]) == [(0,is_one),(3,is_two),(6,is_three_or_four)]
#  search(pattern, [1]) == [(0,is_one)]
def search(pattern, items):
    if len(pattern) == 0:
        return []
    for index,item in enumerate(items):
        if pattern[0](item):
            return [(index, pattern[0]), *map(lambda x: (x[0] + index + 1,x[1]), search(pattern[1:],items[index+1:]))]
    return []

def is_pattern(pattern, items):
    match = search(pattern, items)
    return len(match) == len(pattern)