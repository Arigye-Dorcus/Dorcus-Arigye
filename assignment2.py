while True:
    try:
        
        num1 = float(input("Enter first number: "))
        
        while True:
            num2 = float(input("Enter second number (cannot be zero): "))
            if num2 != 0:
                break
            print("Error: Division by zero is not allowed. Please try again.")
        
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
        break
        
    except ValueError:
        print("Error: Please enter valid numbers only.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")