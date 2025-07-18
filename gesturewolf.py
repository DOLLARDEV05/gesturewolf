import subprocess
from configparser import ConfigParser 

config  = ConfigParser()
config.read('config.ini')

proc = subprocess.Popen(["sudo", "libinput", "debug-events"],
                        stdout=subprocess.PIPE, text=True)

active_fingers = 0
delta_y =0
delta_x =0

for line in proc.stdout:
    
    if "GESTURE_SWIPE_BEGIN" in line:
        parts = line.split()
        active_fingers = int(parts[3])
        if active_fingers==3:
            print("3 Finger swipe started\n")
        
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
        delta_x += float(axis[0]) #might want to look into this.
        delta_y += float(axis[1]) #might want to look into this.
        
        if 3 == active_fingers:
            print("3 finger swiping\n")

        elif 4 == active_fingers:
            print("4 finger swiping\n")
    
    elif "GESTURE_SWIPE_END" in line:
        if  3 == active_fingers:
            if abs(delta_x) < abs(delta_y) and delta_y>0.00:
                print("3 finger swipe swiping up to down\n")
                DownSwipe = config.get('3FingerSwipe','Down')
                DownSwipe = DownSwipe.split()
                subprocess.run(DownSwipe)
            elif abs(delta_x) < abs(delta_y) and delta_y<0.00:
                print("3 finger swipe swiping down to up\n")
                UpSwipe = config.get('3FingerSwipe','Up')
                UpSwipe = UpSwipe.split()
                subprocess.run(UpSwipe)
            elif abs(delta_x) > abs(delta_y) and delta_x>0.00:
                print("3 finger swipe left to right\n")
                RightSwipe = config.get('3FingerSwipe','Right')
                RightSwipe = RightSwipe.split()
                subprocess.run(RightSwipe)
            elif abs(delta_x) > abs(delta_y) and delta_x<0.00:
                print("3 finger swipe right to left") 
                LeftSwipe = config.get('3FingerSwipe','Left')
                LeftSwipe = LeftSwipe.split()
                subprocess.run(LeftSwipe)
            active_fingers =None
        
        elif 4 == active_fingers:
            if abs(delta_x) < abs(delta_y) and delta_y>0.00:
                print("4 finger swipe swiping up to down\n")
            elif abs(delta_x) < abs(delta_y) and delta_y<0.00:
                print("4 finger swipe swiping down to up\n")
            elif abs(delta_x) > abs(delta_y) and delta_x>0.00:
                print("4 finger swipe left to right\n")
                subprocess.run(["xdotool","key","alt+Tab+Right"])
            elif abs(delta_x) > abs(delta_y) and delta_x<0.00:
                print("4 finger swipe right to left")
                subprocess.run(["xdotool","key","alt+Tab+Left"])
            active_fingers =None
        delta_x =0
        delta_y =0
    
    else:
        print(line)

#1️⃣ make the volume bar logic (if possible make this dynamic)

#2️⃣ make this autorun at runtime.

#3️⃣ complete the config file and autoload defaults when no config is 
# found

#4️⃣ make pinching gestures 

#5️⃣ clean up the code and reorganise