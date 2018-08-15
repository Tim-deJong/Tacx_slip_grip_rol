import wx as wx
import sys
from os import path


class Main(wx.Frame):
    def __init__(self, parent, title):
        """
        """

        wx.Frame.__init__(self, parent, title=title,
                          style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX), size=(500, 530))
        self.top_panel = wx.Panel(self)
        self.SetBackgroundColour("white")

        # 1: Create the file menu
        file_menu = wx.Menu()

        menu_about = file_menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        file_menu.AppendSeparator()
        menu_exit = file_menu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")

        # 2: Create the menu bar
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        self.SetMenuBar(menu_bar)

        # 3: Creating buttons
        self.exit_button = wx.Button(self.top_panel, -1, label='Exit', pos=(350, 390), size=(100, 30))
        self.reset_button = wx.Button(self.top_panel, -1, label='Reset', pos=(350, 355), size=(100, 30))

        # 4: Loading images
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = path.abspath('.')
        image_path = path.join(base_path, 'tacx-logo.png')

        image_file_png = wx.Image(image_path, wx.BITMAP_TYPE_PNG)
        image_file_png.Rescale(image_file_png.GetWidth() * 0.15, image_file_png.GetHeight() * 0.15)
        image_file_png = wx.Bitmap(image_file_png)
        self.image = wx.StaticBitmap(self.top_panel, -1, image_file_png, pos=(335, 260),
                                     size=(image_file_png.GetWidth(), image_file_png.GetHeight()))

        # 5: Creating panels
        self.font_header = wx.Font(12, family=wx.FONTFAMILY_DECORATIVE, style=wx.FONTSTYLE_NORMAL, weight=wx.FONTWEIGHT_BOLD)
        self.font_header_1 = wx.Font(10, family=wx.FONTFAMILY_DECORATIVE, style=wx.FONTSTYLE_NORMAL, weight=wx.FONTWEIGHT_BOLD)
        self.font_normal = wx.Font(10, family=wx.FONTFAMILY_DECORATIVE, style=wx.FONTSTYLE_NORMAL, weight=wx.FONTWEIGHT_NORMAL)
        self.font_big = wx.Font(12, family=wx.FONTFAMILY_DECORATIVE, style=wx.FONTSTYLE_NORMAL, weight=wx.FONTWEIGHT_NORMAL)
        self.statistics_titles = ["Roller diameter", "Contact force between roller and wheel"]

        for i in range(len(self.statistics_titles)):
            self.data_panel = wx.Panel(self.top_panel, -1, size=(465, 100), pos=(10, 10 + (1.2*i) * 60))
            self.data_panel_header = wx.StaticText(self.data_panel, label=self.statistics_titles[i], pos=(4, 2))
            if i == 0:
                self.slider_1 = wx.Slider(self.data_panel, -1, 30, 20, 70, pos=(0, 25), size=(300, -1), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS)
                self.panel_output_1 = wx.Panel(self.data_panel, -1, style=wx.BORDER_SUNKEN, size=(40, 27), pos=(350, 20))
                self.text_1 = wx.StaticText(self.data_panel, label='mm', pos=(395, 23))
                self.text_1.SetFont(self.font_big)
                self.data_panel_slider_1 = wx.StaticText(self.panel_output_1, label='30', pos=(14, 2))
                self.data_panel_slider_1.SetFont(self.font_big)
            if i == 1:
                self.slider_2 = wx.Slider(self.data_panel, -1, 400, 200, 800, pos=(0, 25), size=(300, -1), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS)
                self.panel_output_2 = wx.Panel(self.data_panel, -1, style=wx.BORDER_SUNKEN, size=(40, 27), pos=(350, 20))
                self.text_1 = wx.StaticText(self.data_panel, label='N', pos=(395, 23))
                self.text_1.SetFont(self.font_big)
                self.data_panel_slider_2 = wx.StaticText(self.panel_output_2, label='400', pos=(4, 2))
                self.data_panel_slider_2.SetFont(self.font_big)
            self.data_panel_header.SetFont(self.font_header)

        self.output_panel = wx.Panel(self.top_panel, -1, style=wx.BORDER_RAISED, size=(300, 200), pos=(10, 220))
        self.text = wx.StaticText(self.output_panel, label='Calculated friction force: \n(bigger = better)', pos=(14, 2))
        self.text.SetFont(self.font_header_1)
        self.text = wx.StaticText(self.output_panel, label='Calculated rolling resistance: \n(smaller = better)', pos=(14, 90))
        self.text.SetFont(self.font_header_1)
        self.panel_output_3 = wx.Panel(self.output_panel, -1, style=wx.BORDER_SUNKEN, size=(40, 27), pos=(180, 42))
        self.data_output_text = wx.StaticText(self.output_panel, label='N', pos=(225, 45))
        self.data_output_text.SetFont(self.font_big)
        self.data_panel_friction= wx.StaticText(self.panel_output_3, label='30', pos=(14, 2))
        self.data_panel_friction.SetFont(self.font_big)

        self.panel_output_4 = wx.Panel(self.output_panel, -1, style=wx.BORDER_SUNKEN, size=(40, 27), pos=(180, 130))
        self.data_output_text = wx.StaticText(self.output_panel, label='N', pos=(225, 133))
        self.data_output_text.SetFont(self.font_big)
        self.data_panel_resistance= wx.StaticText(self.panel_output_4, label='30', pos=(14, 2))
        self.data_panel_resistance.SetFont(self.font_big)

        # 7: Set start-up message
        welcome_dialog = wx.MessageDialog(self.top_panel,
                                          message="Welcome to the Tacx design tool. \nIf you have read the README.pdf, you're good to go. \nIf you haven't yet, please do.",
                                          caption="Welcome!")
        welcome_dialog.CenterOnParent()
        if welcome_dialog.ShowModal() == wx.OK:
            welcome_dialog.Destroy()
            return


        # 8: Create status bar
        self.statusbar = self.CreateStatusBar()


        # 9: Create empty parameters
        self.testdata = [[20, 200, 10, 20], [20, 300, 12, 22], [20, 400, 14, 24], [20, 500, 16, 26], [20, 600, 18, 28],
                         [20, 700, 20, 30], [20, 800, 22, 32], [30, 200, 20, 30], [30, 300, 22, 32], [30, 400, 24, 34],
                         [30, 500, 26, 36], [30, 600, 28, 38], [30, 700, 30, 40], [30, 800, 32, 42], [40, 200, 30, 40],
                         [40, 300, 32, 42], [40, 400, 34, 44], [40, 500, 36, 46], [40, 600, 38, 48], [40, 700, 40, 50],
                         [40, 800, 42, 52], [50, 200, 40, 50], [50, 300, 42, 52], [50, 400, 44, 54], [50, 500, 46, 56],
                         [50, 600, 48, 58], [50, 700, 50, 60], [50, 800, 52, 62], [60, 200, 50, 60], [60, 300, 52, 62],
                         [60, 400, 54, 64], [60, 500, 56, 66], [60, 600, 58, 68], [60, 700, 60, 70], [60, 800, 62, 72],
                         [70, 200, 50, 60]]

        # 6: Set events
        self.Bind(wx.EVT_MENU, self.on_about, menu_about)
        self.Bind(wx.EVT_MENU, self.on_exit, menu_exit)
        self.Bind(wx.EVT_SLIDER, self.on_slider_1, self.slider_1)
        self.Bind(wx.EVT_SLIDER, self.on_slider_2, self.slider_2)
        self.exit_button.Bind(wx.EVT_BUTTON, self.on_exit_button)
        self.exit_button.Bind(wx.EVT_ENTER_WINDOW, self.on_exit_widget_enter)
        self.reset_button.Bind(wx.EVT_BUTTON, self.on_reset)
        self.reset_button.Bind(wx.EVT_ENTER_WINDOW, self.on_reset_widget_enter)

        # Some variables needed
        self.value_slider_1 = self.slider_1.GetValue()
        self.value_slider_2 = self.slider_2.GetValue()
        self.interpolation()

    def interpolation(self):
        dummy = []
        for i in range(len(self.testdata)):
            if abs(self.testdata[i][0] - self.value_slider_1) <= 9 and abs(self.testdata[i][1] - self.value_slider_2) <= 99:
                dummy.append(self.testdata[i])

        if len(dummy) == 1:
            self.friction = dummy[0][2]
            self.rolling_resistance = dummy[0][3]
        elif len(dummy) == 2:
            if dummy[0][0] == dummy[1][0]:
                # The diameter is the same
                self.friction = dummy[0][2] + (dummy[0][2] - dummy[1][2])/(dummy[0][1] - dummy[1][1]) * abs(dummy[0][1] - self.value_slider_2)
                self.rolling_resistance = dummy[0][3] + (dummy[0][3] - dummy[1][3])/(dummy[0][1] - dummy[1][1]) * abs(dummy[0][1] - self.value_slider_2)

            elif dummy[0][1] == dummy[1][1]:
                # The contact force is the same
                self.friction = dummy[0][2] + (dummy[0][2] - dummy[1][2])/(dummy[0][0] - dummy[1][0]) * abs(dummy[0][0] - self.value_slider_1)
                self.rolling_resistance = dummy[0][3] + (dummy[0][3] - dummy[1][3])/(dummy[0][0] - dummy[1][0]) * abs(dummy[0][0] - self.value_slider_1)
        elif len(dummy)  == 4:
            data_1 = dummy[0]
            data_2 = dummy[1]
            data_3 = dummy[2]
            data_4 = dummy[3]
            data_interpolated_force_1 = []
            data_interpolated_force_2 = []

            data_interpolated_force_1.append(data_1[0])
            data_interpolated_force_1.append(self.value_slider_2)
            data_interpolated_force_1.append(data_1[2] + (data_1[2] - data_2[2])/(data_1[1] - data_2[1]) * abs(data_1[1] - self.value_slider_2))
            data_interpolated_force_1.append(data_1[3] + (data_1[3] - data_2[3])/(data_1[1] - data_2[1]) * abs(data_1[1] - self.value_slider_2))

            data_interpolated_force_2.append(data_3[0])
            data_interpolated_force_2.append(self.value_slider_2)
            data_interpolated_force_2.append(data_3[2] + (data_3[2] - data_4[2])/(data_3[1] - data_4[1]) * abs(data_3[1] - self.value_slider_2))
            data_interpolated_force_2.append(data_3[3] + (data_3[3] - data_4[3])/(data_3[1] - data_4[1]) * abs(data_3[1] - self.value_slider_2))

            self.friction = data_interpolated_force_1[2] + (data_interpolated_force_1[2] - data_interpolated_force_2[2])/(data_interpolated_force_1[0] - data_interpolated_force_2[0]) * abs(data_interpolated_force_1[0] - self.value_slider_1)
            self.rolling_resistance = data_interpolated_force_1[3] + (data_interpolated_force_1[3] - data_interpolated_force_2[3])/(data_interpolated_force_1[0] - data_interpolated_force_2[0]) * abs(data_interpolated_force_1[0] - self.value_slider_1)

        self.data_panel_resistance.SetLabel(str(int(self.rolling_resistance)))
        self.data_panel_friction.SetLabel(str(int(self.friction)))

    def on_about(self, e):
        """"Message box with OK button"""
        prompted_dialog = wx.MessageDialog(self, "A file which can be used by designing a new Tacx \n"
                                                 "roller trainer and give an indication for the \n"
                                                 "rolling resistance and occurring friction. \n"
                                                 "\n"
                                                 "Built in Python 3.6.6, compiled with PyInstaller"
                                                 "\n"
                                                 "\n"
                                                 "Created by Tim de Jong and Jelle Haasnoot at Tacx B.V.",
                                           "About Tacx design tool", wx.OK)
        prompted_dialog.ShowModal()
        prompted_dialog.Destroy()

    def on_slider_1(self, e):
        self.value_slider_1 = self.slider_1.GetValue()
        self.data_panel_slider_1.SetLabel(str(self.value_slider_1))
        self.interpolation()

    def on_slider_2(self, e):
        self.value_slider_2 = self.slider_2.GetValue()
        self.data_panel_slider_2.SetLabel(str(self.value_slider_2))
        self.interpolation()

    def on_exit(self, e):
        self.Close(True)

    def on_exit_button(self, event):
        self.Close()

    def on_reset(self, event):
        if __name__ == '__main__':
            self.Close()
            frame = Main(None, 'Tacx design tool').Show()

    def on_exit_widget_enter(self, event):
        self.statusbar.SetStatusText('Exit the program')
        event.Skip()

    def on_open_widget_enter(self, event):
        self.statusbar.SetStatusText('Open multiple LOG-files')
        event.Skip()

    def on_reset_widget_enter(self, event):
        self.statusbar.SetStatusText('Reset the program')
        event.Skip()

    def on_excel_widget_enter(self, event):
        self.statusbar.SetStatusText('Open the created Excel-file')
        event.Skip()

    def on_check_hover(self, event):
        self.statusbar.SetStatusText('Enable the option to use user-input simulated mass')
        event.Skip()

    def on_save_hover(self, event):
        self.statusbar.SetStatusText('Save the entered inputs to use them in calculations')
        event.Skip()


if __name__ == '__main__':
    Application = wx.App(False)
    frame = Main(None, 'Tacx design tool                           '
                       '             [v1.0]').Show()
    Application.MainLoop()
