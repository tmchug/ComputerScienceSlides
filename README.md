
[🚧 Hmmmm.. Seeing this?
click top-right image icons to hide the code]: #

<div>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/w.png">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/b.png">
    <img alt="Shows a black logo in light color mode and a white one in dark color mode." src="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png" width="80" height="80" align="center">
  </picture>
  
  <h3 align="center">Projects</h3>

  <p align="center">
    Below you can find all the slides / projects we completed as a team!
    <br />
  </p>
</div>

### 🧾- Notices

---

https://replit.com/join/ewiuhekewy-tmchug1
Information, tips, tricks...

This document was written by me, it's here for explaining why the 
windows dock may disappear and other functions linked within the 
programme. 

This document is also here to inform you about my:

` icon sources and colours.`
##

- ### Brief run-through:
 This code block bellow basically removes the taskbar ( lines 2, 3 )
, and increases the image DPI ( line 1 ), meaning you have a higher
gui quality rather than a very pixelated frame.

```
1   ctypes.windll.shcore.SetProcessDpiAwareness(True)
2   h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)
3   windll.user32.ShowWindow(h, 1)
   ```
This is done by importing,

```
import ctypes
from ctypes import windll
   ```

Finally,
the rest of the programme is using globals to connect
different functions with main_screen() and other windows.

##

- ### Some Bugs:
Only issue I have noticed is please install the
cutomtkinter package with 5.2.0 or later, since the
newer version works differently and the programme is
not optimised for this.


###

## 📁 - Sources

---

- ### Colour Schemes:

All the colours are found in the .py files most of them are used as hover or fg colours.

 ![#1B1B1B](https://via.placeholder.com/10/0a192f?text=+) `#1B1B1B` | Text colour

 ![#E4E3E2](https://via.placeholder.com/10/E4E3E2?text=+) `#E4E3E2` | Fg Colour-1 | used in all .py files

 ![#D7D7D7](https://via.placeholder.com/10/D7D7D7?text=+) `#D7D7D7` | Hover Colour-1 |

 ![#3d424c](https://via.placeholder.com/10/3d424c?text=+) `#3D424C` | Fg Colour-2 | found in game.py

 ![#424852](https://via.placeholder.com/10/424852?text=+) `#424852` | Hover Colour-2 |

---
- ### Icons:

I have used a series of icons found in:

`C:\Users\PycharmProjects\TkinterLogIn\icons`

However, all the icons in the folder are from Lucide-Icons

[![lucide-icons](https://img.shields.io/badge/-Lucide%20Icons%20-303236?logo=abletonlive&logoColor=white&logoWidth=20&style=flat-square)](https://lucide.dev/)

###

##  Flowchart Version

---

A flowchart copy of main.py, made in figma.

There will be a better version of the photo in the drive.

![App Screenshot](award.png)

