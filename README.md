# pyIDE

A lightweight, cross-platform Python IDE built with Tkinter. pyIDE (python-ide) is a minimal graphical code editor that lets you write and run Python (and other) files from a simple GUI.


## Features

- Simple text editor with open / save / save-as functionality
- Run Python (.py), javascript (.js), Windows batch (.bat) files, or open HTML files in the default browser
- Separate output pane to show program stdout/stderr
- Toggleable dark / light mode


## Requirements

- Python 3.7+
- Node.js if you want to run `.js` files from the app



When you run a file, the app determines the command based on its extension:

- `.py` — runs with the `python` command
- `.js` — runs with the `node` command (requires Node.js installed)
- `.bat` — executed via `cmd /c` on Windows
- `.html` — opened in the default web browser

Program stdout and stderr are displayed in the output pane.

