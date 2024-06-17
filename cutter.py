import controller as C
import platform

cutter = False
if "raspbian" in platform.platform():
    cutter = True

if __name__ == '__main__':
    import time
    joy = C.XboxController()
    while True:
        time.sleep(0.1)
        pushed = joy.read()
        for key in pushed:
            if type(pushed[key]) is not list and abs(pushed[key]) > 0.5:
                print(f"pushed {key}: {pushed[key]}")
            if type(pushed[key]) is list and (abs(pushed[key][0]) > 0.1 or abs(pushed[key][1]) > 0.1):
                mv = pushed[key]
                if abs(mv[0])<0.1: mv[0]=0
                if abs(mv[1])<0.1: mv[1]=0
                print(f"moving {key}: {mv}")


def run(direction):
    if not cutter: return
    import RPi.GPIO as gpio
    gpio.setmode(gpio.BOARD)
    _left_ahead = gpio.setup(0,gpio.OUT)
    _right_ahead = gpio.setup(0,gpio.OUT)
    _left_back = gpio.setup(0,gpio.OUT)
    _right_back = gpio.setup(0,gpio.OUT)
    '''
        mv(x,y)
        y>0.5 r
        y<-0.5 l
        x>0.5 b
        x<-0.5 u
    '''
    if mv[0] < -0.5 and mv[1] < 0.1: #fron
        gpio.output(_left_ahead, gpio.HIGH)
        gpio.output(_right_ahead, gpio.HIGH)
        gpio.output(_left_back, gpio.LOW)
        gpio.output(_right_back, gpio.LOW)
    elif mv[0] > 0.5 and mv[1] < 0.1: #back
        gpio.output(_left_ahead, gpio.LOW)
        gpio.output(_right_ahead, gpio.LOW)
        gpio.output(_left_back, gpio.HIGH)
        gpio.output(_right_back, gpio.HIGH)
    elif mv[0] < 0.1 and mv[1] > 0.5: #right
        gpio.output(_left_ahead, gpio.LOW)
        gpio.output(_right_ahead, gpio.HIGH)
        gpio.output(_left_back, gpio.HIGH)
        gpio.output(_right_back, gpio.LOW)
    elif mv[0] < 0.1 and mv[1] < -0.5: #left
        gpio.output(_left_ahead, gpio.HIGH)
        gpio.output(_right_ahead, gpio.LOW)
        gpio.output(_left_back, gpio.LOW)
        gpio.output(_right_back, gpio.HIGH)
    elif mv[0] < -0.5 and mv[1] > 0.5: #front-right
        gpio.output(_left_ahead, gpio.LOW)
        gpio.output(_right_ahead, gpio.HIGH)
        gpio.output(_left_back, gpio.HIGH)
        gpio.output(_right_back, gpio.LOW)
        time.sleep(0.5)
        gpio.output(_left_ahead, gpio.HIGH)
        gpio.output(_right_ahead, gpio.HIGH)
        gpio.output(_left_back, gpio.LOW)
        gpio.output(_right_back, gpio.LOW)
    elif mv[0] > 0.5 and mv[1] > 0.5: #back-right
        gpio.output(_left_ahead, gpio.LOW)
        gpio.output(_right_ahead, gpio.HIGH)
        gpio.output(_left_back, gpio.HIGH)
        gpio.output(_right_back, gpio.LOW)
        time.sleep(0.5)
        gpio.output(_left_ahead, gpio.LOW)
        gpio.output(_right_ahead, gpio.LOW)
        gpio.output(_left_back, gpio.HIGH)
        gpio.output(_right_back, gpio.HIGH)
    elif mv[0] < -0.5 and mv[1] < -0.5: #front-left
        gpio.output(_left_ahead, gpio.HIGH)
        gpio.output(_right_ahead, gpio.LOW)
        gpio.output(_left_back, gpio.LOW)
        gpio.output(_right_back, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(_left_ahead, gpio.HIGH)
        gpio.output(_right_ahead, gpio.HIGH)
        gpio.output(_left_back, gpio.LOW)
        gpio.output(_right_back, gpio.LOW)
    elif mv[0] > 0.5 and mv[1] < -0.5: #back-left
        gpio.output(_left_ahead, gpio.HIGH)
        gpio.output(_right_ahead, gpio.LOW)
        gpio.output(_left_back, gpio.LOW)
        gpio.output(_right_back, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(_left_ahead, gpio.LOW)
        gpio.output(_right_ahead, gpio.LOW)
        gpio.output(_left_back, gpio.HIGH)
        gpio.output(_right_back, gpio.HIGH)

    
