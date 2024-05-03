#=============================
#Lists
#=============================
# เริ่มจาก mylist = ["apple", "banana", "cherry"] 

thislist = ["apple", "banana", "cherry"]
print(thislist)
# Output ได้  ['apple', 'banana', 'cherry']

#-------------------------
# Allow Duplicates
#=============================
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# Output ได้ ['apple', 'banana', 'cherry', 'apple', 'cherry']


#-------------------------
# List Length
#=============================
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# Output ได้  3

#-------------------------
# List Items - Data Types
#=============================
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)
# Output ได้  ['apple', 'banana', 'cherry']
#            [1, 5, 7, 9, 3]
#            [True, False, False]

#-------------------------
# A list with strings, integers and boolean values:
#-------------------------
list1 = ["abc", 34, True, 40, "male"]
print(list1)
# Output ได้  ['abc', 34, True, 40, 'male']

#-------------------------
# What is the data type of a list?
#-------------------------
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# Output ได้   <class 'list'>

#-------------------------
# the list() constructor to make a List:
#-------------------------
thislist = list(("apple", "banana", "cherry"))
print(thislist)
# Output ได้  ['apple', 'banana', 'cherry']

#-------------------------
# Print the second item of the list:
#-------------------------
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# Output ได้  banana  (#The first item has index 0.)

#-------------------------
# Negative Indexing
#-------------------------
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# Output ได้  cherry

#-------------------------
# Range of Indexes
#-------------------------
# Return the third, fourth, and fifth item:
Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# Output ได้   ['cherry', 'orange', 'kiwi']

#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

#------------------------- Example
This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# Output ได้   ['apple', 'banana', 'cherry', 'orange']



# Tuple unpacking

# Set

#Dictionary 
