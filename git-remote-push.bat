git push -u origin main
choice /t 5 /d n /m "press y to stay, timeout or n to exit"
if errorlevel 2 goto eof
pause
:eof