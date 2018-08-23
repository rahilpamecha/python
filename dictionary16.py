empty={}
print(type(empty))
print(empty == dict())   #=> True

a=dict(one=1,two=2,three=3)
b={"one":1,"two":2,"three":3}
print(a==b)




my_dic={"name":"Rahil Pamecha","Skillset":"Python","UID":123151005}
print(my_dic)
print(my_dic["name"])
#print(my_dic["achievement"])   #=>raises keyError

my_dic["strength"]="tolerance"
my_dic["UID"]=153838531843
print(my_dic)

#create a dictionary using list
di={"CS":[100,102,123],"MATH":[125,152]}
#di["STATS"] raises error
print(di.get("CS"))
print(di.get("MATH"))
print(di.get("STATS"))   #=> None iistead of a keyerror

english_classes=di.get("ENGLISH",[])  #works even if we don't have english class in our dictionary
num_english=len(english_classes)
print(english_classes)
print(num_english)
del b["three"]
print(b)
b.pop("one",)    #=>3
print(b.popitem())   #it is destructive deletion

c={"one":1,"two":2,"three":3}
print(c.keys())
print(c.values())
print(c.items())
print(len(c.keys()))
print(("one",1) in c.items())   #member in function
for value in c.values():
    print(value)
print(len(c))
print("one" in c)
print(1 in c.values())
e=c.copy()
print(e)




    
