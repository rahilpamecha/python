easy_as=[1,2,3]
print(easy_as)
print(type(easy_as))

#empty list
empty=[]
print(empty)
letters=['a','b','c','d','e']
print(letters)
mixed=[4,5,"seconds"]
print(mixed)
numbers=[1,2,3,4]
numbers.append(5)
print(numbers)

print(numbers[0])
print(numbers[-1])

print(letters[:3])
print(letters[1:-1])


#nested list

x=[letters,numbers]
print(x)
print(x[0])
print(x[0][1])
print(x[1][2:])


"""
>>> len([])
0
>>> len("python")
6
>>> len([1,2,3,4,5,6,])
6
>>>
>>> len([4,5,"second"])
3

now, member in function
>>> 'p' in 'Python'
False
>>> 'P' in 'Python'
True
>>> 'R' in 'Rahil'
True
>>> 'a' in 'Rahil'
True
>>> 'h' in 'Rahil'
True
>>> 'i' in 'Rahil'
True
>>> 'l' in 'Rahil'
True
>>>0 in []
False
>>> 'Apple' in ['Banana','grapes','apple']
False
>>> 'Apple' in ['Banana','grapes','Apple']
True

"""


