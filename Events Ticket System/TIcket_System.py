import collections
import time
import os

'''
Things to know: 
                1. Class: A blueprint for creating objects that encapsulate data and methods to operate on that data.
                2. Functions: Blocks of reusable code that perform specific tasks. They are defined using the `def` keyword.
                3. For Loops: A control flow statement for iterating over a sequence (like a list, tuple, or string).
                4. self (the one inside the function as parameter): A reference to the current instance of the class. It is used to access variables and methods associated with the object.
                5. _init_: This method acts as the constructor for a class. It is automatically called when a new instance of the class is created.
                6. self.(name of variable): Here in Python, `self.variable_name` is used instead of `this.variable_name` (as in some other languages like java) to refer to instance variables like a constructor ba.
'''

# Ticket class to hold ticket details
class Ticket:
    # Function is a constructor of the class that holds the necessary customer details for all the function processes below
    def __init__(self, ticket_id, event, holder, quantity, price):
        self.ticket_id = ticket_id
        self.event = event
        self.holder = holder
        self.quantity = quantity
        self.price = price

    # Function for calculating the total amount of ticket purchased
    def total_price(self):
        return self.quantity * self.price # Multiplying price by the quantity

    # Function for displaying customer request details in the queue
    def __str__(self):
        return f"ID: {self.ticket_id}, Event: {self.event}, Holder: {self.holder}, Qty: {self.quantity}, Total: ${self.total_price():.2f}" # Printing their information

# Customer request class where we store their request details from the initialized queue from the _init_ function of the main class for easy calling
class CustomerRequest:
    # Function where we store the values in their respective variable
    def __init__(self, name, event, quantity, price):
        self.name = name
        self.event = event
        self.quantity = quantity
        self.price = price

# Ticket system main class for all the system's processes
class TicketSystem:
    def __init__(self):
        # Initializing the queue of customer requests
        self.waiting_queue = collections.deque([
            # Customers request details
            CustomerRequest("Enzo", "Concert", 2, 50.0),
            CustomerRequest("Mon", "Fan Meet", 3, 75.0),
            CustomerRequest("Neil", "Musical Play", 1, 60.0),
            CustomerRequest("Kath", "Film Festival", 4, 80.0),
            CustomerRequest("John", "Art Exhibition", 2, 55.0)
        ])

        self.sold_ticket_stack = []  # Initializing the inventory as stack for sold tickets
        self.next_ticket_id = 1001 # Initializing our base and first transaction id

    # Function for displaying the queue or waiting queue
    def display_queue(self):
        print("\nWaiting Queue:")
        if not self.waiting_queue: # Check if we have a queue (meron man yan pero just incase)
            print("Queue is empty.")
            return
        # If there is a queue we will proceed with this for loop after the return syntax
        # For this for loop we examine or check the index number (i) and the actual item while looping through the whole people in the waiting list staring by the position number 1
        for i, req in enumerate(self.waiting_queue, 1):
            print(f"{i}. {req.name} | {req.event} | Qty: {req.quantity} | Price: {req.price}") # Display their requests details

    # Function for processing the current first customer in the waiting queue
    def process_next_in_queue(self):
        # Check if there is really people in the waiting queue
        if not self.waiting_queue:
            print("No ticket requests in the queue.")
            return

        req = self.waiting_queue[0]  # Peek front after return if there is a person for us to display (below is the code) storing in the variable "req"
        # Display the ticket request details of the first in queue
        print("\nFirst Customer in Queue:")
        print(f"Name: {req.name}")
        print(f"Event: {req.event}")
        print(f"Quantity: {req.quantity}")
        print(f"Price: {req.price}")

        choice = input("\nApprove this customer's request? (Y/N): ").strip().lower() # strip() to remove unnecessary spaces
        # Condition for processing the request if input was "y (yes)"
        if choice == 'y':
            self.waiting_queue.popleft() # Since we are processing this customer request, we will now dequeue him from the waiting queue
            ticket = Ticket( # Get the person's information from the class ticket in the first function we made (the inventory of the waiting queue)
                self.next_ticket_id,
                req.event,
                req.name,
                req.quantity,
                req.price
            )
            
            self.sold_ticket_stack.append(ticket) # Now we add the sold ticket information to our inventory for sold ticket which is a stack
            self.next_ticket_id += 1 # We add one to the current ticket id (check line 55 if you forgot) for number incrementation of the ticket id for uniqueness and to avoid duplication. demo: from 1001 -> 1001 = 1001 + 1 -> 1002

            print("\n...")
            time.sleep(1) # Delay for realistic type shi ah transaction

            # Display the transaction information
            print("\nTransaction Completed:")
            print(ticket)

        # Condition for processing the request if input was "n (no)"
        elif choice == 'n':
        # Move customer to end of queue because we are skipping his queue. why move to the last? since we skip the person we now need to process the next in queue to avoid dealy if we are skipping the current person
            req = self.waiting_queue.popleft()
            self.waiting_queue.append(req) # Add the person's information to the rear location of the queue using append (enqueue) operation
            print("\nCustomer moved to the end of the queue.")
        # Condition for invalid input
        else:
            print("Invalid input. Please enter Y or N.")

    # Function for viewing last sold tickets
    def view_last_sold(self):
        # Check if there was a ticket sold
        if not self.sold_ticket_stack:
            print("No sold tickets yet.")
            return
        # If none proceed here after return then display the last sold ticket details
        print("\nLast Sold Ticket:")
        print(self.sold_ticket_stack[-1])

    # Function foe cancelling the last sold ticket
    def cancel_last_sold(self):
        # Check if there was a ticket sold
        if not self.sold_ticket_stack:
            print("No sold tickets yet.")
            return
        # If none proceed here after return then display the last sold ticket details
        print("\nLast Sold Ticket:")
        print(self.sold_ticket_stack[-1])

        choice = input("\nAre you certain? (Y/N): ").strip().lower() # strip() to remove unnecessary spaces
        # Condition for processing the request if input was "y (yes)"
        if choice == 'y':
            # Cancel the last sold ticket by popping it from the stack inventory
            canceled = self.sold_ticket_stack.pop()
            print("\nCanceled Last Ticket:")
            print(canceled)

            # Enqueue customer back to front of waiting queue
            self.waiting_queue.appendleft(
                CustomerRequest(
                    canceled.holder,
                    canceled.event,
                    canceled.quantity,
                    canceled.price
                )
            )

        elif choice == 'n':
            print("Cancellation aborted.")

        else:
            print("Invalid input. Please enter Y or N.")
    

    # Function for cancelling the sold ticket/s
    def cancel_ticket_by_id(self, ticket_id):
        # Check if there was a ticket sold
        if not self.sold_ticket_stack:
            print("No sold tickets yet.")
            return

        # Initialized a stack name temp_stack and assigned to a variable the None value
        temp_stack = []
        found = None

        # Pop until we find the ticket
        while self.sold_ticket_stack:
            top = self.sold_ticket_stack.pop()
            if top.ticket_id == ticket_id:
                found = top
                break
            temp_stack.append(top)

        # Restore the stack by appending (push) it again
        while temp_stack:
            self.sold_ticket_stack.append(temp_stack.pop())

        # Condition if the ticket ID wa nots found
        if not found:
            print("Ticket ID not found.")
            return

        # Display cancel
        print("\nCanceled Ticket:")
        print(found)

        # Enqueue customer back to the front of the waiting list
        self.waiting_queue.appendleft(
            CustomerRequest(
                found.holder,
                found.event,
                found.quantity,
                found.price
            )
        )

    # Function for history of the sold tickets
    def display_sold_history(self):
        print("\nSold Ticket History:")
        # Check if there was a ticket sold
        if not self.sold_ticket_stack:
            print("No tickets sold.")
        # If there was print the ticket sold information
        else:
            for t in self.sold_ticket_stack:
                print(t)

