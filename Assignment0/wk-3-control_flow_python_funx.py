"""
Question 1
Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount.
The function should take the original price (price) and the discount percentage (discount_percent) as parameters.
If the discount is 20% or higher, apply the discount; otherwise, return the original price.
"""

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


"""
Question 2
Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage.
Print the final price after applying the discount, or if no discount was applied, print the original price.
"""

def calculate_discount(price, discount_percent):
    return price * (1 - discount_percent / 100) if discount_percent >= 20 else price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"Original price: ${original_price:.2f}")
    print(f"Discount applied: {discount_percent}%")
    print(f"Final price after discount: ${final_price:.2f}")
else:
    print(f"No discount applied (discount must be 20% or higher)")
    print(f"Final price: ${final_price:.2f}")
