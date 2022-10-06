print(                 "Geometry Calculator" )
print("")

while True:
    print("[1] Find Parimeter: ")
    print("[2] Find Area: ")
    option1 = int(input("Enter your option: "))
     
    if option1 == 1:
    
     print("[1] triangle: ")
     print("[2] rectangle: ")
     print("[3] circle: ")
     print("[4] Quit")
     option2 = int(input("Enter your choice: "))
     
     if option2 == 1:
        a = int(input("Enter A side: "))
        b = int(input("Enter B side: "))
        c = int(input("Enter C side: "))        
        PT = a+b+c 
        print("Parimeter of Triangle is ",PT)
     elif option2 == 2:
        height = int(input("Enter Height: "))
        width = int(input("Enter width:")) 
        PR = 2 * height + width  
        print("Perimeter of Rectangle is ",PR)
     elif option2 == 3:
        radius = int(input("Enter radius:"))
        PC = 2 * 3.14 * radius
        print("Perimeter of Circle is ",PC)
     else:
        print("Enter valid option ")
        break
    elif option1 == 2:
     print("[1] triangle: ")
     print("[2] rectangle: ")
     print("[3] circle: ")
     print("[4] Quit")
     option3 = int(input("Enter your choice: "))
     
     if option3 == 1:
        height = int(input("Enter height:"))
        width = int(input("Enter width:"))                
        AT = height * width / 2  
        print("Area of Triangle is ",AT)
     elif option3 == 2:
        height = int(input("Enter Height: "))
        width = int(input("Enter width:")) 
        AR = height * width  
        print("Area of Rectangle is ",AR)
     elif option3 == 3:
        radius = int(input("Enter radius:"))
        AC = 3.14 * radius * radius
        print("Area of Circle is ",AC)
     else:
        print("Enter valid option ")

