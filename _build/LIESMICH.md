# Bau-Skript der Website

Alle Seiten im Hauptordner werden aus diesen Dateien erzeugt:

    python3 _build/build.py . /tmp/vorschau

- `landing_main.html`: Inhalt der Startseite
- `prices.js`: Ankaufpreise (bestätigt 10.11.2026)
- `datenschutz.html`: Text der Datenschutzerklärung
- `glass.css`: Glas-Optik wie die Turnierseite (Kopfzeile, Karten, Knöpfe, Farbflächen), wird an das CSS aller Ankaufseiten angehängt
- `build.py`: Unterseiten (Ankauf, Danke, Versand, Ablauf, Impressum, Datenschutz) und gemeinsames Design

Schriften liegen in `fonts/` (SIL Open Font License). Ordner mit `_` am Anfang veröffentlicht GitHub Pages nicht.