# Main class for all the code processes happening (calling function and a menu)
class Main:
    @staticmethod # Static method so only works in this class and there was no instance
    def run():
        ticket_system = TicketSystem() # Initialization of object name for the class TicketSystem
        returning = "\nPress Enter..." # Initialization of the please enter to return as returning variable

        # Our biggest contributor, the menu
        while True:
            os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
            print("=== Ticket System Admin Menu For Different Events ===")
            print("\n1. View Waiting Queue")
            print("2. Process Request by Position")
            print("3. Cancel Last Sold Ticket")
            print("4. Cancel Ticket by ID")
            print("5. View Last Sold Ticket")
            print("6. View Sold Ticket History")
            print("7. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                print("\n== View Waiting Queue ==")
                ticket_system.display_queue() # Call the function that display the queue in the class TicketSystem
                input(returning)
            elif choice == '2':
                print("\n== Process Request by Position ==")
                ticket_system.display_queue() # Call the function that display the queue in the class TicketSystem
                ticket_system.process_next_in_queue() # Call the function that processed the request in the waiting list in the class TicketSystem
                input(returning)
            elif choice == '3':
                print("\n== Cancel Last Sold Ticket ==")
                ticket_system.cancel_last_sold() # Call the function that cancels the last sold in the class TicketSystem
                input(returning)
            elif choice == '4':
                print("\n=== Cancel Ticket by ID ==\n")
                try:
                    tid = int(input("Enter Ticket ID: "))
                    ticket_system.cancel_ticket_by_id(tid) # Call the function that cancels the sold by id in the class TicketSystem
                except ValueError:
                    print("Invalid ID.")
                input(returning)
            elif choice == '5':
                print("\n== View Last Sold Ticket ==")
                ticket_system.view_last_sold() # # Call the function that view the last sold in the class TicketSystem
                input(returning)
            elif choice == '6':
                print("\n== View Sold Ticket History ==")
                ticket_system.display_sold_history() # Call the function that view the all transaction of requests history in the class TicketSystem
                input(returning)
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")
                input("\nPress Enter...")

if __name__ == "__main__": # Look for the __main__ method to run the program
    Main.run() # Run the main class if found