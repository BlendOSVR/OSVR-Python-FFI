from osvrClientKit import *

def myAnalogCallback(userdata, timestamp, report):
	print("Got report: channel is %f" % (report.contents.state))

ctx = osvrClientInit("com.osvr.exampleclients.AnalogCallback")

iface = osvrClientGetInterface(ctx, "/controller/left/trigger")

C_AnalogCallback = OSVR_AnalogCallback(myAnalogCallback)

osvrRegisterAnalogCallback(iface, C_AnalogCallback, None)

for i in range (0, 1000000):
	osvrClientUpdate(ctx)

osvrClientShutdown(ctx)
print("Library shut down, exiting.")