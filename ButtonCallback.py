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

def myButtonCallback(userdata, timestamp, report):
    print("Got Report: button is %s" % (report.contents.state))

ctx = osvrClientInit("com.osvr.exampleclients.ButtonCallback")

button1 = osvrClientGetInterface(ctx, "/controller/left/1")

C_ButtonCallback = OSVR_ButtonCallback(myButtonCallback)

osvrRegisterButtonCallback(button1, C_ButtonCallback, None)

for i in range (0, 1000000):
    osvrClientUpdate(ctx)

osvrClientShutdown(ctx)
print("Library shut down, exiting.")