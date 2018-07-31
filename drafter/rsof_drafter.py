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
    
    menu_edit = wx.Menu()
    edit_item_undo = menu_edit.Append(wx.ID_UNDO, "&Undo", "Undo the last action performed")
    edit_item_redo = menu_edit.Append(wx.ID_REDO, "&Redo", "Redo the last action undone")
    menu_edit.Append(wx.ID_SEPARATOR)
    edit_item_cut = menu_edit.Append(wx.ID_CUT, "Cu&t", "Remove selected text and save a copy to the clipboard")
    edit_item_copy = menu_edit.Append(wx.ID_COPY, "&Copy", "Add the selected text to the clipboard")
    edit_item_paste = menu_edit.Append(wx.ID_PASTE, "&Paste", "Paste text from the clipboard")
    menu_edit.Append(wx.ID_SEPARATOR)
    file_item_select_all = menu_edit.Append(wx.ID_SELECTALL, "Select &All", "Select all text in the current post")
    file_item_delete = menu_edit.Append(wx.ID_DELETE, "&Delete", "Delete the selected text")
    menu_bar.Append(menu_edit, "&Edit")
    
    menu_format = wx.Menu()
    format_item_bold = menu_format.Append(wx.ID_BOLD, "&Bold", "Bold the selected text")
    format_item_italic = menu_format.Append(wx.ID_ITALIC, "&Italic", "Italicise the selected text")
    format_item_underline = menu_format.Append(wx.ID_UNDERLINE, "&Underline", "Underline the selected text")
    format_item_strike = menu_format.Append(wx.ID_STRIKETHROUGH, "&Strikethrough", "Add a line through the selcted text")
    menu_format.Append(wx.ID_SEPARATOR)
    format_item_align_left = menu_format.Append(wx.ID_JUSTIFY_LEFT, "Align &Left", "Left-align the selected text")
    format_item_align_center = menu_format.Append(wx.ID_JUSTIFY_CENTER, "Align C&entre", "Centre-align the selected text")
    format_item_align_right = menu_format.Append(wx.ID_JUSTIFY_RIGHT, "Align &Right", "Right-align the selcted text")
    menu_format.Append(wx.ID_SEPARATOR)
    format_item_text_color = menu_format.Append(wx.ID_ANY, "Text &Colour", "Change the text's colour")
    menu_format.Append(wx.ID_SEPARATOR)
    format_item_link = menu_format.Append(wx.ID_ANY, "Add Lin&k", "Add a general hyperlink")
    format_item_qfc = menu_format.Append(wx.ID_ANY, "Add &Quick Find Code", "Add a forum quick find code")
    menu_format.Append(wx.ID_SEPARATOR)
    format_item_spoiler = menu_format.Append(wx.ID_ANY, "S&poiler Tag", "Enclose the selection in a spoiler tag")
    format_item_noparse = menu_format.Append(wx.ID_ANY, "&No-Parse", "Ignore formatting tags in the selection")
    menu_format.Append(wx.ID_SEPARATOR)
    format_item_emojis = menu_format.Append(wx.ID_ANY, "Add Emo&ji", "Add an emoji or emoticon")
    format_item_imgur = menu_format.Append(wx.ID_ANY, "Add Im&gur Embed", "Add an image from Imgur")
    menu_bar.Append(menu_format, "For&mat")
    
    menu_settings = wx.Menu()
    settings_item_preferences = menu_settings.Append(wx.ID_PREFERENCES, "&Preferences...", "Change your preferences")
    settings_item_shortcuts = menu_settings.Append(wx.ID_PROPERTIES, "&Keyboard Shortcuts...", "View or edit keybinds")
    menu_bar.Append(menu_settings, "Se&ttings")
    
    menu_help = wx.Menu()
    help_item_about = menu_help.Append(wx.ID_ABOUT, "&About...", "More info about the RSOF Drafter")
    help_item_forum_help = menu_help.Append(wx.ID_HELP, "&Forums Help...", "Help with Runescape Forums formatting")
    menu_bar.Append(menu_help, "&Help")
    
    self.SetMenuBar(menu_bar)


if __name__ == "__main__":
  app = wx.App()
  window = DrafterMainFrame(None, title = "RSOF Drafter", size = (800, 600))
  panel = wx.Panel(window)

  window.Show(True)
  app.MainLoop()
