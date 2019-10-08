# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udpin:127.0.0.1:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# http://mavlink.org/messages/common#MAV_CMD_COMPONENT_ARM_DISARM

# Disarm
# master.arducopter_disarm() or:
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    0, 0, 0, 0, 0, 0, 0)
