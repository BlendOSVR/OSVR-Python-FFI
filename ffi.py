from ctypes import *

mylib = cdll.LoadLibrary("osvrClientKit")

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

class OSVR_TimeValue(Structure):
    _fields_ = [("seconds", c_int64),("microseconds", c_int32)]

class OSVR_EyeTracker3DState(Structure):
    _fields_ = [("direction", OSVR_Vec3), ("basePoint", OSVR_Vec3)]

# Error checking

class ReturnError(Exception):
    def __init__(self, value, function):
        self.value = value
        self.function = function
    def __str__(self):
        return repr(self.function)

def checkReturn(returnValue, function):
    if returnValue == c_int8(1):
        raise ReturnError(returnValue, function)

# ContextC.h functions

def osvrClientInit(applicationIdentifier):
    mylib.osvrClientInit.argtypes = [c_char_p, c_uint32]
    mylib.osvrClientInit.restype = OSVR_ClientContext
    return mylib.osvrClientInit(c_char_p(applicationIdentifier.encode("utf8")), c_uint32(0))

def osvrClientUpdate(ctx):
    mylib.osvrClientUpdate.argtypes = [OSVR_ClientContext]
    mylib.osvrClientUpdate.restype = c_int8
    returnvalue = mylib.osvrClientUpdate(ctx)
    checkReturn(returnvalue, 'osvrClientUpdate')
    return

def osvrClientCheckStatus(ctx):
    mylib.osvrClientCheckStatus.argtypes = [OSVR_ClientContext]
    mylib.osvrClientCheckStatus.restype = c_int8
    returnvalue = mylib.osvrClientCheckStatus(ctx)
    checkReturn(returnvalue, 'osvrClientCheckStatus')
    return returnvalue

def osvrClientShutdown(ctx):
    mylib.osvrClientShutdown.argtypes = [OSVR_ClientContext]
    mylib.osvrClientShutdown.restype = c_int8
    returnvalue = mylib.osvrClientShutdown(ctx)
    checkReturn(returnvalue, 'osvrClientShutdown')
    return

# DisplayC.h functions

def osvrClientGetDisplay(ctx):
    mylib.osvrClientGetDisplay.argtypes = [OSVR_ClientContext, POINTER(OSVR_DisplayConfigObject)]
    mylib.osvrClientGetDisplay.restype = c_int8
    disp = OSVR_DisplayConfigObject()
    returnvalue = mylib.osvrClientGetDisplay(ctx, pointer(disp))
    checkReturn(returnvalue, 'osvrClientGetDisplay')
    return disp

def osvrClientFreeDisplay(disp):
    mylib.osvrClientFreeDisplay.argtypes = [OSVR_DisplayConfig]
    mylib.osvrClientFreeDisplay.restype = c_int8
    returnvalue = mylib.osvrClientFreeDisplay(disp)
    checkReturn(returnvalue, 'osvrClientFreeDisplay')
    return

def osvrClientCheckDisplayStartup(disp):
    mylib.osvrClientCheckDisplayStartup.argtypes = [OSVR_DisplayConfig]
    mylib.osvrClientCheckDisplayStartup.restype = c_int8
    returnvalue = mylib.osvrClientCheckDisplayStartup(disp)
    checkReturn(returnvalue, 'osvrClientCheckDisplayStartup')
    return returnvalue

def osvrClientGetNumDisplayInputs(disp):
    mylib.osvrClientGetNumDisplayInputs.argtypes = [OSVR_DisplayConfig, POINTER(c_uint8)]
    mylib.osvrClientGetNumDisplayInputs.restype = c_int8
    numDisplayInputs = c_uint8()
    returnvalue = mylib.osvrClientGetNumDisplayInputs(disp, pointer(numDisplayInputs))
    checkReturn(returnvalue, 'osvrClientGetNumDisplayInputs')
    return numDisplayInputs

#Need to continue changing return types from here down

def osvrClientGetDisplayDimensions(disp, displayInputIndex, width, height):
    mylib.osvrClientGetDisplayDimensions.argtypes = [OSVR_DisplayConfig, c_uint8, POINTER(c_int32), POINTER(c_int32)]
    mylib.osvrClientGetDisplayDimensions.restype = c_int8
    returnvalue = mylib.osvrClientGetDisplayDimensions(disp, displayInputIndex, width, height)
    checkReturn(returnvalue, 'osvrClientGetDisplayDimensions')
    return returnvalue

