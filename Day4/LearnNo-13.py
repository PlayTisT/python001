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
del people[:]  # ลบข้อมูลออกจาก people ทั้งหมดแต่ยังคงเหลือตัว List ว่างเปล่าๆ
print(people)

# Output ออกมาเป็นค่า ดังนี้
['Alice', 'Bob', 'Carl', 'Paarena', 'Takkie']
['Bob', 'Carl', 'Paarena', 'Takkie']
['Carl', 'Paarena', 'Takkie']
[]

#------------------------------------------



List Comprehension
Sort Lists
Copy Lists
Join Lists
