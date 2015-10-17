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
def OSVR_DisplayDimension(Structure):
    pass
def OSVR_ViewerCount(Structure):
    pass
def OSVR_Pose3(Structure):
    pass
def OSVR_EyeCount(Structure):
    pass
def OSVR_SurfaceCount(Structure):
    pass

def osvrClientInit(applicationIdentifier, flags):
	mylib.osvrClientInit.argtypes = [c_char_p, c_uint32]
    mylib.osvrClientInit.restype = OSVR_ClientContext
    return mylib.osvrClientInit(c_char_p(applicationIdentifier), c_uint32(flags))

def osvrClientUpdate(ctx):
    mylib.osvrClientUpdate.argtypes = [OSVR_ClientContext]
	mylib.osvrClientUpdate.restype = OSVR_ReturnCode
    return mylib.osvrClientUpdate(ctx)

def osvrClientCheckStatus(ctx):
    mylib.osvrClientCheckStatus.argtypes = [OSVR_ClientContext]
    mylib.osvrClientCheckStatus.restype = OSVR_ReturnCode
	return mylib.osvrClientCheckStatus(ctx)

def osvrClientShutdown(ctx):
    mylib.osvrClientShutdown.argtypes = [OSVR_ClientContext]
    mylib.osvrClientShutdown.restype = OSVR_ReturnCode
	return mylib.osvrClientShutdown(ctx)

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

def osvrClientGetDisplay(ctx, disp):
    mylib.osvrClientGetDisplay.argtypes = [OSVR_ClientContext, pointer(OSVR_DisplayConfig)]
    mylib.osvrClientGetDisplay.restype = OSVR_ReturnCode
    return mylib.osvrClientGetDisplay(ctx, disp)

def osvrClientFreeDisplay(disp):
    mylib.osvrClientFreeDisplay.argtypes = [OSVR_DisplayConfig]
    mylib.osvrClientFreeDisplay.restype = OSVR_ReturnCode
    return mylib.osvrClientFreeDisplay(disp)

def osvrClientCheckDisplayStartup(disp):
    mylib.osvrClientCheckDisplayStartup.argtypes = [OSVR_DisplayConfig]
    mylib.osvrClientCheckDisplayStartup.restype = OSVR_ReturnCode
    return mylib.osvrClientCheckDisplayStartup(disp)

def osvrClientGetNumDisplayInputs(disp, numDisplayInputs):
    mylib.osvrClientGetNumDisplayInputs.argtypes = [OSVR_DisplayConfig, pointer(OSVR_DisplayInputCount)]
    mylib.osvrClientGetNumDisplayInputs.restype = OSVR_ReturnCode
    return mylib.osvrClientGetNumDisplayInputs(disp, numDisplayInputs)

def osvrClientGetDisplayDimensions(disp, displayInputIndex, width, height):
    mylib.osvrClientGetDisplayDimensions.argtypes = [OSVR_DisplayConfig, OSVR_DisplayInputCount, pointer(OSVR_DisplayDimension), pointer(OSVR_DisplayDimension)]
    mylib.osvrClientGetDisplayDimensions.restype = OSVR_ReturnCode
    return mylib.osvrClientGetDisplayDimensions(disp, displayInputIndex, width, height)

def osvrClientGetNumViewers(disp, viewers):
    mylib.osvrClientGetNumViewers.argtypes = [OSVR_DisplayConfig, pointer(OSVR_ViewerCount)]
    mylib.osvrClientGetNumViewers.restype = OSVR_ReturnCode
    return mylib.osvrClientGetNumViewers(disp, viewers)

def osvrClientGetViewerPose(disp, viewer, pose):
    mylib.osvrClientGetViewerPose.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, pointer(OSVR_Pose3)]
    mylib.osvrClientGetViewerPose.restype = OSVR_ReturnCode
    return mylib.osvrClientGetViewerPose(disp, viewer, pose)

def osvrClientGetNumEyesForViewer(disp, viewer, eyes):
    mylib.osvrClientGetNumEyesForViewer.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, pointer(OSVR_EyeCount)]
    mylib.osvrClientGetNumEyesForViewer.restype = OSVR_ReturnCode
    return mylib.osvrClientGetNumEyesForViewer(disp, viewer, eyes)

