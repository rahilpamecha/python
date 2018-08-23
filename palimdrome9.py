word=input("plz enter a word:")
reversed_word = word[::-1]
if word == reversed_word:
    print("palimdrome")
else:
    print("not a palimdrone")
    
"""
>>> bool(None)
False
>>> bool(False)
False
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool('')
False
"""
data=[]
if data:                          #empty means false
    print(data)
else:
    print("empty")
