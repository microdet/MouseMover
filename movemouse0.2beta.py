import tkinter as tk
import ctypes
import time
import threading

# Definiáljuk a mouse_event függvény paramétereit
MOUSEEVENTF_MOVE = 0x0001
MyTime = 60  # Definiáljuk a várakozási időt
MySpace = 1  # Definiáljuk a távolságot

# Create Tkinter window
window = tk.Tk()
window.title("Mouse Mover")

# Label to display mouse movement status
status_label = tk.Label(window, text="")
status_label.pack()


# Function to move the mouse

def move_mouse(dx, dy):
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, dx, dy, 0, 0)


# Function to perform mouse movement
def perform_mouse_movement():
    while True:
        # Szimulált egérmozgás
        status_label.config(
            text='Mouse moved ({0} pixels). Current time: {1}. Waiting for {2} seconds.'.format(MySpace, time.time(),
                                                                                                MyTime))
        move_mouse(MySpace, MySpace)
        time.sleep(MyTime)  # Várakozás 3 másodpercig

        # Újabb szimulált egérmozgás (50 pixel balra, 50 pixel felfelé)
        status_label.config(
            text='Mouse moved ({0} pixels). Current time: {1}. Waiting for {2} seconds.'.format(-1 * MySpace,
                                                                                                time.time(), MyTime))
        move_mouse(-1 * MySpace, -1 * MySpace)
        time.sleep(MyTime)  # Várakozás 3 másodpercig


# Start mouse movement function in a separate thread
threading.Thread(target=perform_mouse_movement).start()

# Run Tkinter event loop
window.mainloop()
