"""
list is a collections/group of items/values/elements
they can be enclosed within the square brackets[] seperated by(,)
list methods: append/extend/count/mutability/index/remove/pop/insert
syntax:listname.methodname()

"""
#append: this method is used to add the elements
# list1=[ "india", "scotland", "spain"]
# print(list1)
# list1.append("london")
# print(list1)

#extend:this method is used to add the elements at the end but as a sublist

# list2=[ "guava", "orange", "apple", "kiwi"]
# print(list2)
# list2.extend( ["grapes", "dragon","pineapple", "blueberry"])
# print(list2)

#count: this method counts the number of repeated elements in a list
# flowers=[ "rose","sunflower", "jasmine", "mariegold", "lotus"]
# flowers.count(("rose"))
# print(flowers)

#mutability : changing the elements in a list
#using mutability the element will be removed 
# mylist=["hello","ece",123,34.56,56+78j]
# print(mylist)
# mylist[2]="agri"
# print(mylist)

#pop: removes the elements using index
# list3=[12,34,565,78.9,34+56j,"Hello"]
# print(list3)
# list3.pop(2)
# print(list3)
#remove: removes the element directly that present in a list
# list3.remove(34)
# print(list3)

#count: its counts the number of occurance of a item in a list 
#NOTE:(it takes one arguement at a time)
# list4=[22,33,33,22,55,22,44,67,56,22]
# print(list4.count(22))

#insert: it just inserts the element into the list using the index
#syntax: list.insert(position,element)
#by using insert no element is removed they just replaces the position
# list5=[22,33,44,77,88]
# print(list5)
# list5.insert(1,"Hello")
# print(list5)

#index: this method tells the index of first occurance of a element
# list6=[22,44,55,55,44,66,67,89]
# print(list6.index(44))
# print(list6.index(55))
#reverse: it just reverse the elements
# list6.reverse()
# print(list6)

#copy: it just copy the elements in a list
# list7=[22,33,44,55,66,77]
# print(list7)
# list8=list7.copy()
# print(list8)
#clear: it clears the elements in a list
# print(list8.clear())
# print(list8)

#sort: it just arrange the elements in a sorting array
# to sort we have to give homogenious elements
# list9=[22,11,77,9,89,0]
# list9.sort()
# print(list9)
# list10=["m","a","k","b","c","s","k","j"]
# list10.sort()
# print(list10)
# list11=[12,13,"hello"]
# list11.sort()
# print(list11)
#in built functions
list12=[23,34,56,89]
print(len(list12))
print(max(list12))
print(min(list12))
print(sum(list12))