# mayuda
Maya + Ayuda (Spanish for "help")
Random tools to make Maya easier to script and use

* Always `from pymel.core import *` for easy pymel access
* Import `os` and `sys` for easy access
* `fullReload(<module name>)` helper to reload a module and all of it's imported submodules
* Helper variables `o`, `o2` .. `o4` to track global selection
* `openFromClipboard` will open the file in your clipboard
* `openFolder` opens the folder of the currently open file
* `reopenFile` reopens the file (doesn't prompt to save)