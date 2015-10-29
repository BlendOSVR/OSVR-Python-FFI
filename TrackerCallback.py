from ctypes import *
from osvrClientKit import *

def myTrackerCallback(userdata, timestamp, report):
	print("Got POSE report: Position = (%f, %f, %f), orientation = (%f, %f, %f, %f)\n" % (report.contents.pose.translation.data[0], report.contents.pose.translation.data[1], report.contents.pose.translation.data[2], report.contents.pose.rotation.data[0], report.contents.pose.rotation.data[1], report.contents.pose.rotation.data[2], report.contents.pose.rotation.data[3]))

def myOrientationCallback(userdata, timestamp, report):
	print("Got ORIENTATION report: Orientation = (%f, %f, %f, %f)\n" % (report.contents.pose.rotation.data[0], report.contents.pose.rotation.data[1], report.contents.pose.rotation.data[2], report.contents.pose.rotation.data[3]))

def myPositionCallback(userdata, timestamp, report):
	print("Got POSITION report: Position = (%f, %f, %f)\n" % (report.contents.xyz.data[0], report.contents.xyz.data[1], report.contents.xyz.data[2]))
ctx = osvrClientInit("com.osvr.exampleclients.TrackerCallback")

lefthand = osvrClientGetInterface(ctx, "/me/hands/left")

osvrRegisterPoseCallback(lefthand, OSVR_PoseCallback(myTrackerCallback), None)

osvrRegisterOrientationCallback(lefthand, OSVR_OrientationCallback(myOrientationCallback), None)

osvrRegisterPositionCallback(lefthand, OSVR_PositionCallback(myPositionCallback), None)

for i in range(0, 1000000):
    osvrClientUpdate(ctx)

osvrClientShutdown(ctx)

print("Library shut down, exiting.\n")