#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx


class SmartMenuBar (wx.MenuBar):
    """Меню с автоматической расстановкой подчеркиваний"""
    def __init__(self, style=0):
        super(SmartMenuBar , self).__init__(style)


    def assignShortcuts (self):
        """
        Расставить клашишные сокращения (подчеркнутые буквы) для доступа к меню (с использованием комбинаций, Alt+...)
        Метод проходится по всем меню и расставляет подчеркивания там, где их еще нет. Заодно проверяет, чтобы у двух разных пунктов меню не было одних и тех же клавиатурных сокращений

        Метод бросает исключение ValueError, если находит совпадение двух клавишных сокращений
        """
        # Проверить сокращения для заголовков меню первого уровня
        self._assignMenuShortcuts (self)

        menus = self.GetMenus()
        newmenus = [(menu, menu.GetTitle().replace (u"_", u"&")) for menu, _ in menus]
        self.SetMenus (newmenus)
        self.UpdateMenus()


    def Append (self, menu, title):
        menu.SetTitle (title)
        wx.MenuBar.Append (self, menu, title)


    def _assignMenuShortcuts (self, menu):
        """
        Проверить и применить клавишные сокращения для одного меню
        Метод бросает исключение ValueError, если находит совпадение двух клавишных сокращений
        """
        # Ключ - буква, клавиатурного сокращения (подчеркнутая буква, буква перед которой стоит &)
        # Значение - название пункта меню.
        shortcuts = {}

        for menuitem in self._getMenuItems (menu):
            title = self._getText (menuitem)
            shortcut = self._extractShortcut (title)
            # print title

            if shortcut in shortcuts:
                raise ValueError (u'Совпадение клавиатурных сокращений у пунктов меню "{0}" и {1}'.format (shortcuts[shortcut], title))

            if len (shortcut) != 0:
                shortcuts[shortcut] = title
            else:
                newtitle, newshortcut = self._findNewShortcut (title, shortcuts)
                if len (newshortcut) != 0:
                    shortcuts[newshortcut] = newtitle
                    self._setText (menuitem, newtitle)

            # print self._getText (menuitem)

            submenu = self._getSubMenu (menuitem)
            if submenu != None:
                self._assignMenuShortcuts (submenu)


    def _getSubMenu (self, menuitem):
        if isinstance (menuitem, wx.MenuItem):
            return menuitem.GetSubMenu()

        assert isinstance (menuitem, wx.Menu)
        return menuitem


    def _getMenuItems (self, menu):
        """
        Получить список подменю в зависимости от класса menu
        """
        if isinstance (menu, wx.Menu):
            return menu.GetMenuItems()

        assert isinstance (menu, wx.MenuBar)
        return [menu for menu, title in menu.GetMenus()]


    def _getText (self, menuitem):
        """
        Получить заголовок меню (или элемента меню) в зависимости от типа menuitem
        """
        if isinstance (menuitem, wx.MenuItem):
            return menuitem.GetItemLabel()

        assert isinstance (menuitem, wx.Menu)
        return menuitem.GetTitle()


    def _setText (self, menuitem, title):
        """
        Получить заголовок меню (или элемента меню) в зависимости от типа menuitem
        """
        if isinstance (menuitem, wx.MenuItem):
            # menuitem.SetText (title)
            menuitem.SetItemLabel (title)
        else:
            assert isinstance (menuitem, wx.Menu)
            menuitem.SetTitle (title)


    def _findNewShortcut (self, title, shortcuts):
        """
        Метод подбирает наиболее подходящее место для подчеркивания (если это возможно) и возвращает кортеж из нового заголовка меню и нового клавиатурного сокращения
        title - исходный заголовок меню
        shortcuts - словарь уже занятых шорткатов

        Если невозможно подобр шорткат, то возвращается кортеж из исходного заголовка и пустой строки
        """
        newtitle = title
        newshortcut = u""

        for index in range (len (title)):
            if (title[index].lower() not in shortcuts and
                    len (title[index].strip()) != 0):
                newshortcut = title[index].lower()
                newtitle = title[:index] + "&" + title[index:]
                break

        return newtitle, newshortcut
        


    def _extractShortcut (self, title):
        """
        Возвращает букву, перед которой стоит знак &. Если такой буквы нет, возвращает пустую строку
        Учитывается тот факт, что строка && означает, что & надо просто показать
        "&&&&Бла-бла-бла" не делает подчеркнутым первый &
        "&&&Бла-бла-бла" делает подчеркнутой букву "Б"

        В реальности вместо амперсандов мы получим знаки подчеркивания "_"
        """
        # Удалим все не значащие &&, чтобы они не мешались
        cleartitle = title.replace (u"&&", "")
        index = cleartitle.find (u"&")
        if index == -1 or index == len (cleartitle) - 1:
            return u""
        
        return cleartitle[index + 1].lower()
