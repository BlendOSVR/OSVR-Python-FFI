from ctypes import *

mylib = cdll.LoadLibrary("osvrClientKit")

#Not sure how to handle return code
class OSVR_ReturnCode(Structure):
    pass

#Not sure if return failure needs to be a struct, pretty sure it's just a #define
class OSVR_Return_Failure(Structure):
    pass


class OSVR_ClientContextObject(Structure):
    pass

OSVR_ClientContext = POINTER(OSVR_ClientContextObject)

class OSVR_ClientInterfaceObject(Structure):
    pass

OSVR_ClientInterface = POINTER(OSVR_ClientInterfaceObject)

class OSVR_DisplayConfigObject(Structure):
    pass

OSVR_DisplayConfig = POINTER(OSVR_DisplayConfigObject)

class OSVR_Vec2(Structure):
    _fields_ = [("data", c_double * 2)]

class OSVR_Vec3(Structure):
    _fields_ = [("data", c_double * 3)]

class OSVR_Quaternion(Structure):
    _fields_ = [("data", c_double * 4)]

class OSVR_Pose3(Structure):
    _fields_ = [("translation", OSVR_Vec3), ("rotation", OSVR_Quaternion)]

class OSVR_RadialDistortionParameters(Structure):
    _fields_ = [("k1", OSVR_Vec3), ("centerOfProjection", OSVR_Vec2)]

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
    return mylib.osvrClientInit(applicationIdentifier, flags)

def osvrClientUpdate(ctx):
    mylib.osvrClientUpdate.argtypes = [OSVR_ClientContext]
    #mylib.osvrClientUpdate.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientUpdate(ctx)
    checkReturn(returnvalue, 'osvrClientUpdate')
    return returnvalue

def osvrClientCheckStatus(ctx):
    mylib.osvrClientCheckStatus.argtypes = [OSVR_ClientContext]
    #mylib.osvrClientCheckStatus.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientCheckStatus(ctx)
    checkReturn(returnvalue, 'osvrClientCheckStatus')
    return returnvalue

def osvrClientShutdown(ctx):
    mylib.osvrClientShutdown.argtypes = [OSVR_ClientContext]
    #mylib.osvrClientShutdown.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientShutdown(ctx)
    checkReturn(returnvalue, 'osvrClientShutdown')
    return returnvalue

# DisplayC.h functions

def osvrClientGetDisplay(ctx, disp):
    mylib.osvrClientGetDisplay.argtypes = [OSVR_ClientContext, pointer(OSVR_DisplayConfig)]
    #mylib.osvrClientGetDisplay.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetDisplay(ctx, disp)
    checkReturn(returnvalue, 'osvrClientGetDisplay')
    return returnvalue

def osvrClientFreeDisplay(disp):
    mylib.osvrClientFreeDisplay.argtypes = [OSVR_DisplayConfig]
    #mylib.osvrClientFreeDisplay.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientFreeDisplay(disp)
    checkReturn(returnvalue, 'osvrClientFreeDisplay')
    return returnvalue

def osvrClientCheckDisplayStartup(disp):
    mylib.osvrClientCheckDisplayStartup.argtypes = [OSVR_DisplayConfig]
    #mylib.osvrClientCheckDisplayStartup.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientCheckDisplayStartup(disp)
    checkReturn(returnvalue, 'osvrClientCheckDisplayStartup')
    return returnvalue

def osvrClientGetNumDisplayInputs(disp, numDisplayInputs):
    mylib.osvrClientGetNumDisplayInputs.argtypes = [OSVR_DisplayConfig, pointer(c_uint8)]
    #mylib.osvrClientGetNumDisplayInputs.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetNumDisplayInputs(disp, numDisplayInputs)
    checkReturn(returnvalue, 'osvrClientGetNumDisplayInputs')
    return returnvalue

def osvrClientGetDisplayDimensions(disp, displayInputIndex, width, height):
    mylib.osvrClientGetDisplayDimensions.argtypes = [OSVR_DisplayConfig, c_uint8, pointer(c_int32), pointer(c_int32)]
    #mylib.osvrClientGetDisplayDimensions.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetDisplayDimensions(disp, displayInputIndex, width, height)
    checkReturn(returnvalue, 'osvrClientGetDisplayDimensions')
    return returnvalue