def osvrClientGetNumViewers(disp, viewers):
    mylib.osvrClientGetNumViewers.argtypes = [OSVR_DisplayConfig, POINTER(c_uint32)]
    mylib.osvrClientGetNumViewers.restype = c_int8
    returnvalue = mylib.osvrClientGetNumViewers(disp, viewers)
    checkReturn(returnvalue, 'osvrClientGetNumViewers')
    return returnvalue

def osvrClientGetViewerPose(disp, viewer, pose):
    mylib.osvrClientGetViewerPose.argtypes = [OSVR_DisplayConfig, c_uint32, POINTER(OSVR_Pose3)]
    mylib.osvrClientGetViewerPose.restype = c_int8
    returnvalue = mylib.osvrClientGetViewerPose(disp, viewer, pose)
    checkReturn(returnvalue, 'osvrClientGetViewerPose')
    return returnvalue

def osvrClientGetNumEyesForViewer(disp, viewer, eyes):
    mylib.osvrClientGetNumEyesForViewer.argtypes = [OSVR_DisplayConfig, c_uint32, POINTER(c_uint8)]
    mylib.osvrClientGetNumEyesForViewer.restype = c_int8
    returnvalue = mylib.osvrClientGetNumEyesForViewer(disp, viewer, eyes)
    checkReturn(returnvalue, 'osvrClientGetNumEyesForViewer')
    return returnvalue

def osvrClientGetViewerEyePose(disp, viewer, eye, pose):
    mylib.osvrClientGetViewerEyePose.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, POINTER(OSVR_Pose3)]
    mylib.osvrClientGetViewerEyePose.restype = c_int8
    returnvalue = mylib.osvrClientGetViewerPose(disp, viewer, eye, pose)
    checkReturn(returnvalue, 'osvrClientGetViewerEyePose')
    return returnvalue

def osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, mat):
    mylib.osvrClientGetViewerEyeViewMatrixd.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, c_uint16, POINTER(c_double)]
    mylib.osvrClientGetViewerEyeViewMatrixd.restype = c_int8
    returnvalue = mylib.osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, mat)
    checkReturn(returnvalue, 'osvrClientGetViewerEyeViewMatrixd')
    return returnvalue

def osvrClientGetViewerEyeViewMatrixf(disp, viewer, eye, flags, mat):
    mylib.osvrClientGetViewerEyeViewMatrixf.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, c_uint16, POINTER(c_float)]
    mylib.osvrClientGetViewerEyeViewMatrixf.restype = c_int8
    returnvalue = mylib.osvrClientGetViewerEyeViewMatrixd(disp, viewer, eye, flags, mat)
    checkReturn(returnvalue, 'osvrClientGetViewerEyeViewMatrixf')
    return returnvalue

def osvrClientGetNumSurfacesForViewerEye(disp, viewer, eye, surfaces):
    mylib.osvrClientGetNumSurfacesForViewerEye.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, POINTER(c_uint32)]
    mylib.osvrClientGetNumSurfacesForViewerEye.restype = c_int8
    returnvalue = mylib.osvrClientGetNumSurfacesForViewerEye(disp, viewer, eye, surfaces)
    checkReturn(returnvalue, 'osvrClientGetNumSurfacesForViewerEye')
    return returnvalue

def osvrClientGetRelativeViewportForViewerEyeSurface(disp, viewer, eye, surface, left, bottom, width, height):
    mylib.osvrClientGetRelativeViewportForViewerEyeSurface.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, c_uint32, POINTER(c_int32), POINTER(c_int32), POINTER(c_int32), POINTER(c_int32)]
    mylib.osvrClientGetRelativeViewportForViewerEyeSurface.restype = c_int8
    returnvalue = mylib.osvrClientGetRelativeViewportForViewerEyeSurface(disp, viewer, eye, surface, left, bottom, width, height)
    checkReturn(returnvalue, 'osvrClientGetRelativeViewportForViewerEyeSurface')
    return returnvalue

