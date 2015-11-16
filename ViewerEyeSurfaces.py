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

ctx = osvrClientInit("com.osvr.example.ViewerEyeSurfaces")

while True:
    print("Trying to get the display config")
    osvrClientUpdate(ctx)
    try:
        display = osvrClientGetDisplay(ctx)
    except ReturnError:
        continue
    else:
        break

viewers = osvrClientGetNumViewers(display)

for viewer in range(0, viewers.value):
    print("Viewer %d" % (viewer))
    eyes = osvrClientGetNumEyesForViewer(display, viewer)

    for eye in range(0, eyes.value):
        print("\tEye %d" % (eye))
        surfaces = osvrClientGetNumSurfacesForViewerEye(display, viewer, eye)

        for surface in range(0, surfaces.value):
            print("\t\tSurface %d" %(surface))

osvrClientFreeDisplay(display)

osvrClientShutdown(ctx)
print("Library shut down, exiting")