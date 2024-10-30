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


print('Exercise 3:', apply_discount(100)) 

