from ctypes import *

mylib = cdll.LoadLibrary("osvrClientKit")

ctx = mylib.osvrClientInit("com.osvr.exampleclients.MinimalInit", 0)

for i in range(0, 1000000):
	mylib.osvrClientUpdate(ctx)

mylib.osvrClientShutdown(ctx)