def osvrClientGetViewerEyeSurfaceDisplayInputIndex(disp, viewer, eye, surface, displayInput):
    mylib.osvrClientGetViewerEyeSurfaceDisplayInputIndex.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, c_uint32, POINTER(c_uint8)]
    mylib.osvrClientGetViewerEyeSurfaceDisplayInputIndex.restype = c_int8
    returnvalue = osvrClientGetViewerEyeSurfaceDisplayInputIndex(disp, viewer, eye, surface, displayInput)
    checkReturn(returnvalue, 'osvrClientGetRelativeViewportEyeSurfaceDisplayInputIndex')
    return returnvalue

def osvrClientGetViewerEyeSurfaceProjectionMatrixd(disp, viewer, eye, surface, near, far, flags, matrix):
    mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixd.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, c_uint32, c_double, c_double, c_uint16, POINTER(c_double)]
    mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixd.restype = c_int8
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixd(disp, viewer, eye, surface, near, far, flags, matrix)
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceProjectionMatrixd')
    return returnvalue

def osvrClientGetViewerEyeSurfaceProjectionMatrixf(disp, viewer, eye, surface, near, far, flags, matrix):
    mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixf.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, c_uint32, c_double, c_double, c_uint16, POINTER(c_float)]
    mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixf.restype = c_int8
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceProjectionMatrixf(disp, viewer, eye, surface, near, far, flags, matrix)
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceProjectionMatrixf')
    return returnvalue

def osvrClientGetViewerEyeSurfaceProjectionClippingPlanes(disp, viewer, eye, surface, left, right, bottom, top):
    mylib.osvrClientGetViewerEyeSurfaceProjectionClippingPlanes.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint32, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    mylib.osvrClientGetViewerEyeSurfaceProjectionClippingPlanes.restype = c_int8
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceProjectionClippingPlanes(disp, viewer, eye, surface, left, right, bottom, top)
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceProjectionClippingPlanes')
    return returnvalue

def osvrClientDoesViewerEyeSurfaceWantDistortion(disp, viewer, eye, surface, distortionRequested):
    mylib.osvrClientDoesViewerEyeSurfaceWantDistortion.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint32, POINTER(c_uint8_t)]
    mylib.osvrClientDoesViewerEyeSurfaceWantDistortion.restype = c_int8
    returnvalue = mylib.osvrClientDoesViewerEyeSurfaceWantDistortion(disp, viewer, eye, surface, distortionRequested)
    checkReturn(returnvalue, 'osvrClientDoesViewerEyeSurfaceWantDistortion')
    return returnvalue

def osvrClientGetViewerEyeSurfaceRadialDistortionPriority(disp, viewer, eye, surface, priority):
    mylib.osvrClientGetViewerEyeSurfaceRadialDistortionPriority.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint32, POINTER(c_int32_t)]
    mylib.osvrClientGetViewerEyeSurfaceRadialDistortionPriority.restype = c_int8
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceRadialDistortionPriority(disp, viewer, eye, surface, priority)
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceRadialDistortionPriority')
    return returnvalue

def osvrClientGetViewerEyeSurfaceRadialDistortion(disp, viewer, eye, surface, params):
    mylib.osvrClientGetViewerEyeSurfaceRadialDistortion.argtypes = [OSVR_DisplayConfig, c_uint32, c_uint8, c_uint32, POINTER(OSVR_RadialDistortionParameters)]
    mylib.osvrClientGetViewerEyeSurfaceRadialDistortion.restype = c_int8
    returnvalue = mylib.osvrClientGetViewerEyeSurfaceRadialDistortion(disp, viewer, eye, surface, params)
    checkReturn(returnvalue, 'osvrClientGetViewerEyeSurfaceRadialDistortion')
    return returnvalue

# ImagingC.h functions
# These don't seem to be included in the doxygen docs

# c_ubyte is the ctypes type for unsigned char
def osvrClientFreeImage(ctx, buf):
    mylib.osvrClientFreeImage.argtypes = [OSVR_ClientContext, POINTER(c_ubyte)]
    mylib.osvrClientFreeImage.restype = c_int8
    returnvalue = mylib.osvrClientFreeImage(ctx, buf)
    checkReturn(returnvalue, 'osvrClientFreeImage')
    return

