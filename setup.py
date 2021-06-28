import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['GSLogo.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="GSLogo.ico"
)

# SETUP CX FREEZE
setup(
    name = "Globalstratos Main UI",
    version = "1.0",
    description = "Frontend control system for data processing",
    author = "Ryan Blumenow",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
