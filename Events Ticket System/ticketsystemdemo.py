import collections
import time
import os
import re
from enum import Enum

# ENUM CLASS
class Availability(Enum):
    AVAILABLE = "AVAILABLE"
    SOLD = "SOLD"
    VOID = "VOID"
    RESERVED = "RESERVED"

class SeatType(Enum):
    REGULAR = "Regular"
    VIP = "VIP"
    VVIP = "VVIP"

class PaymentMethod(Enum):
    E_WALLET = "E-Wallet"
    DEBIT = "Debit"

# DATA CLASS
class Event:
    def __init__(self, name, venue, date, time, price, total_seats=100):
        self.name = name
        self.venue = venue
        self.date = date
        self.time = time
        self.price = price
        self.total_seats = total_seats
        self.sold_seats = 0

    @property
    def remaining_seats(self):
        return self.total_seats - self.sold_seats

    @property
    def availability(self):
        if self.remaining_seats <= 0:
            return Availability.SOLD
        return Availability.AVAILABLE

    def __str__(self):
        return (
            f"{self.name:<20} {self.venue:<20} {self.date:<20} {self.time:<12} "
            f"${self.price:<12} {self.remaining_seats:<14} {self.availability.value:<19}"
        )

class CustomerRequest:
    def __init__(self, holder, event, quantity, price, seat_type=SeatType.REGULAR, payment_method=PaymentMethod.E_WALLET):
        self.holder = holder
        self.event = event
        self.quantity = quantity
        self.price = price
        self.seat_type = seat_type
        self.payment_method = payment_method

class Notification:
    def __init__(self, recipient, message, timestamp=None):
        self.recipient = recipient
        self.message = message
        self.timestamp = timestamp or time.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"\n{self.timestamp:<20} {self.message:<50}"

class Payment:
    def __init__(self, method: PaymentMethod, amount: float):
        self.method = method
        self.amount = amount
        self.status = 'pending'

class Ticket:
    def __init__(self, ticket_id, event, holder, quantity, price, seat_type=SeatType.REGULAR, status=Availability.SOLD, payment=None):
        self.ticket_id = ticket_id
        self.event = event
        self.holder = holder
        self.quantity = quantity
        self.price = price
        self.seat_type = seat_type
        self.status = status
        self.payment = payment

    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return (
            f"{self.ticket_id:<5} {self.event.name if isinstance(self.event, Event) else self.event:<20} "
            f"{self.holder:<15} {self.quantity:<5} {self.seat_type.value:<7} {self.status.value:<10} ${self.total_price():<6.2f}"
        )

