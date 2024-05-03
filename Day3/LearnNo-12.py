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

#------------------------- Example
This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#This will return the items from index 2 to the end.
#Remember that index 0 is the first item, and index 2 is the third
# Output ได้  ['cherry', 'orange', 'kiwi', 'melon', 'mango']

#---------------------
example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# Output ได้  ['orange', 'kiwi', 'melon']

#---------------------
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
# Output ได้  
Yes, 'apple' is in the fruits list

#--------------------- Change List Items
Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# Output ได้   ['apple', 'blackcurrant', 'cherry']


#--------------------- 
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
#--------------------- 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)    
 # Output ได้    ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']


#--------------------- 
Change the second value by replacing it with two new values:
#--------------------- 
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# Output ได้ ['apple', 'blackcurrant', 'watermelon', 'cherry']

#--------------------- 
Change the second and third value by replacing it with one value:
#--------------------- 
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# Output ได้  ['apple', 'watermelon']

#--------------------- 
Insert "watermelon" as the third item:
#--------------------- 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 
# Output ได้  ['apple', 'banana', 'watermelon', 'cherry']



#--------------------- 
Using the append() method to append an item:
#=============================
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# Output ได้  ['apple', 'banana', 'cherry', 'orange']

#--------------------- 
Insert an item as the second position:
#--------------------- 
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# Output ได้  ['apple', 'orange', 'banana', 'cherry']

#--------------------- 
Add the elements of tropical to thislist:
#--------------------- 
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# Output ได้  ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#--------------------- 
Add elements of a tuple to a list:
#--------------------- 
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) 
# Output ได้ ['apple', 'banana', 'cherry', 'kiwi', 'orange']




# Tuple unpacking

# Set

#Dictionary 
