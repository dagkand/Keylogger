import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
from keylogger import start_keylogger, stop_keylogger
from detector import scan_for_keyloggers

# GUI Setup
root = tk.Tk()
root.title("Keylogger & Detector")
root.geometry("500x450")
root.resizable(False, False)

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))

# Frame
frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

# Status Label
status_label = ttk.Label(frame, text="Status: Stopped", foreground="red")
status_label.pack(pady=5)

# Buttons
def start_keylogger_wrapper():
    result = start_keylogger()
    status_label.config(text="Status: Running", foreground="green")
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, f"{result}\n")
    log_text.config(state=tk.DISABLED)

start_button = ttk.Button(frame, text="Start Keylogger", command=lambda: threading.Thread(target=start_keylogger_wrapper, daemon=True).start())
start_button.pack(pady=5, fill=tk.X)

def stop_keylogger_wrapper():
    result = stop_keylogger()
    status_label.config(text="Status: Stopped", foreground="red")
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, f"{result}\n")
    log_text.config(state=tk.DISABLED)

stop_button = ttk.Button(frame, text="Stop Keylogger", command=stop_keylogger_wrapper)
stop_button.pack(pady=5, fill=tk.X)

def scan_for_keyloggers_wrapper():
    result = scan_for_keyloggers()
    log_text.config(state=tk.NORMAL)
    log_text.delete(1.0, tk.END)
    log_text.insert(tk.END, result)
    log_text.config(state=tk.DISABLED)

scan_button = ttk.Button(frame, text="Scan for Possible Malicous software", command=scan_for_keyloggers_wrapper)
scan_button.pack(pady=5, fill=tk.X)

# Log Output
log_text = scrolledtext.ScrolledText(frame, width=60, height=10, state=tk.DISABLED)
log_text.pack(pady=10, fill=tk.BOTH, expand=True)

# Run GUI
root.mainloop()