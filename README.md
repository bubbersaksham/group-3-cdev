# NSW Rugby Union — RWC 2027 Legacy Dashboard

A front-end prototype for measuring the impact of NSW Rugby Union's Rugby World Cup 2027 legacy programs (Pillar 2: Western Sydney and Hunter; Pillar 5: RWC Activation).

It has five sections:
- **Overview**: portfolio KPIs and recorded activity
- **Log activity**: record attendance, sign-ups, new coaches, referees and volunteers
- **Events & QR**: create event codes and check-in QR codes
- **Impact calculator**: social benefit and benefit–cost ratio by program and scenario
- **Reports**: CSV and JSON exports, plus importing a saved workspace

## Run it

No build step and no install. Either:
- open `index.html` in Chrome, or
- serve the folder locally, e.g. `python3 -m http.server 8000`, then visit http://localhost:8000

## Files

| File | Purpose |
|---|---|
| `index.html` | Page structure |
| `styles.css` | Visual design and responsive layout |
| `images/hero.jpg` | Banner photo used on the Overview and Reports pages |
| `model-data.js` | Model inputs and defaults, taken from *Excel Prototype NSW RUGBY (3).xlsx* |
| `app.js` | Calculations, forms, exports and the QR check-in flow |
| `QR_SETUP.html` | Standalone tool that turns a Google Form link into a printable event QR poster |
| `STANDALONE_WEBSITE.html` | Earlier all-in-one version of the site for offline use. It is **not** kept in sync with the source files above, so edit those instead |

## Updating the model

The calculator's defaults live in `model-data.js` (the `WORKBOOK` object, keyed by spreadsheet cell, e.g. `p5.C25`). To update assumptions, change the values there or override them in the website's Impact calculator. Overrides are saved in the browser.

## Data storage: important

This is a prototype with **no backend**. Everything entered (activity logs, events, check-ins, calculator overrides) is stored in the browser's `localStorage` on that device only. It is not shared between users or devices.
- Use **Reports → Export all data JSON** to back up or share a workspace, and **Import workspace** to restore it.
- QR check-ins in the app are saved on the device that scans the code. To collect responses from attendees, use `QR_SETUP.html` with a Google Form.
- For shared, multi-device data, connect a backend or database (e.g. Supabase or Firebase).

## Deploy

It's a static site, so any static host works:
- **Vercel / Netlify**: import this repository; no build command; output directory is the repository root.
- **GitHub Pages**: Settings → Pages → deploy from the `main` branch, root folder.

## Editing

Open the folder in VS Code, edit the HTML, CSS or JS, and refresh the browser to see changes.
