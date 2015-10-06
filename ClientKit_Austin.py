#Author: Austin Needham
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