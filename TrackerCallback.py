from ctypes import *
import ffi

ctx = ffi.osvrClientInit(c_char_p("com.osvr.exampleclients.TrackerCallback".encode("utf8")), c_uint32(0))

lefthand = ffi.OSVR_ClientInterface()

ffi.osvrClientGetInterface(ctx, c_char_p("/me/hands/left".encode("utf8")), lefthand)

ffi.osvrClientUpdate(ctx)

ffi.osvrClientShutdown(ctx)