def osvrClientGetViewerEyePose(disp, viewer, eye, pose):
    mylib.osvrClientGetViewerEyePose.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_EyeCount, pointer(OSVR_Pose3)]
    mylib.osvrClientGetViewerEyePose.restype = OSVR_ReturnCode
    return mylib.osvrClientGetViewerPose(disp, viewer, eye, pose)

def osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, mat):
    mylib.osvrClientGetViewerEyeViewMatrixd.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_EyeCount, OSVR_MatrixConventions, pointer(c_double)]
    mylib.osvrClientGetViewerEyeViewMatrixd.restype = OSVR_ReturnCode
    return mylib.osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, pointer(c_double(mat)))

def osvrClientGetViewerEyeViewMatrixf(disp, viewer, eye, flags, mat):
    mylib.osvrClientGetViewerEyeViewMatrixf.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_EyeCount, OSVR_MatrixConventions, pointer(c_float)]
    mylib.osvrClientGetViewerEyeViewMatrixf.restype = OSVR_ReturnCode
    return mylib.osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, pointer(c_float(mat)))

def osvrClientGetNumSurfacesForViewerEye(disp, viewer, eye, surfaces):
    mylib.osvrClientGetNumSurfacesForViewerEye.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_EyeCount, pointer(OSVR_SurfaceCount)]
    mylib.osvrClientGetNumSurfacesForViewerEye.restype = OSVR_ReturnCode
    return mylib.osvrClientGetNumSurfacesForViewerEye(disp, viewer, eye, surfaces)

def osvrClientGetRelativeViewportForViewerEyeSurface(disp, viewer, eye, surface, left, bottom, width, height):
    mylib.osvrClientGetRelativeViewportForViewerEyeSurface.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_EyeCount, OSVR_SurfaceCount, pointer(OSVR_ViewportDimension), pointer(OSVR_ViewportDimension), pointer(OSVR_ViewportDimension), pointer(OSVR_ViewportDimension)]
    mylib.osvrClientGetRelativeViewportForViewerEyeSurface.restype = OSVR_ReturnCode
    return mylib.osvrClientGetRelativeViewportForViewerEyeSurface(disp, viewer, eye, surface, left, bottom, width, height)

def osvrClientGetViewerEyeSurfaceDisplayInputIndex(disp, viewer, eye, surface, displayInput):
    return osvrClientGetViewerEyeSurfaceDisplayInputIndex(disp, viewer, eye, surface, displayInput)

def osvrClientGetViewerEyeSurfaceProjectionMatrixd(disp, viewer, eye, surface, near, far, flags, matrix):
    return mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixd(disp, viewer, eye, surface, near, far, flags, matrix)

def osvrClientGetViewerEyeSurfaceProjectionMatrixf(disp, viewer, eye, surface, near, far, flags, matrix):
    return mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixf(disp, viewer, eye, surface, near, far, flags, matrix)

def osvrClientGetViewerEyeSurfaceProjectionClippingPlanes(disp, viewer, eye, surface, left, right, bottom, top):
    return mylib.osvrClientGetViewerEyeSurfaceProjectionClippingPlanes(disp, viewer, eye, surface, left, right, bottom, top)

def osvrClientDoesViewerEyeSurfaceWantDistortion(disp, viewer, eye, surface, distortionRequested):
    return mylib.osvrClientDoesViewerEyeSurfaceWantDistortion(disp, viewer, eye, surface, distortionRequested)

def osvrClientGetViewerEyeSurfaceRadialDistortionPriority(disp, viewer, eye, surface, priority):
    return mylib.osvrClientGetViewerEyeSurfaceRadialDistortionPriority(disp, viewer, eye, surface, priority)

def osvrClientGetViewerEyeSurfaceRadialDistortion(disp, viewer, eye, surface, params):
    return mylib.osvrClientGetViewerEyeSurfaceRadialDistortion(disp, viewer, eye, surface, params)