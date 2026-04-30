# exam-rfp-cc1
Exam project for the RFP: Strengthening Education Continuity in Conflict-Affected Regions - Master ICT4D (2026)

## Haiti Border Map
A simple, interactive Leaflet map showing the administrative borders of Haiti.

## How to update the data
If you want to refresh the border data from OpenStreetMap, run:
```bash
python3 fetch_haiti.py
```

## How to view the map
Simply open `index.html` in your web browser.

## Project Structure
- `index.html`: The main web page (Leaflet map).
- `fetch_haiti.py`: Python script to download data from OpenStreetMap.
- `haiti_border.geojson`: The geographic data file.
