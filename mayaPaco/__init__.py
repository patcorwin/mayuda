from __future__ import print_function
import os
import sys
import traceback

from pymel.core import *

import inspect


class FullReload(object):

    @staticmethod
    def cleanpath(path):
        return os.path.normcase( os.path.normpath(path) )

    def __call__(self, top):
        
        self.reloaded = set()
        self.src_path = os.path.dirname( self.cleanpath(top.__file__) )
        
        self.reload_module(top)
        print('done', len(self.reloaded))

    def reload_module(self, top):
        self.reloaded.add(top.__file__)
        for name in dir(top):
            sub = getattr(top, name)
            if inspect.ismodule( sub ):
                if hasattr(sub, '__file__') and sub.__file__ not in self.reloaded:
                    try:
                        if self.cleanpath(sub.__file__).startswith( self.src_path ):
                            self.reload_module(sub)
                    except AttributeError:
                        raise
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


scriptJob( e=("SelectionChanged", alwaysSelected) )