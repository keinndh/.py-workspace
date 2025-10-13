# Programming Exercise 14
# Marajan, Abduljal A. BSCOE 2

print("ABC STORE 10th ANNIVERSARY")

while True:
    try:
        amount_purchased = float(input("\nEnter the amount purchased: "))
        break
    except ValueError:
        print("Invalid input. Please try a valid value")

if amount_purchased > 500.0:
    discount_rate = 0.20 #20%
    discounted_amount = amount_purchased * discount_rate
else:
    discount_rate = 0.05 #5%
    discounted_amount = amount_purchased * discount_rate

due_customer_amount = amount_purchased - discounted_amount

print("\nAmount Purchase: Php", int(amount_purchased))
print("Discounted Amount : Php", discounted_amount)
print("Due Amount: Php", due_customer_amount)