def osvrClientGetNumViewers(disp, viewers):
    mylib.osvrClientGetNumViewers.argtypes = [OSVR_DisplayConfig, pointer(c_uint32)]
    #mylib.osvrClientGetNumViewers.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetNumViewers(disp, viewers)
    checkReturn(returnvalue, 'osvrClientGetNumViewers')
    return returnvalue

def osvrClientGetViewerPose(disp, viewer, pose):
    mylib.osvrClientGetViewerPose.argtypes = [OSVR_DisplayConfig, c_uint32, pointer(OSVR_Pose3)]
    #mylib.osvrClientGetViewerPose.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerPose(disp, viewer, pose)
    checkReturn(returnvalue, 'osvrClientGetViewerPose')
    return returnvalue

def osvrClientGetNumEyesForViewer(disp, viewer, eyes):
    mylib.osvrClientGetNumEyesForViewer.argtypes = [OSVR_DisplayConfig, c_uint32, pointer(c_uint8)]
    #mylib.osvrClientGetNumEyesForViewer.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetNumEyesForViewer(disp, viewer, eyes)
    checkReturn(returnvalue, 'osvrClientGetNumEyesForViewer')
    return returnvalue

def osvrClientGetViewerEyePose(disp, viewer, eye, pose):
    mylib.osvrClientGetViewerEyePose.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, pointer(OSVR_Pose3)]
    #mylib.osvrClientGetViewerEyePose.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerPose(disp, viewer, eye, pose)
    checkReturn(returnvalue, 'osvrClientGetViewerEyePose')
    return returnvalue

def osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, mat):
    mylib.osvrClientGetViewerEyeViewMatrixd.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, c_uint16, pointer(c_double)]
    #mylib.osvrClientGetViewerEyeViewMatrixd.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, mat)
    checkReturn(returnvalue, 'osvrClientGetViewerEyeViewMatrixd')
    return returnvalue

def osvrClientGetViewerEyeViewMatrixf(disp, viewer, eye, flags, mat):
    mylib.osvrClientGetViewerEyeViewMatrixf.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, c_uint16, pointer(c_float)]
    #mylib.osvrClientGetViewerEyeViewMatrixf.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, mat)
    checkReturn(returnvalue, 'osvrClientGetViewerEyeViewMatrixf')
    return returnvalue

def osvrClientGetNumSurfacesForViewerEye(disp, viewer, eye, surfaces):
    mylib.osvrClientGetNumSurfacesForViewerEye.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, pointer(c_uint32)]
    #mylib.osvrClientGetNumSurfacesForViewerEye.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetNumSurfacesForViewerEye(disp, viewer, eye, surfaces)
    checkReturn(returnvalue, 'osvrClientGetNumSurfacesForViewerEye')
    return returnvalue

def osvrClientGetRelativeViewportForViewerEyeSurface(disp, viewer, eye, surface, left, bottom, width, height):
    mylib.osvrClientGetRelativeViewportForViewerEyeSurface.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, c_uint32, pointer(c_int32), pointer(c_int32), pointer(c_int32), pointer(c_int32)]
    #mylib.osvrClientGetRelativeViewportForViewerEyeSurface.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetRelativeViewportForViewerEyeSurface(disp, viewer, eye, surface, left, bottom, width, height)
    checkReturn(returnvalue, 'osvrClientGetRelativeViewportForViewerEyeSurface')
    return returnvalue

def osvrClientGetViewerEyeSurfaceDisplayInputIndex(disp, viewer, eye, surface, displayInput):
    mylib.osvrClientGetViewerEyeSurfaceDisplayInputIndex.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, c_uint32, pointer(c_uint8)]
    #mylib.osvrClientGetViewerEyeSurfaceDisplayInputIndex.restype = OSVR_ReturnCode
    returnvalue = osvrClientGetViewerEyeSurfaceDisplayInputIndex(disp, viewer, eye, surface, displayInput)
    checkReturn(returnvalue, 'osvrClientGetRelativeViewportEyeSurfaceDisplayInputIndex')
    return returnvalue

def osvrClientGetViewerEyeSurfaceProjectionMatrixd(disp, viewer, eye, surface, near, far, flags, matrix):
    mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixd.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, c_uint32, c_double, c_double, c_uint16, pointer(c_double)]
    #mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixd.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixd(disp, viewer, eye, surface, near, far, flags, matrix)
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceProjectionMatrixd')
    return returnvalue

def osvrClientGetViewerEyeSurfaceProjectionMatrixf(disp, viewer, eye, surface, near, far, flags, matrix):
    mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixf.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, c_uint32, c_double, c_double, c_uint16, pointer(c_float)]
    #mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixf.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixf(disp, viewer, eye, surface, near, far, flags, matrix)
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceProjectionMatrixf')
    return returnvalue

