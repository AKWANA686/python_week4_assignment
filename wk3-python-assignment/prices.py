def calculate_discount(price, discount_percent): # creating a function takes the original price (price) and the discount percentage (discount_percent) as parameters.
    if discount_percent >= 20:
        discount_amount = (price * discount_percent) / 100
        final_price = price - discount_amount # calculates the final price after applying a discount
        return final_price
    else:
        return price # return the original price if discount is less than 20%.
    
    
# Get user input 
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

#Call the function with user input 
final_price = calculate_discount(price, discount_percent)

#Print the result
if discount_percent >= 20:
    print(f"Discount applied. Final price: ${final_price}")
else:
    print(f"No discount applied. Price remains: ${final_price}")