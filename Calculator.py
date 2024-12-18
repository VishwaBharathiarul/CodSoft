while True:
    ch = input('''\nEnter the choice for the operation you wish to perform\n
    Press 1 for Addition\n
    Press 2 for Subtraction\n
    Press 3 for Multiplication\n
    Press 4 for Division\n
    Press 5 for Exponent operation\n
    Press "q" to Exit Calculator: ''')
    if ch == 'q':
        print("Exiting Calculator...")
        break
    a = eval(input("Enter number 1: "))
    b = eval(input("Enter number 2: "))
    print()
    if ch == '1':
        res = a + b
        print(f"Sum of the two numbers = {res:.2f}")
    elif ch == '2':
        res = a - b
        print(f"Difference of the two numbers =  {res:.2f}")
    elif ch == '3':
        res = a*b
        print(f"Product of the two numbers =  {res:.2f}")
    elif ch == '4':
        if b==0:
            print("ERROR: Division by zero!! Please enter valid divisor")
        else:
            res = a/b
            print(f"Divsion of the two numbers = {res:.2f}")
    elif ch == '5':
        value = a**b
        print(a,"to the power of",b,"=",value)
    else:
        print("Invalid choice. Please try again with valid options")
    
        
