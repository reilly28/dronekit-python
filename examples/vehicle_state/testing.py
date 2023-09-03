import dronekit#from dronekit import connect, VehicleMode
import time

# Connect to the Vehicle.
connection_string = "com11"
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = dronekit.connect('com11', wait_ready=True, baud=57600, timeout=60, heartbeat_timeout=60)

# Get some vehicle attributes (state)
print ("Get some vehicle attribute values:")
print (" GPS: %s" % vehicle.gps_0)
print (" Battery: %s" % vehicle.battery)
print (" Last Heartbeat: %s" % vehicle.last_heartbeat)
print (" Is Armable?: %s" % vehicle.is_armable)
print (" System status: %s" % vehicle.system_status.state)
print (" Mode: %s" % vehicle.mode.name)    # settable
while True:
    time.sleep(1)
# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
sitl.stop()
print("Completed")