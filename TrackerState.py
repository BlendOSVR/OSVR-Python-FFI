from osvrClientKit import *

ctx = osvrClientInit("com.osvr.exampleclients.TrackerState")

lefthand = osvrClientGetInterface(ctx, "/me/head")

for i in range (0, 1000000):
    osvrClientUpdate(ctx)
    if(i%100 == 0):
        try:
            state, timestamp = osvrGetPoseState(lefthand)
        except ReturnError:
            pass
        else:
            print("Got pose state: Position = (%f, %f, %f), orientation = (%f, %f, %f, %f)" % (state.translation.data[0], state.translation.data[1], state.translation.data[2], state.rotation.data[0], state.rotation.data[1], state.rotation.data[2], state.rotation.data[3]))
osvrClientShutdown(ctx)
print("Library shut down, exiting.")