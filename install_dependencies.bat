@echo off

:check_pip
if exist "C:\Users\kimmy\AppData\Local\Programs\Python\Python313\Scripts\pip.exe" (
    pip install pillow
    pip install tkinter
    pip install configparser
    pip install threading

) else (
    echo PIP is not installed.
)