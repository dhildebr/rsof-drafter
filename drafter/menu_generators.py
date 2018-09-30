"""
A module for generators for the RSOF Drafter's standard menus. Each
GenerateFoo function returns a dict containing, among other things, an
instance of wx.Menu with the approprite menu items.

In each case, a GenerateFoo function will return a dict with a string
key "menu" which refers to the instance of wx.Menu. The key "items" will
grant access to a list of 2-tuples: each menu item and its ID. The list
of menu items returned does not include separators.
"""

import wx

def GenerateFileMenu():
  """
  
  """

  newMenu = wx.Menu()

  itemNew = newMenu.Append(wx.ID_NEW, "&New...", "Create a new thread")
  itemOpen = newMenu.Append(wx.ID_OPEN, "&Open...", "Open an existing thread")
  itemSave = newMenu.Append(wx.ID_SAVE, "&Save", "Save the current thread")
  itemSaveAs = newMenu.Append(wx.ID_SAVEAS, "Save &As...", "Save a copy of the current thread")
  newMenu.AppendSeparator()
  itemClose = newMenu.Append(wx.ID_CLOSE, "&Close", "Close the current thread")
  itemQuit = newMenu.Append(wx.ID_EXIT, "&Quit", "Quit the RSOF Drafter")
  
  return {
      "menu": newMenu,
      "items": [(itemNew, itemNew.GetId()), (itemOpen, itemOpen.GetId()), (itemSave, itemSave.GetId()),
                (itemSaveAs, itemSaveAs.GetId()), (itemClose, itemClose.GetId()), (itemQuit, itemQuit.GetId())]
  }

def GenerateEditMenu():
  """
  
  """
  
  newMenu = wx.Menu()
  
  itemUndo = newMenu.Append(wx.ID_UNDO, "&Undo", "Undo the last action performed")
  itemRedo = newMenu.Append(wx.ID_REDO, "&Redo", "Redo the last action undone")
  newMenu.AppendSeparator()
  itemCut = newMenu.Append(wx.ID_CUT, "Cu&t", "Remove selected text and save a copy to the clipboard")
  itemCopy = newMenu.Append(wx.ID_COPY, "&Copy", "Add the selected text to the clipboard")
  itemPaste = newMenu.Append(wx.ID_PASTE, "&Paste", "Paste text from the clipboard")
  newMenu.AppendSeparator()
  itemSelectAll = newMenu.Append(wx.ID_SELECTALL, "Select &All", "Select all text in the current post")
  itemDelete = newMenu.Append(wx.ID_DELETE, "&Delete", "Delete the selected text")
  
  return {
      "menu": newMenu,
      "items": [(itemUndo, itemUndo.GetId()), (itemRedo, itemRedo.GetId()), (itemCut, itemCut.GetId()),
                (itemCopy, itemCopy.GetId()), (itemPaste, itemPaste.GetId()),
                (itemSelectAll, itemSelectAll.GetId()), (itemDelete, itemDelete.GetId())]
  }

def GenerateFormatMenu():
  """
  
  """
  
  newMenu = wx.Menu()
  
  itemBold = newMenu.Append(wx.ID_BOLD, "&Bold", "Bold the selected text")
  itemItalic = newMenu.Append(wx.ID_ITALIC, "&Italic", "Italicise the selected text")
  itemUnderline = newMenu.Append(wx.ID_UNDERLINE, "&Underline", "Underline the selected text")
  itemStrikethrough = newMenu.Append(wx.ID_STRIKETHROUGH, "&Strikethrough", "Add a line through the selcted text")
  newMenu.AppendSeparator()
  itemLeftJustify = newMenu.Append(wx.ID_JUSTIFY_LEFT, "Align &Left", "Left-align the selected text")
  itemCenter = newMenu.Append(wx.ID_JUSTIFY_CENTER, "Align C&entre", "Centre-align the selected text")
  itemRightJustify = newMenu.Append(wx.ID_JUSTIFY_RIGHT, "Align &Right", "Right-align the selcted text")
  newMenu.AppendSeparator()
  itemTextColor = newMenu.Append(wx.ID_ANY, "Text &Colour", "Change the text's colour")
  newMenu.AppendSeparator()
  itemLink = newMenu.Append(wx.ID_ANY, "Add Lin&k", "Add a general hyperlink")
  itemQfc = newMenu.Append(wx.ID_ANY, "Add &Quick Find Code", "Add a forum quick find code")
  newMenu.AppendSeparator()
  itemSpoiler = newMenu.Append(wx.ID_ANY, "S&poiler Tag", "Enclose the selection in a spoiler tag")
  itemNoParse = newMenu.Append(wx.ID_ANY, "&No-Parse", "Ignore formatting tags in the selection")
  newMenu.AppendSeparator()
  itemEmoji = newMenu.Append(wx.ID_ANY, "Add Emo&ji", "Add an emoji or emoticon")
  itemImgur = newMenu.Append(wx.ID_ANY, "Add Im&gur Embed", "Add an image from Imgur")
  
  return {
      "menu": newMenu,
      "items": [(itemBold, itemBold.GetId()), (itemItalic, itemItalic.GetId()),
                (itemUnderline, itemUnderline.GetId()), (itemStrikethrough, itemStrikethrough.GetId()),
                (itemLeftJustify, itemLeftJustify.GetId()), (itemCenter, itemCenter.GetId()),
                (itemRightJustify, itemRightJustify.GetId()), (itemTextColor, itemTextColor.GetId()),
                (itemLink, itemLink.GetId()), (itemQfc, itemQfc.GetId()), (itemSpoiler, itemSpoiler.GetId()),
                (itemNoParse, itemNoParse.GetId()), (itemEmoji, itemEmoji.GetId()), (itemImgur, itemImgur.GetId())]
  }

def GenerateSettingsMenu():
  """
  
  """
  
  newMenu = wx.Menu()
  
  itemPreferences = newMenu.Append(wx.ID_PREFERENCES, "&Preferences...", "Change your preferences")
  itemProperties = newMenu.Append(wx.ID_PROPERTIES, "&Keyboard Shortcuts...", "View or edit keybinds")
  
  return {
      "menu": newMenu,
      "items": [(itemPreferences, itemPreferences.GetId()), (itemProperties, itemProperties.GetId())]
  }

def GenerateHelpMenu():
  """
  
  """
  
  newMenu = wx.Menu()
  
  itemAbout = newMenu.Append(wx.ID_ABOUT, "&About...", "More info about the RSOF Drafter")
  itemHelp = newMenu.Append(wx.ID_HELP, "&Forums Help...", "Help with Runescape Forums formatting")
  
  return {
      "menu": newMenu,
      "items": [(itemAbout, itemAbout.GetId()), (itemHelp, itemHelp.GetId())]
  }
