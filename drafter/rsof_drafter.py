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
    menu_bar = wx.MenuBar()
    
    menu_bar.Append(menus.file.FileMenu(), "&File")
    menu_bar.Append(menus.edit.EditMenu(), "&Edit")
    menu_bar.Append(menus.format.FormatMenu(), "For&mat")
    menu_bar.Append(menus.settings.SettingsMenu(), "Se&ttings")
    menu_bar.Append(menus.help.HelpMenu(), "&Help")
    
    self.SetMenuBar(menu_bar)


if __name__ == "__main__":
  app = wx.App()
  window = DrafterMainFrame(None, title = "RSOF Drafter", size = (800, 600))
  panel = wx.Panel(window)

  window.Show(True)
  app.MainLoop()
