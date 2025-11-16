import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from TIcket_System import TicketSystem   # change to your actual filename

class TicketSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket System")
        self.system = TicketSystem()

        # Main frame
        frame = tk.Frame(root, padx=20, pady=20)
        frame.pack()

        # Title
        tk.Label(frame, text="Ticket System Admin Panel", font=("Arial", 16, "bold")).pack(pady=10)

        # Buttons
        btns = [
            ("View Waiting Queue", self.view_queue),
            ("Process Next Request", self.process_next),
            ("Cancel Last Sold Ticket", self.cancel_last_sold),
            ("Cancel Ticket by ID", self.cancel_by_id),
            ("View Last Sold Ticket", self.view_last_sold),
            ("View Sold Ticket History", self.view_sold_history),
            ("Exit", root.quit)
        ]

        for text, cmd in btns:
            tk.Button(frame, text=text, width=30, command=cmd).pack(pady=4)

        # Text display box
        self.text_box = tk.Text(root, width=80, height=20, wrap="word")
        self.text_box.pack(pady=10)

    # Utility display
    def display(self, content):
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, content)

    # Display queue
    def view_queue(self):
        if not self.system.waiting_queue:
            self.display("Queue is empty.")
            return
        output = "Waiting Queue:\n\n"
        for i, req in enumerate(self.system.waiting_queue, 1):
            output += f"{i}. {req.name} | {req.event} | Qty: {req.quantity} | Price: {req.price}\n"
        self.display(output)

    # Process next request using Y/N prompt simulation
    def process_next(self):
        if not self.system.waiting_queue:
            messagebox.showinfo("Info", "No tickets in the queue.")
            return

        req = self.system.waiting_queue[0]
        details = f"Name: {req.name}\nEvent: {req.event}\nQuantity: {req.quantity}\nPrice: {req.price}"

        approve = messagebox.askyesno("Process Request", f"{details}\n\nApprove this request?")
        if approve:
            self.system.process_next_in_queue()
            messagebox.showinfo("Success", "Request processed.")
        else:
            self.system.waiting_queue.append(self.system.waiting_queue.popleft())
            messagebox.showinfo("Moved", "Customer moved to end of queue.")

    # Cancel last sold
    def cancel_last_sold(self):
        if not self.system.sold_ticket_stack:
            messagebox.showinfo("Info", "No sold tickets.")
            return

        last = self.system.sold_ticket_stack[-1]
        details = str(last)

        sure = messagebox.askyesno("Cancel Ticket", f"{details}\n\nAre you sure?")
        if sure:
            self.system.cancel_last_sold()
            messagebox.showinfo("Canceled", "Last sold ticket canceled.")
        else:
            messagebox.showinfo("Aborted", "Operation canceled.")

    # Cancel by ID
    def cancel_by_id(self):
        try:
            tid = simpledialog.askinteger("Cancel Ticket by ID", "Enter Ticket ID:")
            if tid is None:
                return
            self.system.cancel_ticket_by_id(tid)
            messagebox.showinfo("Done", "Ticket processed. Check queue.")
        except:
            messagebox.showerror("Error", "Invalid ID.")

    # View last sold
    def view_last_sold(self):
        if not self.system.sold_ticket_stack:
            self.display("No sold tickets yet.")
            return
        self.display(f"Last Sold Ticket:\n\n{self.system.sold_ticket_stack[-1]}")

    # View sold history
    def view_sold_history(self):
        if not self.system.sold_ticket_stack:
            self.display("No tickets sold.")
            return
        output = "Sold Ticket History:\n\n"
        for t in self.system.sold_ticket_stack:
            output += str(t) + "\n"
        self.display(output)

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    TicketSystemGUI(root)
    root.mainloop()