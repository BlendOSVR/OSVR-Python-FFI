# OSVR-Python-FFI
> Maintained at <https://github.com/BlendOSVR/OSVR-Blender>
>
> For details, see <http://osvr.github.io>
>
> For support, see <http://support.osvr.com>

##FFI layer for OSVR ClientKit
This repository contains basic python code which allows access to the C API of OSVR from python.  This is a simple wrapper, and does not modify the structure of the API (i.e. it does not create objects or assign methods to them, it is the same collection of functions and structures used by the C API), with the exception that in many cases return values from functions are not placed in pointers passed as parameters, but as tuples or single values, as is expected from Python.

## License
This project: Licensed under the Apache License, Version 2.0.
