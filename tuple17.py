t=(1,"cat")
print(t)
myt=("name: rahil pamecha","DOB: 23 april 1997","Degree: MCA")
print(myt)
fish=(1,2,"red","blue")
print(fish[0])
#fish[0]=7  #raise a typeerror ...becoz tuple is immutable and can't be modified

print(len(fish))
fish[:2]
print("red" in fish)


#argument packing and unpacking
tu=1234,"abc",1.2
print(tu)
print(type(tu))
#unpacking
x,y,z=tu
print(x)
print(y)
print(z)

#swapping values
f=5
g=3
temp=f
f=g
g=temp
print(f,g)
#by bitwise operators
f=f^g
g=f^g
f=f^g
print(f,g)
#by tuple packing
f,g=g,f
print(f,g)

