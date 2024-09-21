op1 = eval(input("put ur first number"))
ore = input("put your arithmetic operant in phyton format")
op2 = eval(input("put ur second number"))
if ore == "+":
    print (op1 + op2)
elif ore == "-":
    print (op1 - op2)
elif ore == "*":
    print (op1 * op2)
elif ore == "/":
    print (op1 / op2)
elif ore == "%":
    print (op1 % op2)
elif ore == "**":
    print (op1 ** op2)
elif ore == "//":
    print (op1 // op2)
else:
    print("Your operant is not in the library")
