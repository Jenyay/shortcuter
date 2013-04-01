#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import os.path
import sys

import wxversion

try:
    wxversion.select("2.8")
except wxversion.VersionError:
    if os.name == "nt":
        pass
    else:
        raise

import wx


class ExampleApp (wx.App):
    def __init__(self, *args, **kwds):
        wx.App.__init__ (self, *args, **kwds)


    def OnInit(self):
        from mainwindow import MainWindow

        wx.InitAllImageHandlers()
        self.mainWnd = MainWindow(None, -1, u"SmartMenuBar Example")
        self.mainWnd.Show()
        self.SetTopWindow (self.mainWnd)

        return True


# end of class OutWiker

if __name__ == "__main__":
    example = ExampleApp (False)
    example.MainLoop()
