num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
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
          if num2 == 0:
              print("cannot devided by zero")
          else:
              result = (num1 / num2)
              print(f"the result is {result}")
    
            
       case _:
          print("invalid input")
          
     
        
          
    
       