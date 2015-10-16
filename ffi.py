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

def osvrClientGetDisplay(ctx, disp)
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