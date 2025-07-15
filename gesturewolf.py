import subprocess


proc = subprocess.Popen(["sudo", "libinput", "debug-events"],
                        stdout=subprocess.PIPE, text=True)

active_fingers = 0

for line in proc.stdout:
    
    if "GESTURE_SWIPE_BEGIN" in line:
        delta_x =0
        delta_y =0
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
        delta_x += float(axis[0])
        delta_y += float(axis[1])
        
        if 3 == active_fingers:
            print("3 finger swiping\n"
                  f"{just_printing}")
            

        elif 4 == active_fingers:
            print("4 finger swiping\n")
    
    elif "GESTURE_SWIPE_END" in line:
        print(delta_x,delta_y)
        delta_x =0
        delta_y =0
        if  3 == active_fingers:
            print("3 finger swipe ended\n")
            active_fingers =None
        
        elif 4 == active_fingers:
            print("4 finger swipe ended\n")
            active_fingers =None
    
    else:
        print(line)

# # # when swiping up to down.
#  event5   GESTURE_SWIPE_UPDATE    +25.546s      3  4.18/146.08 ( 1.03/36.12 unaccelerated)
#  event5   GESTURE_SWIPE_UPDATE    +25.553s      3  4.68/172.62 ( 1.03/38.13 unaccelerated)
#  event5   GESTURE_SWIPE_UPDATE    +25.562s      3  3.44/154.38 ( 0.83/37.13 unaccelerated)

# implies that y>x (in term of value not sign)

# # when swiping down to up.
#  event5   GESTURE_SWIPE_UPDATE    +1026.959s    3 -0.41/-3.76 (-0.41/-3.76 unaccelerated)
#  event5   GESTURE_SWIPE_UPDATE    +1026.966s    3 -0.62/-4.01 (-0.62/-4.01 unaccelerated)
#  event5   GESTURE_SWIPE_UPDATE    +1026.975s    3 -0.41/-5.02 (-0.41/-5.02 unaccelerated)

# implies that y>x (in terms of value not sign)

# # # when swiping left to right.
#  event5   GESTURE_SWIPE_UPDATE    +26.547s      3  2.07/-0.25 ( 2.07/-0.25 unaccelerated)
#  event5   GESTURE_SWIPE_UPDATE    +26.555s      3  2.27/ 0.00 ( 2.27/ 0.00 unaccelerated)
#  event5   GESTURE_SWIPE_UPDATE    +26.562s      3  1.86/ 0.00 ( 1.86/ 0.00 unaccelerated)

# implies that x>y 

# # # when swiping right to left.
#  event5   GESTURE_SWIPE_UPDATE    +78.542s      3 10.54/-0.25 (10.54/-0.25 unaccelerated)
#  event5   GESTURE_SWIPE_UPDATE    +78.550s      3 11.21/ 0.50 (11.16/ 0.50 unaccelerated)
#  event5   GESTURE_SWIPE_UPDATE    +78.557s      3 13.88/ 0.00 (12.81/ 0.00 unaccelerated)

# implies that x>y