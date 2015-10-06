#Author: Adam Wang
from ctypes import cdll

mylib = cdll.LoadLibrary("osvrClientKit")

def osvrClientGetInterface(ctx, path, iface):
	return mylib.osvrClientGetInterface(ctx, path, iface)
	
def osvrClientFreeInterface(ctx, iface):
	return mylib.osvrClientFreeInterface(ctx, iface)

def osvrClientGetStringParameterLength(ctx, path, len):
	return mylib.osvrGetStringParameterLength(ctx, path, len)
	
def osvrClientGetStringParameter(ctx, path, buf, len):
	return mylib.osvrClientGetStringParameter(ctx, path, buf, len);
