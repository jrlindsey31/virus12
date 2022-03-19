import os

os.startfile("C:\Windows\System32\cmd.exe") # Open any program, text or office document

import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\rick\Desktop\c\backgrounds.jpg" , 0)