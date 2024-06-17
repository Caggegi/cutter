import controller as C

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
