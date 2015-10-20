from ctypes import * 
from ffi import *

ctx = osvrClientInit(c_char_p("com.osvr.exampleclients.MinimalInit".encode("utf8")), c_uint32(0))

for i in range(0, 1000000):
    osvrClientUpdate(ctx)

osvrClientShutdown(ctx)