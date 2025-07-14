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
        if 3 == active_fingers:
            print("3 finger swiping\n"
                  f"{just_printing}")
            subparts = parts[4:6]
            cordinate_list = [cordinate for number in numbers  subpart.split("/") for subpart in subparts]
            # trying to make a running nested list comprehension !
            print(cordinate_list)
        elif 4 == active_fingers:
            print("4 figer swiping\n")
    
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

#  event5   GESTURE_SWIPE_UPDATE    +11.523s      3 -1.65/ 1.51 (-1.65/ 1.51 unaccelerated)

# we have a few cases in which the program have to work fine!
# '0.2''0.5' and '0.4/0.5' numbers here used are arbitrary!