from osvrClientKit import *

ctx = osvrClientInit("com.osvr.example.ViewerEyeSurfaces")

while True:
    print("Trying to get the display config")
    osvrClientUpdate(ctx)
    display, code = osvrClientGetDisplay(ctx)
    if(code == 0):
        break

viewers = osvrClientGetNumViewers(display)

for viewer in range(0, viewers.value):
    print("Viewer %d" % (viewer))
    eyes = osvrClientGetNumEyesForViewer(display, viewer)

    for eye in range(0, eyes.value):
        print("\tEye %d" % (eye))
        surfaces = osvrClientGetNumSurfacesForViewerEye(display, viewer, eye)

        for surface in range(0, surfaces.value):
            print("\t\tSurface %d" %(surface))

osvrClientFreeDisplay(display)

osvrClientShutdown(ctx)
print("Library shut down, exiting")