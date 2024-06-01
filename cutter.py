import platform
import pygame
import time
import subprocess
import importlib

rp = platform.system() == "Linux" and platform.machine == "armv6l"

def gpioCommand(controller_event):
    try:
        importlib.import_module('RPi.GPIO')
    except ImportError:
        if not rp:
            print(f"Il pacchetto RPi.GPIO non è installato e non siamo su Raspberry.")
        else:
            subprocess.check_call(['pip', 'install', 'RPi.GPIO'])
            globals()['gpio'] = importlib.import_module('RPi.GPIO')
            gpio.setMode(gpio.BCM)
            _sx = 22 #15
            _dx = 23 #16
            gpio.setup(_sx, gpio.OUT)
            gpio.setup(_dx, gpio.OUT)
            try:
                print(gpio)
            finally:
                gpio.cleanup()


pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("Nessun joystick trovato.")
    pygame.quit()
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Joystick collegato: {joystick.get_name()}")

try:
    while True:
        # Gestisci gli eventi di pygame
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Tasto premuto: {event.button}")
            elif event.type == pygame.JOYBUTTONUP:
                print(f"Tasto rilasciato: {event.button}")
        
        # Dormi per un breve periodo per evitare di usare troppo CPU
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Programma terminato dall'utente.")

finally:
    # Chiudi pygame
    pygame.quit()