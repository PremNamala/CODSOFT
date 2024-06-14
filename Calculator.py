import os, sys
print("----Calculator----")
result = int(input("Enter a Numbers: "))
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("----Calculator----")
    print("\nResult : ",result,"\n")
    choice = input("Addition\nSubtraction\nMultiplication\nDivision\nExit\n\nEnter Your Choice : ")
    choice.lower()
    if choice in ['exit','e']:
      os.system('cls' if os.name == 'nt' else 'clear')
      sys.exit(f"----END----\n\nFINAL RESULT : {result}")
    else:
      y = int(input("Enter Number : "))
      if choice in ['add','+','addition']:
        result += y
        print("\nResult : ",result)
      elif choice in ['sub','-','subtraction']:
        result -= y
        print("\nResult : ",result)
      elif choice in ['mul','*','multiplication']:
        result *= y
        print("\nResult : ",result)
      elif choice in ['div','/','division']:
        result /= y
        print("\nResult : ",result)
        result = int(result)
  
