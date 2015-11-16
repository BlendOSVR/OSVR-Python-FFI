# Copyright 2015 Sensics and OSVR community

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from osvrClientKit import *

def myTrackerCallback(userdata, timestamp, report):
    print("Got POSE report: Position = (%f, %f, %f), orientation = (%f, %f, %f, %f)" % (report.contents.pose.translation.data[0], report.contents.pose.translation.data[1], report.contents.pose.translation.data[2], report.contents.pose.rotation.data[0], report.contents.pose.rotation.data[1], report.contents.pose.rotation.data[2], report.contents.pose.rotation.data[3]))

def myOrientationCallback(userdata, timestamp, report):
    print("Got ORIENTATION report: Orientation = (%f, %f, %f, %f)" % (report.contents.rotation.data[0], report.contents.rotation.data[1], report.contents.rotation.data[2], report.contents.rotation.data[3]))

def myPositionCallback(userdata, timestamp, report):
    print("Got POSITION report: Position = (%f, %f, %f)" % (report.contents.xyz.data[0], report.contents.xyz.data[1], report.contents.xyz.data[2]))

ctx = osvrClientInit("com.osvr.exampleclients.TrackerCallback")

lefthand = osvrClientGetInterface(ctx, "/me/head")

C_PoseCallback = OSVR_PoseCallback(myTrackerCallback)

C_OrientationCallback = OSVR_OrientationCallback(myOrientationCallback)

C_PositionCallback = OSVR_PositionCallback(myPositionCallback)

osvrRegisterPoseCallback(lefthand, C_PoseCallback, None)

osvrRegisterOrientationCallback(lefthand, C_OrientationCallback, None)

osvrRegisterPositionCallback(lefthand, C_PositionCallback, None)

for i in range (0, 1000000):
    osvrClientUpdate(ctx)

osvrClientShutdown(ctx)

print("Library shut down, exiting.")