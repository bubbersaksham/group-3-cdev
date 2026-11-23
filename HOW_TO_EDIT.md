# How to open and edit this website

You don't need to install anything to view the site. To edit it, you need a free text editor.

---

## 1. Unzip the folder

- **Mac:** double-click the zip file.
- **Windows:** right-click the zip file → **Extract All** → **Extract**.

You'll get a folder called something like `nsw-rugby-legacy-dashboard-main`. Do all your work inside this folder, and keep the files together. The website needs all of them.

## 2. Open the website

Double-click **`index.html`**. It opens in your web browser (Chrome works best).

That's the whole website. Click through the menu on the left to see each page.

> Need internet for: fonts and the event QR codes. Everything else works offline.

## 3. Install an editor (one time only)

Download **Visual Studio Code**, which is free: https://code.visualstudio.com

Then open it, choose **File → Open Folder…**, and select the unzipped folder. All the files appear in the list on the left.

## 4. Make a change

1. Click a file on the left to open it.
2. Press **Ctrl+F** (Windows) or **Cmd+F** (Mac) to find the text you want to change.
3. Type your change.
4. Save with **Ctrl+S** or **Cmd+S**.
5. Go back to the browser and **refresh the page** to see the change.

If something breaks, press **Ctrl+Z** or **Cmd+Z** in the editor to undo, save, and refresh again.

## 5. Which file to edit

| I want to change… | Open this file | Tip |
|---|---|---|
| Words, headings, buttons, menu items | `index.html` | Search for the exact words you see on the page |
| Colours, fonts, spacing | `styles.css` | Colours are listed near the top. Search for `--red:` or `--navy:` |
| The banner photo | `images/hero.jpg` | Replace it with your own photo, using the **same file name** |
| Costs, participant numbers, model assumptions | `model-data.js` | Numbers come from the Excel workbook. Change only the numbers, and keep the commas and quote marks |
| How the calculator or forms work | `app.js` | For people comfortable with JavaScript |
| The printable QR poster tool | `QR_SETUP.html` | Opens on its own. Paste in a Google Form link to make a QR poster |

**Don't edit `STANDALONE_WEBSITE.html`.** It's an automatic one-file copy of the site. After editing the files above, you can rebuild it by running `python3 scripts/build_standalone.py` in a terminal opened in the folder.

## 6. Good to know

- **Data you type into the website stays on your computer.** Activity logs, events and check-ins are saved in your browser only, so other people can't see them. To share them, go to **Reports → Export all data JSON** and send the file. The other person loads it with **Import workspace**.
- **Clearing your browser history may delete that data,** so export it first.
- **Want to put your edited version online?** Drag the whole folder onto https://app.netlify.com/drop to get a free web link in seconds.

---

More technical detail (file structure, model, deployment) is in `README.md`.
