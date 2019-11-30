#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Nov 21 12:54:09 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import iio
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import epy_block_0
import epy_module_0  # embedded python module
import sip
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.Rx4_Cal = Rx4_Cal = 0
        self.Rx3_Cal = Rx3_Cal = 0
        self.Rx2_Cal = Rx2_Cal = 0
        self.Rx1_Cal = Rx1_Cal = 0
        self.Phase_Delta = Phase_Delta = 0
        self.samp_rate = samp_rate = int(40000000)
        self.TX_freq = TX_freq = 5.81
        self.RxGain = RxGain = 30
        self.Rx4 = Rx4 = ((Phase_Delta*3+Rx4_Cal) % 360)
        self.Rx3 = Rx3 = ((Phase_Delta*2+Rx3_Cal) % 360)
        self.Rx2 = Rx2 = ((Phase_Delta*1+Rx2_Cal) % 360)
        self.Rx1 = Rx1 = ((Phase_Delta*0+Rx1_Cal) % 360)
        self.Center_freq = Center_freq = 10819
        self.BlankSpacerToFormatTab = BlankSpacerToFormatTab = "  "

        ##################################################
        # Blocks
        ##################################################
        self.ControlTab = Qt.QTabWidget()
        self.ControlTab_widget_0 = Qt.QWidget()
        self.ControlTab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ControlTab_widget_0)
        self.ControlTab_grid_layout_0 = Qt.QGridLayout()
        self.ControlTab_layout_0.addLayout(self.ControlTab_grid_layout_0)
        self.ControlTab.addTab(self.ControlTab_widget_0, 'Pluto Control')
        self.ControlTab_widget_1 = Qt.QWidget()
        self.ControlTab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ControlTab_widget_1)
        self.ControlTab_grid_layout_1 = Qt.QGridLayout()
        self.ControlTab_layout_1.addLayout(self.ControlTab_grid_layout_1)
        self.ControlTab.addTab(self.ControlTab_widget_1, 'ADAR1000 Phase Control')
        self.top_grid_layout.addWidget(self.ControlTab, 7,0, 7,7)
        self._RxGain_range = Range(0, 60, 1, 30, 200)
        self._RxGain_win = RangeWidget(self._RxGain_range, self.set_RxGain, "RxGain", "counter_slider", float)
        self.ControlTab_grid_layout_0.addWidget(self._RxGain_win, 1,0)
        self._Rx4_Cal_range = Range(0, 357.1875, 2.8125, 0, 200)
        self._Rx4_Cal_win = RangeWidget(self._Rx4_Cal_range, self.set_Rx4_Cal, 'Rx4_Phase', "counter_slider", float)
        self.ControlTab_grid_layout_1.addWidget(self._Rx4_Cal_win, 4,1,1,5)
        self._Rx3_Cal_range = Range(0, 357.1875, 2.8125, 0, 200)
        self._Rx3_Cal_win = RangeWidget(self._Rx3_Cal_range, self.set_Rx3_Cal, 'Rx3_Phase', "counter_slider", float)
        self.ControlTab_grid_layout_1.addWidget(self._Rx3_Cal_win, 3,1,1,5)
        self._Rx2_Cal_range = Range(0, 357.1875, 2.8125, 0, 200)
        self._Rx2_Cal_win = RangeWidget(self._Rx2_Cal_range, self.set_Rx2_Cal, 'Rx2_Phase', "counter_slider", float)
        self.ControlTab_grid_layout_1.addWidget(self._Rx2_Cal_win, 2,1,1,5)
        self._Rx1_Cal_range = Range(0, 357.1875, 2.8125, 0, 200)
        self._Rx1_Cal_win = RangeWidget(self._Rx1_Cal_range, self.set_Rx1_Cal, 'Rx1_Phase', "counter_slider", float)
        self.ControlTab_grid_layout_1.addWidget(self._Rx1_Cal_win, 1,1,1,5)
        self._Phase_Delta_range = Range(-199.6875, 199.6875, 2.8125, 0, 200)
        self._Phase_Delta_win = RangeWidget(self._Phase_Delta_range, self.set_Phase_Delta, "Phase_Delta", "counter_slider", float)
        self.ControlTab_grid_layout_1.addWidget(self._Phase_Delta_win, 0,1,1,5)
        self._Center_freq_range = Range(10000, 11000, 0.1, 10819, 10)
        self._Center_freq_win = RangeWidget(self._Center_freq_range, self.set_Center_freq, 'Signal Freq (MHz)', "counter_slider", float)
        self.ControlTab_grid_layout_0.addWidget(self._Center_freq_win, 0,0)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	int(Center_freq*1000000), #fc
        	int(samp_rate), #bw
        	"", #name
        	True, #plotfreq
        	False, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win, 0, 0, 6, 8)
        
        self.qtgui_sink_x_0.enable_rf_freq(False)
        
        
          
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.1)
        self.qtgui_number_sink_0.set_title('SteeringAngle')
        
        labels = ['   ', '', '', '', '',
                  '', '', '', '', '']
        units = ['deg', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -90)
            self.qtgui_number_sink_0.set_max(i, 90)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 5, 2, 1, 4)
        self.pluto_source_0 = iio.pluto_source('', int(int((Center_freq/1000-TX_freq)*1000000000)), int(int(samp_rate)), int(int(samp_rate/4)), int(2**10), False, True, True, "manual", int(RxGain), '', True)
        self.pluto_sink_0 = iio.pluto_sink('', int(int(TX_freq*1000000000)), int(int(samp_rate)), int(300000), int(2**16), True, 3, '', True)
        self.epy_block_0 = epy_block_0.blk(PhaseDelta=Phase_Delta, SignalFreq=int(Center_freq*1000000), UpdateRate=0.1, Rx1_Phase_Cal=Rx1_Cal, Rx2_Phase_Cal=Rx2_Cal, Rx3_Phase_Cal=Rx3_Cal, Rx4_Phase_Cal=Rx4_Cal)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, int(100000), 1, 0)
        self._Rx4_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._Rx4_formatter = None
        else:
          self._Rx4_formatter = lambda x: x
        
        self._Rx4_tool_bar.addWidget(Qt.QLabel("Rx4"+": "))
        self._Rx4_label = Qt.QLabel(str(self._Rx4_formatter(self.Rx4)))
        self._Rx4_tool_bar.addWidget(self._Rx4_label)
        self.ControlTab_grid_layout_1.addWidget(self._Rx4_tool_bar, 4,0,1,1)
          
        self._Rx3_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._Rx3_formatter = None
        else:
          self._Rx3_formatter = lambda x: x
        
        self._Rx3_tool_bar.addWidget(Qt.QLabel("Rx3"+": "))
        self._Rx3_label = Qt.QLabel(str(self._Rx3_formatter(self.Rx3)))
        self._Rx3_tool_bar.addWidget(self._Rx3_label)
        self.ControlTab_grid_layout_1.addWidget(self._Rx3_tool_bar, 3,0,1,1)
          
        self._Rx2_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._Rx2_formatter = None
        else:
          self._Rx2_formatter = lambda x: x
        
        self._Rx2_tool_bar.addWidget(Qt.QLabel("Rx2"+": "))
        self._Rx2_label = Qt.QLabel(str(self._Rx2_formatter(self.Rx2)))
        self._Rx2_tool_bar.addWidget(self._Rx2_label)
        self.ControlTab_grid_layout_1.addWidget(self._Rx2_tool_bar, 2,0,1,1)
          
        self._Rx1_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._Rx1_formatter = None
        else:
          self._Rx1_formatter = lambda x: x
        
        self._Rx1_tool_bar.addWidget(Qt.QLabel("Rx1"+": "))
        self._Rx1_label = Qt.QLabel(str(self._Rx1_formatter(self.Rx1)))
        self._Rx1_tool_bar.addWidget(self._Rx1_label)
        self.ControlTab_grid_layout_1.addWidget(self._Rx1_tool_bar, 1,0,1,1)
          
        self._BlankSpacerToFormatTab_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._BlankSpacerToFormatTab_formatter = None
        else:
          self._BlankSpacerToFormatTab_formatter = lambda x: x
        
        self._BlankSpacerToFormatTab_tool_bar.addWidget(Qt.QLabel("  "+": "))
        self._BlankSpacerToFormatTab_label = Qt.QLabel(str(self._BlankSpacerToFormatTab_formatter(self.BlankSpacerToFormatTab)))
        self._BlankSpacerToFormatTab_tool_bar.addWidget(self._BlankSpacerToFormatTab_label)
        self.ControlTab_grid_layout_0.addWidget(self._BlankSpacerToFormatTab_tool_bar, 2,0,4,5)
          

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_1, 0), (self.pluto_sink_0, 0))    
        self.connect((self.epy_block_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.pluto_source_0, 0), (self.qtgui_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_Rx4_Cal(self):
        return self.Rx4_Cal

    def set_Rx4_Cal(self, Rx4_Cal):
        self.Rx4_Cal = Rx4_Cal
        self.epy_block_0.Rx4_Phase_Cal = self.Rx4_Cal
        self.set_Rx4(self._Rx4_formatter(((self.Phase_Delta*3+self.Rx4_Cal) % 360)))

    def get_Rx3_Cal(self):
        return self.Rx3_Cal

    def set_Rx3_Cal(self, Rx3_Cal):
        self.Rx3_Cal = Rx3_Cal
        self.epy_block_0.Rx3_Phase_Cal = self.Rx3_Cal
        self.set_Rx3(self._Rx3_formatter(((self.Phase_Delta*2+self.Rx3_Cal) % 360)))

    def get_Rx2_Cal(self):
        return self.Rx2_Cal

    def set_Rx2_Cal(self, Rx2_Cal):
        self.Rx2_Cal = Rx2_Cal
        self.epy_block_0.Rx2_Phase_Cal = self.Rx2_Cal
        self.set_Rx2(self._Rx2_formatter(((self.Phase_Delta*1+self.Rx2_Cal) % 360)))

    def get_Rx1_Cal(self):
        return self.Rx1_Cal

    def set_Rx1_Cal(self, Rx1_Cal):
        self.Rx1_Cal = Rx1_Cal
        self.epy_block_0.Rx1_Phase_Cal = self.Rx1_Cal
        self.set_Rx1(self._Rx1_formatter(((self.Phase_Delta*0+self.Rx1_Cal) % 360)))

    def get_Phase_Delta(self):
        return self.Phase_Delta

    def set_Phase_Delta(self, Phase_Delta):
        self.Phase_Delta = Phase_Delta
        self.epy_block_0.PhaseDelta = self.Phase_Delta
        self.set_Rx4(self._Rx4_formatter(((self.Phase_Delta*3+self.Rx4_Cal) % 360)))
        self.set_Rx3(self._Rx3_formatter(((self.Phase_Delta*2+self.Rx3_Cal) % 360)))
        self.set_Rx2(self._Rx2_formatter(((self.Phase_Delta*1+self.Rx2_Cal) % 360)))
        self.set_Rx1(self._Rx1_formatter(((self.Phase_Delta*0+self.Rx1_Cal) % 360)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(int(self.Center_freq*1000000), int(self.samp_rate))
        self.pluto_source_0.set_params(int(int((self.Center_freq/1000-self.TX_freq)*1000000000)), int(int(self.samp_rate)), int(int(self.samp_rate/4)), False, True, True, "manual", int(self.RxGain), '', True)
        self.pluto_sink_0.set_params(int(int(self.TX_freq*1000000000)), int(int(self.samp_rate)), int(300000), 3, '', True)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)

    def get_TX_freq(self):
        return self.TX_freq

    def set_TX_freq(self, TX_freq):
        self.TX_freq = TX_freq
        self.pluto_source_0.set_params(int(int((self.Center_freq/1000-self.TX_freq)*1000000000)), int(int(self.samp_rate)), int(int(self.samp_rate/4)), False, True, True, "manual", int(self.RxGain), '', True)
        self.pluto_sink_0.set_params(int(int(self.TX_freq*1000000000)), int(int(self.samp_rate)), int(300000), 3, '', True)

    def get_RxGain(self):
        return self.RxGain

    def set_RxGain(self, RxGain):
        self.RxGain = RxGain
        self.pluto_source_0.set_params(int(int((self.Center_freq/1000-self.TX_freq)*1000000000)), int(int(self.samp_rate)), int(int(self.samp_rate/4)), False, True, True, "manual", int(self.RxGain), '', True)

    def get_Rx4(self):
        return self.Rx4

    def set_Rx4(self, Rx4):
        self.Rx4 = Rx4
        Qt.QMetaObject.invokeMethod(self._Rx4_label, "setText", Qt.Q_ARG("QString", str(self.Rx4)))

    def get_Rx3(self):
        return self.Rx3

    def set_Rx3(self, Rx3):
        self.Rx3 = Rx3
        Qt.QMetaObject.invokeMethod(self._Rx3_label, "setText", Qt.Q_ARG("QString", str(self.Rx3)))

    def get_Rx2(self):
        return self.Rx2

    def set_Rx2(self, Rx2):
        self.Rx2 = Rx2
        Qt.QMetaObject.invokeMethod(self._Rx2_label, "setText", Qt.Q_ARG("QString", str(self.Rx2)))

    def get_Rx1(self):
        return self.Rx1

    def set_Rx1(self, Rx1):
        self.Rx1 = Rx1
        Qt.QMetaObject.invokeMethod(self._Rx1_label, "setText", Qt.Q_ARG("QString", str(self.Rx1)))

    def get_Center_freq(self):
        return self.Center_freq

    def set_Center_freq(self, Center_freq):
        self.Center_freq = Center_freq
        self.qtgui_sink_x_0.set_frequency_range(int(self.Center_freq*1000000), int(self.samp_rate))
        self.pluto_source_0.set_params(int(int((self.Center_freq/1000-self.TX_freq)*1000000000)), int(int(self.samp_rate)), int(int(self.samp_rate/4)), False, True, True, "manual", int(self.RxGain), '', True)

    def get_BlankSpacerToFormatTab(self):
        return self.BlankSpacerToFormatTab

    def set_BlankSpacerToFormatTab(self, BlankSpacerToFormatTab):
        self.BlankSpacerToFormatTab = BlankSpacerToFormatTab
        Qt.QMetaObject.invokeMethod(self._BlankSpacerToFormatTab_label, "setText", Qt.Q_ARG("QString", str(self.BlankSpacerToFormatTab)))


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
