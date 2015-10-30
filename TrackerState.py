from osvrClientKit import *

ctx = osvrClientInit("com.osvr.exampleclients.TrackerState")

lefthand = osvrClientGetInterface(ctx, "/me/head")

for i in range (0, 1000000):
    osvrClientUpdate(ctx)
    if(i%100 == 0):
        rval, t_state = osvrGetPoseState(lefthand)
        print("Got pose state: Position = (%f, %f, %f), orientation = (%f, %f, %f, %f)\n" % (t_state.state.translation.data[0], t_state.state.translation.data[1], t_state.state.translation.data[2], t_state.state.rotation.data[0], t_state.state.rotation.data[1], t_state.state.rotation.data[2], t_state.state.rotation.data[3]))
osvrClientShutdown(ctx)
print("Library shut down, exiting.\n")