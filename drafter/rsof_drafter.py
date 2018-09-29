import wx

import menus.file
import menus.edit
import menus.format
import menus.settings
import menus.help

class DrafterMainFrame(wx.Frame):
  """

  """

  def __init__(self, *args, **kwargs):
    super(DrafterMainFrame, self).__init__(*args, **kwargs)

    self.__InitMenuBar()

  def __InitMenuBar(self):
    menuBar = wx.MenuBar()

    menuBar.Append(menus.file.FileMenu(), "&File")
    menuBar.Append(menus.edit.EditMenu(), "&Edit")
    menuBar.Append(menus.format.FormatMenu(), "For&mat")
    menuBar.Append(menus.settings.SettingsMenu(), "Se&ttings")
    menuBar.Append(menus.help.HelpMenu(), "&Help")
    
    self.Bind(wx.EVT_MENU, menus.file.OnQuit, menuBar.GetMenu(menuBar.FindMenu("File")).FindItemById(wx.ID_EXIT))

    self.SetMenuBar(menuBar)


if __name__ == "__main__":
  app = wx.App()
  window = DrafterMainFrame(None, title = "RSOF Drafter", size = (800, 600))
  panel = wx.Panel(window)

  window.Show(True)
  app.MainLoop()
