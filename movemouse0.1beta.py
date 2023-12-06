import ctypes
import time

# Definiáljuk a mouse_event függvény paramétereit
MOUSEEVENTF_MOVE = 0x0001

# Elkészítjük az INPUT struktúrát
class INPUT(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]

# Az egér mozgatása (1 pixel jobbra, 1 pixel lefelé)
def move_mouse(dx, dy):
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, dx, dy, 0, 0)


while True:

	# Szimulált egérmozgás
	print('Az eger  megmozditva (1 pixel). Kilepeshez: ctrl+c ' + str(time.time()) + ' 30 másodperc várakozás')
	move_mouse(1, 1)

	# Várakozás 3 másodpercig
	time.sleep(30)

	# Újabb szimulált egérmozgás (50 pixel balra, 50 pixel felfelé)
	print('Az eger  megmozditva (1 pixel). Kilepeshez: ctrl+c ' + str(time.time()) + ' 30 másodperc várakozás')
	move_mouse(-1, -1)
	time.sleep(30)