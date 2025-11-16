import collections
import time
import os

class Ticket:
    def __init__(self, ticket_id, event, holder, quantity, price):
        self.ticket_id = ticket_id
        self.event = event
        self.holder = holder
        self.quantity = quantity
        self.price = price
      
    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f"ID: {self.ticket_id}, Event: {self.event}, Holder: {self.holder}, Qty: {self.quantity}, Total: ${self.total_price():.2f}"

class CustomerRequest:
    def __init__(self, name, event, quantity, price):
        self.name = name
        self.event = event
        self.quantity = quantity
        self.price = price

class TicketSystem:
    def __init__(self):
        self.waiting_queue = collections.deque([
            CustomerRequest("Enzo", "Concert", 2, 50.0),
            CustomerRequest("Mon", "Fan Meet", 3, 75.0),
            CustomerRequest("Neil", "Musical Play", 1, 60.0),
            CustomerRequest("Kath", "Film Festival", 4, 80.0),
            CustomerRequest("John", "Art Exhibition", 2, 55.0)
        ])

        self.sold_ticket_stack = [] 
        self.next_ticket_id = 1001

    def display_queue(self):
        print("\nWaiting Queue:")
        if not self.waiting_queue:
            print("Queue is empty.")
            return
        for i, req in enumerate(self.waiting_queue, 1):
            print(f"{i}. {req.name} | {req.event} | Qty: {req.quantity} | Price: {req.price}")
          
    def process_next_in_queue(self):
        if not self.waiting_queue:
            print("No ticket requests in the queue.")
            return

        req = self.waiting_queue[0] 
      
        print("\nFirst Customer in Queue:")
        print(f"Name: {req.name}")
        print(f"Event: {req.event}")
        print(f"Quantity: {req.quantity}")
        print(f"Price: {req.price}")

        choice = input("\nApprove this customer's request? (Y/N): ").strip().lower()
        if choice == 'y':
            self.waiting_queue.popleft()
            ticket = Ticket(
                self.next_ticket_id,
                req.event,
                req.name,
                req.quantity,
                req.price
            )
            
            self.sold_ticket_stack.append(ticket)
            self.next_ticket_id += 1 
          
            print("\n...")
            time.sleep(1)

            print("\nTransaction Completed:")
            print(ticket)
          
        elif choice == 'n':
            req = self.waiting_queue.popleft()
            self.waiting_queue.append(req)
            print("\nCustomer moved to the end of the queue.")
        else:
            print("Invalid input. Please enter Y or N.")

    def view_last_sold(self):
        if not self.sold_ticket_stack:
            print("No sold tickets yet.")
            return
        print("\nLast Sold Ticket:")
        print(self.sold_ticket_stack[-1])

    def cancel_last_sold(self):
        if not self.sold_ticket_stack:
            print("No sold tickets yet.")
            return

        print("\nLast Sold Ticket:")
        print(self.sold_ticket_stack[-1])

        choice = input("\nAre you certain? (Y/N): ").strip().lower() 
      
        if choice == 'y':
            canceled = self.sold_ticket_stack.pop()
            print("\nCanceled Last Ticket:")
            print(canceled)

            self.waiting_queue.appendleft(
                CustomerRequest(
                    canceled.holder,
                    canceled.event,
                    canceled.quantity,
                    canceled.price
                )
            )

        elif choice == 'n':
            print("Cancellation aborte
        else:
            print("Invalid input. Please enter Y or N.")
    

    def cancel_ticket_by_id(self, ticket_id):
        if not self.sold_ticket_stack:
            print("No sold tickets yet.")
            return

        temp_stack = []
        found = None

        while self.sold_ticket_stack:
            top = self.sold_ticket_stack.pop()
            if top.ticket_id == ticket_id:
                found = top
                break
            temp_stack.append(top)

        while temp_stack:
            self.sold_ticket_stack.append(temp_stack.pop())

        if not found:
            print("Ticket ID not found.")
            return

        print("\nCanceled Ticket:")
        print(found)

        self.waiting_queue.appendleft(
            CustomerRequest(
                found.holder,
                found.event,
                found.quantity,
                found.price
            )
        )

    def display_sold_history(self):
        print("\nSold Ticket History:")
        if not self.sold_ticket_stack:
            print("No tickets sold.")
        else:
            for t in self.sold_ticket_stack:
                print(t)

class Main:
    @staticmethod
    def run():
        ticket_system = TicketSystem()
        returning = "\nPress Enter..."

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
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
                ticket_system.display_queue()
                input(returning)
            elif choice == '2':
                print("\n== Process Request by Position ==")
                ticket_system.display_queue()
                ticket_system.process_next_in_queue()
                input(returning)
            elif choice == '3':
                print("\n== Cancel Last Sold Ticket ==")
                ticket_system.cancel_last_sold()
                input(returning)
            elif choice == '4':
                print("\n=== Cancel Ticket by ID ==\n")
                try:
                    tid = int(input("Enter Ticket ID: "))
                    ticket_system.cancel_ticket_by_id(tid)
                except ValueError:
                    print("Invalid ID.")
                input(returning)
            elif choice == '5':
                print("\n== View Last Sold Ticket ==")
                ticket_system.view_last_sold()
                input(returning)
            elif choice == '6':
                print("\n== View Sold Ticket History ==")
                ticket_system.display_sold_history()
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")
                input("\nPress Enter...")

if __name__ == "__main__":

    Main.run()


