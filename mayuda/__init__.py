from __future__ import absolute_import, division, print_function

import inspect
import os
import subprocess
import sys
import traceback

try: # python3 prep
    reload
except NameError:
    from importlib import reload
    
from PySide2 import QtGui

from pymel.core import mel, openFile, Path, sceneName, selected, warning


class FullReload(object):

    @staticmethod
    def cleanpath(path):
        return os.path.normcase( os.path.normpath(path) )

    def __call__(self, top, printLog=False):
        
        self.reloaded = set()
        self.src_path = os.path.dirname( self.cleanpath(top.__file__) )
        
        self.reload_module(top, printLog)
        print('done', len(self.reloaded))

    def reload_module(self, top, printLog):
        self.reloaded.add(top.__file__)
        for name in dir(top):
            sub = getattr(top, name)
            if inspect.ismodule( sub ):
                if hasattr(sub, '__file__') and sub.__file__ not in self.reloaded:
                    try:
                        if self.cleanpath(sub.__file__).startswith( self.src_path ):
                            self.reload_module(sub, printLog)
                    except AttributeError:
                        raise
        if printLog:
            print('About to reload', top)
        reload(top)


fullReload = FullReload()


def alwaysSelected():
    '''
    This always puts the current selection into "o"
    '''
    try:
        sel = selected()
        if sel:
            setattr(sys.modules['__main__'], 'o', sel[0] )
            
            for i, obj in enumerate(sel[1:5], 2):
                setattr(sys.modules['__main__'], 'o%i' % i, sel[i - 1] )
    except Exception:
        print( traceback.format_exc() )


def reopen():
    openFile( sceneName(), f=1 )
    
    
if 'filepathProcessors' not in globals():
    filepathProcessors = []
    
    
def openFromClipboard():
    
    global filepathProcessors
    
    filepath = Path(QtGui.QClipboard().text().strip())
    
    # Strip out quotes (windows adds them when copying a filepath from explorer)
    if filepath.startswith(('"', "'")):
        filepath = filepath[1:]
    if filepath.endsswith(('"', "'")):
        filepath = filepath[:-1]
    
    filepath = os.path.expandvars( os.path.expanduser(filepath) )
    
    
    if not os.path.exists(filepath):
        
        for processor in filepathProcessors:
            path = processor(filepath)
            if path and os.path.exists(path):
                filepath = path
                break
        else:
            warning(filepath + ' does not exist')
            return
        
    fileType = ''
    if filepath.ext.lower() == '.mb':
        fileType = 'mayaBinary'
    if filepath.ext.lower() == '.ma':
        fileType = 'mayaAscii'
    
    mel.addRecentFile(filepath.cannonicalPath(), fileType)

    openFile( filepath, f=True )
    
    
def openFolder():
    
    filename = sceneName()
    if not filename:
        return
    
    subprocess.call( ['explorer', filename.dirname().replace('/', '\\')] )