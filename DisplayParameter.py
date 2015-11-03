from osvrClientKit import *

ctx = osvrClientInit("com.osvr.exampleclients.DisplayParameter")

path = "/display"

length = osvrClientGetStringParameterLength(ctx, path)

displayDescription = osvrClientGetStringParameter(ctx, path, length)

print("Got value of %s: \n%s" % (path, displayDescription))

osvrClientShutdown(ctx)
print("Library shut down, exiting.")