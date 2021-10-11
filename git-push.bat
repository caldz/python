@echo off
set server=https://github.com/caldz/python
set branch=main
git push %server% %branch%
choice /t 5 /d n /m "press y to stay, timeout or n to exit"
if errorlevel 2 goto eof
pause
:eof