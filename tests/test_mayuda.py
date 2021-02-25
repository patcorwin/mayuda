import datetime
import os
import tempfile

from pytest import approx

from pymel.core import getAttr, newFile, openFile, polyCube, saveAs, sceneName

import mayuda


tempdir = tempfile.gettempdir() + '/mayatests'

if not os.path.exists(tempdir):
    os.makedirs(tempdir)

def getTempName():
    return tempdir + str(datetime.datetime.now()).replace(':', '_') + '.ma'


def test_fake():
    pass


""" &&& Not sure I need tests right now since I dogfood these constantly
def test_reopen():
    # given
    newFile(f=True)
    
    cube = polyCube()[0]
    cubeName = 'tester'
    cube.rename(cubeName)
    someNumber = 33.3
    cube.tx.set(someNumber)
    
    filename = getTempName()
    saveAs( filename )
    
    # when
    cube.tx.set(someNumber - 30)
    mayuda.reopen()

    # then
    assert getAttr(cubeName + '.tx') == approx(someNumber)
    

def test_loadFromClipboard():
    # given
    newFile(f=True)
    <some path into clipboard>
    
    # when
    mayuda.openFromClipboard()
    
    # then
    assert sceneName() == <some path>
    
    
def test_openFolder():
    # given
    openFile(<some path>, f=True)
    
    # when
    mayuda.openFolder()
    
    # then
    <can python find running processes?>
    assert 0
    
"""