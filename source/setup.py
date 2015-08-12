from distutils.core import setup, Extension

# Change these to point to the right locations
clIncludeDir = "/opt/AMDAPP/SDK/include/"
clLibDir = "/usr/lib/"

extension_mod = Extension(name="_htfe", sources=["HTFE.i", "system/ComputeSystem.cpp", "system/ComputeProgram.cpp", "htfe/HTFE.cpp"], swig_opts=["-c++"], extra_compile_args=['-std=c++11'], language=["c++"], include_dirs=[clIncludeDir, "./"], library_dirs=[clLibDir], libraries=["OpenCL"])

setup(name = "htfe", version="1.0", ext_modules=[extension_mod], package_data={"htfe": ["../resources/*.cl"]})
