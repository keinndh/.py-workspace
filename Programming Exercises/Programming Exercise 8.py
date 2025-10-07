# Programming Exercise 8
# Marajan, Abduljal A. BSCOE 2

eur = 0
usd = 0.0
print("Money Conversion (verison 4)")
while True:
    try:
        eur = int(input("\nEnter amount in EUR: "))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        
usd = eur * 1.18
print("Equivalent amount in USD: ", usd)


