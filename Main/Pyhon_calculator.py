#Python calculator, Black_Knight

import math
try:
  num1 = input("Enter the first number: ")
  num2 = input("Enter the second number: ")

  num1 = float(num1)
  num2 = float(num2)

except ValueError:
    print("Error: One or both inputs are not valid numbers.")
    quit()
operator = input("Enter an operator (+ - * / %): ")


if operator !="+" and operator !="-" and operator !="*" and operator !="/" and operator !="%":
    print("Error: The operator is not valid.")

if operator == "+":
    if num1==int(num1) and num2==int(num2):
        print(f"The sum of number {math.trunc(num1)} and number {math.trunc(num2)} is {math.trunc(num1+num2)}.")
    elif num1!=int(num1) and num2==int(num2):
        print(f"The sum of number {num1} and number {math.trunc(num2)} is {(num1 + num2)}.")
    elif num1==int(num1) and num2!=int(num2):
        print(f"The sum of number {math.trunc(num1)} and number {num2} is {num1 + num2}.")
    elif num1!=int(num1) and num2!=int(num2):
        print(f"The sum of number {num1} and number {num2} is {num1 + num2}.")

elif operator == "-":
    if num1==num2:
        if num1!=int(num1) and num2!=int(num2):
            print(f"The difference between number {num1} and number {num2} is {math.trunc((round(num1 - num2, 5)))}.")
        else:
            print(f"The difference between number {math.trunc(num1)} and number {math.trunc(num2)} is {math.trunc((round(num1 - num2, 5)))}.")
    elif num1==int(num1) and num2==int(num2):
        print(f"The difference between number {math.trunc(num1)} and number {math.trunc(num2)} is {math.trunc(num1-num2)}.")
    elif num1!=int(num1) and num2==int(num2):
        print(f"The difference between number {num1} and number {math.trunc(num2)} is {(round(num1 - num2, 5))}.")
    elif num1==int(num1) and num2!=int(num2):
        print(f"The difference between number {math.trunc(num1)} and number {num2} is {(round(num1 - num2, 5))}.")
    elif num1!=int(num1) and num2!=int(num2):
        print(f"The difference between number {num1} and number {num2} is {(round(num1 - num2, 5))}.")

elif operator == "*":
    if num1==int(num1) and num2==int(num2):
        print(f"The product of number {math.trunc(num1)} and number {math.trunc(num2)} is {math.trunc(num1*num2)}.")
    elif num1!=int(num1) and num2==int(num2):
        print(f"The product of number {num1} and number {math.trunc(num2)} is {(num1 * num2)}.")
    elif num1==int(num1) and num2!=int(num2):
        print(f"The product of number {math.trunc(num1)} and number {num2} is {num1 * num2}.")
    elif num1!=int(num1) and num2!=int(num2):
        print(f"The product of number {num1} and number {num2} is {num1 * num2}.")

elif operator == "/":
   try:
    if num1==int(num1) and num2==int(num2):
        if num1 == 0:
            print(f"The quotient of number {math.trunc(num1)} and number {math.trunc(num2)} is {(math.trunc(round(num1 / num2, 5)))}.")
        elif num1==num2:
            print(f"The quotient of number {math.trunc(num1)} and number {math.trunc(num2)} is {(math.trunc(round(num1 / num2, 5)))}.")
        elif num1 / num2 == int(num1 / num2):
            print(f"The quotient of number {math.trunc(num1)} and number {math.trunc(num2)} is {(math.trunc(round(num1 / num2, 5)))}.")
        else:
            print(f"The quotient of number {math.trunc(num1)} and number {math.trunc(num2)} is {(round(num1/num2, 5))}.")
    elif num1!=int(num1) and num2==int(num2):
        print(f"The quotient of number {num1} and number {math.trunc(num2)} is {(round(num1 / num2, 5))}.")
    elif num1==int(num1) and num2!=int(num2):
        print(f"The quotient of number {math.trunc(num1)} and number {num2} is {(round(num1 / num2, 5))}.")
    elif num1!=int(num1) and num2!=int(num2):
        if num1 / num2 != int(num1 / num2):
            print(f"The quotient of number {num1} and number {num2} is {(round(num1 / num2, 5))}.")
        else:
            print(f"The quotient of number {num1} and number {num2} is {(math.trunc(round(num1 / num2, 5)))}.")
   except ZeroDivisionError:
       print("You can't divide with 0.")

elif operator == "%":
  try:
    if num1==int(num1) and num2==int(num2):
        if num1 % num2==0 or num2 % num1==0:
            print(f"The remainder when number {math.trunc(num1)} and number {math.trunc(num2)} are divided is {(math.trunc(round(num1%num2, 5)))}.")
        elif num1 % num2 == int(num1 % num2) or num2 % num1 == int(num2 % num1):
            print(f"The remainder when number {math.trunc(num1)} and number {math.trunc(num2)} are divided is {(math.trunc(round(num1 % num2, 5)))}.")
        else:
            print(f"The remainder when number {math.trunc(num1)} and number {math.trunc(num2)} are divided is {(round(num1 % num2, 5))}.")
    elif num1!=int(num1) and num2==int(num2):
        print(f"The remainder when number {num1} and number {math.trunc(num2)} are divided is {(round(num1 % num2, 5))}.")
    elif num1==int(num1) and num2!=int(num2):
        if num1 % num2 != int(num1 % num2):
            print(f"The remainder when number {math.trunc(num1)} and number {num2} are divided is {(round(num1 % num2, 5))}.")
        else:
            print(f"The remainder when number {math.trunc(num1)} and number {num2} are divided is {math.trunc((round(num1 % num2, 5)))}.")

    elif num1!=int(num1) and num2!=int(num2):
        if num1 % num2 != int(num1 % num2):
            print(f"The remainder when number {num1} and number {num2} are divided is {(round(num1 % num2, 5))}.")
        else:
            print(f"The remainder when number {num1} and number {num2} are divided is {(math.trunc(round(num1 % num2, 5)))}.")
  except ZeroDivisionError:
      print("You cannot use 0 as the divisor in a modulus operation.")





