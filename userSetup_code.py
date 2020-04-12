
from pymel.core import *

try:
    # I always want os and sys accessible
    import os # noqa
    import sys # noqa
    
    # Bring in fullReload to easily reload modules
    from mayaPaco import fullReload, alwaysSelected # noqa
    
    # Track the selection, `o = selected()[0], o2 = selected()[1]` for the first 5 objects.
    scriptJob( e=("SelectionChanged", alwaysSelected) )
    
except Exception:
    import traceback
    print( traceback.format_exc() )
    warning('An error occurred in mayaPaco use')