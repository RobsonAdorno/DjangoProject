import os
from sys import platform

version_python = os.system('python3 --version')

if version_python != 0:
    decision = input('Gostaria de instalar?[S/N]').strip()
    decision = decision.lower()

def verify_system_operational():
    if platform == "win32":
        pass