#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

from shortcuter import Shortcuter


class MainWindow (wx.Frame):
    """Главное окно программы"""
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        super (MainWindow, self).__init__(*args, **kwds)

        DEFAULT_WIDTH = 600
        DEFAULT_HEIGHT = 500

        self.SetSize ((DEFAULT_WIDTH, DEFAULT_HEIGHT))
        self.Centre()

        self._sizer = wx.BoxSizer ()

        self._createMenu ()
        self._createCheckButton ()

        self.SetSizer (self._sizer)
        self.Layout()

        # !!! Добавление шорткатов, которые не были расставлены вручную
        Shortcuter (self.menubar).assignShortcuts()


    def _createMenu (self):
        self.menubar = wx.MenuBar()

        menu1 = wx.Menu()
        menu1.Append (wx.NewId(), u"&Бла-бла-бла 1\tCtrl+O")
        menu1.Append (wx.NewId(), u"Bla-bla-bla 2\tCtrl+P")
        menu1.Append (wx.NewId(), u"Бла-бла-бла 3")
        menu1.Append (wx.NewId(), u"Б&ла-бла-бла 4")
        menu1.Append (wx.NewId(), u"Бла-бла-бла 5")
        self.menubar.Append (menu1, u"Заголовок меню 1")

        menu2 = wx.Menu()
        menu2.Append (wx.NewId(), u"Бла-бла-бла 1")
        menu2.Append (wx.NewId(), u"Бла-бла-бла 2")
        menu2.Append (wx.NewId(), u"Бла-бла-бла 3")
        menu2.Append (wx.NewId(), u"Бла-бла-бла 4")
        self.menubar.Append (menu2, u"&Заголовок меню 2")

        menu3 = wx.Menu()
        menu3.Append (wx.NewId(), u"Бла-бла-бла 1")
        menu3.Append (wx.NewId(), u"Бла-бла-бла 2")
        menu3.Append (wx.NewId(), u"Бла-бла-бла 3")
        menu3.Append (wx.NewId(), u"Бла-бла-бла 4")

        submenu1 = wx.Menu ()
        submenu1.Append (wx.NewId(), u"Подменю 1")
        submenu1.Append (wx.NewId(), u"&Подменю 2")
        submenu1.Append (wx.NewId(), u"&Подменю 3")
        submenu1.Append (wx.NewId(), u"&Подменю 4")

        submenu2 = wx.Menu ()
        submenu2.Append (wx.NewId(), u"&Подменю 1")
        submenu2.Append (wx.NewId(), u"П одменю 2")
        submenu2.Append (wx.NewId(), u"Подменю 3")
        submenu2.Append (wx.NewId(), u"Подменю 4")
        submenu1.AppendSubMenu (submenu2, u"Абырвалг")

        menu3.AppendSubMenu (submenu1, u"Абырвалг")

        self.menubar.Append (menu3, u"Заголовок меню 3")

        self.SetMenuBar (self.menubar)


    def _createCheckButton (self):
        """
        Добавить кнопку для проверки повторения шорткатов
        """
        checkDublicateBtn = wx.Button (self, label = u"Проверить дубликаты шорткатов")
        checkDublicateBtn.SetMinSize ((300, -1))
        checkDublicateBtn.Bind (wx.EVT_BUTTON, self._onCheckDublicate)

        self._sizer.Add (checkDublicateBtn)


    def _onCheckDublicate (self, event):
        dublicates = Shortcuter (self.menubar).checkDublicates()

        if len (dublicates) == 0:
            message = u"Повторяющихся шорткатов не обнаружено"
        else:
            message = u"Список повторяющихся шорткатов:\n\t" + u"\n\t".join (dublicates)

        wx.MessageBox (message)
