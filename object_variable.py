print(isinstance(4,object))
print(isinstance("Hello",object))
print(isinstance(None,object))
print(isinstance([1,2,3],object))
'''gives object's identity
"identity" is unique and fixed during an object's lifetime
Objects are tagged with their type at runtime
Objects contain pointer to their data blob
This means even small things take up a lot of space'''
print(id(object))

print((624).__sizeof__())#find the size.
'''Variables
->variable are references to an object
->Assigning from a variable does not copy an object.
Instead, it adds another refrence to the same object.
Python will always handle the creation of new object.
'''

'''Duck Tying'''
def compute(a,b,c):
    return(a+b)*c

print(compute(1,2,3))
print(compute([1],[2,3],2))#when we add two list actually the list will be concated not added
print(compute("l","olo",4))
'''for compute all that number that should be suport + and * symbol'''
