import wx

class EditMenu(wx.Menu):
  """
  
  """
  
  def __init__(self, *args, **kwargs):
    super(EditMenu, self).__init__(*args, **kwargs)
    
    self.Append(wx.ID_UNDO, "&Undo", "Undo the last action performed")
    self.Append(wx.ID_REDO, "&Redo", "Redo the last action undone")
    self.AppendSeparator()
    self.Append(wx.ID_CUT, "Cu&t", "Remove selected text and save a copy to the clipboard")
    self.Append(wx.ID_COPY, "&Copy", "Add the selected text to the clipboard")
    self.Append(wx.ID_PASTE, "&Paste", "Paste text from the clipboard")
    self.AppendSeparator()
    self.Append(wx.ID_SELECTALL, "Select &All", "Select all text in the current post")
    self.Append(wx.ID_DELETE, "&Delete", "Delete the selected text")
  
  def OnUndo(self):
    pass
  
  def OnRedo(self):
    pass
  
  def OnCut(self):
    pass
  
  def OnCopy(self):
    pass
  
  def OnPaste(self):
    pass
  
  def OnSelectAll(self):
    pass
  
  def OnDelete(self):
    pass
