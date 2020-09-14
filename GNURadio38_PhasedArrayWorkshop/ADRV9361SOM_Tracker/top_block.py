#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Top Block
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
import ADAR1000_Dual_Sweeper
import epy_module_1  # embedded python module

from gnuradio import qtgui

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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
        self.LO_freq = LO_freq = 9500
        self.Center_freq = Center_freq = 10113
        self.BW = BW = 0
        self.variable_qtgui_label_0_0_0_0_0_0 = variable_qtgui_label_0_0_0_0_0_0 = ("%d" % (Center_freq)).rjust(16)
        self.variable_qtgui_label_0_0_0_0_0 = variable_qtgui_label_0_0_0_0_0 = ("%d" % ((Center_freq-BW))).rjust(10)
        self.variable_qtgui_label_0_0_0_0 = variable_qtgui_label_0_0_0_0 = ("%d" % (BW)).rjust(28)
        self.variable_qtgui_label_0_0_0 = variable_qtgui_label_0_0_0 = ("%d" % ((Center_freq - LO_freq))).rjust(27)
        self.variable_qtgui_label_0_0 = variable_qtgui_label_0_0 = ("%d" % (LO_freq)).rjust(32)
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = ("%d" % (Center_freq)).rjust(20)
        self.samp_rate = samp_rate = 5000000
        self.Times_To_Average = Times_To_Average = 1
        self.SymmetricTaper = SymmetricTaper = 0
        self.ScanMaxAngle = ScanMaxAngle = 0
        self.Rx_gain = Rx_gain = 15
        self.Rx8_Cal = Rx8_Cal = 0
        self.Rx8Gain = Rx8Gain = 5
        self.Rx7_Cal = Rx7_Cal = 0
        self.Rx7Gain = Rx7Gain = 33
        self.Rx6_Cal = Rx6_Cal = 0
        self.Rx6Gain = Rx6Gain = 66
        self.Rx5_Cal = Rx5_Cal = 0
        self.Rx5Gain = Rx5Gain = 127
        self.Rx4_Cal = Rx4_Cal = 0
        self.Rx4Gain = Rx4Gain = 127
        self.Rx3_Cal = Rx3_Cal = 0
        self.Rx3Gain = Rx3Gain = 66
        self.Rx2_Cal = Rx2_Cal = 0
        self.Rx2Gain = Rx2Gain = 33
        self.Rx1_to_Rx2_Offset = Rx1_to_Rx2_Offset = 0
        self.Rx1_Cal = Rx1_Cal = 0
        self.Rx1Gain = Rx1Gain = 5
        self.IgnorePhaseCals = IgnorePhaseCals = 0
        self.Error_Threshold = Error_Threshold = .01
        self.BeamTaper = BeamTaper = 0

        ##################################################
        # Blocks
        ##################################################
        self.ControlTab = Qt.QTabWidget()
        self.ControlTab_widget_0 = Qt.QWidget()
        self.ControlTab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ControlTab_widget_0)
        self.ControlTab_grid_layout_0 = Qt.QGridLayout()
        self.ControlTab_layout_0.addLayout(self.ControlTab_grid_layout_0)
        self.ControlTab.addTab(self.ControlTab_widget_0, 'Control')
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
        _SymmetricTaper_check_box = Qt.QCheckBox('SymmetricTaper')
        self._SymmetricTaper_choices = {True: 1, False: 0}
        self._SymmetricTaper_choices_inv = dict((v,k) for k,v in self._SymmetricTaper_choices.items())
        self._SymmetricTaper_callback = lambda i: Qt.QMetaObject.invokeMethod(_SymmetricTaper_check_box, "setChecked", Qt.Q_ARG("bool", self._SymmetricTaper_choices_inv[i]))
        self._SymmetricTaper_callback(self.SymmetricTaper)
        _SymmetricTaper_check_box.stateChanged.connect(lambda i: self.set_SymmetricTaper(self._SymmetricTaper_choices[bool(i)]))
        self.ControlTab_grid_layout_1.addWidget(_SymmetricTaper_check_box, 9, 0, 1, 1)
        for r in range(9, 10):
            self.ControlTab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ControlTab_grid_layout_1.setColumnStretch(c, 1)
        _ScanMaxAngle_push_button = Qt.QPushButton('')
        _ScanMaxAngle_push_button = Qt.QPushButton('ScanMaxAngle')
        self._ScanMaxAngle_choices = {'Pressed': 1, 'Released': 0}
        _ScanMaxAngle_push_button.pressed.connect(lambda: self.set_ScanMaxAngle(self._ScanMaxAngle_choices['Pressed']))
        _ScanMaxAngle_push_button.released.connect(lambda: self.set_ScanMaxAngle(self._ScanMaxAngle_choices['Released']))
        self.ControlTab_grid_layout_0.addWidget(_ScanMaxAngle_push_button, 3, 0, 1, 2)
        for r in range(3, 4):
            self.ControlTab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_0.setColumnStretch(c, 1)
        self._Rx_gain_range = Range(0, 60, 1, 15, 10)
        self._Rx_gain_win = RangeWidget(self._Rx_gain_range, self.set_Rx_gain, 'Rx_gain', "counter_slider", int)
        self.ControlTab_grid_layout_0.addWidget(self._Rx_gain_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.ControlTab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_0.setColumnStretch(c, 1)
        self._Rx8_Cal_range = Range(-180, 180, 2.8125, 0, 10)
        self._Rx8_Cal_win = RangeWidget(self._Rx8_Cal_range, self.set_Rx8_Cal, 'Rx8_Cal', "counter_slider", float)
        self.ControlTab_grid_layout_2.addWidget(self._Rx8_Cal_win, 7, 0, 1, 2)
        for r in range(7, 8):
            self.ControlTab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_2.setColumnStretch(c, 1)
        self._Rx8Gain_range = Range(0, 127, 1, 5, 20)
        self._Rx8Gain_win = RangeWidget(self._Rx8Gain_range, self.set_Rx8Gain, 'Rx8Gain', "counter_slider", int)
        self.ControlTab_grid_layout_1.addWidget(self._Rx8Gain_win, 7, 0, 1, 2)
        for r in range(7, 8):
            self.ControlTab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_1.setColumnStretch(c, 1)
        self._Rx7_Cal_range = Range(-180, 180, 2.8125, 0, 10)
        self._Rx7_Cal_win = RangeWidget(self._Rx7_Cal_range, self.set_Rx7_Cal, 'Rx7_Cal', "counter_slider", float)
        self.ControlTab_grid_layout_2.addWidget(self._Rx7_Cal_win, 6, 0, 1, 2)
        for r in range(6, 7):
            self.ControlTab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_2.setColumnStretch(c, 1)
        self._Rx7Gain_range = Range(0, 127, 1, 33, 20)
        self._Rx7Gain_win = RangeWidget(self._Rx7Gain_range, self.set_Rx7Gain, 'Rx7Gain', "counter_slider", int)
        self.ControlTab_grid_layout_1.addWidget(self._Rx7Gain_win, 6, 0, 1, 2)
        for r in range(6, 7):
            self.ControlTab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_1.setColumnStretch(c, 1)
        self._Rx6_Cal_range = Range(-180, 180, 2.8125, 0, 10)
        self._Rx6_Cal_win = RangeWidget(self._Rx6_Cal_range, self.set_Rx6_Cal, 'Rx6_Cal', "counter_slider", float)
        self.ControlTab_grid_layout_2.addWidget(self._Rx6_Cal_win, 5, 0, 1, 2)
        for r in range(5, 6):
            self.ControlTab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_2.setColumnStretch(c, 1)
        self._Rx6Gain_range = Range(0, 127, 1, 66, 20)
        self._Rx6Gain_win = RangeWidget(self._Rx6Gain_range, self.set_Rx6Gain, 'Rx6Gain', "counter_slider", int)
        self.ControlTab_grid_layout_1.addWidget(self._Rx6Gain_win, 5, 0, 1, 2)
        for r in range(5, 6):
            self.ControlTab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_1.setColumnStretch(c, 1)
        self._Rx5_Cal_range = Range(-180, 180, 2.8125, 0, 10)
        self._Rx5_Cal_win = RangeWidget(self._Rx5_Cal_range, self.set_Rx5_Cal, 'Rx5_Cal', "counter_slider", float)
        self.ControlTab_grid_layout_2.addWidget(self._Rx5_Cal_win, 4, 0, 1, 2)
        for r in range(4, 5):
            self.ControlTab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_2.setColumnStretch(c, 1)
        self._Rx5Gain_range = Range(0, 127, 1, 127, 20)
        self._Rx5Gain_win = RangeWidget(self._Rx5Gain_range, self.set_Rx5Gain, 'Rx5Gain', "counter_slider", int)
        self.ControlTab_grid_layout_1.addWidget(self._Rx5Gain_win, 4, 0, 1, 2)
        for r in range(4, 5):
            self.ControlTab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_1.setColumnStretch(c, 1)
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
        self._Rx3Gain_range = Range(0, 127, 1, 66, 20)
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
        self._Rx2Gain_range = Range(0, 127, 1, 33, 20)
        self._Rx2Gain_win = RangeWidget(self._Rx2Gain_range, self.set_Rx2Gain, 'Rx2Gain', "counter_slider", int)
        self.ControlTab_grid_layout_1.addWidget(self._Rx2Gain_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.ControlTab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_1.setColumnStretch(c, 1)
        self._Rx1_to_Rx2_Offset_range = Range(-180, 180, 2.8125, 0, 10)
        self._Rx1_to_Rx2_Offset_win = RangeWidget(self._Rx1_to_Rx2_Offset_range, self.set_Rx1_to_Rx2_Offset, 'Rx1_to_Rx2_Offset', "counter_slider", float)
        self.ControlTab_grid_layout_2.addWidget(self._Rx1_to_Rx2_Offset_win, 8, 0, 1, 2)
        for r in range(8, 9):
            self.ControlTab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_2.setColumnStretch(c, 1)
        self._Rx1_Cal_range = Range(-180, 180, 2.8125, 0, 10)
        self._Rx1_Cal_win = RangeWidget(self._Rx1_Cal_range, self.set_Rx1_Cal, 'Rx1_Cal', "counter_slider", float)
        self.ControlTab_grid_layout_2.addWidget(self._Rx1_Cal_win, 0, 0, 1, 2)
        for r in range(0, 1):
            self.ControlTab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_2.setColumnStretch(c, 1)
        self._Rx1Gain_range = Range(0, 127, 1, 5, 20)
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
        self.ControlTab_grid_layout_2.addWidget(_IgnorePhaseCals_check_box, 9, 0, 1, 2)
        for r in range(9, 10):
            self.ControlTab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_2.setColumnStretch(c, 1)
        self._Error_Threshold_range = Range(0, 1, .01, .01, 10)
        self._Error_Threshold_win = RangeWidget(self._Error_Threshold_range, self.set_Error_Threshold, 'Error_Threshold', "counter_slider", float)
        self.ControlTab_grid_layout_0.addWidget(self._Error_Threshold_win, 4, 0, 1, 2)
        for r in range(4, 5):
            self.ControlTab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.ControlTab_grid_layout_0.setColumnStretch(c, 1)
        self._Center_freq_range = Range(10000, 11000, 0.1, 10113, 10)
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
        self.ControlTab_grid_layout_1.addWidget(_BeamTaper_check_box, 8, 0, 1, 1)
        for r in range(8, 9):
            self.ControlTab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ControlTab_grid_layout_1.setColumnStretch(c, 1)
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
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            4000, #size
            'Elevation Waterfall Plot', #name
            1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(0, 4000)
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 0, 2, 6, 6)
        for r in range(0, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(-1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self._BW_range = Range(0, 2000, 100, 0, 10)
        self._BW_win = RangeWidget(self._BW_range, self.set_BW, 'Signal BW (MHz)', "counter_slider", float)
        self.ControlTab_grid_layout_3.addWidget(self._BW_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.ControlTab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.ControlTab_grid_layout_3.setColumnStretch(c, 1)
        self.ADAR1000_Dual_Sweeper = ADAR1000_Dual_Sweeper.blk(IP=[192, 168, 0, 3], LO_freq=int((Center_freq-LO_freq)*1000000), TX_freq=int(LO_freq*1000000), SampleRate=int(samp_rate), Rx_gain=int(Rx_gain), Averages=int(Times_To_Average), Taper=int(BeamTaper), SymTaper=int(SymmetricTaper), PhaseCal=int(IgnorePhaseCals), ScanMaxAngle=int(ScanMaxAngle), Error_Threshold=Error_Threshold, SignalFreq=int(Center_freq*1000000), RxGain1=Rx1Gain, RxGain2=Rx2Gain, RxGain3=Rx3Gain, RxGain4=Rx4Gain, Rx1_cal=Rx1_Cal+33.75, Rx2_cal=Rx2_Cal+30.9375, Rx3_cal=Rx3_Cal+11.25, Rx4_cal=Rx4_Cal, RxGain5=Rx5Gain, RxGain6=Rx6Gain, RxGain7=Rx7Gain, RxGain8=Rx8Gain, Rx5_cal=Rx5_Cal+Rx1_to_Rx2_Offset+75.9375, Rx6_cal=Rx6_Cal+Rx1_to_Rx2_Offset+101.25, Rx7_cal=Rx7_Cal+Rx1_to_Rx2_Offset+112.5, Rx8_cal=Rx8_Cal+Rx1_to_Rx2_Offset+109.6875)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.ADAR1000_Dual_Sweeper, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.ADAR1000_Dual_Sweeper, 1), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_float_to_complex_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_LO_freq(self):
        return self.LO_freq

    def set_LO_freq(self, LO_freq):
        self.LO_freq = LO_freq
        self.set_variable_qtgui_label_0_0(self._variable_qtgui_label_0_0_formatter(("%d" % (self.LO_freq)).rjust(32)))
        self.set_variable_qtgui_label_0_0_0(self._variable_qtgui_label_0_0_0_formatter(("%d" % ((self.Center_freq - self.LO_freq))).rjust(27)))
        self.ADAR1000_Dual_Sweeper.LO_freq = int((self.Center_freq-self.LO_freq)*1000000)
        self.ADAR1000_Dual_Sweeper.TX_freq = int(self.LO_freq*1000000)

    def get_Center_freq(self):
        return self.Center_freq

    def set_Center_freq(self, Center_freq):
        self.Center_freq = Center_freq
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(("%d" % (self.Center_freq)).rjust(20)))
        self.set_variable_qtgui_label_0_0_0(self._variable_qtgui_label_0_0_0_formatter(("%d" % ((self.Center_freq - self.LO_freq))).rjust(27)))
        self.set_variable_qtgui_label_0_0_0_0_0(self._variable_qtgui_label_0_0_0_0_0_formatter(("%d" % ((self.Center_freq-self.BW))).rjust(10)))
        self.set_variable_qtgui_label_0_0_0_0_0_0(self._variable_qtgui_label_0_0_0_0_0_0_formatter(("%d" % (self.Center_freq)).rjust(16)))
        self.ADAR1000_Dual_Sweeper.LO_freq = int((self.Center_freq-self.LO_freq)*1000000)
        self.ADAR1000_Dual_Sweeper.SignalFreq = int(self.Center_freq*1000000)

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.set_variable_qtgui_label_0_0_0_0(self._variable_qtgui_label_0_0_0_0_formatter(("%d" % (self.BW)).rjust(28)))
        self.set_variable_qtgui_label_0_0_0_0_0(self._variable_qtgui_label_0_0_0_0_0_formatter(("%d" % ((self.Center_freq-self.BW))).rjust(10)))

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
        self.ADAR1000_Dual_Sweeper.SampleRate = int(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_Times_To_Average(self):
        return self.Times_To_Average

    def set_Times_To_Average(self, Times_To_Average):
        self.Times_To_Average = Times_To_Average
        self.ADAR1000_Dual_Sweeper.Averages = int(self.Times_To_Average)

    def get_SymmetricTaper(self):
        return self.SymmetricTaper

    def set_SymmetricTaper(self, SymmetricTaper):
        self.SymmetricTaper = SymmetricTaper
        self._SymmetricTaper_callback(self.SymmetricTaper)
        self.ADAR1000_Dual_Sweeper.SymTaper = int(self.SymmetricTaper)

    def get_ScanMaxAngle(self):
        return self.ScanMaxAngle

    def set_ScanMaxAngle(self, ScanMaxAngle):
        self.ScanMaxAngle = ScanMaxAngle
        self.ADAR1000_Dual_Sweeper.ScanMaxAngle = int(self.ScanMaxAngle)

    def get_Rx_gain(self):
        return self.Rx_gain

    def set_Rx_gain(self, Rx_gain):
        self.Rx_gain = Rx_gain
        self.ADAR1000_Dual_Sweeper.Rx_gain = int(self.Rx_gain)

    def get_Rx8_Cal(self):
        return self.Rx8_Cal

    def set_Rx8_Cal(self, Rx8_Cal):
        self.Rx8_Cal = Rx8_Cal
        self.ADAR1000_Dual_Sweeper.Rx8_cal = self.Rx8_Cal+self.Rx1_to_Rx2_Offset+109.6875

    def get_Rx8Gain(self):
        return self.Rx8Gain

    def set_Rx8Gain(self, Rx8Gain):
        self.Rx8Gain = Rx8Gain
        self.ADAR1000_Dual_Sweeper.RxGain8 = self.Rx8Gain

    def get_Rx7_Cal(self):
        return self.Rx7_Cal

    def set_Rx7_Cal(self, Rx7_Cal):
        self.Rx7_Cal = Rx7_Cal
        self.ADAR1000_Dual_Sweeper.Rx7_cal = self.Rx7_Cal+self.Rx1_to_Rx2_Offset+112.5

    def get_Rx7Gain(self):
        return self.Rx7Gain

    def set_Rx7Gain(self, Rx7Gain):
        self.Rx7Gain = Rx7Gain
        self.ADAR1000_Dual_Sweeper.RxGain7 = self.Rx7Gain

    def get_Rx6_Cal(self):
        return self.Rx6_Cal

    def set_Rx6_Cal(self, Rx6_Cal):
        self.Rx6_Cal = Rx6_Cal
        self.ADAR1000_Dual_Sweeper.Rx6_cal = self.Rx6_Cal+self.Rx1_to_Rx2_Offset+101.25

    def get_Rx6Gain(self):
        return self.Rx6Gain

    def set_Rx6Gain(self, Rx6Gain):
        self.Rx6Gain = Rx6Gain
        self.ADAR1000_Dual_Sweeper.RxGain6 = self.Rx6Gain

    def get_Rx5_Cal(self):
        return self.Rx5_Cal

    def set_Rx5_Cal(self, Rx5_Cal):
        self.Rx5_Cal = Rx5_Cal
        self.ADAR1000_Dual_Sweeper.Rx5_cal = self.Rx5_Cal+self.Rx1_to_Rx2_Offset+75.9375

    def get_Rx5Gain(self):
        return self.Rx5Gain

    def set_Rx5Gain(self, Rx5Gain):
        self.Rx5Gain = Rx5Gain
        self.ADAR1000_Dual_Sweeper.RxGain5 = self.Rx5Gain

    def get_Rx4_Cal(self):
        return self.Rx4_Cal

    def set_Rx4_Cal(self, Rx4_Cal):
        self.Rx4_Cal = Rx4_Cal
        self.ADAR1000_Dual_Sweeper.Rx4_cal = self.Rx4_Cal

    def get_Rx4Gain(self):
        return self.Rx4Gain

    def set_Rx4Gain(self, Rx4Gain):
        self.Rx4Gain = Rx4Gain
        self.ADAR1000_Dual_Sweeper.RxGain4 = self.Rx4Gain

    def get_Rx3_Cal(self):
        return self.Rx3_Cal

    def set_Rx3_Cal(self, Rx3_Cal):
        self.Rx3_Cal = Rx3_Cal
        self.ADAR1000_Dual_Sweeper.Rx3_cal = self.Rx3_Cal+11.25

    def get_Rx3Gain(self):
        return self.Rx3Gain

    def set_Rx3Gain(self, Rx3Gain):
        self.Rx3Gain = Rx3Gain
        self.ADAR1000_Dual_Sweeper.RxGain3 = self.Rx3Gain

    def get_Rx2_Cal(self):
        return self.Rx2_Cal

    def set_Rx2_Cal(self, Rx2_Cal):
        self.Rx2_Cal = Rx2_Cal
        self.ADAR1000_Dual_Sweeper.Rx2_cal = self.Rx2_Cal+30.9375

    def get_Rx2Gain(self):
        return self.Rx2Gain

    def set_Rx2Gain(self, Rx2Gain):
        self.Rx2Gain = Rx2Gain
        self.ADAR1000_Dual_Sweeper.RxGain2 = self.Rx2Gain

    def get_Rx1_to_Rx2_Offset(self):
        return self.Rx1_to_Rx2_Offset

    def set_Rx1_to_Rx2_Offset(self, Rx1_to_Rx2_Offset):
        self.Rx1_to_Rx2_Offset = Rx1_to_Rx2_Offset
        self.ADAR1000_Dual_Sweeper.Rx5_cal = self.Rx5_Cal+self.Rx1_to_Rx2_Offset+75.9375
        self.ADAR1000_Dual_Sweeper.Rx6_cal = self.Rx6_Cal+self.Rx1_to_Rx2_Offset+101.25
        self.ADAR1000_Dual_Sweeper.Rx7_cal = self.Rx7_Cal+self.Rx1_to_Rx2_Offset+112.5
        self.ADAR1000_Dual_Sweeper.Rx8_cal = self.Rx8_Cal+self.Rx1_to_Rx2_Offset+109.6875

    def get_Rx1_Cal(self):
        return self.Rx1_Cal

    def set_Rx1_Cal(self, Rx1_Cal):
        self.Rx1_Cal = Rx1_Cal
        self.ADAR1000_Dual_Sweeper.Rx1_cal = self.Rx1_Cal+33.75

    def get_Rx1Gain(self):
        return self.Rx1Gain

    def set_Rx1Gain(self, Rx1Gain):
        self.Rx1Gain = Rx1Gain
        self.ADAR1000_Dual_Sweeper.RxGain1 = self.Rx1Gain

    def get_IgnorePhaseCals(self):
        return self.IgnorePhaseCals

    def set_IgnorePhaseCals(self, IgnorePhaseCals):
        self.IgnorePhaseCals = IgnorePhaseCals
        self._IgnorePhaseCals_callback(self.IgnorePhaseCals)
        self.ADAR1000_Dual_Sweeper.PhaseCal = int(self.IgnorePhaseCals)

    def get_Error_Threshold(self):
        return self.Error_Threshold

    def set_Error_Threshold(self, Error_Threshold):
        self.Error_Threshold = Error_Threshold
        self.ADAR1000_Dual_Sweeper.Error_Threshold = self.Error_Threshold

    def get_BeamTaper(self):
        return self.BeamTaper

    def set_BeamTaper(self, BeamTaper):
        self.BeamTaper = BeamTaper
        self._BeamTaper_callback(self.BeamTaper)
        self.ADAR1000_Dual_Sweeper.Taper = int(self.BeamTaper)





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
