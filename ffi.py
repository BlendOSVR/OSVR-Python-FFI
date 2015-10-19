from ctypes import *

mylib = cdll.LoadLibrary("osvrClientKit")

class OSVR_ClientContext(Structure):
    pass
class OSVR_ReturnCode(Structure):
    pass
class OSVR_Return_Failure(Structure):
    pass
class OSVR_ClientInterface(Structure):
    pass
class OSVR_DisplayConfigObject(Structure):
    pass
class OSVR_DisplayDimension(Structure):
    pass
class OSVR_ViewerCount(Structure):
    pass
class OSVR_Pose3(Structure):
    pass
class OSVR_EyeCount(Structure):
    pass
class OSVR_SurfaceCount(Structure):
    pass
class OSVR_RadialDistortionParameters(Structure):
    pass
#does CBool need to be redefined?

# Error checking

class ReturnError(Exception):
    def __init__(self, value, function):
        self.value = value
        self.function = function
    def __str__(self):
        return repr(self.function)

def checkReturn(returnValue, function):
    if returnValue == OSVR_Return_Failure:
        raise ReturnError(returnValue, function)

# ContextC.h functions

def osvrClientInit(applicationIdentifier, flags):
    mylib.osvrClientInit.argtypes = [c_char_p, c_uint32]
    mylib.osvrClientInit.restype = OSVR_ClientContext
    return mylib.osvrClientInit(c_char_p(applicationIdentifier), c_uint32(flags))

def osvrClientUpdate(ctx):
    mylib.osvrClientUpdate.argtypes = [OSVR_ClientContext]
    mylib.osvrClientUpdate.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientUpdate(ctx)
    checkReturn(returnvalue, 'osvrClientUpdate')
    return returnvalue

def osvrClientCheckStatus(ctx):
    mylib.osvrClientCheckStatus.argtypes = [OSVR_ClientContext]
    mylib.osvrClientCheckStatus.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientCheckStatus(ctx)
    checkReturn(returnvalue, 'osvrClientCheckStatus')
    return returnvalue

def osvrClientShutdown(ctx):
    mylib.osvrClientShutdown.argtypes = [OSVR_ClientContext]
    mylib.osvrClientShutdown.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientShutdown(ctx)
    checkReturn(returnvalue, 'osvrClientShutdown')
    return returnvalue

# DisplayC.h functions

def osvrClientGetDisplay(ctx, disp):
    mylib.osvrClientGetDisplay.argtypes = [OSVR_ClientContext, pointer(OSVR_DisplayConfig)]
    mylib.osvrClientGetDisplay.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetDisplay(ctx, pointer(disp))
    checkReturn(returnvalue, 'osvrClientGetDisplay')
    return returnvalue

def osvrClientFreeDisplay(disp):
    mylib.osvrClientFreeDisplay.argtypes = [OSVR_DisplayConfig]
    mylib.osvrClientFreeDisplay.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientFreeDisplay(disp)
    checkReturn(returnvalue, 'osvrClientFreeDisplay')
    return returnvalue

def osvrClientCheckDisplayStartup(disp):
    mylib.osvrClientCheckDisplayStartup.argtypes = [OSVR_DisplayConfig]
    mylib.osvrClientCheckDisplayStartup.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientCheckDisplayStartup(disp)
    checkReturn(returnvalue, 'osvrClientCheckDisplayStartup')
    return returnvalue

def osvrClientGetNumDisplayInputs(disp, numDisplayInputs):
    mylib.osvrClientGetNumDisplayInputs.argtypes = [OSVR_DisplayConfig, pointer(OSVR_DisplayInputCount)]
    mylib.osvrClientGetNumDisplayInputs.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetNumDisplayInputs(disp, numDisplayInputs)
    checkReturn(returnvalue, 'osvrClientGetNumDisplayInputs')
    return returnvalue

def osvrClientGetDisplayDimensions(disp, displayInputIndex, width, height):
    mylib.osvrClientGetDisplayDimensions.argtypes = [OSVR_DisplayConfig, OSVR_DisplayInputCount, pointer(OSVR_DisplayDimension), pointer(OSVR_DisplayDimension)]
    mylib.osvrClientGetDisplayDimensions.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetDisplayDimensions(disp, displayInputIndex, pointer(width), pointer(height))
    checkReturn(returnvalue, 'osvrClientGetDisplayDimensions')
    return returnvalue

def osvrClientGetNumViewers(disp, viewers):
    mylib.osvrClientGetNumViewers.argtypes = [OSVR_DisplayConfig, pointer(OSVR_ViewerCount)]
    mylib.osvrClientGetNumViewers.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetNumViewers(disp, pointer(viewers))
    checkReturn(returnvalue, 'osvrClientGetNumViewers')
    return returnvalue

