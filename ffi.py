from ctypes import cdll

mylib = cdll.LoadLibrary("osvrClientKit")

def OSVR_ClientContext(Structure):
    pass
def OSVR_ReturnCode(Structure):
    pass
def OSVR_ClientInterface(Structure):
    pass
def OSVR_DisplayConfigObject(Structure):
    pass

def osvrClientInit(applicationIdentifier, flags):
	mylib.osvrClientInit.argtypes = [c_char_p, c_uint32]
    mylib.osvrClientInit.restype = OSVR_ClientContext
    rval = mylib.osvrClientInit(c_char_p(applicationIdentifier), c_uint32(flags))
	return rval

def osvrClientUpdate(ctx):
    mylib.osvrClientUpdate.argtypes = [OSVR_ClientContext]
	mylib.osvrClientUpdate.restype = OSVR_ReturnCode
    rval = mylib.osvrClientUpdate(ctx)
	return rval

def osvrClientCheckStatus(ctx):
    mylib.osvrClientCheckStatus.argtypes = [OSVR_ClientContext]
    mylib.osvrClientCheckStatus.restype = OSVR_ReturnCode
	rval = mylib.osvrClientCheckStatus(ctx)
	return rval

def osvrClientShutdown(ctx):
    mylib.osvrClientShutdown.argtypes = [OSVR_ClientContext]
    mylib.osvrClientShutdown.restype = OSVR_ReturnCode
	rval = mylib.osvrClientShutdown(ctx)
	return rval

def osvrClientGetInterface(ctx, path, iface):
    mylib.osvrClientGetInterface.argtypes = [OSVR_ClientContext, c_char_p, pointer(OSVR_ClientInterface)]
    mylib.osvrClientGetInterace.restype = OSVR_ReturnCode
	return mylib.osvrClientGetInterface(ctx, c_char_p(path), iface)
	
def osvrClientFreeInterface(ctx, iface):
    mylib.osvrClientFreeInterface.argtypes = [OSVR_ClientContext, OSVR_ClientInterface]
    mylib.osvrClientFreeInterface.restype = OSVR_ReturnCode
	return mylib.osvrClientFreeInterface(ctx, iface)

def osvrClientGetStringParameterLength(ctx, path, len):
    mylib.osvrClientGetStringParameterLength.argtypes = [OSVR_ClientContext, c_char_p, c_size_t]
    mylib.osvrClientGetStringParameterLength.restype = OSVR_ReturnCode
	return mylib.osvrGetStringParameterLength(ctx, c_char_p(path), c_size_t(len)
	
def osvrClientGetStringParameter(ctx, path, buf, len):
    mylib.osvrClientGetStringParameterLength.argtypes = [OSVR_ClientContext, c_char_p, c_char_p c_size_t]
    mylib.osvrClientGetStringParameterLength.restype = OSVR_ReturnCode
	return mylib.osvrClientGetStringParameter(ctx, c_char_p(path), c_char_p(buf), c_size_t(len);

def osvrClientGetDisplay(ctx, disp)
    mylib.osvrClientGetDisplay.argtypes = [OSVR_ClientContext, pointer(OSVR_DisplayConfig)]
    mylib.osvrClientGetDisplay.restype = OSVR_ReturnCode
    return mylib.osvrClientGetDisplay(ctx, disp)

def osvrClientFreeDisplay(disp)
    return mylib.osvrClientFreeDisplay(disp)

def osvrClientCheckDisplayStartup(disp)
    return mylib.osvrClientCheckDisplayStartup(disp)

def osvrClientGetNumDisplayInputs(disp, numDisplayInputs)
    return mylib.osvrClientGetNumDisplayInputs(disp, numDisplayInputs)

def osvrClientGetDisplayDimensions(disp, displayInputIndex, width, height)
    return mylib.osvrClientGetDisplayDimensions(disp, displayInputIndex, width, height)

def osvrClientGetNumViewers(disp, viewers)
    return mylib.osvrClientGetNumViewers(disp, viewers)

def osvrClientGetViewerPose(disp, viewer, pose)
    return mylib.osvrClientGetViewerPose(disp, viewer, pose)

def osvrClientGetNumEyesForViewer(disp, viewer, eyes)
    return mylib.osvrClientGetNumEyesForViewer(disp, viewer, eyes)

def osvrClientGetViewerEyePose(disp, viewer, eye, pose)
    return mylib.osvrClientGetViewerPose(disp, viewer, eye, pose)

def osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, mat)
    return mylib.osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, mat)

def osvrClientGetViewerEyeViewMatrixf(disp, viewer, eye, flags, mat)
    return mylib.osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, mat)

def osvrClientGetNumSurfacesForViewerEye(disp, viewer, eye, surfaces)
    return mylib.osvrClientGetNumSurfacesForViewerEye(disp, viewer, eye, surfaces)

def osvrClientGetRelativeViewportForViewerEyeSurface(disp, viewer, eye, surface, left, bottom, width, height)
    return mylib.osvrClientGetRelativeViewportForViewerEyeSurface(disp, viewer, eye, surface, left, bottom, width, height)

def osvrClientGetViewerEyeSurfaceDisplayInputIndex(disp, viewer, eye, surface, displayInput)
    return osvrClientGetViewerEyeSurfaceDisplayInputIndex(disp, viewer, eye, surface, displayInput)

def osvrClientGetViewerEyeSurfaceProjectionMatrixd(disp, viewer, eye, surface, near, far, flags, matrix)
    return mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixd(disp, viewer, eye, surface, near, far, flags, matrix)

def osvrClientGetViewerEyeSurfaceProjectionMatrixf(disp, viewer, eye, surface, near, far, flags, matrix)
    return mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixf(disp, viewer, eye, surface, near, far, flags, matrix)

def osvrClientGetViewerEyeSurfaceProjectionClippingPlanes(disp, viewer, eye, surface, left, right, bottom, top)
    return mylib.osvrClientGetViewerEyeSurfaceProjectionClippingPlanes(disp, viewer, eye, surface, left, right, bottom, top)

def osvrClientDoesViewerEyeSurfaceWantDistortion(disp, viewer, eye, surface, distortionRequested)
    return mylib.osvrClientDoesViewerEyeSurfaceWantDistortion(disp, viewer, eye, surface, distortionRequested)

def osvrClientGetViewerEyeSurfaceRadialDistortionPriority(disp, viewer, eye, surface, priority)
    return mylib.osvrClientGetViewerEyeSurfaceRadialDistortionPriority(disp, viewer, eye, surface, priority)

def osvrClientGetViewerEyeSurfaceRadialDistortion(disp, viewer, eye, surface, params)
    return mylib.osvrClientGetViewerEyeSurfaceRadialDistortion(disp, viewer, eye, surface, params)