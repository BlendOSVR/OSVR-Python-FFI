from ctypes import *
from ffi import *

ctx = osvrClientInit("com.osvr.exampleclients.TrackerCallback")

lefthand = osvrClientGetInterface(ctx, "/me/hands/left")

osvrClientUpdate(ctx)

osvrClientShutdown(ctx)