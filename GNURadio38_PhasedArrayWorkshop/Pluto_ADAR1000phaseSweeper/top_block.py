#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Beamformer_Ex4
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
import sip
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio.qtgui import Range, RangeWidget
import epy_block_0

from gnuradio import qtgui

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Beamformer_Ex4")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Beamformer_Ex4")
        qtgui.util.check_set_qss()
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

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.Center_freq = Center_freq = 10508.0
        self.BW = BW = 0
        self.variable_qtgui_label_0_0_0_0_0_0 = variable_qtgui_label_0_0_0_0_0_0 = ("%d" % (Center_freq)).rjust(16)
        self.variable_qtgui_label_0_0_0_0_0 = variable_qtgui_label_0_0_0_0_0 = ("%d" % ((Center_freq-BW))).rjust(10)
        self.variable_qtgui_label_0_0_0_0 = variable_qtgui_label_0_0_0_0 = ("%d" % (BW)).rjust(28)
        self.variable_qtgui_label_0_0_0 = variable_qtgui_label_0_0_0 = ("%d" % ((Center_freq - 5810))).rjust(27)
        self.variable_qtgui_label_0_0 = variable_qtgui_label_0_0 = ("%d" % (5810)).rjust(32)
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = ("%d" % (Center_freq)).rjust(20)
        self.samp_rate = samp_rate = 40000000
        self.Times_To_Average = Times_To_Average = 1
        self.SymmetricTaper = SymmetricTaper = 0
        self.Rx_gain = Rx_gain = 20
        self.Rx4_Cal = Rx4_Cal = 0
        self.Rx4Gain = Rx4Gain = 127
        self.Rx3_Cal = Rx3_Cal = 0
        self.Rx3Gain = Rx3Gain = 127
        self.Rx2_Cal = Rx2_Cal = 0
        self.Rx2Gain = Rx2Gain = 127
        self.Rx1_Cal = Rx1_Cal = 0
        self.Rx1Gain = Rx1Gain = 127
        self.IgnorePhaseCals = IgnorePhaseCals = 0
        self.BeamTaper = BeamTaper = 0

        ##################################################
        # Blocks
        ##################################################
        self.ControlTab = Qt.QTabWidget()
        self.ControlTab_widget_0 = Qt.QWidget()
        self.ControlTab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ControlTab_widget_0)
        self.ControlTab_grid_layout_0 = Qt.QGridLayout()
        self.ControlTab_layout_0.addLayout(self.ControlTab_grid_layout_0)
        self.ControlTab.addTab(self.ControlTab_widget_0, 'Pluto_Controls')
        self.ControlTab_widget_1 = Qt.QWidget()
        self.ControlTab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ControlTab_widget_1)
        self.ControlTab_grid_layout_1 = Qt.QGridLayout()
        self.ControlTab_layout_1.addLayout(self.ControlTab_grid_layout_1)
        self.ControlTab.addTab(self.ControlTab_widget_1, 'Gain')
        self.ControlTab_widget_2 = Qt.QWidget()
        self.ControlTab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ControlTab_widget_2)
        self.ControlTab_grid_layout_2 = Qt.QGridLayout()
        self.ControlTab_layout_2.addLayout(self.ControlTab_grid_layout_2)
        self.ControlTab.addTab(self.ControlTab_widget_2, 'Phase')
        self.ControlTab_widget_3 = Qt.QWidget()
        self.ControlTab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ControlTab_widget_3)
        self.ControlTab_grid_layout_3 = Qt.QGridLayout()
        self.ControlTab_layout_3.addLayout(self.ControlTab_grid_layout_3)
        self.ControlTab.addTab(self.ControlTab_widget_3, 'Bandwidth')
        self.top_grid_layout.addWidget(self.ControlTab, 0, 0, 6, 2)
        for r in range(0, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Times_To_Average_range = Range(1, 50, 1, 1, 10)
        self._Times_To_Average_win = RangeWidget(self._Times_To_Average_range, self.set_Times_To_Average, 'Times_To_Average', "counter_slider", int)
        self.ControlTab_grid_layout_0.addWidget(self._Times_To_Average_win, 2, 0, 1, 2)
        for r in range(2, 3):
            self.ControlTab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_0.setColumnStretch(c, 1)
        _SymmetricTaper_check_box = Qt.QCheckBox('Set Rx4Gain = Rx1Gain (Symmetric Taper)')
        self._SymmetricTaper_choices = {True: 1, False: 0}
        self._SymmetricTaper_choices_inv = dict((v,k) for k,v in self._SymmetricTaper_choices.items())
        self._SymmetricTaper_callback = lambda i: Qt.QMetaObject.invokeMethod(_SymmetricTaper_check_box, "setChecked", Qt.Q_ARG("bool", self._SymmetricTaper_choices_inv[i]))
        self._SymmetricTaper_callback(self.SymmetricTaper)
        _SymmetricTaper_check_box.stateChanged.connect(lambda i: self.set_SymmetricTaper(self._SymmetricTaper_choices[bool(i)]))
        self.ControlTab_grid_layout_1.addWidget(_SymmetricTaper_check_box, 5, 0, 1, 1)
        for r in range(5, 6):
            self.ControlTab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ControlTab_grid_layout_1.setColumnStretch(c, 1)
        self._Rx_gain_range = Range(0, 60, 1, 20, 10)
        self._Rx_gain_win = RangeWidget(self._Rx_gain_range, self.set_Rx_gain, 'Rx_gain', "counter_slider", int)
        self.ControlTab_grid_layout_0.addWidget(self._Rx_gain_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.ControlTab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_0.setColumnStretch(c, 1)
        self._Rx4_Cal_range = Range(-180, 180, 2.8125, 0, 10)
        self._Rx4_Cal_win = RangeWidget(self._Rx4_Cal_range, self.set_Rx4_Cal, 'Rx4_Cal', "counter_slider", float)
        self.ControlTab_grid_layout_2.addWidget(self._Rx4_Cal_win, 3, 0, 1, 2)
        for r in range(3, 4):
            self.ControlTab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_2.setColumnStretch(c, 1)
        self._Rx4Gain_range = Range(0, 127, 1, 127, 20)
        self._Rx4Gain_win = RangeWidget(self._Rx4Gain_range, self.set_Rx4Gain, 'Rx4Gain', "counter_slider", int)
        self.ControlTab_grid_layout_1.addWidget(self._Rx4Gain_win, 3, 0, 1, 2)
        for r in range(3, 4):
            self.ControlTab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_1.setColumnStretch(c, 1)
        self._Rx3_Cal_range = Range(-180, 180, 2.8125, 0, 10)
        self._Rx3_Cal_win = RangeWidget(self._Rx3_Cal_range, self.set_Rx3_Cal, 'Rx3_Cal', "counter_slider", float)
        self.ControlTab_grid_layout_2.addWidget(self._Rx3_Cal_win, 2, 0, 1, 2)
        for r in range(2, 3):
            self.ControlTab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_2.setColumnStretch(c, 1)
        self._Rx3Gain_range = Range(0, 127, 1, 127, 20)
        self._Rx3Gain_win = RangeWidget(self._Rx3Gain_range, self.set_Rx3Gain, 'Rx3Gain', "counter_slider", int)
        self.ControlTab_grid_layout_1.addWidget(self._Rx3Gain_win, 2, 0, 1, 2)
        for r in range(2, 3):
            self.ControlTab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_1.setColumnStretch(c, 1)
        self._Rx2_Cal_range = Range(-180, 180, 2.8125, 0, 10)
        self._Rx2_Cal_win = RangeWidget(self._Rx2_Cal_range, self.set_Rx2_Cal, 'Rx2_Cal', "counter_slider", float)
        self.ControlTab_grid_layout_2.addWidget(self._Rx2_Cal_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.ControlTab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_2.setColumnStretch(c, 1)
        self._Rx2Gain_range = Range(0, 127, 1, 127, 20)
        self._Rx2Gain_win = RangeWidget(self._Rx2Gain_range, self.set_Rx2Gain, 'Rx2Gain', "counter_slider", int)
        self.ControlTab_grid_layout_1.addWidget(self._Rx2Gain_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.ControlTab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_1.setColumnStretch(c, 1)
        self._Rx1_Cal_range = Range(-180, 180, 2.8125, 0, 10)
        self._Rx1_Cal_win = RangeWidget(self._Rx1_Cal_range, self.set_Rx1_Cal, 'Rx1_Cal', "counter_slider", float)
        self.ControlTab_grid_layout_2.addWidget(self._Rx1_Cal_win, 0, 0, 1, 2)
        for r in range(0, 1):
            self.ControlTab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_2.setColumnStretch(c, 1)
        self._Rx1Gain_range = Range(0, 127, 1, 127, 20)
        self._Rx1Gain_win = RangeWidget(self._Rx1Gain_range, self.set_Rx1Gain, 'Rx1Gain', "counter_slider", int)
        self.ControlTab_grid_layout_1.addWidget(self._Rx1Gain_win, 0, 0, 1, 2)
        for r in range(0, 1):
            self.ControlTab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_1.setColumnStretch(c, 1)
        _IgnorePhaseCals_check_box = Qt.QCheckBox('Set All Phase Cals to 0 deg')
        self._IgnorePhaseCals_choices = {True: 1, False: 0}
        self._IgnorePhaseCals_choices_inv = dict((v,k) for k,v in self._IgnorePhaseCals_choices.items())
        self._IgnorePhaseCals_callback = lambda i: Qt.QMetaObject.invokeMethod(_IgnorePhaseCals_check_box, "setChecked", Qt.Q_ARG("bool", self._IgnorePhaseCals_choices_inv[i]))
        self._IgnorePhaseCals_callback(self.IgnorePhaseCals)
        _IgnorePhaseCals_check_box.stateChanged.connect(lambda i: self.set_IgnorePhaseCals(self._IgnorePhaseCals_choices[bool(i)]))
        self.ControlTab_grid_layout_2.addWidget(_IgnorePhaseCals_check_box, 4, 0, 1, 2)
        for r in range(4, 5):
            self.ControlTab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_2.setColumnStretch(c, 1)
        self._Center_freq_range = Range(10000, 11000, 0.1, 10508.0, 10)
        self._Center_freq_win = RangeWidget(self._Center_freq_range, self.set_Center_freq, 'Signal Freq (MHz)', "counter_slider", float)
        self.ControlTab_grid_layout_0.addWidget(self._Center_freq_win, 0, 0, 1, 2)
        for r in range(0, 1):
            self.ControlTab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_0.setColumnStretch(c, 1)
        _BeamTaper_check_box = Qt.QCheckBox('Set All Element Gains to Max (127)')
        self._BeamTaper_choices = {True: 1, False: 0}
        self._BeamTaper_choices_inv = dict((v,k) for k,v in self._BeamTaper_choices.items())
        self._BeamTaper_callback = lambda i: Qt.QMetaObject.invokeMethod(_BeamTaper_check_box, "setChecked", Qt.Q_ARG("bool", self._BeamTaper_choices_inv[i]))
        self._BeamTaper_callback(self.BeamTaper)
        _BeamTaper_check_box.stateChanged.connect(lambda i: self.set_BeamTaper(self._BeamTaper_choices[bool(i)]))
        self.ControlTab_grid_layout_1.addWidget(_BeamTaper_check_box, 4, 0, 1, 1)
        for r in range(4, 5):
            self.ControlTab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ControlTab_grid_layout_1.setColumnStretch(c, 1)
        self._BW_range = Range(0, 2000, 100, 0, 10)
        self._BW_win = RangeWidget(self._BW_range, self.set_BW, 'Signal BW (MHz)', "counter_slider", float)
        self.ControlTab_grid_layout_3.addWidget(self._BW_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.ControlTab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ControlTab_grid_layout_3.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_0_0_0_0_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_0_0_0_0_0_formatter = None
        else:
            self._variable_qtgui_label_0_0_0_0_0_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_0_0_0_0_0_tool_bar.addWidget(Qt.QLabel('Angle Measured at (MHz)' + ": "))
        self._variable_qtgui_label_0_0_0_0_0_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_0_0_0_0_0_formatter(self.variable_qtgui_label_0_0_0_0_0_0)))
        self._variable_qtgui_label_0_0_0_0_0_0_tool_bar.addWidget(self._variable_qtgui_label_0_0_0_0_0_0_label)
        self.ControlTab_grid_layout_3.addWidget(self._variable_qtgui_label_0_0_0_0_0_0_tool_bar, 6, 0, 1, 1)
        for r in range(6, 7):
            self.ControlTab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ControlTab_grid_layout_3.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_0_0_0_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_0_0_0_0_formatter = None
        else:
            self._variable_qtgui_label_0_0_0_0_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_0_0_0_0_tool_bar.addWidget(Qt.QLabel('Beam Weights Calc at (MHz)' + ": "))
        self._variable_qtgui_label_0_0_0_0_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_0_0_0_0_formatter(self.variable_qtgui_label_0_0_0_0_0)))
        self._variable_qtgui_label_0_0_0_0_0_tool_bar.addWidget(self._variable_qtgui_label_0_0_0_0_0_label)
        self.ControlTab_grid_layout_3.addWidget(self._variable_qtgui_label_0_0_0_0_0_tool_bar, 5, 0, 1, 1)
        for r in range(5, 6):
            self.ControlTab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ControlTab_grid_layout_3.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_0_0_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_0_0_0_formatter = None
        else:
            self._variable_qtgui_label_0_0_0_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_0_0_0_tool_bar.addWidget(Qt.QLabel('Signal BW (MHz)' + ": "))
        self._variable_qtgui_label_0_0_0_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_0_0_0_formatter(self.variable_qtgui_label_0_0_0_0)))
        self._variable_qtgui_label_0_0_0_0_tool_bar.addWidget(self._variable_qtgui_label_0_0_0_0_label)
        self.ControlTab_grid_layout_3.addWidget(self._variable_qtgui_label_0_0_0_0_tool_bar, 4, 0, 1, 1)
        for r in range(4, 5):
            self.ControlTab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ControlTab_grid_layout_3.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_0_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_0_0_formatter = None
        else:
            self._variable_qtgui_label_0_0_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_0_0_tool_bar.addWidget(Qt.QLabel('Pluto Rx LO (MHz)' + ": "))
        self._variable_qtgui_label_0_0_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_0_0_formatter(self.variable_qtgui_label_0_0_0)))
        self._variable_qtgui_label_0_0_0_tool_bar.addWidget(self._variable_qtgui_label_0_0_0_label)
        self.ControlTab_grid_layout_3.addWidget(self._variable_qtgui_label_0_0_0_tool_bar, 3, 0, 1, 1)
        for r in range(3, 4):
            self.ControlTab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ControlTab_grid_layout_3.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_0_formatter = None
        else:
            self._variable_qtgui_label_0_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_0_tool_bar.addWidget(Qt.QLabel('Mixer LO (MHz)' + ": "))
        self._variable_qtgui_label_0_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_0_formatter(self.variable_qtgui_label_0_0)))
        self._variable_qtgui_label_0_0_tool_bar.addWidget(self._variable_qtgui_label_0_0_label)
        self.ControlTab_grid_layout_3.addWidget(self._variable_qtgui_label_0_0_tool_bar, 2, 0, 1, 1)
        for r in range(2, 3):
            self.ControlTab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ControlTab_grid_layout_3.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_formatter = None
        else:
            self._variable_qtgui_label_0_formatter = lambda x: repr(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Received Signal (MHz)' + ": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.ControlTab_grid_layout_3.addWidget(self._variable_qtgui_label_0_tool_bar, 1, 0, 1, 1)
        for r in range(1, 2):
            self.ControlTab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ControlTab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            1,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.1)
        self.qtgui_number_sink_0.set_title('Elevation')

        labels = ['   ', '', '', '', '',
            '', '', '', '', '']
        units = ['deg', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0.set_min(i, -80)
            self.qtgui_number_sink_0.set_max(i, 80)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 5, 2, 1, 1)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
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

        for i in range(1):
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 0, 2, 5, 3)
        for r in range(0, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.epy_block_0 = epy_block_0.blk(SDR_ip='ip:192.168.2.1', LO_freq=int(Center_freq*1000000 - 5810000000), TX_freq=5810000000, SampleRate=int(samp_rate), Rx_gain=int(Rx_gain), Averages=int(Times_To_Average), Taper=int(BeamTaper), SymTaper=int(SymmetricTaper), PhaseCal=int(IgnorePhaseCals), SignalFreq=int((Center_freq-BW)*1000000), RxGain1=int(Rx1Gain), RxGain2=int(Rx2Gain), RxGain3=int(Rx3Gain), RxGain4=int(Rx4Gain), Rx1_cal=Rx1_Cal, Rx2_cal=Rx2_Cal, Rx3_cal=Rx3_Cal, Rx4_cal=Rx4_Cal)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(1000, 0.001, samp_rate, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.epy_block_0, 1), (self.blocks_throttle_0, 0))
        self.connect((self.epy_block_0, 0), (self.qtgui_const_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_Center_freq(self):
        return self.Center_freq

    def set_Center_freq(self, Center_freq):
        self.Center_freq = Center_freq
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(("%d" % (self.Center_freq)).rjust(20)))
        self.set_variable_qtgui_label_0_0_0(self._variable_qtgui_label_0_0_0_formatter(("%d" % ((self.Center_freq - 5810))).rjust(27)))
        self.set_variable_qtgui_label_0_0_0_0_0(self._variable_qtgui_label_0_0_0_0_0_formatter(("%d" % ((self.Center_freq-self.BW))).rjust(10)))
        self.set_variable_qtgui_label_0_0_0_0_0_0(self._variable_qtgui_label_0_0_0_0_0_0_formatter(("%d" % (self.Center_freq)).rjust(16)))
        self.epy_block_0.LO_freq = int(self.Center_freq*1000000 - 5810000000)
        self.epy_block_0.SignalFreq = int((self.Center_freq-self.BW)*1000000)

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.set_variable_qtgui_label_0_0_0_0(self._variable_qtgui_label_0_0_0_0_formatter(("%d" % (self.BW)).rjust(28)))
        self.set_variable_qtgui_label_0_0_0_0_0(self._variable_qtgui_label_0_0_0_0_0_formatter(("%d" % ((self.Center_freq-self.BW))).rjust(10)))
        self.epy_block_0.SignalFreq = int((self.Center_freq-self.BW)*1000000)

    def get_variable_qtgui_label_0_0_0_0_0_0(self):
        return self.variable_qtgui_label_0_0_0_0_0_0

    def set_variable_qtgui_label_0_0_0_0_0_0(self, variable_qtgui_label_0_0_0_0_0_0):
        self.variable_qtgui_label_0_0_0_0_0_0 = variable_qtgui_label_0_0_0_0_0_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_0_0_0_0_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0_0_0_0_0_0))

    def get_variable_qtgui_label_0_0_0_0_0(self):
        return self.variable_qtgui_label_0_0_0_0_0

    def set_variable_qtgui_label_0_0_0_0_0(self, variable_qtgui_label_0_0_0_0_0):
        self.variable_qtgui_label_0_0_0_0_0 = variable_qtgui_label_0_0_0_0_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_0_0_0_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0_0_0_0_0))

    def get_variable_qtgui_label_0_0_0_0(self):
        return self.variable_qtgui_label_0_0_0_0

    def set_variable_qtgui_label_0_0_0_0(self, variable_qtgui_label_0_0_0_0):
        self.variable_qtgui_label_0_0_0_0 = variable_qtgui_label_0_0_0_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_0_0_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0_0_0_0))

    def get_variable_qtgui_label_0_0_0(self):
        return self.variable_qtgui_label_0_0_0

    def set_variable_qtgui_label_0_0_0(self, variable_qtgui_label_0_0_0):
        self.variable_qtgui_label_0_0_0 = variable_qtgui_label_0_0_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_0_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0_0_0))

    def get_variable_qtgui_label_0_0(self):
        return self.variable_qtgui_label_0_0

    def set_variable_qtgui_label_0_0(self, variable_qtgui_label_0_0):
        self.variable_qtgui_label_0_0 = variable_qtgui_label_0_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0_0))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.epy_block_0.SampleRate = int(self.samp_rate)

    def get_Times_To_Average(self):
        return self.Times_To_Average

    def set_Times_To_Average(self, Times_To_Average):
        self.Times_To_Average = Times_To_Average
        self.epy_block_0.Averages = int(self.Times_To_Average)

    def get_SymmetricTaper(self):
        return self.SymmetricTaper

    def set_SymmetricTaper(self, SymmetricTaper):
        self.SymmetricTaper = SymmetricTaper
        self._SymmetricTaper_callback(self.SymmetricTaper)
        self.epy_block_0.SymTaper = int(self.SymmetricTaper)

    def get_Rx_gain(self):
        return self.Rx_gain

    def set_Rx_gain(self, Rx_gain):
        self.Rx_gain = Rx_gain
        self.epy_block_0.Rx_gain = int(self.Rx_gain)

    def get_Rx4_Cal(self):
        return self.Rx4_Cal

    def set_Rx4_Cal(self, Rx4_Cal):
        self.Rx4_Cal = Rx4_Cal
        self.epy_block_0.Rx4_cal = self.Rx4_Cal

    def get_Rx4Gain(self):
        return self.Rx4Gain

    def set_Rx4Gain(self, Rx4Gain):
        self.Rx4Gain = Rx4Gain
        self.epy_block_0.RxGain4 = int(self.Rx4Gain)

    def get_Rx3_Cal(self):
        return self.Rx3_Cal

    def set_Rx3_Cal(self, Rx3_Cal):
        self.Rx3_Cal = Rx3_Cal
        self.epy_block_0.Rx3_cal = self.Rx3_Cal

    def get_Rx3Gain(self):
        return self.Rx3Gain

    def set_Rx3Gain(self, Rx3Gain):
        self.Rx3Gain = Rx3Gain
        self.epy_block_0.RxGain3 = int(self.Rx3Gain)

    def get_Rx2_Cal(self):
        return self.Rx2_Cal

    def set_Rx2_Cal(self, Rx2_Cal):
        self.Rx2_Cal = Rx2_Cal
        self.epy_block_0.Rx2_cal = self.Rx2_Cal

    def get_Rx2Gain(self):
        return self.Rx2Gain

    def set_Rx2Gain(self, Rx2Gain):
        self.Rx2Gain = Rx2Gain
        self.epy_block_0.RxGain2 = int(self.Rx2Gain)

    def get_Rx1_Cal(self):
        return self.Rx1_Cal

    def set_Rx1_Cal(self, Rx1_Cal):
        self.Rx1_Cal = Rx1_Cal
        self.epy_block_0.Rx1_cal = self.Rx1_Cal

    def get_Rx1Gain(self):
        return self.Rx1Gain

    def set_Rx1Gain(self, Rx1Gain):
        self.Rx1Gain = Rx1Gain
        self.epy_block_0.RxGain1 = int(self.Rx1Gain)

    def get_IgnorePhaseCals(self):
        return self.IgnorePhaseCals

    def set_IgnorePhaseCals(self, IgnorePhaseCals):
        self.IgnorePhaseCals = IgnorePhaseCals
        self._IgnorePhaseCals_callback(self.IgnorePhaseCals)
        self.epy_block_0.PhaseCal = int(self.IgnorePhaseCals)

    def get_BeamTaper(self):
        return self.BeamTaper

    def set_BeamTaper(self, BeamTaper):
        self.BeamTaper = BeamTaper
        self._BeamTaper_callback(self.BeamTaper)
        self.epy_block_0.Taper = int(self.BeamTaper)





def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