def osvrClientGetViewerPose(disp, viewer, pose):
    mylib.osvrClientGetViewerPose.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, pointer(OSVR_Pose3)]
    mylib.osvrClientGetViewerPose.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerPose(disp, viewer, pointer(pose))
    checkReturn(returnvalue, 'osvrClientGetViewerPose')
    return returnvalue

def osvrClientGetNumEyesForViewer(disp, viewer, eyes):
    mylib.osvrClientGetNumEyesForViewer.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, pointer(OSVR_EyeCount)]
    mylib.osvrClientGetNumEyesForViewer.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetNumEyesForViewer(disp, viewer, pointer(eyes))
    checkReturn(returnvalue, 'osvrClientGetNumEyesForViewer')
    return returnvalue

def osvrClientGetViewerEyePose(disp, viewer, eye, pose):
    mylib.osvrClientGetViewerEyePose.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_EyeCount, pointer(OSVR_Pose3)]
    mylib.osvrClientGetViewerEyePose.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerPose(disp, viewer, eye, pointer(pose))
    checkReturn(returnvalue, 'osvrClientGetViewerEyePose')
    return returnvalue

def osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, mat):
    mylib.osvrClientGetViewerEyeViewMatrixd.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_EyeCount, OSVR_MatrixConventions, pointer(c_double)]
    mylib.osvrClientGetViewerEyeViewMatrixd.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, pointer(c_double(mat)))
    checkReturn(returnvalue, 'osvrClientGetViewerEyeViewMatrixd')
    return returnvalue

def osvrClientGetViewerEyeViewMatrixf(disp, viewer, eye, flags, mat):
    mylib.osvrClientGetViewerEyeViewMatrixf.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_EyeCount,rOSVR_MatrixConventions, pointer(c_float)]
    mylib.osvrClientGetViewerEyeViewMatrixf.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, pointer(c_float(mat)))
    checkReturn(returnvalue, 'osvrClientGetViewerEyeViewMatrixf')
    return returnvalue

def osvrClientGetNumSurfacesForViewerEye(disp, viewer, eye, surfaces):
    mylib.osvrClientGetNumSurfacesForViewerEye.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_EyeCount, pointer(OSVR_SurfaceCount)]
    mylib.osvrClientGetNumSurfacesForViewerEye.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetNumSurfacesForViewerEye(disp, viewer, eye, pointer(surfaces))
    checkReturn(returnvalue, 'osvrClientGetNumSurfacesForViewerEye')
    return returnvalue

def osvrClientGetRelativeViewportForViewerEyeSurface(disp, viewer, eye, surface, left, bottom, width, height):
    mylib.osvrClientGetRelativeViewportForViewerEyeSurface.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_EyeCount, OSVR_SurfaceCount, pointer(OSVR_ViewportDimension), pointer(OSVR_ViewportDimension), pointer(OSVR_ViewportDimension), pointer(OSVR_ViewportDimension)]
    mylib.osvrClientGetRelativeViewportForViewerEyeSurface.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetRelativeViewportForViewerEyeSurface(disp, viewer, eye, surface, pointer(left), pointer(bottom), pointer(width), pointer(height))
    checkReturn(returnvalue, 'osvrClientGetRelativeViewportForViewerEyeSurface')
    return returnvalue

def osvrClientGetViewerEyeSurfaceDisplayInputIndex(disp, viewer, eye, surface, displayInput):
    mylib.osvrClientGetViewerEyeSurfaceDisplayInputIndex.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_EyeCount, OSVR_SurfaceCount, pointer(OSVR_DisplayInputCount)]
    mylib.osvrClientGetViewerEyeSurfaceDisplayInputIndex.restype = OSVR_ReturnCode
    returnvalue = osvrClientGetViewerEyeSurfaceDisplayInputIndex(disp, viewer, eye, surface, pointer(displayInput))
    checkReturn(returnvalue, 'osvrClientGetRelativeViewportEyeSurfaceDisplayInputIndex')
    return returnvalue

def osvrClientGetViewerEyeSurfaceProjectionMatrixd(disp, viewer, eye, surface, near, far, flags, matrix):
    mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixd.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_EyeCount, OSVR_SurfaceCount, c_double, c_double, OSVR_MatrixConventions, pointer(c_double)]
    mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixd.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixd(disp, viewer, eye, surface, near, far, flags, pointer(matrix))
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceProjectionMatrixd')
    return returnvalue

