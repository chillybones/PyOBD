from obd import OBD

# Create the OBD object - we will leave the port blank so the app will run a port scan and let us know which port
# the OBD connector will be plugged into.  This will be different on each device so this may help debug some initial
# issues when running on the pi for the first time

conn = OBD(portstr=None, baudrate=None, protocol=None, fast=True)

