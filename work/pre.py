import math
# for area and perimeter find ractangle , circle and triangle
def rectangle():
    lenght =5
    width =3
    area = lenght*width
    perimeter = 2*(lenght+width)
    print("This is a Ractangle : ")
    print(area)
    print(perimeter)
rectangle()

def circle():
    radius = 7
    circle_area = math.pi * radius**2
    circle_circumference = 2 * math.pi * radius
    print("This is a circle : ")
    print("circle area : ",circle_area)
    print("circle circumference : ",circle_circumference)
circle()

def triangle():
    base =6
    height =4
    side1 =5
    side2 =6
    side3 =7
    area = 0.5 * base * height
    perimeter = side1 +side2+side3
    print("This is a Triangle : ")
    print(area)
    print(perimeter)
triangle()

# conversion calculation

def length_conversions():
    #inch to centimeter
    inches =10
    centimeter = inches*2.54
    print("inch to centimeter : ", centimeter)

    # cm to inch
    cm =25.4
    inch =cm/2.54
    print("cm to inch : ",inch)

    #temperature conversion
    celsius =25
    fehrenheit = celsius *9/5 +32
    print(fehrenheit,"F")

    #fehrenheit conversion
    fehrenheit =70
    celsius = fehrenheit -32 *9/5
    print(celsius,"c")

length_conversions()


def number_properties():
     print("__________________________________________________")
     print("even / odd number")
     num = int(input("Enter a number: "))

     if num % 2 == 0:
          print(f"{num} is Even")
     else:
        print(f"{num} is Odd")


     print("Enter number for negaitive and positive")
     num=int(input("Enter number"))
     if num > 0:
         print(num,"is positive")
     elif num <0 :
         print(num,"is nagative")
     else:
         print(num,"is Zero")
number_properties()