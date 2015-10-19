from ctypes import *
import test

ctx = test.osvrClientInit("com.osvr.exampleclients.MinimalInit", 0)

test.osvrClientUpdate(ctx)

test.osvrClientShutdown(ctx)