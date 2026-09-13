#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: LAB_1_P1
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class LAB_1_P1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "LAB_1_P1", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("LAB_1_P1")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
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

        self.settings = Qt.QSettings("GNU Radio", "LAB_1_P1")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 8000
        self.fase_random = fase_random = __import__('random').uniform(-1.0472, 1.0472)

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_time_sink_x_2_0_0 = qtgui.time_sink_f(
            64, #size
            samp_rate, #samp_rate
            " punto 6 uniforme + 650hz", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_2_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_2_0_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_2_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2_0_0.enable_tags(True)
        self.qtgui_time_sink_x_2_0_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_2_0_0.enable_grid(False)
        self.qtgui_time_sink_x_2_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_2_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_2_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_2_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_2_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_0_0_win)
        self.qtgui_time_sink_x_2_0 = qtgui.time_sink_f(
            64, #size
            samp_rate, #samp_rate
            " punto 5 uniforme + 650hz", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_2_0.set_update_time(0.10)
        self.qtgui_time_sink_x_2_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_2_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2_0.enable_tags(True)
        self.qtgui_time_sink_x_2_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2_0.enable_autoscale(False)
        self.qtgui_time_sink_x_2_0.enable_grid(False)
        self.qtgui_time_sink_x_2_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_2_0.enable_control_panel(False)
        self.qtgui_time_sink_x_2_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_0_win = sip.wrapinstance(self.qtgui_time_sink_x_2_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_0_win)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
            320, #size
            samp_rate, #samp_rate
            "180hz + 184hz", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_win)
        self.qtgui_time_sink_x_0_2_1 = qtgui.time_sink_f(
            320, #size
            samp_rate, #samp_rate
            "650hz + 75hz", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_2_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_2_1.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_0_2_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_2_1.enable_tags(True)
        self.qtgui_time_sink_x_0_2_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_2_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_2_1.enable_grid(False)
        self.qtgui_time_sink_x_0_2_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_2_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_2_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_2_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_2_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_2_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_2_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_2_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_2_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_2_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_2_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_2_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_2_1_win)
        self.qtgui_time_sink_x_0_2 = qtgui.time_sink_f(
            320, #size
            samp_rate, #samp_rate
            "180hz + 260hz", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_2.set_update_time(0.10)
        self.qtgui_time_sink_x_0_2.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_0_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_2.enable_tags(True)
        self.qtgui_time_sink_x_0_2.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_2.enable_autoscale(False)
        self.qtgui_time_sink_x_0_2.enable_grid(False)
        self.qtgui_time_sink_x_0_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_2.enable_control_panel(False)
        self.qtgui_time_sink_x_0_2.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_2_win = sip.wrapinstance(self.qtgui_time_sink_x_0_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_2_win)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
            64, #size
            samp_rate, #samp_rate
            "fase aleatoria comparativa", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "Señal 75hz", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "Señal 650hz", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.blocks_throttle2_1_0_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(0.8) * samp_rate) if "time" == "time" else int(0.8), 1) )
        self.blocks_throttle2_1_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(0.8) * samp_rate) if "time" == "time" else int(0.8), 1) )
        self.blocks_throttle2_1 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(1.2) * samp_rate) if "time" == "time" else int(1.2), 1) )
        self.blocks_throttle2_0_2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0_2 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0_1 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(1.2) * samp_rate) if "time" == "time" else int(1.2), 1) )
        self.blocks_throttle2_0_0_2 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(1.2) * samp_rate) if "time" == "time" else int(1.2), 1) )
        self.blocks_throttle2_0_0_1_1 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(1.2) * samp_rate) if "time" == "time" else int(1.2), 1) )
        self.blocks_throttle2_0_0_1 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(1.2) * samp_rate) if "time" == "time" else int(1.2), 1) )
        self.blocks_throttle2_0_0_0_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(1.2) * samp_rate) if "time" == "time" else int(1.2), 1) )
        self.blocks_throttle2_0_0_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(1.2) * samp_rate) if "time" == "time" else int(1.2), 1) )
        self.blocks_throttle2_0_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(1.2) * samp_rate) if "time" == "time" else int(1.2), 1) )
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "time" == "auto" else max( int(float(1.2) * samp_rate) if "time" == "time" else int(1.2), 1) )
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_ff(0.5)
        self.blocks_multiply_const_vxx_0_0_1 = blocks.multiply_const_ff(0.5)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_ff(0.5)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(0.5)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(0.5)
        self.blocks_add_xx_2 = blocks.add_vff(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_ff(0.75)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(0.5)
        self.audio_sink_1_0_3 = audio.sink(samp_rate, '', True)
        self.audio_sink_1_0_2 = audio.sink(samp_rate, '', True)
        self.audio_sink_1_0_1 = audio.sink(samp_rate, '', True)
        self.audio_sink_1_0_0 = audio.sink(samp_rate, '', True)
        self.audio_sink_1_0 = audio.sink(samp_rate, '', True)
        self.analog_sig_source_x_6_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 650, 1, 0, 0)
        self.analog_sig_source_x_6 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 650, 1, 0, fase_random)
        self.analog_sig_source_x_4 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 184, 1, 0, 0)
        self.analog_sig_source_x_3 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 180, 1, 0, 0)
        self.analog_sig_source_x_2_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 75, 1, 0, 0)
        self.analog_sig_source_x_2 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 260, 1, 0, 0)
        self.analog_sig_source_x_1_1_1_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 650, 1, 0, 0)
        self.analog_sig_source_x_1_1_1_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 650, 1, 0, 0)
        self.analog_sig_source_x_1_1_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 650, 1, 0, 0)
        self.analog_sig_source_x_1_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 180, 1, 0, 0)
        self.analog_sig_source_x_1_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 75, 1, 0, 1.0472)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 75, 1, 0, 0)
        self.analog_sig_source_x_0_1_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 75, 1, 0, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 650, 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 650, 1, 0, 1.0472)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 650, 1, 0, 0)
        self.analog_noise_source_x_0_0 = analog.noise_source_f(analog.GR_UNIFORM, 0.35, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_UNIFORM, 1.3, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.analog_noise_source_x_0_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_throttle2_0_1, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_throttle2_0_2, 0))
        self.connect((self.analog_sig_source_x_0_1_0, 0), (self.blocks_throttle2_0_2_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_throttle2_0_0, 0))
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_throttle2_0_0_0, 0))
        self.connect((self.analog_sig_source_x_1_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_1_1_1, 0), (self.blocks_add_xx_0_1, 0))
        self.connect((self.analog_sig_source_x_1_1_1_0, 0), (self.blocks_add_xx_2, 1))
        self.connect((self.analog_sig_source_x_1_1_1_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_2_1, 0), (self.blocks_add_xx_0_1, 1))
        self.connect((self.analog_sig_source_x_3, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.analog_sig_source_x_4, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.analog_sig_source_x_6, 0), (self.blocks_throttle2_0_0_2, 0))
        self.connect((self.analog_sig_source_x_6_0, 0), (self.blocks_throttle2_0_0_0_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_add_xx_2, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle2_0_0_1, 0))
        self.connect((self.blocks_add_xx_0_1, 0), (self.blocks_throttle2_0_0_1_1, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_throttle2_1, 0))
        self.connect((self.blocks_add_xx_2, 0), (self.blocks_throttle2_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_1_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.audio_sink_1_0_2, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_1, 0), (self.audio_sink_1_0_3, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.audio_sink_1_0_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle2_1_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle2_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_throttle2_0_0_0, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.blocks_throttle2_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 1))
        self.connect((self.blocks_throttle2_0_0_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_throttle2_0_0_1, 0), (self.qtgui_time_sink_x_0_2, 0))
        self.connect((self.blocks_throttle2_0_0_1_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_throttle2_0_0_1_1, 0), (self.qtgui_time_sink_x_0_2_1, 0))
        self.connect((self.blocks_throttle2_0_0_2, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_throttle2_0_1, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_throttle2_0_2, 0), (self.blocks_multiply_const_vxx_0_0_1, 0))
        self.connect((self.blocks_throttle2_0_2_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_throttle2_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.blocks_throttle2_1, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.blocks_throttle2_1_0, 0), (self.qtgui_time_sink_x_2_0, 0))
        self.connect((self.blocks_throttle2_1_0_0, 0), (self.qtgui_time_sink_x_2_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "LAB_1_P1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_1_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_1_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_1_1_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_3.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_4.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_6.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_6_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_0_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_0_1_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_0_2.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_2.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_1_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_1_0_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_2_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_2_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_2_0_0.set_samp_rate(self.samp_rate)

    def get_fase_random(self):
        return self.fase_random

    def set_fase_random(self, fase_random):
        self.fase_random = fase_random
        self.analog_sig_source_x_6.set_phase(self.fase_random)




def main(top_block_cls=LAB_1_P1, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
