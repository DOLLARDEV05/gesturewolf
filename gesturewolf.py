import subprocess


proc = subprocess.Popen(["sudo", "libinput", "debug-events"],
                        stdout=subprocess.PIPE, text=True)

active_fingers = 0

for line in proc.stdout:
    
    if "GESTURE_SWIPE_BEGIN" in line:
        parts = line.split()
        active_fingers = int(parts[3])
        just_printing = int(parts[3])
        if active_fingers==3:
            print("3 Finger swipe started\n"
                  f"{just_printing}")
        
        elif 4 == active_fingers:
            print("4 Finger swipe started\n")

    elif "GESTURE_SWIPE_UPDATE" in line:
        
        parts = line.split()
        subparts = parts[4:6]
        axis = []
        for item in subparts:
            temp_var=item.split("/")
            for thing in temp_var:
                if thing != '':
                    axis.append(thing)
        if 3 == active_fingers:
            print("3 finger swiping\n"
                  f"{just_printing}")
            

        elif 4 == active_fingers:
            print("4 finger swiping\n")
    
    elif "GESTURE_SWIPE_END" in line:
        
        if  3 == active_fingers:
            print("3 finger swipe ended\n"
                  f"{just_printing}")
            active_fingers =None
        
        elif 4 == active_fingers:
            print("4 finger swipe ended\n")
            active_fingers =None
    
    else:
        print(line)