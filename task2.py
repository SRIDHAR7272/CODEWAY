import math
while True:
    print("\nPlease select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n"
        "5. Square Root\n"
        "6. Exponentiation\n")

    
    operator = int(input("Select operations form 1, 2, 3, 4, 5, 6 :"))
    
    
    if operator == 1:
       number_1 = int(input("Enter first number: "))
       number_2 = int(input("Enter second number: "))
       print(number_1, "+", number_2, "=",
    					number_1+number_2)
    
    elif operator == 2:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: ")) 
        print(number_1, "-", number_2, "=",number_1-number_2)
    
    elif operator == 3:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: ")) 
        print(number_1, "*", number_2, "=",number_1*number_2)
    
    elif operator == 4:
        number_1 = int(input("Enter first number: "))
        number_2 = int(input("Enter second number: ")) 
        print(number_1, "/", number_2, "=", number_1/number_2)
    elif operator == 5:
        number_1 = int(input("Enter  number: "))
        print("Square root of", number_1, "=", math.sqrt(number_1))

    elif operator == 6:
        number_1 = int(input("Enter Base number: "))
        number_2 = int(input("Enter power number: ")) 
        print(number_1, "raised to the power of", number_2, "=", math.pow(number_1, number_2))
				
    else:
    	print("Invalid input")