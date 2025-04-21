# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    # Apply discount only if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Call the function to calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if discount_percentage >= 20:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${final_price:.2f}")
