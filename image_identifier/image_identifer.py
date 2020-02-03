
import wx
import cv2
import pdb
import msvcrt

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg
from matplotlib.figure import Figure

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, id=wx.ID_ANY, title='Christine can lick my balls', size=(500,500))
        
        # Dummy variables
        self.points = []
        self.xin = None
        self.xmax = None
        self.ymin = None
        self.ymax = None
        self.dimensions = None
        
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
        self.add_picture()
        
        # Connect clicking event
        self.canvas.mpl_connect('button_press_event', self.pick_point)
        

    def add_picture(self):
        pic_path = 'cage.jpg'
        my_pic = cv2.imread(pic_path, cv2.IMREAD_COLOR)
        self.dimensions = my_pic.shape

        self.axes.imshow(my_pic)
    
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
        
        self.xmin = min(x_val)
        self.xmax = max(x_val)
        self.ymin = min(y_val)
        self.ymax = max(y_val)
        
    def on_ok_button(self, event):
        print('Okay')
    
    def on_cancel_button(self, event):
        self.points = []
        self.xin = None
        self.xmax = None
        self.ymin = None
        self.ymax = None
        del self.axes.lines[:]
        self.canvas.draw()
        
if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()