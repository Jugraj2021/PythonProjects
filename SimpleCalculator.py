def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

while (True):

    try:
        
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")
        num = int(input("Enter Your Choice :- "))
        
        
        if (num==1):
            num1 = eval(input("1st number :-"))
            num2 = eval(input("2nd number :-"))
            print(num1, "+", num2, "=", add(num1, num2))

        elif(num==2):
            num1 = eval(input("1st number :-"))
            num2 = eval(input("2nd number :-"))
            print(num1, "-", num2, "=", subtract(num1, num2))
            

        elif (num==3):
            num1 = eval(input("1st number :-"))
            num2 = eval(input("2nd number :-"))
            print(num1, "*", num2, "=", multiply(num1, num2))
                
                

        elif (num==4):
            num1 = eval(input("1st number :-"))
            num2 = eval(input("2nd number :-"))
            print(num1, "/", num2, "=", divide(num1, num2))

                    
        elif (num==5):
            break


            
        else:
            print("Enter Number Between 1 To 5 ")
        
    except:
        print("Something went wrong")