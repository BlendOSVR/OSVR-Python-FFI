from ctypes import cdll

mylib = cdll.LoadLibrary("osvrClientKit")

def osvrClientInit(applicationIdentifier, flags):
	rval = mylib.osvrClientInit()
	return rval

def osvrClientUpdate(ctx):
	rval = mylib.osvrClientUpdate(ctx)
	return rval

def osvrClientCheckStatus(ctx):
	rval = mylib.osvrClientCheckStatus(ctx)
	return rval

def osvrClientShutdown(ctx):
	rval = mylib.osvrClientShutdown(ctx)
	return rval

def osvrClientGetInterface(ctx, path, iface):
	return mylib.osvrClientGetInterface(ctx, path, iface)
	
def osvrClientFreeInterface(ctx, iface):
	return mylib.osvrClientFreeInterface(ctx, iface)

def osvrClientGetStringParameterLength(ctx, path, len):
	return mylib.osvrGetStringParameterLength(ctx, path, len)
	
def osvrClientGetStringParameter(ctx, path, buf, len):
	return mylib.osvrClientGetStringParameter(ctx, path, buf, len);
