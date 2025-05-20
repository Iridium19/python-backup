# Datei: backup-github.ps1
cd "C:\Users\Justus\Desktop\Python"

# Datum/Zeit für Commit-Nachricht
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# Git-Befehle
git add .
git commit -m "Automatisches Backup: $timestamp" --allow-empty
git push origin main
