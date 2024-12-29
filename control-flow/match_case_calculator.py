num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the first number:"))
operation = input("choose the operation(+, -, *, /):")
match operation :
       case '+':
           result = (num1 + num2)
           print(f"the result is {result}")

       case '-':
          result = (num1 - num2)
          print(f"the result is {result}")
       case '*':
          result = (num1 * num2)
          print(f"the result is {result}")
       case '/':
          result = (num1 / num2)
          print(f"the result is {result}")
       case _:
          print("invalid input")
          
     
        
          
    
       