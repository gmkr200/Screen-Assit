# 🕵️‍♂️ macOS Stealth Overlay (Python + PyObjC)

A proof-of-concept overlay application that displays a floating UI  only visible to the local user  but  invisible during screen sharing  (Google Meet, Teams, etc.).  
Built for  educational purposes only  to understand macOS graphics stacks, transparency layers, and system-level visibility.

## 📦 Project Structure
screen-assit/
├── AppDelegate.swift          # (optional) Swift-based Metal overlay (experimental)
├── overlay_app.py            # ✅ Main PyObjC app that creates the stealth overlay window
├── setup.py                  # Py2app build configuration
├── dist/                     # Py2app bundled application
├── build/                    # Py2app build artifacts
├── venv/                     # Python virtual environment
```

## 🔧 Technologies & Packages Used

| Tool / Library     | Purpose |
|--------------------|---------|
|  Python 3.11     | Main language for building the app logic |
|  PyObjC          | Python ↔ macOS Cocoa bridge (UIKit, NSWindow, etc.) |
|  AppKit (Cocoa)  | Used to create windows, views, text fields, layering |
|  CALayer         | Lightweight GPU-backed background layer, simulating Metal |
|  py2app          | Bundle the Python app as a `.app` for macOS execution |
|  Swift (optional) | Used to experiment with Metal-backed invisible overlays |

## 🧠 What the App Does

- Creates a  transparent NSPanel  that floats over all other apps (including fullscreen).
- Sets  collection behaviors  and  sharing settings  to  avoid being captured  during screen sharing.
- Uses  CALayer  instead of Metal for simplicity — retains GPU-acceleration and invisibility tricks.
- Adds static  dummy UI elements  (like labels) for testing content injection.
- Runs in  stealth mode  — no dock icon, non-interruptive, lightweight.

## 🔐 System Permissions

To run this invisibly and explore screen-sharing avoidance:

### ✅ Required:

1.  Disable SIP (System Integrity Protection)   
   _⚠️ Advanced — only for local development/experimentation_  
   Reboot into  macOS Recovery , then run:

   ```bash
   csrutil disable
   ```

2.  Allow Accessibility (optional)   
   If you plan to simulate keyboard/mouse automation.

3.  Grant Screen Recording (optional)   
   Only if debugging or testing what the app looks like via screen capture.

## 🚀 How to Run

1.  Create virtual environment   
   ```bash
   python3 -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   ```

2.  Run manually for testing   
   ```bash
   python3 overlay_app.py
   ```

3.  Build .app for full behavior   
   ```bash
   python3 setup.py py2app
   ./dist/PrivateOverlay.app/Contents/MacOS/PrivateOverlay
   ```

## 🔍 How It Avoids Screen Sharing

- `NSPanel` used instead of `NSWindow` (less likely to be mirrored)
- `setSharingType(NSWindowSharingNone)` used
- `NSWindowCollectionBehaviorCanJoinAllSpaces | Transient | IgnoresCycle` to detach from window list
- `NSScreenSaverWindowLevel` puts it on top of all normal windows
- Uses `CALayer` with `alpha < 1` to avoid screen compositing in screen sharing APIs

## 🧪 Status

✅ Window renders correctly  
✅ Tested on Google Meet and Teams screen sharing  
🟡 Still refining dynamic input/data injection  
🟢 Next up: Add interaction (AI tips, Copilot, timer...)

## ⚠️ Disclaimer

This app is for  educational and ethical exploration only.   
Do not use this to mislead, cheat, or manipulate online interviews or meetings. Respect the integrity of digital spaces.

## 📬 Contact

Built by:  Manikumar Reddy Gajjela   
For questions, drop a message here or contribute ideas in issues!
