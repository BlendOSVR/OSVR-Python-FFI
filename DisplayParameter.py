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

ctx = osvrClientInit("com.osvr.exampleclients.DisplayParameter")

path = "/display"

length = osvrClientGetStringParameterLength(ctx, path)

displayDescription = osvrClientGetStringParameter(ctx, path, length)

print("Got value of %s: \n%s" % (path, displayDescription))

osvrClientShutdown(ctx)
print("Library shut down, exiting.")