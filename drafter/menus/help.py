import wx

class HelpMenu(wx.Menu):
  """
  
  """
  
  def __init__(self, *args, **kwargs):
    super(HelpMenu, self).__init__(*args, **kwargs)
    
    self.Append(wx.ID_ABOUT, "&About...", "More info about the RSOF Drafter")
    self.Append(wx.ID_HELP, "&Forums Help...", "Help with Runescape Forums formatting")
  
  def OnAbout(self):
    pass
  
  def OnForumHelp(self):
    pass
