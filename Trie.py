'''
Created on Apr 13, 2013

@author: avarga
'''

# This will allow you to store unhashables like lists in dict-like structure
# My documentation sucks so check out the example usage at the bottom

def store(d, state, data):
    if len(state) == 1:
        d[state[0]] = data
    else:
        if state[0] not in d:
            d[state[0]] = {}
        if isinstance(d[state[0]], dict):
            store(d[state[0]], state[1:], data)
        
def retrieve(d, state):
    if len(state) == 0:
        return d
    elif len(state) == 1:
        return d[state[0]] if state[0] in d else None
    else:
        return retrieve(d[state[0]], state[1:]) if state[0] in d and isinstance(d[state[0]], dict) else None
    
def retrieveAll(d, path = None):
    if path == None:
        path = []
    if isinstance(d, dict):
        for key,val in d.items():
            for n in retrieveAll(val, path+[key]):
                yield n
    else:
        yield path, d
    
def size(d):
    return sum([size(d2) for d2 in d.values()]) if isinstance(d, dict) else 1

### Example Usage ###

d = {}
store(d, [1,2,3], 'a')
store(d, [1,2,5], 'b')
store(d, [1,1], 'c')
store(d, [7], 'd')

print d                         # {1: {1: 'c', 2: {3: 'a', 5: 'b'}}, 7: 'd'}
print retrieve(d, [])           # {1: {1: 'c', 2: {3: 'a', 5: 'b'}}, 7: 'd'}
print

print retrieve(d, [1])          # {1: 'c', 2: {3: 'a', 5: 'b'}}
print retrieve(d, [1,2,5])      # b
print retrieve(d, [1,2,9])      # None
print retrieve(d, [1,2,5,6])    # None
print

print size(d)                   # 4
print

print list(retrieveAll(d))      # [([1, 1], 'c'), ([1, 2, 3], 'a'), ([1, 2, 5], 'b'), ([7], 'd')]
    
    
    
    
    


