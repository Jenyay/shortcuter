#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

from smartmenubar.smartmenubar import SmartMenuBar


class MainWindow (wx.Frame):
    """Главное окно программы"""
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        super (MainWindow, self).__init__(*args, **kwds)

        DEFAULT_WIDTH = 600
        DEFAULT_HEIGHT = 500

        self.SetSize ((DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.Centre()

        self._createMenu ()

        try:
            self.menubar.assignShortcuts()
        except ValueError as e:
            print repr (e)

        self.menubar.UpdateMenus()
        self.Update()


    def _createMenu (self):
        self.menubar = SmartMenuBar()

        menu1 = wx.Menu()
        menu1.Append (wx.NewId(), u"&Бла-бла-бла 1\tCtrl+O")
        menu1.Append (wx.NewId(), u"Бла-бла-бла 2")
        menu1.Append (wx.NewId(), u"Бла-бла-бла 3")
        menu1.Append (wx.NewId(), u"Бла-бла-бла 4")
        self.menubar.Append (menu1, u"Пункт меню 1")

        menu2 = wx.Menu()
        menu2.Append (wx.NewId(), u"Бла-бла-бла 1")
        menu2.Append (wx.NewId(), u"Бла-бла-бла 2")
        menu2.Append (wx.NewId(), u"Бла-бла-бла 3")
        menu2.Append (wx.NewId(), u"Бла-бла-бла 4")
        self.menubar.Append (menu2, u"Пункт меню 2")

        menu3 = wx.Menu()
        menu3.Append (wx.NewId(), u"Бла-бла-бла 1")
        menu3.Append (wx.NewId(), u"Бла-бла-бла 2")
        menu3.Append (wx.NewId(), u"Бла-бла-бла 3")
        menu3.Append (wx.NewId(), u"Бла-бла-бла 4")
        self.menubar.Append (menu3, u"Пункт меню 3")

        self.SetMenuBar (self.menubar)
