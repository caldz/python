@echo off
REM set server=https://github.com/caldz/python
REM set branch=main
REM git push %server% %branch%
git push origin main
choice /t 5 /d n /m "press y to stay, timeout or n to exit"
if errorlevel 2 goto eof
pause
:eof