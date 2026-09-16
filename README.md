# 🖐️ Hand Frame FX — Setup Guide for Beginners

Hey! 👋 This guide will help you set up a fun webcam app on your computer.
Here's what it does: you hold up both hands like you're framing a photo
with your fingers, and a cool visual effect (comic book, glass, neon,
Spider-Man-style hero suit, and more!) shows up **inside the shape your
fingers make** — live, over your webcam video.

No coding experience needed. Just follow the steps below **in order**,
one at a time. If something doesn't look right, don't panic — just
re-read the step, or ask whoever sent you this guide for help.

---

## 📁 Step 0: What you should have

You should have a Google Drive folder with these 3 files in it:

- `handy_eff.py` — the main app
- `requirements.txt` — a shopping list of tools the app needs
- `make_contact_sheet (1).py` — a bonus tool that shows you all the effects in one image, without needing a webcam

Keep reading — we'll download these in a bit.

---

## 🧩 Step 1: Install Python

Python is the "engine" that runs this app. Your computer probably
doesn't have the right version yet, so let's install it.

1. Go to this link: **https://www.python.org/downloads/release/python-3119/**
2. Scroll down to the section called **"Files"**
3. Click **"Windows installer (64-bit)"** to download it
4. Open the downloaded file to start installing
5. ⚠️ **VERY IMPORTANT:** On the very first screen of the installer,
   check the box that says **"Add python.exe to PATH"** — don't skip this!
6. Click **Install Now** and let it finish

### Check it worked
1. Open the **Start Menu**, type `cmd`, and open **Command Prompt**
   (this is a black typing window — don't worry, it's not scary!)
2. Type this and press **Enter**:
   ```
   py -3.11 --version
   ```
3. It should show something like `Python 3.11.9`. If it does, great — move on!

---

## 📂 Step 2: Make a project folder and download your files

1. On your Desktop, create a new folder and name it `handy_eff`
2. Open the Google Drive folder you were given
3. Download all 3 files (`handy_eff.py`, `requirements.txt`,
   `make_contact_sheet (1).py`) into that `handy_eff` folder on your Desktop

### Rename one file (important!)
The file `make_contact_sheet (1).py` has spaces and parentheses in its
name, which can confuse the computer. Rename it to remove them:

1. Right-click `make_contact_sheet (1).py`
2. Click **Rename**
3. Change it to exactly: `make_contact_sheet.py`
4. Press Enter

Your folder should now have exactly:
```
handy_eff/
├── handy_eff.py
├── requirements.txt
└── make_contact_sheet.py
```

---

## 💻 Step 3: Open the Command Prompt in that folder

1. Open your `handy_eff` folder in File Explorer
2. Click on the address bar at the top (where the folder path is shown)
3. Type `cmd` and press **Enter** — this opens a Command Prompt already
   pointed at your folder (no typing paths needed!)

You should see a black window with something like:
```
C:\Users\YourName\Desktop\handy_eff>
```

---

## 🧪 Step 4: Create a safe "container" for this project

This keeps the app's tools separate from everything else on your PC,
so nothing gets messed up.

Type this and press Enter:
```
py -3.11 -m venv venv
```
Wait a few seconds. It will create a new folder called `venv` — that's normal.

### Turn the container on
Type:
```
venv\Scripts\activate
```
✅ If it worked, you'll see `(venv)` appear at the start of the line, like:
```
(venv) C:\Users\YourName\Desktop\handy_eff>
```

> ⚠️ **Remember this:** every time you close and reopen Command Prompt to
> use this app later, you'll need to redo this step (`venv\Scripts\activate`)
> before running anything. It only takes 2 seconds.

---

## 📦 Step 5: Install the app's tools

With `(venv)` showing at the start of your line, type:
```
pip install -r requirements.txt
```
Press Enter and wait — this downloads everything the app needs
(usually takes 1-3 minutes). You'll see a bunch of text scroll by —
that's normal, just let it finish.

---

## ▶️ Step 6: Run the app!

Type:
```
py handy_eff.py
```

A window should pop up showing your webcam! 🎥

### Try it out:
- Hold up **both hands** and make an "L" shape or frame shape with your
  thumb + pointer finger on each hand — you'll see an effect appear
  inside the shape!
- Press **Spacebar** — switches to the next effect
- Press **`r`** — starts/stops recording a video of what you see
  (it saves automatically in your `handy_eff` folder)
- Press **`l`** — shows little dots/lines tracking your hand (fun to see how it works!)
- Press **`q`** — quits the app safely

**Bonus trick:** bring your two hands close together (like clapping,
but not quite touching) and it'll automatically switch to the next
effect too — no need to press spacebar!

---

## 🖼️ Bonus: See all the effects at once (no webcam needed)

Want to preview every single effect without opening your camera? Run:
```
py make_contact_sheet.py
```
This creates a picture called `effects_contact_sheet.png` right in your
`handy_eff` folder — open it to see every effect side-by-side!

---

## 🔁 Quick recap — every time you want to use the app again:

1. Open your `handy_eff` folder
2. Click the address bar, type `cmd`, press Enter
3. Type: `venv\Scripts\activate`
4. Type: `py handy_eff.py`

That's it! 🎉

---

## 🆘 Something went wrong?

- **"Python was not found"** → Windows might redirect `python` to the
  Microsoft Store by mistake. Use `py` instead of `python` in every command.
- **A red error message appears** → Don't worry! Copy the *entire* error
  message (not just the last line) and send it to whoever gave you this
  guide — it usually takes just one small fix.
- **The webcam window won't open** → Make sure no other app (Zoom,
  Teams, FaceTime, etc.) is currently using your camera. Close those first.
- **`requirements.txt` not found** → You're probably not in the right
  folder. Make sure you did Step 3 correctly (opening Command Prompt
  *from inside* the `handy_eff` folder).

Have fun! 🕸️✨
