git init
choice /t 5 /d n /m "press y to lock the message, n or 5s timeout to exit"
if errorlevel 2 goto eof
pause
:eof