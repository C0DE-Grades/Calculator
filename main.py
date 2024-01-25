#Area of Rectangle Calculator
L=int(input("Enter a number for the length for the rectangle [Area]\n> "))
W=int(input("Enter a number for the width for the rectangle [Area]\n> "))
AREA=L*W
print(f"\nYour total area is: {AREA}")

#Perimeter Calculator
L=int(input("---\nEnter a number for the length for the rectangle [Perimeter]\n> "))
W=int(input("Enter a number for the width for the rectangle [Perimeter]\n> "))
PERIMETER=2*(L+W)
print(f"\nYour total perimeter is: {PERIMETER}")

#Tip Calculator 
MEAL=int(input("---\nEnter the price of your meal [Tip]\n> "))
TIP=MEAL*2/10
print(f"\nYour tip (20%) is: ${TIP}0\nYour total is: ${MEAL+TIP}0")

#Volume and Surface Calculator 
L=int(input("---\nEnter a number for the length for the rectangle [Volume and Surface Area]\n> "))
W=int(input("Enter a number for the width for the rectangle [Volume and Surface Area]\n> "))
H=int(input("Enter a number for the height for the rectangle [Volume and Total Surface Area]\n> "))
VOL=L*W*H
TSA=(L*W)+(W*H)+(H*L)
TSA=TSA*2
print(f"\nYour total volume is: {VOL}\nYour total surface area is: {TSA}")

#cant find a way to input a if X = True, while X == True: Y = "": print("Try again.\n"), else: print(something something on to the next number to pick) :(
# ^^ to do this, you will need to use functions and then call on them when the condition is met. For example def area() would run the entire area program if you simple call on area()