def osvrClientGetViewerEyeSurfaceProjectionClippingPlanes(disp, viewer, eye, surface, left, right, bottom, top):
    mylib.osvrClientGetViewerEyeSurfaceProjectionClippingPlanes.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint32, pointer(c_double), pointer(c_double), pointer(c_double), pointer(c_double)]
    #mylib.osvrClientGetViewerEyeSurfaceProjectionClippingPlanes.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceProjectionClippingPlanes(disp, viewer, eye, surface, left, right, bottom, top)
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceProjectionClippingPlanes')
    return returnvalue

def osvrClientDoesViewerEyeSurfaceWantDistortion(disp, viewer, eye, surface, distortionRequested):
    mylib.osvrClientDoesViewerEyeSurfaceWantDistortion.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint32, pointer(c_uint8_t)]
    #mylib.osvrClientDoesViewerEyeSurfaceWantDistortion.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientDoesViewerEyeSurfaceWantDistortion(disp, viewer, eye, surface, distortionRequested)
    checkReturn(returnvalue, 'osvrClientDoesViewerEyeSurfaceWantDistortion')
    return returnvalue

def osvrClientGetViewerEyeSurfaceRadialDistortionPriority(disp, viewer, eye, surface, priority):
    mylib.osvrClientGetViewerEyeSurfaceRadialDistortionPriority.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint32, pointer(c_int32_t)]
    #mylib.osvrClientGetViewerEyeSurfaceRadialDistortionPriority.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceRadialDistortionPriority(disp, viewer, eye, surface, priority)
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceRadialDistortionPriority')
    return returnvalue

def osvrClientGetViewerEyeSurfaceRadialDistortion(disp, viewer, eye, surface, params):
    mylib.osvrClientGetViewerEyeSurfaceRadialDistortion.argtypes = [OSVR_DisplayConfig, c_uint32, OSVR_EyeCount, c_uint32, pointer(OSVR_RadialDistortionParameters)]
    #mylib.osvrClientGetViewerEyeSurfaceRadialDistortion.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceRadialDistortion(disp, viewer, eye, surface, params)
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceRadialDistortion')
    return returnvalue

# ImagingC.h functions
# These don't seem to be included in the doxygen docs

# c_ubyte is the ctypes type for unsigned char
def osvrClientFreeImage(ctx, buf):
    mylib.osvrClientFreeImage.argtypes = [OSVR_ClientContext, pointer(c_ubyte)]
    #mylib.osvrClientFreeImage.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientFreeImage(ctx, buf)
    checkReturn(returnvalue, 'osvrClientFreeImage')
    return returnvalue

# InterfaceC.h functions

def osvrClientGetInterface(ctx, path, iface):
    mylib.osvrClientGetInterface.argtypes = [OSVR_ClientContext, c_char_p, pointer(OSVR_ClientInterface)]
    #mylib.osvrClientGetInterace.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetInterface(ctx, path, iface)
    checkReturn(returnvalue, 'osvrClientGetInterface')
    return returnvalue

def osvrClientFreeInterface(ctx, iface):
    mylib.osvrClientFreeInterface.argtypes = [OSVR_ClientContext, OSVR_ClientInterface]
    #mylib.osvrClientFreeInterface.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientFreeInterface(ctx, iface)
    checkReturn(returnvalue, 'osvrClientFreeInterface')
    return returnvalue

# ParametersC.h functions

def osvrClientGetStringParameterLength(ctx, path, len):
    mylib.osvrClientGetStringParameterLength.argtypes = [OSVR_ClientContext, c_char_p, c_size_t]
    #mylib.osvrClientGetStringParameterLength.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrGetStringParameterLength(ctx, path, len)
    checkReturn(returnvalue, 'osvrClientGetStringParameterLength')
    return returnvalue

def osvrClientGetStringParameter(ctx, path, buf, len):
    mylib.osvrClientGetStringParameterLength.argtypes = [OSVR_ClientContext, c_char_p, c_char_p, c_size_t]
    #mylib.osvrClientGetStringParameterLength.restype = OSVR_ReturnCode
    returnvalue = mylib.osvrClientGetStringParameter(ctx, path, buf, len)
    checkReturn(returnvalue, 'osvrClientGetStringParameter')
    return returnvalue
