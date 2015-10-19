from ctypes import * 
from ffi import *

osvrClientInit("com.osvr.exampleclients.MinimalInit", 0)

for i in range(0, 1000000):
    osvrClientUpdate(ctx)
osvrClientShutdown(ctx)