# OPERATIONS CLASS
class TicketSystem:
    def __init__(self):
        self.events = [
            Event("Concert", "Arena Manila", "Dec 20, 2025", "7:00 PM", 50.0, 100),
            Event("Fan Meet", "Mall Event Hall", "Jan 10, 2026", "3:00 PM", 75.0, 50),
            Event("Musical Play", "Grand Theater", "Feb 15, 2026", "6:00 PM", 60.0, 80),
            Event("Film Festival", "Cinema City", "Mar 5, 2026", "1:00 PM", 80.0, 60),
            Event("Art Exhibition", "Museum Hall", "Apr 1, 2026", "10:00 AM", 55.0, 120),
        ]
        self.request_queue = collections.deque()
        self.sold_ticket_stack = []
        self.approved_tickets = {}
        self.pending_requests = {}
        self.next_ticket_id = 1001
        self.notifications = {}

    # CUSTOMER INTERFACE
    def browse_events(self):
        print("\n                                           === Available Events ===\n")
        print(f"{'No.':<3} {'Event':<20} {'Venue':<20} {'Date':<20} {'Time':<12} {'Price':<13} {'Remaining':<14} {'Status':<20}")
        print("-"*118)
        for i, ev in enumerate(self.events, 1):
            print(f"{i:<3} {ev}")

    def view_event_details(self, index):
        if 1 <= index <= len(self.events):
            ev = self.events[index - 1]
            print("\nEvent Details:")
            print(f"\nName: {ev.name}")
            print(f"Venue: {ev.venue}")
            print(f"Date: {ev.date}")
            print(f"Time: {ev.time}")
            print(f"Price: ${ev.price:.2f}")
            print(f"Remaining Seats: {ev.remaining_seats}")
            print(f"Availability: {ev.availability.value}")
            return ev
        print("\nInvalid selection.")
        return None

    def request_ticket(self, holder, event, qty, seat_type=SeatType.REGULAR, payment_method=PaymentMethod.E_WALLET):
        req = CustomerRequest(holder, event.name, qty, event.price, seat_type, payment_method)
        self.request_queue.append(req)
        self.pending_requests.setdefault(holder, []).append(req)
        print(f"\nRequest for {qty} ticket(s) to {event.name} added to queue.")

    def view_pending(self, holder):
        print(f"\n=== Pending Requests for {holder} ===\n")
        if holder not in self.pending_requests or not self.pending_requests[holder]:
            print("No pending requests.")
            return
        print(f"{'Event':<20} {'Qty':<5} {'Price':<6} {'Seat':<7} {'Payment':<10}")
        print("-"*60)
        for r in self.pending_requests[holder]:
            print(f"{r.event:<20} {r.quantity:<5} ${r.price:<6.2f} {r.seat_type.value:<7} {r.payment_method.value:<10}")

    def view_approved(self, holder):
        print(f"\n=== Approved Tickets for {holder} ===\n")
        if holder not in self.approved_tickets or not self.approved_tickets[holder]:
            print("No approved tickets yet.")
            return
        print(f"{'ID':<5} {'Event':<20} {'Holder':<15} {'Qty':<5} {'Seat':<7} {'Status':<10} {'Total':<6}")
        print("-"*75)
        for t in self.approved_tickets[holder]:
            print(f"\n{t}")

    def view_notifications(self, holder):
        print(f"\n=== Notifications for {holder} ===\n")
        notes = self.notifications.get(holder, [])
        if not notes:
            print("No notifications.")
            return
        print(f"{'Time':<20} {'Message':<50}")
        print("-"*70)
        for n in notes:
            print(n)

    # ADMIN MENU FUNCTIONS
    def view_queue(self):
        print("\n=== Registration Queue ===\n")
        if not self.request_queue:
            print("Queue is empty.")
            return
        print(f"{'No.':<3} {'Holder':<15} {'Event':<20} {'Qty':<5} {'Seat':<7} {'Payment':<10}")
        print("-"*65)
        for i, req in enumerate(self.request_queue, 1):
            print(f"{i:<3} {req.holder:<15} {req.event:<20} {req.quantity:<5} {req.seat_type.value:<7} {req.payment_method.value:<10}")

    def process_next(self):
        if not self.request_queue:
            print("\nQueue empty.")
            return
        req = self.request_queue[0]
        print(f"\nNext in queue: {req.holder} -> {req.event} ({req.quantity} tickets)")
        choice = input("Approve? (Y/N): ").lower()
        if choice == "y":
            self.request_queue.popleft()
            event_obj = next((ev for ev in self.events if ev.name == req.event), None)
            if event_obj and event_obj.remaining_seats >= req.quantity:
                event_obj.sold_seats += req.quantity
            else:
                print("\nNot enough seats. Skipping request.")
                return
            payment = Payment(req.payment_method, req.price * req.quantity)
            payment.status = 'paid'
            ticket = Ticket(self.next_ticket_id, event_obj, req.holder, req.quantity, req.price, req.seat_type, Availability.SOLD, payment)
            self.sold_ticket_stack.append(ticket)
            self.next_ticket_id += 1
            self.approved_tickets.setdefault(req.holder, []).append(ticket)
            self.pending_requests[req.holder].remove(req)
            self.send_notification(req.holder, f"\nTicket {ticket.ticket_id} for {ticket.event.name} purchased.")
            print("\nApproved and ticket generated.\nTicket Details:")
            print(f"\n{'ID':<5} {'Event':<20} {'Holder':<15} {'Qty':<5} {'Seat':<7} {'Status':<10} {'Total':<6}")
            print("-"*75)
            print(ticket)
        elif choice == "n":
            self.request_queue.append(self.request_queue.popleft())
            print("\nMoved to end of queue.")
        else:
            print("\nInvalid.")

    def view_last_sold(self):
        if not self.sold_ticket_stack:
            print("\nNo tickets sold yet.")
            return
        print(f"\n{'ID':<5} {'Event':<20} {'Holder':<15} {'Qty':<5} {'Seat':<7} {'Status':<10} {'Total':<6}")
        print("-"*75)
        print(self.sold_ticket_stack[-1])

    def cancel_last_sold(self):
        if not self.sold_ticket_stack:
            print("\nNo sold tickets.")
            return
        ticket = self.sold_ticket_stack.pop()
        ticket.status = Availability.VOID
        if isinstance(ticket.event, Event):
            ticket.event.sold_seats -= ticket.quantity
        if ticket.payment:
            ticket.payment.status = 'refunded'
            self.send_notification(ticket.holder, f"\nTicket {ticket.ticket_id} refunded.")
        print(f"\nCanceled ticket:\n{ticket}")
        req = CustomerRequest(ticket.holder, ticket.event.name if isinstance(ticket.event, Event) else ticket.event, ticket.quantity, ticket.price)
        self.request_queue.appendleft(req)

    def cancel_ticket_by_id(self, ticket_id):
        if not self.sold_ticket_stack:
            print("\nNo sold tickets.")
            return
        temp = []
        found = None
        while self.sold_ticket_stack:
            t = self.sold_ticket_stack.pop()
            if t.ticket_id == ticket_id:
                found = t
                break
            temp.append(t)
        for t in reversed(temp):
            self.sold_ticket_stack.append(t)
        if not found:
            print("\nTicket ID not found.")
            return
        found.status = Availability.VOID
        if isinstance(found.event, Event):
            found.event.sold_seats -= found.quantity
        if found.payment:
            found.payment.status = 'refunded'
            self.send_notification(found.holder, f"Ticket {found.ticket_id} refunded.")
        print(f"\nCanceled ticket:\n{found}")
        req = CustomerRequest(found.holder, found.event.name if isinstance(found.event, Event) else found.event, found.quantity, found.price)
        self.request_queue.appendleft(req)

    def history(self):
        print(f"\n{'ID':<5} {'Event':<20} {'Holder':<15} {'Qty':<5} {'Seat':<7} {'Status':<10} {'Total':<6}")
        print("-"*75)
        for t in self.sold_ticket_stack:
            print(t)

    def send_notification(self, recipient, message):
        note = Notification(recipient, message)
        self.notifications.setdefault(recipient, []).append(note)

    @staticmethod
    def name_validation(self, name):
        if re.fullmatch(r"^[A-Za-z\s\-]+$", name):
            return True
        print("Invalid name.")
        return False

