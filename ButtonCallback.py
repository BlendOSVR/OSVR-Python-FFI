from osvrClientKit import *

def myButtonCallback(userdata, timestamp, report):
    print("Got Report: button is %s\n" % (report.contents.state))

ctx = osvrClientInit("com.osvr.exampleclients.ButtonCallback")

button1 = osvrClientGetInterface(ctx, "/controller/left/1")

osvrRegisterButtonCallback(button1, OSVR_ButtonCallback(myButtonCallback), None)

osvrClientUpdate(ctx)

osvrClientShutdown(ctx)
print("Library shut down, exiting.\n")