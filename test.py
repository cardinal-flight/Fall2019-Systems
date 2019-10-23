import time
# Import mavutil
from pymavlink import mavutil

master = mavutil.mavlink_connection('/dev/ttyACM0', baud=192600)

# Get some information !
while True:
            try:
                        print(master.recv_match().to_dict())
            except:
                        pass
            time.sleep(0.1)
