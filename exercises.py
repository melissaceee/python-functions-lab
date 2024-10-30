#exercise 1
def calculate_area_triangle(base, height):
    return (base * height) / 2

print('Exercise 1:', calculate_area_triangle(10, 5))



# Exercise 2: Calculate Simple Interest
def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

print('Exercise 2:', simple_interest(1000, 5, 2))



# Exercise 3: Apply a Discount

def apply_discount(price, discount_percentage):
    discount_amount = (price * discount_percentage) / 100
    new_price = price - discount_amount
    return new_price


print('Exercise 3:', apply_discount(100, 25)) 

# Exercise 4: Convert Temperature

def convert_temperature(temperature, unit):
    if unit == 'C':
        converted_temp = (temperature * 9/5) + 32
    elif unit == 'F':
        converted_temp = (temperature - 32) * 5/9
    else:
        return "Invalid unit"  

    return converted_temp

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))  # Should return 32.0
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))   # Should return 0.0


# Exercise 5: Sum to N
def sum_to(n):
    return n * (n + 1) // 2

print('Exercise 5:', sum_to(6))  
print('Exercise 5:', sum_to(10)) 


# Exercise 6: Find the Largest Number
def largest(a, b, c):
    return max(a, b, c)

print('Exercise 6:', largest(1, 2, 3))  
print('Exercise 6:', largest(10, 4, 2)) 
print('Exercise 6:', largest(5, 7, 6))


# Exercise 7: Calculate a Tip
def calculate_tip(bill_amount, tip_percentage):
    tip = (bill_amount * tip_percentage) / 100
    return tip


print('Exercise 7:', calculate_tip(50, 20))  


# Exercise 8: Calculate Product of Numbers
def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

print('Exercise 8:', product(2, 5, 5)) 
print('Exercise 8:', product(-1, 4))    
print('Exercise 8:', product(3, 7, 2)) 

# Exercise 9: Basic Calculator
def basicCalculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

print('Exercise 9 Result:', basicCalculator(10, 5, "subtract"))  
print('Exercise 9 Result:', basicCalculator(10, 5, "add"))       
print('Exercise 9 Result:', basicCalculator(10, 5, "multiply"))  
print('Exercise 9 Result:', basicCalculator(10, 5, "divide"))   
