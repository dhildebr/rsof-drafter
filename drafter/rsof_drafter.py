import wx

import menu_generators as menugen

class DrafterMainFrame(wx.Frame):
  """

  """

  def __init__(self):
    """
    Constructs the top-level frame of the RSOF Drafter app.
    """
    
    super(DrafterMainFrame, self).__init__(None, title = "RSOF Drafter", size = (800, 600))
    
    self.__menuInfoFile = None
    self.__menuInfoEdit = None
    self.__menuInfoFormat = None
    self.__menuInfoSettings = None
    self.__menuInfoHelp = None
    self.__InitMenuBar()

  def __InitMenuBar(self):
    menuBar = wx.MenuBar()
    
    self.__menuInfoFile = menugen.GenerateFileMenu()
    self.__menuInfoEdit = menugen.GenerateEditMenu()
    self.__menuInfoFormat = menugen.GenerateFormatMenu()
    self.__menuInfoSettings = menugen.GenerateSettingsMenu()
    self.__menuInfoHelp = menugen.GenerateHelpMenu()
    
    menuBar.Append(self.__menuInfoFile["menu"], "&File")
    menuBar.Append(self.__menuInfoEdit["menu"], "&Edit")
    menuBar.Append(self.__menuInfoFormat["menu"], "For&mat")
    menuBar.Append(self.__menuInfoSettings["menu"], "Se&ttings")
    menuBar.Append(self.__menuInfoHelp["menu"], "&Help")
    
    menuCallbacksFile = [self.OnMenuFileNew, self.OnMenuFileOpen, self.OnMenuFileSave,
                         self.OnMenuFileSaveAs, self.OnMenuFileClose, self.OnMenuFileQuit]
    menuCallbacksEdit = [self.OnMenuEditUndo, self.OnMenuEditRedo, self.OnMenuEditCut, self.OnMenuEditCopy,
                         self.OnMenuEditPaste, self.OnMenuEditSelectAll, self.OnMenuEditDelete]
    menuCallbacksFormat = [self.OnMenuFormatBold, self.OnMenuFormatItalic, self.OnMenuFormatUnderline,
                           self.OnMenuFormatStrikethrough, self.OnMenuFormatAlignLeft,
                           self.OnMenuFormatAlignCenter, self.OnMenuFormatAlignRight, self.OnMenuFormatTextColor,
                           self.OnMenuFormatLink, self.OnMenuFormatQfc, self.OnMenuFormatSpoiler,
                           self.OnMenuFormatNoParse, self.OnMenuFormatEmoji, self.OnMenuFormatImgur]
    menuCallbacksSettings = [self.OnMenuSettingsPreferences, self.OnMenuSettingsKeyboardShortcuts]
    menuCallbacksHelp = [self.OnMenuHelpAbout, self.OnMenuHelpForumsHelp]
    
    for index, callback in enumerate(menuCallbacksFile):
      self.Bind(wx.EVT_MENU, callback, self.__menuInfoFile["items"][index][0])
    for index, callback in enumerate(menuCallbacksEdit):
      self.Bind(wx.EVT_MENU, callback, self.__menuInfoEdit["items"][index][0])
    for index, callback in enumerate(menuCallbacksFormat):
      self.Bind(wx.EVT_MENU, callback, self.__menuInfoFormat["items"][index][0])
    for index, callback in enumerate(menuCallbacksSettings):
      self.Bind(wx.EVT_MENU, callback, self.__menuInfoSettings["items"][index][0])
    for index, callback in enumerate(menuCallbacksHelp):
      self.Bind(wx.EVT_MENU, callback, self.__menuInfoHelp["items"][index][0])
    
    self.SetMenuBar(menuBar)
  
  ##################################################################################################
  
  def OnMenuFileNew(self, event):
    """ """
    print("Selected menu item: File -> New...")
    
  def OnMenuFileOpen(self, event):
    """ """
    print("Selected menu item: File -> Open...")
  
  def OnMenuFileSave(self, event):
    """ """
    print("Selected menu item: File -> Save")
  
  def OnMenuFileSaveAs(self, event):
    """ """
    print("Selected menu item: File -> Save As...")
  
  def OnMenuFileClose(self, event):
    """ """
    print("Selected menu item: File -> Close")
  
  def OnMenuFileQuit(self, event):
    """ """
    self.Destroy()
  
  ##################################################################################################
  
  def OnMenuEditUndo(self, event):
    """ """
    print("Selected menu item: Edit -> Undo")
  
  def OnMenuEditRedo(self, event):
    """ """
    print("Selected menu item: Edit -> Redo")
  
  def OnMenuEditCut(self, event):
    """ """
    print("Selected menu item: Edit -> Cut")
  
  def OnMenuEditCopy(self, event):
    """ """
    print("Selected menu item: Edit -> Copy")
  
  def OnMenuEditPaste(self, event):
    """ """
    print("Selected menu item: Edit -> Paste")
  
  def OnMenuEditSelectAll(self, event):
    """ """
    print("Selected menu item: Edit -> Select All")
  
  def OnMenuEditDelete(self, event):
    """ """
    print("Selected menu item: Edit -> Delete")
  
  ##################################################################################################
  
  def OnMenuFormatBold(self, event):
    """ """
    print("Selected menu item: Format -> Bold")
  
  def OnMenuFormatItalic(self, event):
    """ """
    print("Selected menu item: Format -> Italic")
  
  def OnMenuFormatUnderline(self, event):
    """ """
    print("Selected menu item: Format -> Underline")
  
  def OnMenuFormatStrikethrough(self, event):
    """ """
    print("Selected menu item: Format -> Strikethrough")
  
  def OnMenuFormatAlignLeft(self, event):
    """ """
    print("Selected menu item: Format -> Align Left")
  
  def OnMenuFormatAlignCenter(self, event):
    """ """
    print("Selected menu item: Format -> Align Centre")
  
  def OnMenuFormatAlignRight(self, event):
    """ """
    print("Selected menu item: Format -> Align Right")
  
  def OnMenuFormatTextColor(self, event):
    """ """
    print("Selected menu item: Format -> Text Colour...")
  
  def OnMenuFormatLink(self, event):
    """ """
    print("Selected menu item: Format -> Add Link...")
  
  def OnMenuFormatQfc(self, event):
    """ """
    print("Selected menu item: Format -> Add Quick Find Code...")
  
  def OnMenuFormatSpoiler(self, event):
    """ """
    print("Selected menu item: Format -> Spoiler Tag")
  
  def OnMenuFormatNoParse(self, event):
    """ """
    print("Selected menu item: Format -> No-Parse")
  
  def OnMenuFormatEmoji(self, event):
    """ """
    print("Selected menu item: Format -> Add Emoji")
  
  def OnMenuFormatImgur(self, event):
    """ """
    print("Selected menu item: Format -> Add Imgur Embed")
  
  ##################################################################################################
  
  def OnMenuSettingsPreferences(self, event):
    """ """
    print("Selected menu item: Settings -> Preferences...")
  
  def OnMenuSettingsKeyboardShortcuts(self, event):
    """ """
    print("Selected menu item: Settings -> Keyboard Shortcuts...")
  
  ##################################################################################################
  
  def OnMenuHelpAbout(self, event):
    """ """
    print("Selected menu item: Help -> About...")
  
  def OnMenuHelpForumsHelp(self, event):
    """ """
    print("Selected menu item: Help -> Forums Help...")


if __name__ == "__main__":
  app = wx.App()
  window = DrafterMainFrame()
  panel = wx.Panel(window)
  
  textBox = wx.TextCtrl(panel, style = wx.TE_MULTILINE)
  sizer = wx.BoxSizer(wx.HORIZONTAL)
  sizer.Add(textBox, 1, wx.EXPAND, 0)
  sizer.SetSizeHints(panel)
  panel.SetSizer(sizer)

  window.Show(True)
  app.MainLoop()
