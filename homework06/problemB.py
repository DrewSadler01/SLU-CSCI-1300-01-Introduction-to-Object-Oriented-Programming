from cs1graphics import *
name=input('What is your name? ')
space=name.index(' ')
space1=name.count('')
middle=space+1
nexts=name.index(' ',middle)
middlei=name[middle:middle+1]
firstname=name[0:space]+' '
nexts=nexts+1
lastname=name[nexts:space1]
print(firstname+middlei+'. '+lastname)
