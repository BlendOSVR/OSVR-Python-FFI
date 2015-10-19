from ctypes import *

mylib = cdll.LoadLibrary("osvrClientKit")

class OSVR_ClientContextObject(Structure):
    pass

class OSVR_ReturnCode(Structure):
    pass

OSVR_ClientContext = POINTER(OSVR_ClientContextObject)

def osvrClientInit(applicationIdentifier, flags):
    mylib.osvrClientInit.argtypes = [c_char_p, c_uint32]
    mylib.osvrClientInit.restype = OSVR_ClientContext
    return mylib.osvrClientInit(c_char_p(applicationIdentifier.encode("utf8")), c_uint32(flags))

def osvrClientUpdate(ctx):
    mylib.osvrClientUpdate.argtypes = [OSVR_ClientContext]
    return mylib.osvrClientUpdate(ctx)

def osvrClientShutdown(ctx):
    mylib.osvrClientShutdown.argtypes = [OSVR_ClientContext]
    return mylib.osvrClientShutdown(ctx)