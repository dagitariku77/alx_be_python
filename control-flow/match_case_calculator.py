num1 = int(input("insert num 1"))
num2 = int(input("insert num2"))
operation = input("inter opeeration")

match operation :
       case '+':
          print(num1 + num2)
       case '-':
          print(num1 - num2)
       case '*':
          print(num1 * num2)
       case '/':
          print(num1 / num2)
       case _:
          print("invalid input")
          
     
        
          
    
       