"""
datatype tells about the type ofdata thst a variable is holding on 
datatypes were catogarized 
1.numbere
2.sequece
3.boolean
4.set
5.dictionary
"""
# number --- which tells about the number datatypes divided into "3"types
"""
integer --- which holds all the positive and negative wholenumbers is 0 to n and 0 to -n
integer can be represented as int() 
"""
a=123
print(a)
print(type(a))
print(id(a))

"""
type--which tells about the datatype
id-- which tells about the address location of a variable value
"""

a1=-90
print(a1)
print(type(a1))
print(id(a1))

"""
float -- which holds all the decimalmor fractional values i.e 0 to n.n and 0 to -n.n
it can be represented as float() 
"""

b=89.456
print(b)
print(type(b))
print(id(b))

b1=-78.67
print(b1)
print(type(b1))
print(id(b1))

"""
complex datatypes are used ton hold the real and imaginary values
which can be represented as a+bj
"""

c=78+67j
print(c)
print(type(c))
print(id(c))

c1=-456+78j
print(c1)
print(type(c1))
print(id(c1))

"""
sequence datatypes are divided into "3"types
1.string
2.list
3.tuple
"""
"""
string : it is a collection of / group of characters
it can be enclosed using the single quotes or double quotes
"""

a="ists"
print(a)
print(type(a))
print(id(a))

d='ists'
print(d)
print(type(d))
print(id(d))

"""
list : it is a collection of items/values/elements
syntax : listname = [val1, val2,.... valn]
it is mutable-changeable
"""

mylist = [23, 45.67, 56+89j, "hello"] #items/vlues/elements = 4
print(mylist)
print(type(mylist))
print(id(mylist))
print(mylist[2])

"""
in order to acess the elements individually we use indexing
indexing always starts with "0" ends with n-1
syntax to acews the elements
print(listname[element position])
"""

"""
tuple is a collection of values/items/elements
syntax : tuplename = (val1, val2,.... valn)
it is immuatable - unchange
"""
                         #sublist  #subtuple
mytuple=(12, 23.67, "hi", [1,2,3], (56,67,89))
print(mytuple)
print(type(mytuple))
print(id(mytuple)) 
print(mytuple[3])

"""
giving a list within a list is called sublist
giving a tuple within a list is called subtuple
"""

"""
boolean : boolean means check the condition 
they are divided to two ways 1.True 2.False
it can be represented as bool
"""

a= True
print(a)
print(type(a))

b=False
print(b)
print(type(b))

"""
set : it is a collection of values/items/elements
syntax : setname = {val1, val2,.... valn}
a set can't accept the list...
"""
myset = {12, 23.34, 56+78j, "hi", (45,"hello"), True}
print(myset)
print(type(myset))

"""
dictionary : it is a collection of key value pairs
syntax : dictionaryname ={key:val1, ket:val2,..... key:valn} 
"""
mydict={"clg":"ists", "branch":"ece", "loction":"rjy"}
print(mydict)
print(type(mydict))