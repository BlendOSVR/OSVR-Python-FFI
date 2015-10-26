from ctypes import * 
from ffi import *

ctx = osvrClientInit("com.osvr.exampleclients.MinimalInit")

for i in range(0, 1000000):
    osvrClientUpdate(ctx)

osvrClientShutdown(ctx)