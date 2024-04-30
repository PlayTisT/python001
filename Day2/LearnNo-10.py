# Work with string

text = "hello world" # หรือ 'hello world'

long_text = """ This is a   #ไว้ใส่ข้อความยาวๆ
very long text
this is a new line """

#รันออกมาเป็น 
hello world
# This is a 
# very long text
#this is a new line

#-------------------------- string template : fstrings
my_name = "Karn"
location = "Thai"

text = f"Hi! my name ks {My_name} and i live in {location}."
print(text)
#แสดงผลเป็น Hi! my name is Karn and i live in Thai.

"Hi! my name is {}, location: {}". format(my_name, location)
#แสดงผลเป็น 'Hi! my name is Karn, location: Thai'
