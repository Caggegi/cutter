import controller as C
import platform

cutter = False
if "armv6l" in platform.platform():
    cutter = True

toggle = False

def trigger(button):
    if not cutter: return
    import RPi.GPIO as gpio
    gpio.setmode(gpio.BOARD)
    blade  = gpio.setup(16,gpio.OUT)
    _left_ahead  = gpio.setup(31,gpio.OUT)  #6
    _right_ahead = gpio.setup(35,gpio.OUT)  #19
    _left_back   = gpio.setup(32,gpio.OUT)  #12
    _right_back  = gpio.setup(36,gpio.OUT)  #16
    if button == 'A' or button == 'R2':
        gpio.output(blade,  gpio.HIGH)
    elif button == 'L3' or button == 'R3':
        gpio.output(_left_ahead, gpio.LOW)
        gpio.output(_right_ahead, gpio.LOW)
        gpio.output(_left_back, gpio.LOW)
        gpio.output(_right_back, gpio.LOW)
    else:
        gpio.output(blade,  gpio.LOW)

def trigger2(button):
    if cutter: return
    if button == 'A' or button == 'R2':
        print("cutting")
    else:
        print("stop")

def run(direction):
    if not cutter: return
    import RPi.GPIO as gpio
    gpio.setmode(gpio.BOARD)
    _left_ahead  = gpio.setup(31,gpio.OUT)  #6
    _right_ahead = gpio.setup(35,gpio.OUT)  #19
    _left_back   = gpio.setup(32,gpio.OUT)  #12
    _right_back  = gpio.setup(36,gpio.OUT)  #16
    if mv[0] < -0.5 and mv[1] < 0.1: #front
        gpio.output(_left_ahead,  gpio.HIGH)
        gpio.output(_right_ahead, gpio.HIGH)
        gpio.output(_left_back,    gpio.LOW)
        gpio.output(_right_back,   gpio.LOW)
    elif mv[0] > 0.5 and mv[1] < 0.1: #back
        gpio.output(_left_ahead,   gpio.LOW)
        gpio.output(_right_ahead,  gpio.LOW)
        gpio.output(_left_back,   gpio.HIGH)
        gpio.output(_right_back,  gpio.HIGH)
    elif mv[0] < 0.1 and mv[1] > 0.5: #right
        gpio.output(_left_ahead,   gpio.LOW)
        gpio.output(_right_ahead, gpio.HIGH)
        gpio.output(_left_back,   gpio.HIGH)
        gpio.output(_right_back,   gpio.LOW)
    elif mv[0] < 0.1 and mv[1] < -0.5: #left
        gpio.output(_left_ahead,  gpio.HIGH)
        gpio.output(_right_ahead,  gpio.LOW)
        gpio.output(_left_back,    gpio.LOW)
        gpio.output(_right_back,  gpio.HIGH)

def run2(direction):
    if cutter: return
    if mv[0] < -0.5 and mv[1] < 0.1: #front
        print("front")
    elif mv[0] > 0.5 and mv[1] < 0.1: #back
        print("back")
    elif mv[0] < 0.1 and mv[1] > 0.5: #right
        print("right")
    elif mv[0] < 0.1 and mv[1] < -0.5: #left
        print("left")


if __name__ == '__main__':
    import time
    print("starting....")
    joy = C.XboxController()
    while True:
        time.sleep(0.1)
        pushed = joy.read()
        for key in pushed:
            if type(pushed[key]) is not list and abs(pushed[key]) > 0.5:
                print(f"pushed {key}: {pushed[key]}")
                if cutter:
                    trigger(key)
                else:
                    trigger2(key)
            if type(pushed[key]) is list and (abs(pushed[key][0]) > 0.1 or abs(pushed[key][1]) > 0.1):
                mv = pushed[key]
                if abs(mv[0])<0.1: mv[0]=0
                if abs(mv[1])<0.1: mv[1]=0
                if cutter:
                    run(mv)
                else:
                    run2(mv)
