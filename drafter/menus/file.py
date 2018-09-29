import wx

class FileMenu(wx.Menu):
  """
  The File menu of the RSOF Drafter application. The menu contains items
  for the creation of new items, opening existing ones, and saving
  changes to the current thread.
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
  print("Selected menu item: File -> New.");

def OnOpen(self):
  print("Selected menu item: File -> Open.");

def OnSave(self):
  print("Selected menu item: File -> Save.");

def OnSaveAs(self):
  print("Selected menu item: File -> Save As.");

def OnClose(self):
  print("Selected menu item: File -> Close.");

def OnQuit(event):
  print("Selected menu item: File -> Quit.");


def GenerateFileMenu(parentFrame):
  """
  Generates and returns the standard File menu.
  """

  newMenu = wx.Menu()

  newMenu.Append(wx.ID_NEW, "&New", "Create a new thread")
  newMenu.Append(wx.ID_OPEN, "&Open", "Open an existing thread")
  newMenu.Append(wx.ID_SAVE, "&Save", "Save the current thread")
  newMenu.Append(wx.ID_SAVEAS, "Save &As...", "Save a copy of the current thread")
  newMenu.AppendSeparator()
  newMenu.Append(wx.ID_CLOSE, "&Close", "Close the current thread")
  newMenu.Append(wx.ID_EXIT, "&Quit", "Quit the RSOF Drafter")
  
  return newMenu
