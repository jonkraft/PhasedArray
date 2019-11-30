#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Nov 21 12:41:20 2019
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
        self.TX_freq = TX_freq = 5.81
        self.Pluto_Gain = Pluto_Gain = 20
        self.Center_freq = Center_freq = 10500

        ##################################################
        # Blocks
        ##################################################
        self._Pluto_Gain_range = Range(10, 60, 1, 20, 200)
        self._Pluto_Gain_win = RangeWidget(self._Pluto_Gain_range, self.set_Pluto_Gain, "Pluto_Gain", "counter_slider", int)
        self.top_layout.addWidget(self._Pluto_Gain_win)
        self._Center_freq_range = Range(10000, 11500, 5, 10500, 200)
        self._Center_freq_win = RangeWidget(self._Center_freq_range, self.set_Center_freq, 'Signal Source (MHz)', "counter_slider", float)
        self.top_layout.addWidget(self._Center_freq_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	int(Center_freq*1000000), #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	False, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(True)
        
        
          
        self.pluto_source_0 = iio.pluto_source('192.168.2.1', int(int((Center_freq-TX_freq*1000)*1000000)), int(int(samp_rate)), int(int(samp_rate/2)), int(32*256), False, True, True, "manual", int(Pluto_Gain), '', True)
        self.pluto_sink_0 = iio.pluto_sink('192.168.2.1', int(int(TX_freq*1000000000)), int(int(samp_rate)), int(int(300000)), int(2**18), True, 3, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000000, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_1, 0), (self.pluto_sink_0, 0))    
        self.connect((self.pluto_source_0, 0), (self.qtgui_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(int(self.Center_freq*1000000), self.samp_rate)
        self.pluto_source_0.set_params(int(int((self.Center_freq-self.TX_freq*1000)*1000000)), int(int(self.samp_rate)), int(int(self.samp_rate/2)), False, True, True, "manual", int(self.Pluto_Gain), '', True)
        self.pluto_sink_0.set_params(int(int(self.TX_freq*1000000000)), int(int(self.samp_rate)), int(int(300000)), 3, '', True)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)

    def get_TX_freq(self):
        return self.TX_freq

    def set_TX_freq(self, TX_freq):
        self.TX_freq = TX_freq
        self.pluto_source_0.set_params(int(int((self.Center_freq-self.TX_freq*1000)*1000000)), int(int(self.samp_rate)), int(int(self.samp_rate/2)), False, True, True, "manual", int(self.Pluto_Gain), '', True)
        self.pluto_sink_0.set_params(int(int(self.TX_freq*1000000000)), int(int(self.samp_rate)), int(int(300000)), 3, '', True)

    def get_Pluto_Gain(self):
        return self.Pluto_Gain

    def set_Pluto_Gain(self, Pluto_Gain):
        self.Pluto_Gain = Pluto_Gain
        self.pluto_source_0.set_params(int(int((self.Center_freq-self.TX_freq*1000)*1000000)), int(int(self.samp_rate)), int(int(self.samp_rate/2)), False, True, True, "manual", int(self.Pluto_Gain), '', True)

    def get_Center_freq(self):
        return self.Center_freq

    def set_Center_freq(self, Center_freq):
        self.Center_freq = Center_freq
        self.qtgui_sink_x_0.set_frequency_range(int(self.Center_freq*1000000), self.samp_rate)
        self.pluto_source_0.set_params(int(int((self.Center_freq-self.TX_freq*1000)*1000000)), int(int(self.samp_rate)), int(int(self.samp_rate/2)), False, True, True, "manual", int(self.Pluto_Gain), '', True)


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