# MAIN CLASS
name_prompt = "\nYour name: "
invalid_prompt = "\nInvalid input."
enter_prompt = "\nPress Enter to continue..."

class Main:
    @staticmethod
    def run():
        system = TicketSystem()
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            Main.display_customer_menu()
            choice = input("\n>> ")
            Main.handle_customer_choice(choice, system, name_prompt)

    @staticmethod
    def display_customer_menu():
        print("=== Customer Menu ===\n")
        print("1. Browse Events")
        print("2. View Event Details")
        print("3. Request Ticket")
        print("4. View My Pending Requests")
        print("5. View My Approved Tickets")
        print("6. View My Notifications")
        print("7. Admin Interface")
        print("8. Exit")

    @staticmethod
    def handle_customer_choice(choice, system, name_prompt):
        if choice == "1":
            system.browse_events()
            input(enter_prompt)
        elif choice == "2":
            system.browse_events()
            try:
                idx = int(input("\nSelect event number: "))
                system.view_event_details(idx)
            except ValueError:
                print(invalid_prompt)
            input(enter_prompt)
        elif choice == "3":
            system.browse_events()
            try:
                idx = int(input("\nSelect event number: "))
                ev = system.view_event_details(idx)
                if not ev:
                    input(enter_prompt)
                    return
                print("\nEnter ticket request details:")
                name = input("Your name: ")
                qty = int(input("Quantity: "))
                print("\nSeat types:\n1. Regular\n2. VIP\n3. VVIP")
                st = input("\n>> ").strip()
                seat_type = SeatType.REGULAR
                if st == '2':
                    seat_type = SeatType.VIP
                elif st == '3':
                    seat_type = SeatType.VVIP
                print("\nPayment methods:\n1. E-Wallet\n2. Debit")
                pm_choice = input("\n>> ").strip()
                pm = PaymentMethod.E_WALLET if pm_choice != '2' else PaymentMethod.DEBIT
                system.request_ticket(name, ev, qty, seat_type=seat_type, payment_method=pm)
            except ValueError:
                print(invalid_prompt)
            input(enter_prompt)
        elif choice == "4":
            name = input(name_prompt)
            system.view_pending(name)
            input(enter_prompt)
        elif choice == "5":
            name = input(name_prompt)
            system.view_approved(name)
            input(enter_prompt)
        elif choice == "6":
            name = input(name_prompt)
            system.view_notifications(name)
            input(enter_prompt)
        elif choice == "7":
            Main.handle_admin_interface(system)
        elif choice == "8":
            exit()

    @staticmethod
    def handle_admin_interface(system):
        try:
            passcode = int(input("Enter admin passcode: "))
            if passcode == 1234:
                Main.admin_menu(system)
            else:
                print("\nInvalid password.")
        except ValueError:
            print(invalid_prompt)
        input(enter_prompt)

    @staticmethod
    def admin_menu(system):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== Admin Menu ===\n")
            print("1. View Queue")
            print("2. Process First Request")
            print("3. View Last Sold")
            print("4. Cancel Last Sold")
            print("5. Cancel Sold Ticket by ID")
            print("6. Ticket History")
            print("7. Back")
            choice = input("\n>> ")
            if choice == "1":
                system.view_queue()
                input(enter_prompt)
            elif choice == "2":
                system.process_next()
                input(enter_prompt)
            elif choice == "3":
                system.view_last_sold()
                input(enter_prompt)
            elif choice == "4":
                system.cancel_last_sold()
                input(enter_prompt)
            elif choice == "5":
                try:
                    tid = int(input("Enter Ticket ID to cancel: "))
                    system.cancel_ticket_by_id(tid)
                except ValueError:
                    print(invalid_prompt)
                input(enter_prompt)
            elif choice == "6":
                system.history()
                input(enter_prompt)
            elif choice == "7":
                break

if __name__ == "__main__":

    Main.run()
