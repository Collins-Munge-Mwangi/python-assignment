def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Applies the discount only if it's 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# --- Main program to get user input and use the function ---

try:
    # Get user input for the original price
    original_price = float(input("Enter the original price: "))

    # Get user input for the discount percentage
    discount_rate = float(input("Enter the discount percentage: "))

    # Call the function to calculate the final price
    final_price = calculate_discount(original_price, discount_rate)

    # Print the result based on whether a discount was applied
    if discount_rate >= 20:
        print(f"A {discount_rate}% discount was applied.")
        print(f"The final price is: ${final_price:.2f}")
    else:
        print(f"No discount was applied (discount must be 20% or higher).")
        print(f"The original price is: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")