import csv

# Dateiname der CSV-Datei
dateiname = r'C:\Users\Justus\Desktop\IR\B1.csv'

# Öffne die CSV-Datei zum Lesen
with open(dateiname, mode='r', newline='', encoding='utf-8') as infile:
    # Lese den Inhalt der Datei
    inhalt = infile.read()

# Ersetze alle Kommas mit Leerzeichen
inhalt = inhalt.replace(';', '\t')

# Öffne die CSV-Datei zum Schreiben (überschreiben)
with open(dateiname, mode='w', newline='', encoding='utf-8') as outfile:
    # Schreibe den bearbeiteten Inhalt zurück in die Datei
    outfile.write(inhalt)

print(f"Alle Kommas in der Datei '{dateiname}' wurden durch Leerzeichen ersetzt.")
