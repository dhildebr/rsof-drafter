import wx

import menu_generators as menugen

class DrafterMainFrame(wx.Frame):
  """

  """

  def __init__(self, *args, **kwargs):
    super(DrafterMainFrame, self).__init__(*args, **kwargs)
    
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
    
    self.Bind(wx.EVT_MENU, self.OnQuit, self.__menuInfoFile["items"][-1][0])
    
    self.SetMenuBar(menuBar)
  
  def OnQuit(self, event):
    self.Close()


if __name__ == "__main__":
  app = wx.App()
  window = DrafterMainFrame(None, title = "RSOF Drafter", size = (800, 600))
  panel = wx.Panel(window)

  window.Show(True)
  app.MainLoop()
