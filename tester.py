print('spam eggs')
print('doesn\'t')
print("doesn't")
print('"yes,"he said.')
print("\"Yes,\" he said.")
print('"Isn\'t,"she said.')
print('*****************************************')    
print('I\'m in kolkata but I don\'t know that \"You are also here\".')
print('I\'ll see you in Hawrah!. But I\'ll request \'you\' to bring')
print('\"Rasogulla\" for me.')
print('*****************************************')
'''inbuilt function of string'''
greeting="Hello world!"
print(greeting[4])
print('world' in greeting)
print(len(greeting))
print(greeting.find('lo'))
print(greeting.replace('llo','y'))
print(greeting.startswith('Hell'))
print(greeting.isalpha())
print(greeting.lower())
print(greeting.upper())
print(greeting.title())#make every letters first char Capital
ss="hello and welcom All My Name Is!"
print(ss.strip('! '))#is used for deleteing elements from last
'''convert a sting into list'''
a="ham cheese bacan"
print(a.split(sep=' '))
b="30-12-2001"
print(b.split(sep='-'))
'''convert list into strin'''
print(', '.join(['lovely','professional','university']))

'''String Formatting'''
print('{} {}'.format('monthy','python'))
print('{} {}'.format(['a','b']))
print('{0} can be {1} {0}'.format("string","Formatted"))
print('{name} Loves {food}'.format(name="Sam", food="plums"))
print('{} squared is {}'.format(5,5**2))
'''fancier formatting'''
