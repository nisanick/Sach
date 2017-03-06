import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
build_exe_options = {"packages": ["os"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "sach",
        version = "1.0",
        description = "Sach",
        options = {"build_exe": build_exe_options},
        executables = [Executable("hlavny.py", base=base)])