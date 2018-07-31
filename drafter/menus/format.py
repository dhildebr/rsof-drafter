import wx

class FormatMenu(wx.Menu):
  """
  
  """
  
  def __init__(self, *args, **kwargs):
    super(FormatMenu, self).__init__(*args, **kwargs)
    
    self.Append(wx.ID_BOLD, "&Bold", "Bold the selected text")
    self.Append(wx.ID_ITALIC, "&Italic", "Italicise the selected text")
    self.Append(wx.ID_UNDERLINE, "&Underline", "Underline the selected text")
    self.Append(wx.ID_STRIKETHROUGH, "&Strikethrough", "Add a line through the selcted text")
    self.AppendSeparator()
    self.Append(wx.ID_JUSTIFY_LEFT, "Align &Left", "Left-align the selected text")
    self.Append(wx.ID_JUSTIFY_CENTER, "Align C&entre", "Centre-align the selected text")
    self.Append(wx.ID_JUSTIFY_RIGHT, "Align &Right", "Right-align the selcted text")
    self.AppendSeparator()
    self.Append(wx.ID_ANY, "Text &Colour", "Change the text's colour")
    self.AppendSeparator()
    self.Append(wx.ID_ANY, "Add Lin&k", "Add a general hyperlink")
    self.Append(wx.ID_ANY, "Add &Quick Find Code", "Add a forum quick find code")
    self.AppendSeparator()
    self.Append(wx.ID_ANY, "S&poiler Tag", "Enclose the selection in a spoiler tag")
    self.Append(wx.ID_ANY, "&No-Parse", "Ignore formatting tags in the selection")
    self.AppendSeparator()
    self.Append(wx.ID_ANY, "Add Emo&ji", "Add an emoji or emoticon")
    self.Append(wx.ID_ANY, "Add Im&gur Embed", "Add an image from Imgur")
  
  def OnBold(self):
    pass
  
  def OnItalicize(self):
    pass
  
  def OnUnderline(self):
    pass
  
  def OnStrikethrough(self):
    pass
  
  def OnAlignLeft(self):
    pass
  
  def OnAlignCenter(self):
    pass
  
  def OnAlignRight(self):
    pass
  
  def OnTetColor(self):
    pass
  
  def OnAddLink(self):
    pass
  
  def OnAddQfc(self):
    pass
  
  def OnSpoilerTag(self):
    pass
  
  def OnNoParse(self):
    pass
  
  def OnAddEmoji(self):
    pass
  
  def OnAddImgur(self):
    pass
