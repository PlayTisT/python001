#=============================
#Lists (ต่อ)
#=============================
# Loop Lists  ใช้ Loop เพื่อช่วยในการเข้าถึงหรือปรับเปลี่ยนข้อมูล

money = [10, 20, 30, 40] 
total = 0
for i in range(len(money)):
    total = total + money[i]
print(total)
# Output ออกมาเป็นค่า   100

#หรือ การใช้ Loop รันตามตัวข้อมูลใน List ได้เลย
money = [10, 20, 30, 40] 
total = 0
for i in money:
    total = total + i
print(total)
# Output ออกมาเป็นค่า   100 เหมือนกัน

#------------------------------------------
# ลบข้อมูลออกจาก List ที่ใช้ del 

people = ["Alice", "Bob", "Carl", "Paarena", "Takkie"]
print(people)
del people[0]
print(people)
del people[0]
print(people)
del people[:]  
print(people)

# del people[:] คือ ลบข้อมูลออกจาก people ทั้งหมดแต่ยังคงเหลือตัว List ว่างเปล่าๆ
# Output ออกมาเป็นค่า ดังนี้
['Alice', 'Bob', 'Carl', 'Paarena', 'Takkie']
['Bob', 'Carl', 'Paarena', 'Takkie']
['Carl', 'Paarena', 'Takkie']
[]

#-----------ใช้ while loop  -------------------------------

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
# Output ออกมาเป็นค่า ดังนี้ 
apple
banana
cherry



#-----------------------------
# List Comprehension
#-----------------------------


# Sort Lists 
# Sort items เรียง (ascending Order, A-Z)
people = ["Alice", "Bob", "Carl", "Paarena", "Takkie"]
people.sort()
print(people)

# Output ออกมาเป็นค่า ดังนี้    ['Alice', 'Bob', 'Carl', 'Paarena', 'Takkie']
#-----------------------------

# Sort items  Descending Order, แบบ (Z-A)
people = ["Alice", "Bob", "Carl", "Paarena", "Takkie"]
people.sort(reverse=True) # กลับด้านกัน
print(people)
# Output ออกมาเป็นค่า ดังนี้   ['Takkie', 'Paarena', 'Carl', 'Bob', 'Alice']
#-----------------------------

# Remove last item in list

shopitem = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(shopitem)
shopitem.pop() # เอาหลังสุดออก
print(shopitem)
shopitem.append("Snake")
print(shopitem)
shopitem.remove("Snake") #ลบเฉพาะเลยถ้าเจอตัวแลก
print(shopitem)
shopitem.insert(1, "water melon")
print(shopitem)

# Output ออกมาเป็นค่า ดังนี้ 
['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']
['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'Snake']
['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']
['apple', 'water melon', 'banana', 'cherry', 'orange', 'kiwi', 'melon']

#----------------------------- List = List
items1 = ['egg', 'milk']
items2 = ['banana', 'orange']
print(items1+items2)
# Output ออกมาเป็นค่า ดังนี้  ['egg', 'milk', 'banana', 'orange']


# Copy Lists   # Join Lists
