import wx

class SettingsMenu(wx.Menu):
  """
  
  """
  
  def __init__(self, *args, **kwargs):
    super(SettingsMenu, self).__init__(*args, **kwargs)
    
    self.Append(wx.ID_PREFERENCES, "&Preferences...", "Change your preferences")
    self.Append(wx.ID_PROPERTIES, "&Keyboard Shortcuts...", "View or edit keybinds")
  
  def OnPreferences(self):
    pass
  
  def OnProperties(self):
    pass