def osvrClientGetViewerEyeSurfaceProjectionMatrixf(disp, viewer, eye, surface, near, far, flags, matrix):
    mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixf.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_EyeCount, OSVR_SurfaceCount, c_double, c_double, OSVR_MatrixConventions, pointer(c_float)]
    mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixf.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixf(disp, viewer, eye, surface, near, far, flags, pointer(matrix))
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceProjectionMatrixf')
    return returnvalue

def osvrClientGetViewerEyeSurfaceProjectionClippingPlanes(disp, viewer, eye, surface, left, right, bottom, top):
    mylib.osvrClientGetViewerEyeSurfaceProjectionClippingPlanes.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_SurfaceCount, pointer(c_double), pointer(c_double), pointer(c_double), pointer(c_double)]
    mylib.osvrClientGetViewerEyeSurfaceProjectionClippingPlanes.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceProjectionClippingPlanes(disp, viewer, eye, surface, pointer(left), pointer(right), pointer(bottom), pointer(top))
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceProjectionClippingPlanes')
    return returnvalue

def osvrClientDoesViewerEyeSurfaceWantDistortion(disp, viewer, eye, surface, distortionRequested):
    mylib.osvrClientDoesViewerEyeSurfaceWantDistortion.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_SurfaceCount, pointer(uint8_t)]
    mylib.osvrClientDoesViewerEyeSurfaceWantDistortion.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientDoesViewerEyeSurfaceWantDistortion(disp, viewer, eye, surface, pointer(distortionRequested))
    checkReturn(returnvalue, 'osvrClientDoesViewerEyeSurfaceWantDistortion')
    return returnvalue

def osvrClientGetViewerEyeSurfaceRadialDistortionPriority(disp, viewer, eye, surface, priority):
    mylib.osvrClientGetViewerEyeSurfaceRadialDistortionPriority.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_SurfaceCount, pointer(uint32_t)]
    mylib.osvrClientGetViewerEyeSurfaceRadialDistortionPriority.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceRadialDistortionPriority(disp, viewer, eye, surface, pointer(priority))
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceRadialDistortionPriority')
    return returnvalue

def osvrClientGetViewerEyeSurfaceRadialDistortion(disp, viewer, eye, surface, params):
    mylib.osvrClientGetViewerEyeSurfaceRadialDistortion.argtypes = [OSVR_DisplayConfig, OSVR_ViewerCount, OSVR_EyeCount, OSVR_SurfaceCount, pointer(OSVR_RadialDistortionParameters)]
    mylib.osvrClientGetViewerEyeSurfaceRadialDistortion.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceRadialDistortion(disp, viewer, eye, surface, pointer(params))
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceRadialDistortion')
    return returnvalue

# ImagingC.h functions

def osvrClientFreeImage(ctx, buf):
    mylib.osvrClientFreeImage.argtypes = [OSVR_ClientContext, pointer(OSVR_ImageBufferElement)]
    mylib.osvrClientFreeImage.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientFreeImage(ctx, pointer(buf))
    checkReturn(returnvalue, 'osvrClientFreeImage')
    return returnvalue

# InterfaceC.h functions

def osvrClientGetInterface(ctx, path, iface):
    mylib.osvrClientGetInterface.argtypes = [OSVR_ClientContext, c_char_p, pointer(OSVR_ClientInterface)]
    mylib.osvrClientGetInterace.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetInterface(ctx, c_char_p(path), iface)
    checkReturn(returnvalue, 'osvrClientGetInterface')
    return returnvalue

def osvrClientFreeInterface(ctx, iface):
    mylib.osvrClientFreeInterface.argtypes = [OSVR_ClientContext, OSVR_ClientInterface]
    mylib.osvrClientFreeInterface.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientFreeInterface(ctx, iface)
    checkReturn(returnvalue, 'osvrClientFreeInterface')
    return returnvalue

# ParametersC.h functions

def osvrClientGetStringParameterLength(ctx, path, len):
    mylib.osvrClientGetStringParameterLength.argtypes = [OSVR_ClientContext, c_char_p, c_size_t]
    mylib.osvrClientGetStringParameterLength.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrGetStringParameterLength(ctx, c_char_p(path), c_size_t(len))
    checkReturn(returnvalue, 'osvrClientGetStringParameterLength')
    return returnvalue

def osvrClientGetStringParameter(ctx, path, buf, len):
    mylib.osvrClientGetStringParameterLength.argtypes = [OSVR_ClientContext, c_char_p, c_char_p, c_size_t]
    mylib.osvrClientGetStringParameterLength.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetStringParameter(ctx, c_char_p(path), c_char_p(buf), c_size_t(len))
    checkReturn(returnvalue, 'osvrClientGetStringParameter')
    return returnvalue
