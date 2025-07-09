import subprocess


proc = subprocess.Popen(["sudo", "libinput", "debug-events"],
                        stdout=subprocess.PIPE, text=True)

for line in proc.stdout:
    if "GESTURE_SWIPE_BEGIN" in line  and "3" in line:
        print("3 Finger swipe started\n")
    elif "GESTURE_SWIPE_UPDATE" in line and "3" in line:
        print("3 finger swiping\n")
    elif "GESTURE_SWIPE_END" in line and "3" in line:
        print("3 finger swipe ended")
    else:
        print(line)