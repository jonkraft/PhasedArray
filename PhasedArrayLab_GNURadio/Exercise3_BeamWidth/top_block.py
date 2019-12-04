#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Dec  4 11:31:58 2019
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import ADAR1000_Dual_Sweeper
import doa
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
        self.samp_rate = samp_rate = 40000000
        self.Times_To_Average = Times_To_Average = 1
        self.Rx_gain = Rx_gain = 25
        self.Enable_Rx4 = Enable_Rx4 = 127
        self.Enable_Rx3 = Enable_Rx3 = 127
        self.Enable_Rx2 = Enable_Rx2 = 127
        self.Enable_Rx1 = Enable_Rx1 = 127
        self.Center_freq = Center_freq = 10492

        ##################################################
        # Blocks
        ##################################################
        self.PlutoTab = Qt.QTabWidget()
        self.PlutoTab_widget_0 = Qt.QWidget()
        self.PlutoTab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.PlutoTab_widget_0)
        self.PlutoTab_grid_layout_0 = Qt.QGridLayout()
        self.PlutoTab_layout_0.addLayout(self.PlutoTab_grid_layout_0)
        self.PlutoTab.addTab(self.PlutoTab_widget_0, 'Pluto_Controls')
        self.PlutoTab_widget_1 = Qt.QWidget()
        self.PlutoTab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.PlutoTab_widget_1)
        self.PlutoTab_grid_layout_1 = Qt.QGridLayout()
        self.PlutoTab_layout_1.addLayout(self.PlutoTab_grid_layout_1)
        self.PlutoTab.addTab(self.PlutoTab_widget_1, 'ADAR1000 Enable')
        self.top_grid_layout.addWidget(self.PlutoTab, 0,0,5,2)
        self._Times_To_Average_range = Range(1, 50, 1, 1, 10)
        self._Times_To_Average_win = RangeWidget(self._Times_To_Average_range, self.set_Times_To_Average, "Times_To_Average", "counter_slider", int)
        self.PlutoTab_grid_layout_0.addWidget(self._Times_To_Average_win, 2,0,1,2)
        self._Rx_gain_range = Range(0, 60, 1, 25, 10)
        self._Rx_gain_win = RangeWidget(self._Rx_gain_range, self.set_Rx_gain, "Rx_gain", "counter_slider", int)
        self.PlutoTab_grid_layout_0.addWidget(self._Rx_gain_win, 1,0,1,2)
        _Enable_Rx4_check_box = Qt.QCheckBox("Enable_Rx4")
        self._Enable_Rx4_choices = {True: 127, False: 0}
        self._Enable_Rx4_choices_inv = dict((v,k) for k,v in self._Enable_Rx4_choices.iteritems())
        self._Enable_Rx4_callback = lambda i: Qt.QMetaObject.invokeMethod(_Enable_Rx4_check_box, "setChecked", Qt.Q_ARG("bool", self._Enable_Rx4_choices_inv[i]))
        self._Enable_Rx4_callback(self.Enable_Rx4)
        _Enable_Rx4_check_box.stateChanged.connect(lambda i: self.set_Enable_Rx4(self._Enable_Rx4_choices[bool(i)]))
        self.PlutoTab_grid_layout_1.addWidget(_Enable_Rx4_check_box, 3,0,1,1)
        _Enable_Rx3_check_box = Qt.QCheckBox("Enable_Rx3")
        self._Enable_Rx3_choices = {True: 127, False: 0}
        self._Enable_Rx3_choices_inv = dict((v,k) for k,v in self._Enable_Rx3_choices.iteritems())
        self._Enable_Rx3_callback = lambda i: Qt.QMetaObject.invokeMethod(_Enable_Rx3_check_box, "setChecked", Qt.Q_ARG("bool", self._Enable_Rx3_choices_inv[i]))
        self._Enable_Rx3_callback(self.Enable_Rx3)
        _Enable_Rx3_check_box.stateChanged.connect(lambda i: self.set_Enable_Rx3(self._Enable_Rx3_choices[bool(i)]))
        self.PlutoTab_grid_layout_1.addWidget(_Enable_Rx3_check_box, 2,0,1,1)
        _Enable_Rx2_check_box = Qt.QCheckBox("Enable_Rx2")
        self._Enable_Rx2_choices = {True: 127, False: 0}
        self._Enable_Rx2_choices_inv = dict((v,k) for k,v in self._Enable_Rx2_choices.iteritems())
        self._Enable_Rx2_callback = lambda i: Qt.QMetaObject.invokeMethod(_Enable_Rx2_check_box, "setChecked", Qt.Q_ARG("bool", self._Enable_Rx2_choices_inv[i]))
        self._Enable_Rx2_callback(self.Enable_Rx2)
        _Enable_Rx2_check_box.stateChanged.connect(lambda i: self.set_Enable_Rx2(self._Enable_Rx2_choices[bool(i)]))
        self.PlutoTab_grid_layout_1.addWidget(_Enable_Rx2_check_box, 1,0,1,1)
        _Enable_Rx1_check_box = Qt.QCheckBox("Enable_Rx1")
        self._Enable_Rx1_choices = {True: 127, False: 0}
        self._Enable_Rx1_choices_inv = dict((v,k) for k,v in self._Enable_Rx1_choices.iteritems())
        self._Enable_Rx1_callback = lambda i: Qt.QMetaObject.invokeMethod(_Enable_Rx1_check_box, "setChecked", Qt.Q_ARG("bool", self._Enable_Rx1_choices_inv[i]))
        self._Enable_Rx1_callback(self.Enable_Rx1)
        _Enable_Rx1_check_box.stateChanged.connect(lambda i: self.set_Enable_Rx1(self._Enable_Rx1_choices[bool(i)]))
        self.PlutoTab_grid_layout_1.addWidget(_Enable_Rx1_check_box, 0,0,1,1)
        self._Center_freq_range = Range(10000, 11000, 0.1, 10492, 10)
        self._Center_freq_win = RangeWidget(self._Center_freq_range, self.set_Center_freq, 'Signal Freq (MHz)', "counter_slider", float)
        self.PlutoTab_grid_layout_0.addWidget(self._Center_freq_win, 0,0,1,2)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            1,
            qtgui.NUM_GRAPH_NONE,
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
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 4, 2, 1, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	140, #size
        	"Peak Signal vs Steering Angle", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-50, 0)
        self.qtgui_const_sink_x_0.set_x_axis(-80, 80)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(True)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)
        
        if not False:
          self.qtgui_const_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 0,2,4,3)
        self.doa_qt_compass_0 = doa.compass("", -90, 90, 10, 90)
        self.top_grid_layout.addLayout(self.doa_qt_compass_0.this_layout, 4, 2, 3, 3)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(500, 0.002, samp_rate)
        self.ADAR1000_Dual_Sweeper = ADAR1000_Dual_Sweeper.blk(LO_freq=int((Center_freq-5810)*1000000), TX_freq=5810000000, SampleRate=int(samp_rate), Rx_gain=int(Rx_gain), Averages=int(Times_To_Average), Taper=0, SymTaper=0, PhaseCal=0, SignalFreq=int(Center_freq*1000000), RxGain1=int(Enable_Rx1), RxGain2=int(Enable_Rx2), RxGain3=int(Enable_Rx3), RxGain4=int(Enable_Rx4), Rx1_cal=0, Rx2_cal=0, Rx3_cal=0, Rx4_cal=0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.ADAR1000_Dual_Sweeper, 1), (self.blocks_throttle_0, 0))    
        self.connect((self.ADAR1000_Dual_Sweeper, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_moving_average_xx_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.doa_qt_compass_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.ADAR1000_Dual_Sweeper.SampleRate = int(self.samp_rate)

    def get_Times_To_Average(self):
        return self.Times_To_Average

    def set_Times_To_Average(self, Times_To_Average):
        self.Times_To_Average = Times_To_Average
        self.ADAR1000_Dual_Sweeper.Averages = int(self.Times_To_Average)

    def get_Rx_gain(self):
        return self.Rx_gain

    def set_Rx_gain(self, Rx_gain):
        self.Rx_gain = Rx_gain
        self.ADAR1000_Dual_Sweeper.Rx_gain = int(self.Rx_gain)

    def get_Enable_Rx4(self):
        return self.Enable_Rx4

    def set_Enable_Rx4(self, Enable_Rx4):
        self.Enable_Rx4 = Enable_Rx4
        self._Enable_Rx4_callback(self.Enable_Rx4)
        self.ADAR1000_Dual_Sweeper.RxGain4 = int(self.Enable_Rx4)

    def get_Enable_Rx3(self):
        return self.Enable_Rx3

    def set_Enable_Rx3(self, Enable_Rx3):
        self.Enable_Rx3 = Enable_Rx3
        self._Enable_Rx3_callback(self.Enable_Rx3)
        self.ADAR1000_Dual_Sweeper.RxGain3 = int(self.Enable_Rx3)

    def get_Enable_Rx2(self):
        return self.Enable_Rx2

    def set_Enable_Rx2(self, Enable_Rx2):
        self.Enable_Rx2 = Enable_Rx2
        self._Enable_Rx2_callback(self.Enable_Rx2)
        self.ADAR1000_Dual_Sweeper.RxGain2 = int(self.Enable_Rx2)

    def get_Enable_Rx1(self):
        return self.Enable_Rx1

    def set_Enable_Rx1(self, Enable_Rx1):
        self.Enable_Rx1 = Enable_Rx1
        self._Enable_Rx1_callback(self.Enable_Rx1)
        self.ADAR1000_Dual_Sweeper.RxGain1 = int(self.Enable_Rx1)

    def get_Center_freq(self):
        return self.Center_freq

    def set_Center_freq(self, Center_freq):
        self.Center_freq = Center_freq
        self.ADAR1000_Dual_Sweeper.LO_freq = int((self.Center_freq-5810)*1000000)


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
