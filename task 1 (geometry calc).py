print(                 "Geometry Calculator" )
print("")
# asking user to enter parameters
width = int(input("Enter width: "))
height = int(input("Enter height: "))
# asking user to put any options
def menu():
    print("[1] Area of triangle: ")
    print("[2] Area of rectangle: ")
    print("[3] Area of circle: ")
    print("[4] Quit")

menu()
option = int(input("Select any option (1-4): "))

# area of triangle
if option == 1:
    # formula area of triangle
    triangle = height * width / 2  
    print("Area of triangle is: ", triangle)

# area of rectangle    
elif option == 2:
    # formula area of rectangle
    rectangle = height * width   
    print("Area of Rectangle is: ",rectangle)
# area of circle 
elif option == 3:
    #asking user to enter radius 
    radius = int(input("Enter Radius of circle: ")) 
    #formula area of circle 
    #3.14= value of pi
    circle = 3.14 * radius * radius
    print("Area of Circle is: ",circle)
elif option == 4:
    menu()
    option = int(input("Select any option (1-4): "))

else:
  print("Invalid Option")
 
menu()
option = int(input("Select any option (1-4): "))