# InterfaceC.h functions

def osvrClientGetInterface(ctx, path):
    mylib.osvrClientGetInterface.argtypes = [OSVR_ClientContext, c_char_p, POINTER(OSVR_ClientInterface)]
    mylib.osvrClientGetInterface.restype = c_int8
    interface = pointer(OSVR_ClientInterfaceObject())
    returnvalue = mylib.osvrClientGetInterface(ctx, c_char_p(path.encode("utf8")), pointer(interface))
    checkReturn(returnvalue, 'osvrClientGetInterface')
    return interface

def osvrClientFreeInterface(ctx, iface):
    mylib.osvrClientFreeInterface.argtypes = [OSVR_ClientContext, OSVR_ClientInterface]
    mylib.osvrClientFreeInterface.restype = c_int8
    returnvalue = mylib.osvrClientFreeInterface(ctx, iface)
    checkReturn(returnvalue, 'osvrClientFreeInterface')
    return

# InterfaceStateC.h functions
#Probably need to return state and timestamp, probably make a structure for that

def osvrGetPoseState(iface, timestamp):
    mylib.osvrGetPoseState.argtypes = [OSVR_ClientInterface, POINTER(OSVR_TimeValue), POINTER(OSVR_Pose3)]
    mylib.osvrGetPoseState.restype = c_int8
    state = OSVR_Pose3()
    returnvalue = mylib.osvrGetPoseState(iface, timestamp, pointer(state))
    checkReturn(returnvalue, 'osvrGetPoseState')
    return state

def osvrGetPositionState(iface, timestamp):
    mylib.osvrGetPositionState.argtypes = [OSVR_ClientInterface, POINTER(OSVR_TimeValue), POINTER(OSVR_Vec3)]
    mylib.osvrGetPositionState.restype = c_int8
    state = OSVR_Vec3()
    returnvalue = mylib.osvrGetPositionState(iface, timestamp, pointer(state))
    checkReturn(returnvalue, 'osvrGetPositionState')
    return state

def osvrGetOrientationState(iface, timestamp):
    mylib.osvrGetOrientationState.argtypes = [OSVR_ClientInterface, POINTER(OSVR_TimeValue), POINTER(OSVR_Quaternion)]
    mylib.osvrGetOrientationState.restype = c_int8
    state = OSVR_Quaternion()
    returnvalue = mylib.osvrGetOrientationState(iface, timestamp, pointer(state))
    checkReturn(returnvalue, 'osvrGetOrientationState')
    return state

def osvrGetButtonState(iface, timestamp):
    mylib.osvrGetButtonState.argtypes = [OSVR_ClientInterface, POINTER(OSVR_TimeValue), POINTER(c_uint8)]
    mylib.osvrGetButtonState.restype = c_int8
    state = c_uint8()
    returnvalue = mylib.osvrGetButtonState(iface, timestamp, pointer(state))
    checkReturn(returnvalue, 'osvrGetButtonState')
    return state

def osvrGetAnalogState(iface, timestamp):
    mylib.osvrGetAnalogState.argtypes = [OSVR_ClientInterface, POINTER(OSVR_TimeValue), POINTER(c_double)]
    mylib.osvrGetAnalogState.restype = c_int8
    state = c_double()
    returnvalue = mylib.osvrGetAnalogState(iface, timestamp, pointer(state))
    checkReturn(returnvalue, 'osvrGetAnalogState')
    return state

def osvrGetLocation2DState(iface, timestamp):
    mylib.osvrGetLocation2DState.argtypes = [OSVR_ClientInterface, POINTER(OSVR_TimeValue), POINTER(OSVR_Vec2)]
    mylib.osvrGetLocation2DState.restype = c_int8
    state = OSVR_Vec2()
    returnvalue = mylib.osvrGetLocation2DState(iface, timestamp, pointer(state))
    checkReturn(returnvalue, 'osvrGetLocation2DState')
    return state

