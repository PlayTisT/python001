#เรื่อง Function()
# greeting()
def greeting(name="Karn"):
    print("Hello! " + name)

greeting()

# Run ออกมาเป็น  Hello! Karn

#-----------------------------------

# greeting()
def greeting(name="Karn" , location="Thailand" ):
    print("Hello! " + name)
    print("He is in " " + location)
greeting(location="Japan", name="Naruto")

# Run ออกมาเป็น 
# Hello! Naruto
# He is in Japan
          
# หาก greeting("Naruto", "NYC" ) จะแสดงผลเป็น
# Hello! Naruto
# He is in NYC

#-----------------------------------
# การใช้ Return  (อะไร หลัง Return ไม่ทำงาน) ส่งค่าบางอย่างกลับมา
def add_two_nums(num1, num2):
    return num1 + num2
    print("Done") #  return ถูกรันแล้ว มันจะไม่ทำบรรทัดนี้เลย ต้องเอา done ไปไว้บนก่อนบรรทัด return
result = add_two_nums(5, 15)
print(result) #run ออก 20

#-----------------การ typing
# รับ input สองตัว
def add_two_nums(a: int, b: int): -> int.
    return a+b
add_two_nums(5,6)  # Runออกมาเป็น 11

