from sikuli import *

class Shortcuts(object):
    @classmethod
    def Copy(self):
        type('c', Key.CTRL)
        sleep(0.5)

    @classmethod
    def Paste(self):
        type('v', Key.CTRL)
        sleep(0.5)

    @classmethod
    def SelectAll(self):
        type('a', Key.CTRL)
        sleep(0.5)

    @classmethod
    def FocusAddressbar(self):
        type('d', Key.ALT)
        sleep(0.5)

    @classmethod
    def InvokeRunMenu(self):
        type('r', Key.WIN)
        sleep(0.5)

    @classmethod
    def InvokeContextMenu(self):
        type(Key.SPACE, Key.ALT)
        sleep(0.5)