def osvrGetDirectionState(iface, timestamp):
    mylib.osvrGetDirectionState.argtypes = [OSVR_ClientInterface, POINTER(OSVR_TimeValue), POINTER(OSVR_Vec3)]
    mylib.osvrGetDirectionState.restype = c_int8
    state = OSVR_Vec3()
    returnvalue = mylib.osvrGetDirectionState(iface, timestamp, pointer(state))
    checkReturn(returnvalue, 'osvrGetDirectionState')
    return state

def osvrGetEyeTracker2DState(iface, timestamp):
    mylib.osvrGetEyeTracker2DState.argtypes = [OSVR_ClientInterface, POINTER(OSVR_TimeValue), POINTER(OSVR_Vec2)]
    mylib.osvrGetEyeTracker2DState.restype = c_int8
    state = OSVR_Vec2()
    returnvalue = mylib.osvrGetEyeTracker2DState(iface, timestamp, pointer(state))
    checkReturn(returnvalue, 'osvrGetEyeTracker2DState')
    return state

def osvrGetEyeTracker3DState(iface, timestamp):
    mylib.osvrGetEyeTracker3DState.argtypes = [OSVR_ClientInterface, POINTER(OSVR_TimeValue), POINTER(OSVR_EyeTracker3DState)]
    mylib.osvrGetEyeTracker3DState.restype = c_int8
    state = OSVR_EyeTracker3DState()
    returnvalue = mylib.osvrGetEyeTracker3DState(iface, timestamp, pointer(state))
    checkReturn(returnvalue, 'osvrGetEyeTracker3DState')
    return state

def osvrGetEyeTrackerBlinkState(iface, timestamp):
    mylib.osvrGetEyeTrackerBlinkState.argtypes = [OSVR_ClientInterface, POINTER(OSVR_TimeValue), POINTER(c_uint8)]
    mylib.osvrGetEyeTrackerBlinkState.restype = c_int8
    state = c_uint8()
    returnvalue = mylib.osvrGetEyeTrackerBlinkState(iface, timestamp, pointer(state))
    checkReturn(returnvalue, 'osvrGetEyeTrackerBlinkState')
    return state

def osvrGetNaviVelocityState(iface, timestamp):
    mylib.osvrGetNaviVelocityState.argtypes = [OSVR_ClientInterface, POINTER(OSVR_TimeValue), POINTER(OSVR_Vec2)]
    mylib.osvrGetNaviVelocityState.restype = c_int8
    state = OSVR_Vec2()
    returnvalue = mylib.osvrGetNaviVelocityState(iface, timestamp, pointer(state))
    checkReturn(returnvalue, 'osvrGetNaviVelocityState')
    return state

def osvrGetNaviPositionState(iface, timestamp):
    mylib.osvrGetNaviPositionState.argtypes = [OSVR_ClientInterface, POINTER(OSVR_TimeValue), POINTER(OSVR_Vec2)]
    mylib.osvrGetNaviPositionState.restype = c_int8
    state = OSVR_Vec2()
    returnvalue = mylib.osvrGetNaviPositionState(iface, timestamp, pointer(state))
    checkReturn(returnvalue, 'osvrGetNaviPositionState')
    return state


# ParametersC.h functions

def osvrClientGetStringParameterLength(ctx, path):
    mylib.osvrClientGetStringParameterLength.argtypes = [OSVR_ClientContext, c_char_p, c_size_t]
    mylib.osvrClientGetStringParameterLength.restype = c_int8
    length = c_size_t()
    returnvalue = mylib.osvrGetStringParameterLength(ctx, c_char_p(path.encode("uft8")), pointer(length))
    checkReturn(returnvalue, 'osvrClientGetStringParameterLength')
    return length

def osvrClientGetStringParameter(ctx, path, len):
    mylib.osvrClientGetStringParameter.argtypes = [OSVR_ClientContext, c_char_p, c_char_p, c_size_t]
    mylib.osvrClientGetStringParameter.restype = c_int8
    buf = create_string_buffer(len)
    returnvalue = mylib.osvrClientGetStringParameter(ctx, c_char_p(path.encode("utf8")), c_char_p(buf), c_size_t(len))
    checkReturn(returnvalue, 'osvrClientGetStringParameter')
    return buf
