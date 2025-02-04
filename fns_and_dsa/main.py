
from arithmetic_operations import perform_operation

def main():
  
    num1 = float(input("inter the first number"))
    num2 = float(input("inter the second number"))
    operation = input("inetr the operation(add,substract,multiply,divide):").strip().lower()

    result = perform_operation(num1,num2,operation)
    print(f"result: {result}")
