from __future__ import print_function
import traceback

from pymel.core import *

try:
    # Make os and sys accessible
    import os # noqa
    import sys # noqa
    
    # Bring in fullReload to easily reload modules
    from mayuda import fullReload, alwaysSelected # noqa
    
    # Track the selection, `o = selected()[0], o2 = selected()[1]` for the first 5 objects.
    scriptJob( e=("SelectionChanged", alwaysSelected) )
    
except Exception:
    print( traceback.format_exc() )
    warning('An error occurred in mayuda use')