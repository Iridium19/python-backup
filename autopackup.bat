@echo off
cd /d "C:\Users\Justus\Desktop\Python"

REM Aktuelles Datum und Uhrzeit im Format "yyyy-MM-dd HH:mm:ss"
for /f "tokens=1-3 delims=/- " %%a in ("%date%") do (
    set year=%%c
    set month=%%a
    set day=%%b
)
for /f "tokens=1-2 delims=: " %%a in ("%time%") do (
    set hour=%%a
    set minute=%%b
)
set timestamp=%year%-%month%-%day% %hour%:%minute%

REM Git-Befehle
git add .
git commit -m "Automatisches Backup: %timestamp%" --allow-empty
git push origin main
