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

def convert_temperature (temperature, unit):
    if unit == 'C'
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.



print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


