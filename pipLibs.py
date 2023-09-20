import sys
import subprocess

# install library for the gui
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PySimpleGui'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])