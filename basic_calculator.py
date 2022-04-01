def add (n1,n2):
    return n1+n2
def subtract (n1,n2):
    return n1-n2
def multiply (n1,n2):
    return n1*n2
def divide (n1,n2):
    return n1/n2

operations = {"+":add,
              "-":subtract,
              "*":multiply,
              "/":divide
              }
def calculator ():
    num1 = float(input("What's the first number ?\n"))
    continue_calc = True
    while continue_calc:
        for signal in operations:
            print(signal, end = " ")
        operation_signal = input("Choose one operator.\n")
        num2 = float(input("What's the next number?\n"))
        calculation_function = operations[operation_signal]
        answer = calculation_function(num1,num2)
        print(f"{num1}{operation_signal}{num2} = {answer}")

        if input(f"Do you wanna continue with {answer}? y or n\n") .lower() == "y":
            num1 = answer
        else:
            continue_calc = False
            calculator()
calculator()
