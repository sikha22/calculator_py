def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

a=int(input("Enter the 1st value:"))
b=int(input("Enter the 2nd value:"))

choice= input("Enter choice :")
if choice == "add":
            print(a, "+", b, "=", add(a,b))
        
elif choice == "sub":
            print(a, "-", b, "=", sub(a, b))

elif choice == "mul":
            print(a, "*", b, "=", mul(a, b))

elif choice == "div":
            print(a, "/", b, "=", div(a, b))
else:
    print("Invalid Input")
    