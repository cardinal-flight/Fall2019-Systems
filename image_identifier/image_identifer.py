
import wx
import cv2
import pdb
import os

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg
from matplotlib.figure import Figure

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, id=wx.ID_ANY, title='Image Identifier', size=(500,500))
        
        # Dummy variables
        self.points = []
        self.xmin = None
        self.xmax = None
        self.ymin = None
        self.ymax = None
        self.dimensions = None
        self.outfile_paths = []
        self.outfile_xmin = []
        self.outfile_ymin = []
        self.outfile_xmax = []
        self.outfile_ymax = []
        
        # Panels
        graph_panel = wx.Panel(self)
        widget_panel = wx.Panel(self)
        
        # Plot stuff
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(graph_panel, wx.ID_ANY, self.figure)
        
        # Button stuff
        ok_button = wx.Button(widget_panel, id=wx.ID_ANY, label='Ok')
        cancel_button = wx.Button(widget_panel, id=wx.ID_ANY, label='Select Again')
        ok_button.Bind(wx.EVT_BUTTON, self.on_ok_button)
        cancel_button.Bind(wx.EVT_BUTTON, self. on_cancel_button)
        
        # Sizers
        gbs = wx.BoxSizer(wx.HORIZONTAL)
        gbs.Add(self.canvas, 1, wx.EXPAND)
        
        wbs = wx.BoxSizer(wx.HORIZONTAL)
        wbs.Add(ok_button, -1, wx.EXPAND)
        wbs.Add(cancel_button, -1, wx.EXPAND)
        
        bs = wx.BoxSizer(wx.VERTICAL)
        bs.Add(widget_panel, 1, wx.EXPAND)
        bs.Add(graph_panel, 2, wx.EXPAND)
        
        graph_panel.SetSizer(gbs)
        widget_panel.SetSizer(wbs)
        self.SetSizer(bs)
        
        # Call method to show image in plot
        self.index = 0
        self.paths = self.handle_filenames()
        self.add_picture(self.paths[self.index])
        
        # Connect clicking event
        self.canvas.mpl_connect('button_press_event', self.pick_point)
        

    def add_picture(self, pic_path):
        self.axes.clear()
        my_pic = cv2.imread(pic_path, cv2.IMREAD_COLOR)
        self.dimensions = my_pic.shape
        self.axes.imshow(my_pic)
        self.canvas.draw()
    
    def handle_filenames(self):
        cur_dir = os.getcwd()
        all_paths = os.listdir(cur_dir)
        paths = []
        for pathname in all_paths:
            if pathname.endswith('.jpg'):
                paths.append(pathname)
        return paths
    
    def pick_point(self, event):
        if event.inaxes:
            x, y = event.xdata, event.ydata
            self.points.append([x,y])
            if len(self.points) == 2:
                self.set_max_min()
                self.draw_box()
    
    def draw_box(self):
        self.axes.axvline(self.xmin, ymin=(self.dimensions[0] - self.ymin)/self.dimensions[0], ymax=(self.dimensions[0] - self.ymax)/self.dimensions[0], c='r')
        self.axes.axhline(self.ymin, xmin=self.xmin/self.dimensions[1], xmax=self.xmax/self.dimensions[1], c='r')
        self.axes.axvline(self.xmax, ymin=(self.dimensions[0] - self.ymin)/self.dimensions[0], ymax=(self.dimensions[0] - self.ymax)/self.dimensions[0], c='r')
        self.axes.axhline(self.ymax, xmin=self.xmin/self.dimensions[1], xmax=self.xmax/self.dimensions[1], c='r')
        self.canvas.draw()

    
    def set_max_min(self):
        x_val = [self.points[0][0],self.points[1][0]]
        y_val = [self.points[0][1],self.points[1][1]]
        
        self.xmin = int(round(min(x_val)))
        self.xmax = int(round(max(x_val)))
        self.ymin = int(round(min(y_val)))
        self.ymax = int(round(max(y_val)))
        
    def on_ok_button(self, event):
        print('Okay')
        self.outfile_paths.append(self.paths[self.index])
        # Pass coordinates and data
        self.outfile_xmin.append(self.xmin)
        self.outfile_ymin.append(self.ymin)
        self.outfile_xmax.append(self.xmax)
        self.outfile_ymax.append(self.ymax)
        
        self.index += 1
        if self.index < len(self.paths):        
            # Clear variables and move to next picture
            self.points = []
            self.xmin = None
            self.xmax = None
            self.ymin = None
            self.ymax = None
            self.add_picture(self.paths[self.index])
        else:
            self.write_outfile()
            print('info.dat has been created in the current working directory.')
            
    
    def on_cancel_button(self, event):
        self.points = []
        self.xmin = None
        self.xmax = None
        self.ymin = None
        self.ymax = None
        del self.axes.lines[:]
        self.canvas.draw()
        
    def write_outfile(self):
        outfile = open('info.dat', 'w')
        for i in range(len(self.outfile_paths)):
            outfile.write('{}  1  {} {} {} {}\n'.format(self.outfile_paths[i], self.outfile_xmin[i], self.outfile_ymin[i], self.outfile_xmax[i], self.outfile_ymax[i]))
        
        
if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()