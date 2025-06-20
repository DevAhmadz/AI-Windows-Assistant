import tkinter as tk
from tkinter import messagebox
from intent_matcher import get_intent
from pin_check import verify_pin
from command_router import run_command
from logger import log_action

def handle_fix():
    query = entry.get()
    pin = pin_entry.get()

    if not query.strip():
        messagebox.showwarning("Input Missing", "Please describe your issue.")
        return

    intent = get_intent(query)
    if not intent:
        output.config(text="Couldn’t match issue. Try rephrasing.")
        return

    if verify_pin(pin):
        result = run_command(intent)
        log_action(query, intent, result)
        output.config(text=f"✅ Fix executed: {result}")
    else:
        messagebox.showerror("Invalid PIN", "Incorrect PIN. Fix not allowed.")

# UI setup
app = tk.Tk()
app.title("System Buddy - Offline IT Assistant")
app.geometry("500x300")

tk.Label(app, text="💬 Describe your issue:").pack(pady=5)
entry = tk.Entry(app, width=50)
entry.pack()

tk.Label(app, text="🔐 Enter PIN:").pack(pady=5)
pin_entry = tk.Entry(app, show="*", width=20)
pin_entry.pack()

tk.Button(app, text="Run Fix", command=handle_fix, bg="green", fg="white").pack(pady=10)

output = tk.Label(app, text="", wraplength=400, fg="blue")
output.pack(pady=10)

app.mainloop()