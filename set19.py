#set is mutable
s={1,2,3,4}
print(s)
print(type(s))
name={'rahil','pamecha'}
print(name) #............random

empty_set=set()
set_from_list=set([1,2,3,1,5])
print(set_from_list)
bskt={"ap","bn","or","ap"}
print(len(bskt))
#set does not support indexing
print("or" in bskt)
for name in bskt:
    print(name)
a=set("mississippi")
print(a)
a.add('r')
print(a)
a.remove('m')#raise key error if 'm' is not present
print(a)
a.discard('x')  #same as remove, except no error
print(a)
a.pop()
print(a)
a.clear()
print(a)
print(len(a))
c=set("abrakadabra")
print(c)
d=set("alacazam")
print(d)
print(c-d)    #intersection
print(c|d)    #union
print(c & d) #.....common onr
print(c ^ d) #..symmetric differance....(c-d)|(c-d)
#READING IS EFFICIENT WITH SET
EFFICIENT_LETTER = "QWERTYIUOPXCVNMSDGFH"










































