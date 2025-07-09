import subprocess

proc = subprocess.run(["sudo", "libinput" ,"debug-events"])
# proc = subprocess.Popen(["sudo", "libinput", "debug-events"],stdout=subprocess.PIPE, text=True)

for line in proc.stdout:
    print(line)
