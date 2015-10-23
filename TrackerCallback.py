from ctypes import *
from ffi import *

ctx = osvrClientInit(c_char_p("com.osvr.exampleclients.TrackerCallback".encode("utf8")), c_uint32(0))

lefthand = pointer(OSVR_ClientInterfaceObject())

osvrClientGetInterface(ctx, c_char_p("/me/hands/left".encode("utf8")), pointer(lefthand))

osvrClientUpdate(ctx)

osvrClientShutdown(ctx)