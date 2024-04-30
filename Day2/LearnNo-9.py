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
