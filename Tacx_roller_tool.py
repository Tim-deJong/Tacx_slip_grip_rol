import wx as wx
import sys
import wxmplot
import numpy
import matplotlib
from os import path


class Main(wx.Frame):
    def __init__(self, parent, title):
        """
        The application will be made in this function. The style will be adjusted to make it user friendly. Only the
        necessary parameters will be shown in the application. The data, which is used as input data, is obtained by
        tests.
        """

        # Create the main frame
        wx.Frame.__init__(self, parent, title=title,
                          style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX), size=(900, 450))
        self.top_panel = wx.Panel(self)
        self.SetBackgroundColour("white")

        # Create the file menu
        file_menu = wx.Menu()
        menu_about = file_menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        file_menu.AppendSeparator()
        menu_exit = file_menu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")

        # Create the menu bar
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        self.SetMenuBar(menu_bar)

        # Creating buttons to reset or Exit the application
        self.exit_button = wx.Button(self.top_panel, -1, label='Exit', pos=(350, 320), size=(100, 30))
        self.reset_button = wx.Button(self.top_panel, -1, label='Reset', pos=(350, 288), size=(100, 30))

        # Loading image for the Tacx logo, placement of this photo will also be done right here.
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = path.abspath('.')
        image_path = path.join(base_path, 'tacx-logo.png')

        image_file_png = wx.Image(image_path, wx.BITMAP_TYPE_PNG)
        image_file_png.Rescale(image_file_png.GetWidth() * 0.15, image_file_png.GetHeight() * 0.15)
        image_file_png = wx.Bitmap(image_file_png)
        self.image = wx.StaticBitmap(self.top_panel, -1, image_file_png, pos=(340, 210),
                                     size=(image_file_png.GetWidth(), image_file_png.GetHeight()))

        # Creating panels: Every panel and text, which is shown in the application, is created in this piece of code.
        # Firstly, some font are specified to make the text more dynamic and clean.
        self.font_header = wx.Font(12, family=wx.FONTFAMILY_DECORATIVE, style=wx.FONTSTYLE_NORMAL, weight=wx.FONTWEIGHT_BOLD)
        self.font_header_1 = wx.Font(10, family=wx.FONTFAMILY_DECORATIVE, style=wx.FONTSTYLE_NORMAL, weight=wx.FONTWEIGHT_BOLD)
        self.font_normal = wx.Font(10, family=wx.FONTFAMILY_DECORATIVE, style=wx.FONTSTYLE_NORMAL, weight=wx.FONTWEIGHT_NORMAL)
        self.font_big = wx.Font(12, family=wx.FONTFAMILY_DECORATIVE, style=wx.FONTSTYLE_NORMAL, weight=wx.FONTWEIGHT_NORMAL)
        self.statistics_titles = ["Diameter Roller", "Sink Depth Roller"]

        for i in range(len(self.statistics_titles)):
            self.data_panel = wx.Panel(self.top_panel, -1, size=(465, 100), pos=(10, 10 + (1.2*i) * 60))
            self.data_panel_header = wx.StaticText(self.data_panel, label=self.statistics_titles[i], pos=(4, 2))
            if i == 0:
                self.slider_1 = wx.Slider(self.data_panel, -1, 30, 30, 60, pos=(0, 25), size=(300, -1), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS)
                self.slider_1.SetTickFreq(10)
                self.panel_output_1 = wx.Panel(self.data_panel, -1, style=wx.BORDER_SUNKEN, size=(40, 27), pos=(350, 20))
                self.text_1 = wx.StaticText(self.data_panel, label='mm', pos=(395, 23))
                self.text_1.SetFont(self.font_big)
                self.data_panel_slider_1 = wx.StaticText(self.panel_output_1, label='30', pos=(4, 2))
                self.data_panel_slider_1.SetFont(self.font_big)
            if i == 1:
                # TODO: AANPASSEN ALS WE DE ECHTE INDRUKKING WETEN
                self.slider_2 = wx.Slider(self.data_panel, -1, 30, 10, 70, pos=(0, 25), size=(300, -1), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS)
                self.slider_2.SetTickFreq(10)
                self.panel_output_2 = wx.Panel(self.data_panel, -1, style=wx.BORDER_SUNKEN, size=(40, 27), pos=(350, 20))
                self.text_1 = wx.StaticText(self.data_panel, label='mm', pos=(395, 23))
                self.text_1.SetFont(self.font_big)
                self.data_panel_slider_2 = wx.StaticText(self.panel_output_2, label='3', pos=(4, 2))
                self.data_panel_slider_2.SetFont(self.font_big)
            self.data_panel_header.SetFont(self.font_header)

        self.output_panel = wx.Panel(self.top_panel, -1, style=wx.BORDER_RAISED, size=(305, 160), pos=(10, 190))
        self.text = wx.StaticText(self.output_panel, label='Static Friction Force:', pos=(14, 21))
        self.text.SetFont(self.font_header_1)
        self.text = wx.StaticText(self.output_panel, label='Max. Rolling Resistance:', pos=(14, 118))
        self.text.SetFont(self.font_header_1)
        self.text = wx.StaticText(self.output_panel, label='Normal Force (Static): \n', pos=(14, 70))
        self.text.SetFont(self.font_header_1)
        self.panel_output_3 = wx.Panel(self.output_panel, -1, style=wx.BORDER_SUNKEN, size=(55, 27), pos=(220, 17))
        self.data_output_text = wx.StaticText(self.output_panel, label='N', pos=(280, 21))
        self.data_output_text.SetFont(self.font_big)
        self.data_panel_friction= wx.StaticText(self.panel_output_3, label='30', pos=(4, 2))
        self.data_panel_friction.SetFont(self.font_big)

        self.panel_output_4 = wx.Panel(self.output_panel, -1, style=wx.BORDER_SUNKEN, size=(55, 27), pos=(220, 65))
        self.data_output_text = wx.StaticText(self.output_panel, label='N', pos=(280, 69))
        self.data_output_text.SetFont(self.font_big)
        self.data_panel_normal_force = wx.StaticText(self.panel_output_4, label='300', pos=(4, 2))
        self.data_panel_normal_force.SetFont(self.font_big)

        self.panel_output_5 = wx.Panel(self.output_panel, -1, style=wx.BORDER_SUNKEN, size=(55, 27), pos=(220, 113))
        self.data_output_text = wx.StaticText(self.output_panel, label='N', pos=(280, 117))
        self.data_output_text.SetFont(self.font_big)
        self.data_panel_resistance = wx.StaticText(self.panel_output_5, label='30', pos=(4, 2))
        self.data_panel_resistance.SetFont(self.font_big)

        # Set start-up message
        welcome_dialog = wx.MessageDialog(self.top_panel,
                                          message="Welcome to the Tacx design tool. \nIf you have read the README.pdf, you're good to go. \nIf you haven't yet, please do.",
                                          caption="Welcome!")
        welcome_dialog.CenterOnParent()
        if welcome_dialog.ShowModal() == wx.OK:
            welcome_dialog.Destroy()
            return

        # Create status bar
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Right-click graph for zooming / graph options')
        self.top_panel.Bind(wx.EVT_ENTER_WINDOW, self.on_graph_hover)

        # Create parameter which contains all the tested data. These are the parameters which are fixed and will be
        # used to test the traction and resistance.
        # TODO: ALLES AANPASSEN NAAR RESULTATEN EN DE GEBRUIKTE PARAMETERS ALS DEZE BESCHIKBAAR ZIJN
        self.speed = [5, 10, 15, 20, 25, 30, 35, 40, 45]
        self.diameter = [30, 40, 50, 60]
        self.depth = [1, 2, 3, 4, 5, 6, 7]

        # Traction for each depth at each diameter
        # self.traction_dia_20mm = [4, 6, 8, 10, 12, 14, 16]
        self.traction_dia_30mm = [11.266, 43.93333333, 84.46666667, 119.2666667, 163.3333333, 216.96, 275.3]
        self.traction_dia_40mm = [21.93333333, 57.466666678, 91.8666666710, 143.733333312, 192.133333314, 248, 293.3333333]
        self.traction_dia_50mm = [22.533333337, 68.733333339, 111.266666711, 152.333333313, 212.466666715, 274.266666717, 312.066666719]
        self.traction_dia_60mm = [26.666666678, 56, 112.6, 164.133333314, 226.4, 273.466666718, 332.6]
        # self.traction_dia_70mm = [9, 11, 13, 15, 17, 19, 21]
        self.traction = [self.traction_dia_30mm, self.traction_dia_40mm, self.traction_dia_50mm, self.traction_dia_60mm]

        # Normal force for each depth at each diameter
        # self.force_dia_20mm = [4, 6, 8, 10, 12, 14, 16]
        self.force_dia_30mm = [11.880714745, 38.502201327, 70.126567419, 101.879505811, 133.06257313, 188.5, 237.9]
        self.force_dia_40mm = [11.716096146, 33.184797088, 55.3109619510, 91.6324982212, 125.989932614, 164.711920716, 193.505733318]
        self.force_dia_50mm = [11.59149137, 32.316324859, 53.4091589811, 78.0951891713, 107.046263215, 136.794991817, 171.297600219]
        self.force_dia_60mm = [8.7912101718, 18.7199386510, 40.89978712, 60.8439429914, 83.9226259816, 105.030285818, 131.489354320]
        # self.force_dia_70mm = [9, 11, 13, 15, 17, 19, 21]
        self.force = [self.force_dia_30mm, self.force_dia_40mm, self.force_dia_50mm, self.force_dia_60mm]

        # Resistance for each speed at a certain depth and diameter
        # self.resistance_dia_20mm_dept_1 = [0, 1, 1, 2, 3, 4]
        # self.resistance_dia_20mm_dept_2 = [0, 1, 2, 3, 4, 5]
        # self.resistance_dia_20mm_dept_3 = [0, 2, 3, 4, 5, 6]
        # self.resistance_dia_20mm_dept_4 = [0, 3, 4, 5, 6, 7]
        # self.resistance_dia_20mm_dept_5 = [0, 4, 5, 6, 7, 8]
        # self.resistance_dia_20mm_dept_6 = [0, 5, 6, 7, 8, 9]
        # self.resistance_dia_20mm_dept_7 = [0, 6, 7, 8, 9, 10]
        # self.resistance_dia_20mm = [self.resistance_dia_20mm_dept_1, self.resistance_dia_20mm_dept_2,
        #                             self.resistance_dia_20mm_dept_3, self.resistance_dia_20mm_dept_4,
        #                             self.resistance_dia_20mm_dept_5, self.resistance_dia_20mm_dept_6,
        #                             self.resistance_dia_20mm_dept_7]

        self.resistance_dia_30mm_dept_1 = self.resistance_at_diameter(0.86, 0.276)
        self.resistance_dia_30mm_dept_2 = self.resistance_at_diameter(1.29, 0.328)
        self.resistance_dia_30mm_dept_3 = self.resistance_at_diameter(2.47, 0.224)
        self.resistance_dia_30mm_dept_4 = self.resistance_at_diameter(3.39, 0.238)
        self.resistance_dia_30mm_dept_5 = self.resistance_at_diameter(5.09, 0.191)
        self.resistance_dia_30mm_dept_6 = self.resistance_at_diameter(5.46, 0.196)
        self.resistance_dia_30mm_dept_7 = self.resistance_at_diameter(8.1, 0.145)
        self.resistance_dia_30mm = [self.resistance_dia_30mm_dept_1, self.resistance_dia_30mm_dept_2,
                                    self.resistance_dia_30mm_dept_3, self.resistance_dia_30mm_dept_4,
                                    self.resistance_dia_30mm_dept_5, self.resistance_dia_30mm_dept_6,
                                    self.resistance_dia_30mm_dept_7]

        self.resistance_dia_40mm_dept_1 = self.resistance_at_diameter(0.374, 0.425)
        self.resistance_dia_40mm_dept_2 = self.resistance_at_diameter(1.31, 0.247)
        self.resistance_dia_40mm_dept_3 = self.resistance_at_diameter(2.29, 0.238)
        self.resistance_dia_40mm_dept_4 = self.resistance_at_diameter(3.05, 0.238)
        self.resistance_dia_40mm_dept_5 = self.resistance_at_diameter(6.08, 0.13)
        self.resistance_dia_40mm_dept_6 = self.resistance_at_diameter(5.46, 0.196)
        self.resistance_dia_40mm_dept_7 = self.resistance_at_diameter(8.1, 0.145)
        self.resistance_dia_40mm = [self.resistance_dia_40mm_dept_1, self.resistance_dia_40mm_dept_2,
                                    self.resistance_dia_40mm_dept_3, self.resistance_dia_40mm_dept_4,
                                    self.resistance_dia_40mm_dept_5, self.resistance_dia_40mm_dept_6,
                                    self.resistance_dia_40mm_dept_7]

        self.resistance_dia_50mmm_dept_1 = self.resistance_at_diameter(0.894/2, 0.246)
        self.resistance_dia_50mmm_dept_2 = self.resistance_at_diameter(0.894, 0.246)
        self.resistance_dia_50mmm_dept_3 = self.resistance_at_diameter(1.36, 0.278)
        self.resistance_dia_50mmm_dept_4 = self.resistance_at_diameter(2.27, 0.232)
        self.resistance_dia_50mmm_dept_5 = self.resistance_at_diameter(3.47, 0.203)
        self.resistance_dia_50mmm_dept_6 = self.resistance_at_diameter(4.7, 0.184)
        self.resistance_dia_50mmm_dept_7 = self.resistance_at_diameter(5.99, 0.172)
        self.resistance_dia_50mm = [self.resistance_dia_50mmm_dept_1, self.resistance_dia_50mmm_dept_2,
                                    self.resistance_dia_50mmm_dept_3, self.resistance_dia_50mmm_dept_4,
                                    self.resistance_dia_50mmm_dept_5, self.resistance_dia_50mmm_dept_6,
                                    self.resistance_dia_50mmm_dept_7]

        self.resistance_dia_60mmm_dept_1 = self.resistance_at_diameter(0.129, 0.538)
        self.resistance_dia_60mmm_dept_2 = self.resistance_at_diameter(0.364, 0.446)
        self.resistance_dia_60mmm_dept_3 = self.resistance_at_diameter(1.35, 0.222)
        self.resistance_dia_60mmm_dept_4 = self.resistance_at_diameter(1.92, 0.26)
        self.resistance_dia_60mmm_dept_5 = self.resistance_at_diameter(3.03, 0.211)
        self.resistance_dia_60mmm_dept_6 = self.resistance_at_diameter(4.4, 0.171)
        self.resistance_dia_60mmm_dept_7 = self.resistance_at_diameter(5.57, 0.168)
        self.resistance_dia_60mm = [self.resistance_dia_60mmm_dept_1, self.resistance_dia_60mmm_dept_2,
                                    self.resistance_dia_60mmm_dept_3, self.resistance_dia_60mmm_dept_4,
                                    self.resistance_dia_60mmm_dept_5, self.resistance_dia_60mmm_dept_6,
                                    self.resistance_dia_60mmm_dept_7]

        # self.resistance_dia_70mmm_dept_1 = [0, 5, 6, 7, 8, 9]
        # self.resistance_dia_70mmm_dept_2 = [0, 6, 7, 8, 9, 10]
        # self.resistance_dia_70mmm_dept_3 = [0, 7, 8, 9, 10, 11]
        # self.resistance_dia_70mmm_dept_4 = [0, 8, 9, 10, 11, 12]
        # self.resistance_dia_70mmm_dept_5 = [0, 9, 10, 11, 12, 13]
        # self.resistance_dia_70mmm_dept_6 = [0, 10, 11, 12, 13, 14]
        # self.resistance_dia_70mmm_dept_7 = [0, 11, 12, 13, 14, 15]
        # self.resistance_dia_70mm = [self.resistance_dia_70mmm_dept_1, self.resistance_dia_70mmm_dept_2,
        #                             self.resistance_dia_70mmm_dept_3, self.resistance_dia_70mmm_dept_4,
        #                             self.resistance_dia_70mmm_dept_5, self.resistance_dia_70mmm_dept_6,
        #                             self.resistance_dia_70mmm_dept_7]

        self.resistance = [self.resistance_dia_30mm, self.resistance_dia_40mm,
                           self.resistance_dia_50mm, self.resistance_dia_60mm]

        # Set events
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
        self.value_slider_2 = self.slider_2.GetValue()/10
        self.begin = True
        self.interpolation()

        # Create initial plot
        self.figure_panel = wx.Panel(self.top_panel, -1, size=(400, 400), pos=(480, -20))
        self.figure_panel.SetBackgroundColour((255, 255, 255))
        self.figure = wxmplot.PlotPanel(self.figure_panel, size=(400, 400), dpi=100, fontsize=2, axisbg='#FFFFFF')
        self.figure.oplot(numpy.array(self.speed), numpy.array(self.rolling_resistance), framecolor='white',xmin=0, xmax=50, ymin=0, ymax=16)

        # Figure cosmetics
        self.figure.set_xlabel("Velocity [km/h]")
        self.figure.set_ylabel("Rolling resistance [N]")

    def interpolation(self):
        """
        Interpolation to make a graph of the output values.
        """
        dummy = []
        dummy1 = []
        dummy2 = []
        dummy3 = []
        dummy10 = []
        self.rolling_resistance = []
        index_diameter = []
        index_depth = []

        for i in range(len(self.diameter)):
            for j in range(len(self.depth)):
                if abs(self.diameter[i] - self.value_slider_1) <= 9 and abs(self.depth[j] - self.value_slider_2) < 1:
                    index_diameter.append(i)
                    index_depth.append(j)
                    dummy1.append(self.traction[i][j])
                    dummy.append(self.resistance[i][j])
                    dummy10.append(self.force[i][j])

                    if self.diameter[i] == self.value_slider_1:
                        one_diameter = True
                        one_depth = False
                    elif self.depth[j] == self.value_slider_2:
                        one_depth = True
                        one_diameter = False
                    else:
                        one_depth = False
                        one_diameter = False

        if len(dummy) == 1:
            self.rolling_resistance = dummy[0]
        elif len(dummy) == 2:
            for k in range(len(dummy[0])):
                if one_depth:
                    self.rolling_resistance.append(dummy[0][k] + (dummy[0][k] - dummy[1][k]) /
                                                   (self.diameter[index_diameter[0]]-self.diameter[index_diameter[1]]) *
                                                   abs(self.diameter[index_diameter[0]]-self.value_slider_1))
                elif one_diameter:
                    self.rolling_resistance.append(dummy[0][k] + (dummy[0][k] - dummy[1][k]) /
                                                   (self.depth[index_depth[0]] - self.depth[index_depth[1]]) *
                                                   abs(self.depth[index_depth[0]] - self.value_slider_2))
        elif len(dummy) == 4:
            for k in range(len(dummy[0])):
                dummy2.append(dummy[0][k] + (dummy[0][k] - dummy[1][k]) / (self.depth[index_depth[0]]-self.depth[index_depth[1]]) * abs(self.depth[index_depth[0]]-self.value_slider_2))
                dummy3.append(dummy[2][k] + (dummy[2][k] - dummy[3][k]) / (self.depth[index_depth[0]]-self.depth[index_depth[1]]) * abs(self.depth[index_depth[0]]-self.value_slider_2))
                self.rolling_resistance.append(dummy2[k] + (dummy2[k] - dummy3[k]) / (self.diameter[index_diameter[0]]-self.diameter[index_diameter[2]]) * abs(self.diameter[index_diameter[0]]-self.value_slider_1))

        if len(dummy1) == 1:
            self.friction = dummy1[0]
        elif len(dummy1) == 2:
            if one_depth:
                self.friction = dummy1[0] + (dummy1[0] - dummy1[1])/ (self.diameter[index_diameter[0]] - self.diameter[index_diameter[1]]) * abs(self.diameter[index_diameter[0]] - self.value_slider_1)
            elif one_diameter:
                self.friction = dummy1[0] + (dummy1[0] - dummy1[1])/ (self.depth[index_depth[0]] - self.depth[index_depth[1]]) * abs(self.depth[index_depth[0]] - self.value_slider_2)
        elif len(dummy1) == 4:
            dummy4 = dummy1[0] + (dummy1[0] - dummy1[1])/ (self.depth[index_depth[0]] - self.depth[index_depth[1]]) * abs(self.depth[index_depth[0]] - self.value_slider_2)
            dummy5 = dummy1[2] + (dummy1[2] - dummy1[3])/ (self.depth[index_depth[0]] - self.depth[index_depth[1]]) * abs(self.depth[index_depth[0]] - self.value_slider_2)
            self.friction = dummy4 + (dummy4 - dummy5) / (self.diameter[index_diameter[0]]-self.diameter[index_diameter[2]]) * abs(self.diameter[index_diameter[0]]-self.value_slider_1)

        if len(dummy10) == 1:
            self.normal_force = dummy10[0]
        elif len(dummy10) == 2:
            if one_depth:
                self.normal_force = dummy10[0] + (dummy10[0] - dummy10[1])/ (self.diameter[index_diameter[0]] - self.diameter[index_diameter[1]]) * abs(self.diameter[index_diameter[0]] - self.value_slider_1)
            elif one_diameter:
                self.normal_force = dummy10[0] + (dummy10[0] - dummy10[1])/ (self.depth[index_depth[0]] - self.depth[index_depth[1]]) * abs(self.depth[index_depth[0]] - self.value_slider_2)
        elif len(dummy10) == 4:
            dummy6 = dummy10[0] + (dummy10[0] - dummy10[1])/ (self.depth[index_depth[0]] - self.depth[index_depth[1]]) * abs(self.depth[index_depth[0]] - self.value_slider_2)
            dummy7 = dummy10[2] + (dummy10[2] - dummy10[3])/ (self.depth[index_depth[0]] - self.depth[index_depth[1]]) * abs(self.depth[index_depth[0]] - self.value_slider_2)
            self.normal_force = dummy6 + (dummy6 - dummy7) / (self.diameter[index_diameter[0]]-self.diameter[index_diameter[2]]) * abs(self.diameter[index_diameter[0]]-self.value_slider_1)


        self.data_panel_resistance.SetLabel(str(round(max(self.rolling_resistance))))
        self.data_panel_friction.SetLabel(str(round(self.friction)))
        self.data_panel_normal_force.SetLabel(str(round(self.normal_force, 1)))

        # Updating the plot
        if self.begin == False:
            self.figure.update_line(1, numpy.array(self.speed), numpy.array(self.rolling_resistance), draw=True)

        self.begin = False


    def on_about(self, e):
        """"Message box with OK button"""
        prompted_dialog = wx.MessageDialog(self, "A file which can be used for designing a new Tacx \n"
                                                 "roller trainer and give an indication for the \n"
                                                 "rolling resistance and occurring friction. \n"
                                                 "\n\n"
                                                 "Built in Python 3.6.6, compiled with PyInstaller"
                                                 "\n"
                                                 "\n"
                                                 "Created by Tim de Jong and Jelle Haasnoot at Tacx B.V.",
                                           "About Tacx design tool", wx.OK)
        prompted_dialog.ShowModal()
        prompted_dialog.Destroy()

    def resistance_at_diameter(self,a,b):
        resistance_dummy = []
        for i in range(len(self.speed)):
            resistance_dummy.append(a*self.speed[i]**b)
        return resistance_dummy

    def on_slider_1(self, e):
        self.value_slider_1 = self.slider_1.GetValue()
        self.data_panel_slider_1.SetLabel(str(self.value_slider_1))
        self.interpolation()

    def on_slider_2(self, e):
        self.value_slider_2 = self.slider_2.GetValue()/10
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

    def on_graph_hover(self, event):
        self.statusbar.SetStatusText('Right-click to see zooming / graph options')
        event.Skip()


if __name__ == '__main__':
    Application = wx.App(False)
    frame = Main(None, 'Tacx design tool                                                                         '
                       '                                                                     [v1.0]').Show()
    Application.MainLoop()
