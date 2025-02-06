from colorama import Fore, Style, init
import math
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN="\033[36m"
RESET = "\033[0m"  # Resets color back to default


# def age_check():
#     name = input("enter your name : ")
#     #string

#     age= int (input("enter your Age : "))
#     #integer

#     adult = False
#     #boolean

#     if age>18 : adult=True
#     #condition for chack age 18+

#     print("your : ",name)
#     print("adult : ",adult)

# age_check()
# #calling this function

def  Variables_DataTypes_Operators():
    while True: 
        print(f"{BLUE}==================================================================================================================")
        print(f"{BLUE}==================================================={CYAN}PYTHON{BLUE}=========================================================")
        print(f"{BLUE}==================================================================================================================")
        print(f"{YELLOW}** if you learn python in viriables , datatype and operator than select this option :")
        print("-------------------------------------------------------------------------------------")
        print(f"{GREEN}1. Variable")
        print(f"{GREEN}2. Datatype")
        print(f"{GREEN}3. Operator")
        print(f"{GREEN}4. Type casting")
        print(f"{GREEN}5. Basic calculations (area, perimeter, conversions)")
        print(f"{GREEN}6. Number properties (even/odd, positive/negative)")
        print(f"{GREEN}-> Exit : of Exit code\n")

        userres= input(f"{CYAN}Enter Topic Number :{RESET} ").strip().lower()
        if userres == "1"  : 
            print(f"{RED}........................................................................................................")
            print(f"{YELLOW}1. Variables in Python :")
            print("______________________________________________________________")
            print(f"{RESET}--> A variable is a container for storing data values. In Python,\n variables are dynamically typed, meaning you don’t need to declare their type explicitly.\n")
            print(f"{GREEN} * name = 'Tony' {YELLOW}# String")
            print(f"{GREEN} * age = 25       {YELLOW}# INT")
            print(f"{GREEN} * price = 19.99  {YELLOW}# Float")
            print(f"{GREEN} * Bool = True/flase {YELLOW}# Boolean")
            print(f"{RED}........................................................................................................")
        
        elif userres=="2" :
            print(f"{RED}........................................................................................................")
            print(f"{YELLOW}2. Data Types in Python")
            print("______________________________________________________________")
            print(f"{RESET}-->Python provides built-in data types that define the kind of values stored in variables.\n")
            print(f"{BLUE}Basic Datatype")
            print(f"{Fore.YELLOW}Data Type\tExample\t\tDescription{Style.RESET_ALL}")
            print(f"{Fore.GREEN}int{Style.RESET_ALL}\t\tx = 10\t\tWhole numbers")
            print(f"{Fore.GREEN}float{Style.RESET_ALL}\t\ty = 3.14\tDecimal numbers")
            print(f"{Fore.GREEN}str{Style.RESET_ALL}\t\tname = 'Alice'\tText (string)")
            print(f"{Fore.GREEN}bool{Style.RESET_ALL}\t\tis_valid = True\tBoolean (True/False)")
            print(f"{BLUE}Complex Datatype")
            print(f"{Fore.YELLOW}Data Structure\tExample\t\t\t\t\tDescription{Style.RESET_ALL}")
            print(f"{Fore.GREEN}list{Style.RESET_ALL}\t\tnumbers = [1, 2, 3]\t\t\tOrdered, mutable collection")
            print(f"{Fore.GREEN}tuple{Style.RESET_ALL}\t\tpoint = (4, 5)\t\t\t\tOrdered, immutable collection")
            print(f"{Fore.GREEN}set{Style.RESET_ALL}\t\tunique_nums = {{1, 2, 3}}\t\t\tUnordered collection of unique elements")
            print(f"{Fore.GREEN}dict{Style.RESET_ALL}\t\tperson = {{'name': 'Alice', 'age': 25}}\tKey-value pairs")

            print(f"{RED}........................................................................................................")
        
        
        elif userres=="3":
            print(f"{RED}........................................................................................................")
            print(f"{YELLOW}3. Operators in Python")
            print("______________________________________________________________")
            print(f"{RESET}Operators are used to perform operations on variables and values.\n")

            #Arithmetic Operator
            print(f"{YELLOW}Arithmetic Operators")
            print(f"{Fore.BLUE}Operator\tOperation\tExample\t\tResult{Style.RESET_ALL}")
            print(f"{Fore.BLUE}+{Style.RESET_ALL}\t\tAddition\t5 + 3\t\t{5 + 3}")
            print(f"{Fore.BLUE}-{Style.RESET_ALL}\t\tSubtraction\t5 - 3\t\t{5 - 3}")
            print(f"{Fore.BLUE}*{Style.RESET_ALL}\t\tMultiplication\t5 * 3\t\t{5 * 3}")
            print(f"{Fore.BLUE}/{Style.RESET_ALL}\t\tDivision\t5 / 2\t\t{5 / 2}")
            print(f"{Fore.BLUE}//{Style.RESET_ALL}\t\tFloor Division\t5 // 2\t\t{5 // 2}")
            print(f"{Fore.BLUE}%{Style.RESET_ALL}\t\tModulus\t\t5 % 2\t\t{5 % 2}")
            print(f"{Fore.BLUE}*{Style.RESET_ALL}\t\tExponentiation\t2 ** 3\t\t{2 ** 3}")

            #Comparasion Operator
            print(f"{Fore.YELLOW}Comparison Operators{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Operator\tDescription\t\t\tExample\t\tOutput{Style.RESET_ALL}")
            print(f"{Fore.CYAN}=={Style.RESET_ALL}\t\tEqual to\t\t\t5 == 3\t\tFalse")
            print(f"{Fore.CYAN}!={Style.RESET_ALL}\t\tNot equal to\t\t\t5 != 3\t\tTrue")
            print(f"{Fore.CYAN}>{Style.RESET_ALL}\t\tGreater than\t\t\t5 > 3\t\tTrue")
            print(f"{Fore.CYAN}<{Style.RESET_ALL}\t\tLess than\t\t\t5 < 3\t\tFalse")
            print(f"{Fore.CYAN}>={Style.RESET_ALL}\t\tGreater than or equal to\t5 >= 5\t\tTrue")
            print(f"{Fore.CYAN}<={Style.RESET_ALL}\t\tLess than or equal to\t\t5 <= 3\t\tFalse")

            #Logical Operator
            print(f"\n{Fore.YELLOW}Logical Operators{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Operator\tDescription\t\t\t\t\t\tExample\t\t\tOutput{Style.RESET_ALL}")
            print(f"{Fore.CYAN}and{Style.RESET_ALL}\t\tReturns True if both conditions are true\t\t(5 > 3) and (2 < 4)\tTrue")
            print(f"{Fore.CYAN}or{Style.RESET_ALL}\t\tReturns True if at least one condition is true\t\t(5 > 3) or (2 > 4)\tTrue")
            print(f"{Fore.CYAN}not{Style.RESET_ALL}\t\tReverses the result\t\t\t\t\tnot(5 > 3)\t\tFalse")

            # Assignment Operators
            print(f"\n{Fore.YELLOW}Assignment Operators{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Operator\tDescription\t\tExample\t\t\tEquivalent to{Style.RESET_ALL}")
            print(f"{Fore.CYAN}= {Style.RESET_ALL}\t\tAssign value\t\tx = 5\t\t\tx = 5")
            print(f"{Fore.CYAN}+= {Style.RESET_ALL}\t\tAdd and assign\t\tx += 3\t\t\tx = x + 3")
            print(f"{Fore.CYAN}-= {Style.RESET_ALL}\t\tSubtract and assign\tx -= 3\t\t\tx = x - 3")
            print(f"{Fore.CYAN}*= {Style.RESET_ALL}\t\tMultiply and assign\tx *= 3\t\t\tx = x * 3")
            print(f"{Fore.CYAN}/= {Style.RESET_ALL}\t\tDivide and assign\tx /= 3\t\t\tx = x / 3")
            print(f"{Fore.CYAN}%= {Style.RESET_ALL}\t\tModulus and assign\tx %= 3\t\t\tx = x % 3")

            # Bitwise Operators
            print(f"\n{Fore.YELLOW}Bitwise Operators{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Operator\tDescription\t\tExample{Style.RESET_ALL}")
            print(f"{Fore.CYAN}&{Style.RESET_ALL}\t\tBitwise AND\t\t5 & 3 (0101 & 0011 → 0001)")
            print(f"{Fore.CYAN}|{Style.RESET_ALL}\t\tBitwise OR\t\t5 | 3 (0101 | 0011 → 0011)")
            print(f"{Fore.CYAN}^{Style.RESET_ALL}\t\tBitwise XOR\t\t5 ^ 3 (0101 ^ 0011 → 0110)")
            print(f"{Fore.CYAN}~{Style.RESET_ALL}\t\tBitwise NOT\t\t~5 (~0101 → 1010 in 2’s complement)")
            print(f"{Fore.CYAN}<<{Style.RESET_ALL}\t\tLeft shift\t\t5 << 1 (0101 → 1010)")
            print(f"{Fore.CYAN}>>{Style.RESET_ALL}\t\tRight shift\t\t5 >> 1 (0101 → 0010)")

            # Identity and Membership Operators
            print(f"\n{Fore.YELLOW}Identity and Membership Operators{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Operator\tDescription\t\t\t\t\t\tExample\t\t\tOutput{Style.RESET_ALL}")
            print(f"{Fore.CYAN}is{Style.RESET_ALL}\t\tTrue if both variables refer to the same object\t\ta is b\t\t\tTrue or False")
            print(f"{Fore.CYAN}is not{Style.RESET_ALL}\t\tTrue if they refer to different objects\t\t\ta is not b\t\tTrue or False")
            print(f"{Fore.CYAN}in{Style.RESET_ALL}\t\tTrue if value exists in a sequence\t\t\t'A' in 'Alice'\t\tTrue")
            print(f"{Fore.CYAN}not in{Style.RESET_ALL}\t\tTrue if value does not exist\t\t\t\t3 not in [1, 2, 4]\tTrue")
            print(f"{RED}........................................................................................................")
        
        elif userres=="4":
            print(f"{RED}........................................................................................................")
            # Printing the formatted text
            print(f"{Fore.CYAN}{Style.BRIGHT}Type Conversion (Casting) in Python")
            print("______________________________________________________________")
            print(f"{Fore.GREEN}Type conversion (also known as type casting) is the process of converting one data type to another.")
            print(f"In Python, this can be done implicitly or explicitly.\n")

            print(f"{Fore.YELLOW}{Style.BRIGHT}1. Implicit Type Conversion:")
            print(f"{Fore.WHITE}Python automatically converts lower data types into higher data types.\n")

            # Example of Implicit Type Conversion
            a = 10  # Integer
            b = 3.14  # Float
            result = a + b  # Python automatically converts 'a' to float before adding
            print(f"{GREEN}Example:")
            print(f"  a = {a}  (int)")
            print(f"  b = {b}  (float)")
            print(f"  result = a + b  --> {result}")
            print(f"  Type of result: {type(result)}\n")

            print(f"{Fore.YELLOW}{Style.BRIGHT}2. Explicit Type Conversion:")
            print(f"{Fore.WHITE}This happens when the programmer manually converts one type to another using built-in functions.\n")

            # Example of Explicit Type Conversion
            a = 5
            b = float(a)  # Manually converting int to float
            print(f"{GREEN}Example:")
            print(f"  a = {a}  (int)")
            print(f"  b = {b}  --> {type(b)}\n")

            # Convert Float to Integer
            a = 3.9
            b = int(a)  # Manually converting float to int (this truncates the decimal part)
            print(f"{GREEN}Example of float to int conversion:")
            print(f"  a = {a}  (float)")
            print(f"  b = {b}  --> {type(b)}\n")

            # Convert to String
            a = 100
            b = str(a)  # Manually converting int to string
            print(f"{GREEN}Example of int to string conversion:")
            print(f"  a = {a}  (int)")
            print(f"  b = {b}  (string)\n")
            print(f"{RED}........................................................................................................")

        elif userres == "5":
            
            # Printing the formatted text with colors
            print(f"{Fore.CYAN}{Style.BRIGHT}Basic Calculations in Python")
            print(f"{Fore.GREEN}Let's cover how to perform basic calculations such as calculating the area, perimeter, and handling conversions in Python.\n")

            print(f"{Fore.YELLOW}{Style.BRIGHT}1. Area and Perimeter Calculations")

            # 1.1 Rectangle
            print(f"\n{Fore.BLUE}1.1 Rectangle")
            print(f"{Fore.WHITE}Area of a rectangle: ")
            print(f"  Formula: Area = length * width")
            print(f"Perimeter of a rectangle: ")
            print(f"  Formula: Perimeter = 2 * (length + width)")

            length = 5
            width = 3

            # Area and Perimeter
            area = length * width
            perimeter = 2 * (length + width)

            print(f"\n{Fore.GREEN}Example: Rectangle")
            print(f"  length = {length}")
            print(f"  width = {width}")
            print(f"  Area of rectangle: {area}")  # Output: 15
            print(f"  Perimeter of rectangle: {perimeter}")  # Output: 16

            # 1.2 Circle
            print(f"\n{Fore.BLUE}1.2 Circle")
            print(f"{Fore.WHITE}Area of a circle: ")
            print(f"  Formula: Area = π * radius²")
            print(f"Circumference of a circle: ")
            print(f"  Formula: Circumference = 2 * π * radius")

            radius = 7

            # Area and Circumference
            circle_area = math.pi * radius**2
            circle_circumference = 2 * math.pi * radius

            print(f"\n{Fore.GREEN}Example: Circle")
            print(f"  radius = {radius}")
            print(f"  Area of circle: {circle_area:.2f}")  # Output: 153.94
            print(f"  Circumference of circle: {circle_circumference:.2f}")  # Output: 43.98

            # 1.3 Triangle
            print(f"\n{Fore.BLUE}1.3 Triangle")
            print(f"{Fore.WHITE}Area of a triangle: ")
            print(f"  Formula: Area = 0.5 * base * height")
            print(f"Perimeter of a triangle: ")
            print(f"  Formula: Perimeter = side1 + side2 + side3")

            base = 6
            height = 4
            side1 = 5
            side2 = 6
            side3 = 7

            # Area and Perimeter
            triangle_area = 0.5 * base * height
            triangle_perimeter = side1 + side2 + side3

            print(f"\n{Fore.GREEN}Example: Triangle")
            print(f"  base = {base}")
            print(f"  height = {height}")
            print(f"  side1 = {side1}, side2 = {side2}, side3 = {side3}")
            print(f"  Area of triangle: {triangle_area}")  # Output: 12
            print(f"  Perimeter of triangle: {triangle_perimeter}")  # Output: 18

            # 2. Conversion Calculations
            print(f"\n{Fore.YELLOW}{Style.BRIGHT}2. Conversion Calculations")

            # 2.1 Length Conversions
            print(f"\n{Fore.CYAN}2.1 Length Conversions")
            print(f"{Fore.WHITE}1 inch = 2.54 cm")
            print(f"To convert inches to centimeters:")

            inches = 10
            centimeters = inches * 2.54
            print(f"\n{Fore.GREEN}{inches} inches is {centimeters} cm")

            print(f"\nTo convert centimeters to inches:")
            cm = 25.4
            inches = cm / 2.54
            print(f"{Fore.GREEN}{cm} cm is {inches} inches")

            # 2.2 Temperature Conversion
            print(f"\n{Fore.CYAN}2.2 Temperature Conversion")
            print(f"{Fore.WHITE}Celsius to Fahrenheit:")
            celsius = 25
            fahrenheit = (celsius * 9/5) + 32
            print(f"\n{Fore.GREEN}{celsius}°C is {fahrenheit}°F")

            print(f"\n{Fore.WHITE}Fahrenheit to Celsius:")
            fahrenheit = 77
            celsius = (fahrenheit - 32) * 5/9
            print(f"{Fore.GREEN}{fahrenheit}°F is {celsius:.2f}°C")

            # 2.3 Speed Conversion
            print(f"\n{Fore.CYAN}2.3 Speed Conversion")
            print(f"{Fore.WHITE}Kilometers per hour (km/h) to Miles per hour (mph):")
            km_per_hour = 100
            mph = km_per_hour * 0.621371
            print(f"\n{Fore.GREEN}{km_per_hour} km/h is {mph:.2f} mph")

            print(f"\nMiles per hour (mph) to Kilometers per hour (km/h):")
            mph = 62.14
            km_per_hour = mph * 1.60934
            print(f"{Fore.GREEN}{mph} mph is {km_per_hour:.2f} km/h")

            # 3. Example: Area, Perimeter, and Conversion in One Program
            print(f"\n{Fore.YELLOW}{Style.BRIGHT}3. Example: Area, Perimeter, and Conversion in One Program")

            # Rectangle
            length = 8
            width = 5
            rectangle_area = length * width
            rectangle_perimeter = 2 * (length + width)

            # Circle
            radius = 7
            circle_area = math.pi * radius**2
            circle_circumference = 2 * math.pi * radius

            # Conversion
            inches = 12
            cm = inches * 2.54

            # Output Results
            print(f"\n{Fore.GREEN}Rectangle Area: {rectangle_area}")
            print(f"Rectangle Perimeter: {rectangle_perimeter}")
            print(f"Circle Area: {circle_area:.2f}")
            print(f"Circle Circumference: {circle_circumference:.2f}")
            print(f"{inches} inches is {cm} cm")

        elif userres == "6":
             # 1. Checking Even or Odd Numbers
            print(f"{Fore.CYAN}{Style.BRIGHT}1. Checking Even or Odd Numbers")
            print(f"{Fore.WHITE}A number is even if it is divisible by 2, otherwise, it is odd.\n")

            # User Input
            num = int(input(f"{Fore.YELLOW}Enter a number: {Fore.RESET}"))

            # Checking Even or Odd
            if num % 2 == 0:
                print(f"{Fore.GREEN}{num} is Even")
            else:
                print(f"{Fore.RED}{num} is Odd")

            # Example Output
            print(f"\n{Fore.MAGENTA}{Style.DIM}Example Output:")
            print(f"{Fore.BLUE}Enter a number: 7\n{Fore.RED}7 is Odd\n")

            # 2. Checking Positive, Negative, or Zero
            print(f"{Fore.CYAN}{Style.BRIGHT}2. Checking Positive, Negative, or Zero")
            print(f"{Fore.WHITE}A number can be positive, negative, or zero.\n")

            # User Input
            num = float(input(f"{Fore.YELLOW}Enter a number: {Fore.RESET}"))

            # Checking the Number Type
            if num > 0:
                print(f"{Fore.GREEN}{num} is Positive")
            elif num < 0:
                print(f"{Fore.RED}{num} is Negative")
            else:
                print(f"{Fore.BLUE}{num} is Zero")

            # Example Outputs
            print(f"\n{Fore.MAGENTA}{Style.DIM}Example Outputs:")
            print(f"{Fore.BLUE}Enter a number: -3.5\n{Fore.RED}-3.5 is Negative")
            print(f"{Fore.BLUE}Enter a number: 0\n{Fore.BLUE}0 is Zero")

            print(f"{Fore.CYAN}{Style.BRIGHT}Checking Prime Numbers")
            print(f"{Fore.WHITE}A prime number is a number greater than 1 that has no divisors other than 1 and itself.\n")

            # User Input
            num = int(input(f"{Fore.YELLOW}Enter a number: {Fore.RESET}"))

            # Prime Number Check
            if num > 1:
                for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to sqrt(num)
                    if num % i == 0:
                        print(f"{Fore.RED}{num} is NOT a prime number")
                        break
                else:
                    print(f"{Fore.GREEN}{num} is a prime number")
            else:
                print(f"{Fore.RED}{num} is NOT a prime number")

            # Example Outputs
            print(f"\n{Fore.MAGENTA}{Style.DIM}Example Outputs:")
            print(f"{Fore.BLUE}Enter a number: 17\n{Fore.GREEN}17 is a prime number")
            print(f"{Fore.BLUE}Enter a number: 18\n{Fore.RED}18 is NOT a prime number")

        elif userres =="exit":
            break

Variables_DataTypes_Operators()