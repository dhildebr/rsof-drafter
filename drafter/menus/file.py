import wx

class FileMenu(wx.Menu):
  """
  
  """
  
  def __init__(self, *args, **kwargs):
    super(FileMenu, self).__init__(*args, **kwargs)
    
    self.Append(wx.ID_NEW, "&New", "Create a new thread")
    self.Append(wx.ID_OPEN, "&Open", "Open an existing thread")
    self.Append(wx.ID_SAVE, "&Save", "Save the current thread")
    self.Append(wx.ID_SAVEAS, "Save &As...", "Save a copy of the current thread")
    self.AppendSeparator()
    self.Append(wx.ID_CLOSE, "&Close", "Close the current thread")
    self.Append(wx.ID_EXIT, "&Quit", "Quit the RSOF Drafter")
  
  def OnNew(self):
    pass
  
  def OnOpen(self):
    pass
  
  def OnSave(self):
    pass
  
  def OnSaveAs(self):
    pass
  
  def OnClose(self):
    pass
  
  def OnQuit(self):
    pass
