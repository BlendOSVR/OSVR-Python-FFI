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

ctx = osvrClientInit("com.osvr.exampleclients.TrackerState")

lefthand = osvrClientGetInterface(ctx, "/me/head")

for i in range (0, 1000000):
    osvrClientUpdate(ctx)
    if(i%100 == 0):
        try:
            state, timestamp = osvrGetPoseState(lefthand)
        except ReturnError:
            pass
        else:
            print("Got pose state: Position = (%f, %f, %f), orientation = (%f, %f, %f, %f)" % (state.translation.data[0], state.translation.data[1], state.translation.data[2], state.rotation.data[0], state.rotation.data[1], state.rotation.data[2], state.rotation.data[3]))
osvrClientShutdown(ctx)
print("Library shut down, exiting.")