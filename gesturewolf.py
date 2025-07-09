import subprocess


proc = subprocess.Popen(["sudo", "libinput", "debug-events"],
                        stdout=subprocess.PIPE, text=True)

active_fingers = 0

for line in proc.stdout:
    
    if "GESTURE_SWIPE_BEGIN" in line:
        parts = line.split()
        active_fingers = int(parts[3])
        if active_fingers==3:
            print("3 Finger swipe started\n")
        
        elif 4 == active_fingers:
            print("4 Finger swipe started\n")

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