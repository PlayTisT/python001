#==========================================================
# Tuple เหมือน list แต่เป็น () is immutable  (im แปลว่าไม่)
#  เพิ่มอะไรเข้าไปในนั้นไม่ได้
#==========================================================

tup_items = ('egg', 'bread', 'coke')
tup_items

# Output จะแสดงเป็น ('egg', 'bread', 'coke')

 # ทีนี้เราลองเพิ่ม item เปลี่ยนตำแหน่ง 0 เข้าไป 
 tup_items[0] = 'sprite' #มันจะ error ไม่ assignment เข้าไปได้
 
 # ลองพอกด  tup_items.  ดอท  จะมีแค่ 2  (count  and index ) เพราะมันเปลี่ยนค่าไม่ได้ 
 
 เช่น  tup_items = ('egg', 'bread', 'bread', 'coke', 'coke',)
 tup_item.count('bread')

# Output ออกมา แค่ค่าเท่ากับ   2

#------------------------------------------------------------------------------
#username password
#student1, student2

s1 = ("id001", "123456")
s2 = ("id002", "654321")
#ประกาศ tuple ขึ้นมา แล้ว ปริ้นต์  // เหมือนประกาศมา แต่แก่ไขไม่ได้ เก็บใน DB แต่ไม่สามารถอัพเดทได้ 
user_pw = (s1, s2)
print(user_pw)
# Output จะแสดงเป็น (('id001', '123456'), ('id002', '654321'))
#------------------------------------------------------------------------------

# tuple  unpacking 2 ตัวแปร กระจ่ายวิ่งไปเก็บที่ตัวแปลที่ประกาศ   (ใช้โค๊ดต่อเนื่องจากด้านบน)
username, password = s1
print(username, password)
id001 123456
# ตย tuple  unpacking 3 ตัวแปร 
name, age, gpa = ("Karn", 35, 2.86)
print(name, age)  # ลองใส่เรียก 2 ตัวแปร  # Output จะ error ไม่ออก
# จึงใช้วิธีแก้  gpa เป็น  _  ไว้ก่อน ตามด้านล่าง ----------
name, age, _ = ("Karn", 35, 2.86)
print(name, age)    # Output จะออกเป็น Karn 35 



#==========================================================
# Set  {unique} เก็บเฉพาะค่ายูนีค โชว์ค่าที่ไม่ซ้ำกันเป็น O/P ออกมา
#  เพิ่มอะไรเข้าไปในนั้นไม่ได้
#==========================================================
pet = ["Cat", "Dog", "Dog", "Dog", "Bird", "Fish"]
set(pet) 
#ผลออกมาเป็น {'Cat', 'Dog', 'Bird', 'Fish' }
#ถ้าแก้ตัวใน setเป็น case sensitive ก็จะเรียกมาเช่นกันเช่น
pet = ["Cat", "Dog", "DOG", "Dog", "Bird", "Fish"]
set(pet) 
#ผลออกมาเป็น {'Cat', 'Dog', 'DOG', 'Bird', 'Fish' }



#==========================================================
# dictionary  key : Value pairs   ซ้ายมือ Key  ขวา จะเป็น Value    โดยที่ Key (ต้องเป็น immutable ก็ใช้ string เพิ่มอะไรเข้าไปในนั้นไม่ได้  )  
# แต่ list, dictionary เป็น mutable
#==========================================================
course = {
          "name" : "Data sci class",
          "duration" : "4 months", #ตัวอักษร
	      "students": 200,   # ใช้ 200
	      "replay" : True,
          "skills" : ["SQL", "R", "Stats", "Dashbroad"]
		}
course
#ถ้าจะเพิ่ม บรรทัด ที่ O/P ออกมาให้ใส่  สร้างkey ใหม่เพิ่มเข้าไป 

course["start_time"] = "9am"  # Output start time จะไปต่อล่างสุดในการแสดงผล
course["language"] = "Thai"   # Output language จะไปต่อล่างสุดในการแสดงผล
#ถ้าจะลบใช้
del course["language"]
del course["start_time"]

course["replay"] = True  #หรือเปลี่ยน True > False อัพเดตค่า 
#ตัวอย่างจะกลายเป็นว่า อัพเดตค่าได้ จะเป็น mutable

#ดึง มาแสดงแค่ 3 ดู 
couse["skills"][0:2] # Output ออกมาเป็น  ['SQL', 'R', 'Stats']
couse["skills"][-2:] # Output ออกมาเป็น  ['R', 'Stats', 'Dashbroad']

#ลองดึง key แสดงผลออกมา
course.keys() #Output ออกมาเป็น      dict_keys(['name', 'duration', 'students', 'replay', 'skills'])

list(course.keys() )   #Output ออกมาเป็น ['name', 'duration', 'students', 'replay', 'skills']

course.values() #Output ออกมาเป็น dict_value ค่าทางขวามาหมด เหมือน dict_keys

 list(course.values() ) #ให้เรียงดีๆสวยๆ ค่าทางขวามาหมด เรียงลง

course.items()  # ดูสองอันพร้อมกันดูแบบ tuple  ออกมาเป็น key, value แล้วต่อๆกัน  -ขึ้นต้นด้วย dict_items([('name', 'Data sci class'),
# ลงท้ายที่ตรง skill จะขึ้นเป็น  ('skills', ['SQL', 'R', 'Stats', 'Dashbroad'])])

list(course.items() ) # ใส่ list ครอบเข้าไป output ก็จะ  เรียงลง
#-----------------------
course.get() #ถ้าใส่ในวงเล็บค่าถูกจะดึงค่ามา 
course.get("replays") #ใส่ผิดจะไม่ทำอะไรเลย
course.get("Replay") #ใส่ผิด R ใหญ่ จะไม่ทำอะไรเลย
course.get("replay") #ใส่ถูก Output แสดงค่าที่ดึงมาแสดง ก็คือ False 


#=====================================
# list, dictionary เป็น mutable
# tuple, string เป็น immutable
# usecase มีค่าเยอะๆ ก็จะใช้ set เพื่อ convert list หรือ tuple 
