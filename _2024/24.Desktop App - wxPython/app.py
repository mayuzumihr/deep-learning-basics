import wx

class GUISample(wx.Frame):

    def __init__(self, *args, **kw):
        super(GUISample, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.text = wx.TextCtrl(panel)
        vbox.Add(self.text, 0, wx.EXPAND | wx.ALL, 10)

        self.label = wx.StaticText(panel, label='ここにテキストが表示されます', style=wx.ALIGN_CENTER)
        hbox_label = wx.BoxSizer(wx.HORIZONTAL)
        hbox_label.AddStretchSpacer(1)
        hbox_label.Add(self.label, 0, wx.ALIGN_CENTER)
        hbox_label.AddStretchSpacer(1)
        vbox.Add(hbox_label, 0, wx.EXPAND | wx.ALL, 10)

        self.button = wx.Button(panel, label='ボタン')
        hbox_button = wx.BoxSizer(wx.HORIZONTAL)
        hbox_button.AddStretchSpacer(1)
        hbox_button.Add(self.button, 0, wx.ALIGN_CENTER)
        hbox_button.AddStretchSpacer(1)
        vbox.Add(hbox_button, 0, wx.EXPAND | wx.ALL, 10)

        self.button.Bind(wx.EVT_BUTTON, self.show_text)

        panel.SetSizer(vbox)

        self.SetTitle('サンプルアプリ（wxPython）')
        self.SetSize((500, 300))
        self.Centre()

    def show_text(self, event):
        input_text = self.text.GetValue()
        self.label.SetLabel(input_text)

def main():

    app = wx.App()
    ex = GUISample(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
