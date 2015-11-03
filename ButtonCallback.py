from osvrClientKit import *

def myButtonCallback(userdata, timestamp, report):
    print("Got Report: button is %s" % (report.contents.state))

ctx = osvrClientInit("com.osvr.exampleclients.ButtonCallback")

button1 = osvrClientGetInterface(ctx, "/controller/left/1")

C_ButtonCallback = OSVR_ButtonCallback(myButtonCallback)

osvrRegisterButtonCallback(button1, C_ButtonCallback, None)

for i in range (0, 1000000):
    osvrClientUpdate(ctx)

osvrClientShutdown(ctx)
print("Library shut down, exiting.")