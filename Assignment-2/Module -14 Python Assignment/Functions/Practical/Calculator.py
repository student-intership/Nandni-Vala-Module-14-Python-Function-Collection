def Add():
     n = int(input("Enter No : "))
     n1 = int(input("Enter No : "))
     print("Addition is :",n+n1)

def Sub():
     n = int(input("Enter No : "))
     n1 = int(input("Enter No : "))
     print("Substraction is :",n-n1)
    
def Mul():
     n = int(input("Enter No : "))
     n1 = int(input("Enter No : "))
     print("Multiplication is :",n*n1)

def Div():
     n = int(input("Enter No : "))
     n1 = int(input("Enter No : "))
     if n1 != 0:
        print("division is :",n/n1)
     else :
        print("Division by zero is not allowed!!")

def Calculator():
    print(" [1] Is Add!!")
    print(" [2] Is Sub!!")
    print(" [3] Is Mul!!")
    print(" [4] Is Div!!")
    
    ch = int(input("Enter Your Choice :"))

    if ch == 1:
        Add()

    elif ch == 2:
        Sub()

    elif ch == 3:
        Mul()

    elif ch == 4:
        Div()

    else:
        print("Invalid Choice!!")

Calculator()