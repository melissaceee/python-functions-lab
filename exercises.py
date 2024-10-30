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



