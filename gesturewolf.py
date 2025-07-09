import subprocess


proc = subprocess.Popen(["sudo", "libinput", "debug-events"],
                        stdout=subprocess.PIPE, text=True)

active_fingers = None
for line in proc.stdout:
    if "GESTURE_SWIPE_BEGIN" in line:
        if "3" in line:
            print("3 Finger swipe started\n")
            active_fingers = 3
        elif "4" in line:
            print("4 Finger swipe started\n")
            active_fingers = 4
    elif "GESTURE_SWIPE_UPDATE" in line:
        if 3 == active_fingers:
            print("3 finger swiping\n")
        elif 4 == active_fingers:
            print("4 figer swiping\n")
    elif "GESTURE_SWIPE_END" in line:
        if  3 == active_fingers:
            print("3 finger swipe ended\n")
            active_fingers =None
        elif 4 == active_fingers:
            print("4 finger swipe ended\n")
            active_fingers =None
    else:
        print(line)