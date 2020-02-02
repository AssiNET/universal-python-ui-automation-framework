from sikuli import *
from _uimap import *
from shortcuts import *

import os
import datetime
import logging
logging.basicConfig(format='%(message)s',level=logging.INFO)

class Browser(object):
    @classmethod
    def Start(self, url):
        Shortcuts.InvokeRunMenu()
        type("chrome " + url)
        type(Key.ENTER)
        wait(Browser_UI.button_Refresh, 5)

    @classmethod
    def Maximize(self):
        Reporting.TestLog("Maximize Browser")
        Shortcuts.InvokeContextMenu()
        type('x')

    @classmethod
    def OpenNewTab(self):
        type('t', Key.CTRL)

    @classmethod
    def OpenURL(self, url):
        Shortcuts.FocusAddressbar()
        paste(url)
        type(Key.ENTER)

class UIActions(object):
    @classmethod
    def GetClipboard():
        return Env.getClipboard()

    @classmethod
    def CopyAllClipboard(self):
        Shortcuts.SelectAll()
        sleep(1)
        Shortcuts.Copy()
        return Env.getClipboard()

    @classmethod
    def ClearClipboard():
        from java.awt.datatransfer import StringSelection
        from java.awt import Toolkit
        toolkit = Toolkit.getDefaultToolkit()
        clipboard = toolkit.getSystemClipboard()
        clipboard.setContents(StringSelection(""), None)

    @classmethod
    def MaximizeWindow(self):
        Shortcuts.InvokeContextMenu()
        sleep(0.5)
        type('x')

class Network(object):
    @classmethod
    def DownloadFile(self, download_url, destination):
        try:
            if os.path.exists(destination):
                os.remove(destination)

            urllib.urlretrieve(download_url, destination)
        except Exception as ex:
            print("Download failed!")
            print("Exception: " + str(ex))

class String(object):
    @classmethod
    def RemoveNonASCIIchar(self, text):
        '''Removes chars>128'''
        if isinstance(text, (int, long)):
            text = str(text)
        return "".join(i for i in text if ord(i) < 128)

class Reporting(object):
    @classmethod
    def TestLog(self, message):
        '''Print info in the Report.html, Console and Jenkins output'''
        label_timestamp = "[" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S] TEST_LOG: ')

        # print in console and Jenkins
        message_console_jenkins = str(label_timestamp) + str(message)
        logging.info(message_console_jenkins)
        
        # print in Report.html
        message_report_html = str(label_timestamp) + String.RemoveNonASCIIchar(message)
        print(message_report_html)
