# Programming Exercise 11
# Marajan, Abduljal A. BSCOE 2

print("STORE ANNIVERSARY SALE")

shirt_A_price = 50
shirt_B_price = 75
shirt_C_price = 100

while True:
    try:
        shirt_A = int(input("\nEnter quantity for shirt A: "))
        shirt_B = int(input("Enter quantity for shirt B: "))
        shirt_C = int(input("Enter quantity for shirt C: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer amount.")

total_purchases = (shirt_A * shirt_A_price) + (shirt_B * shirt_B_price) + (shirt_C * shirt_C_price)

if total_purchases >= 1000:
    discount_count = int(total_purchases / 1000)
    discount_rate = 0.05 * discount_count
    discountable_amount = shirt_A * shirt_A_price
    discounted_price = discountable_amount * discount_rate
else:
    discounted_price = 0

total_price = total_purchases - discounted_price

print("\nTotal Purchases: Php", round(total_purchases, 2))
print("Discounted Amount: Php", round(discounted_price, 2))
print("Total Amount after Discount: Php", round(total_price, 2))