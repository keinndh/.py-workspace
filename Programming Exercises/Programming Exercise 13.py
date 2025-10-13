# Programming Exercise 13
# Marajan, Abduljal A. BSCOE 2

print("CDE MALL 15th ANNIVERSARY")

while True:
    try:
        amount_purchased = float(input("\nEnter the amount purchased: "))
        break
    except ValueError:
        print("Invalid input. Please try a valid value")
      
if amount_purchased >= 300.0:
    initial_raffle_tickets = 5
    amount_counted = int(amount_purchased / 300)
    raffle_ticket_received = initial_raffle_tickets * amount_counted
else:
    raffle_ticket_received = 0 

print("Ticket Received: ", int(raffle_ticket_received))    
    