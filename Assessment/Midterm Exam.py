import os

# Lists
malls = ["KCC de Zamboanga", "SM Mindpro", "Other Stores", "Repeat or Exit"]
store = ["Grocery Store", "Department Store", "Exit"]

# Prompts
total_purchased_amount_prompt = "Enter Total Amount of Purchases: PHP "
invalid_input_prompt = "Invalid input. Please enter a valid input."
ticket_received_prompt = "Raffle Ticket Received:"
voucher_received_prompt = "100 Cash Voucher Received:"
return_prompt = "Please press Enter to return..."

# Declared Variables
reward = 0
calculated_total_amount = 0
total_purchased_amount = 0

while True:
    os.system('cls')
    print("Marajan, Abduljal A.")
    print("\nMENU")
    for i in range(4):
        print(f"{i + 1}. {malls[i]}")
    print("\nMalls: ")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print(invalid_input_prompt)
        input(return_prompt)
        continue

    if choice <= 0 or choice > 4:
        print(invalid_input_prompt)
        input(return_prompt)
        continue

    if choice == 1:
        while True:
            os.system('cls')
            print(malls[choice - 1])
            print("\nSTORE MENU:")
            for i in range(3):
                print(f"{i + 1}. {store[i]}")
            print("\nLocation of Purchased Items")
            try:
                second_choice = int(input("Enter choice: "))
            except ValueError:
                print(invalid_input_prompt)
                input(return_prompt)
                continue

            if second_choice <= 0 or second_choice > 3:
                print(invalid_input_prompt)
                input(return_prompt)
                continue

            if second_choice == 1:
                os.system('cls')
                print(f"{store[second_choice - 1]}\n")
                try:
                    total_purchased_amount = float(input(total_purchased_amount_prompt))
                except ValueError:
                    print(invalid_input_prompt)
                    input(return_prompt)
                    continue

                if total_purchased_amount >= 600:
                    calculated_total_amount = total_purchased_amount // 600
                    reward = int(calculated_total_amount)
                    print(f"{ticket_received_prompt} {reward}\n")
                else:
                    print(f"{ticket_received_prompt} {reward}\n")
                input(return_prompt)

            elif second_choice == 2:
                os.system('cls')
                print(f"{store[second_choice - 1]}\n")
                try:
                    total_purchased_amount = float(input(total_purchased_amount_prompt))
                except ValueError:
                    print(invalid_input_prompt)
                    input(return_prompt)
                    continue

                if total_purchased_amount >= 300:
                    calculated_total_amount = total_purchased_amount // 300
                    reward = int(calculated_total_amount)
                    print(f"{ticket_received_prompt} {reward}")
                    print(f"{voucher_received_prompt} {reward}\n")
                else:
                    print(f"{ticket_received_prompt} {reward}")
                    print(f"{voucher_received_prompt} {reward}\n")
                input(return_prompt)

            elif second_choice == 3:
                break

    elif choice == 2:
        os.system('cls')
        print(malls[choice - 1])
        try:
            total_purchased_amount = float(input(total_purchased_amount_prompt))
        except ValueError:
            print(invalid_input_prompt)
            input(return_prompt)
            continue

        if total_purchased_amount >= 3000:
            calculated_total_amount = total_purchased_amount - (total_purchased_amount * 0.10)
            print("Discount Received: 10%")
            print(f"Amount of Purchases after Discount : PHP {calculated_total_amount}\n")
        else:
            print(f"Amount of Purchases: PHP {total_purchased_amount}\n")
        input(return_prompt)

    elif choice == 3:
        os.system('cls')
        print(malls[choice - 1])
        print("No Promo AVAILABLE!\n")
        input(return_prompt)

    elif choice == 4:
        break