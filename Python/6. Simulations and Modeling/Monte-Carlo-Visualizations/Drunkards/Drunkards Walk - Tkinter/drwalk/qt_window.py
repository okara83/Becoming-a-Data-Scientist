#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""qt_window.py

Class that holds the configurations for the program window and its
modifications after specific triggers.

    * `PyQt5.QtCore.QSize` defines the size of the window.
    * `PyQt5.QtCore.Qt` holds various enumerations and constants,
        such as alignment options and keyboard keys.
    * `PyQt5.QtWidgets.QDesktopWidget` provides access to the
        screen resolution.
    * `PyQt5.QtWidgets.QGroupBox` provides a frame, a title on top
        and the ability of displaying various widgets inside itself.
    * `PyQt5.QtWidgets.QHBoxLayout` lines up widgets horizontally.
    * `PyQt5.QtWidgets.QMainWindow` provides a main window.
    * `PyQt5.QtWidgets.QProgressBar` provides a progress bar, that gives
        the user an indication that the application is still running.
    * `PyQt5.QtWidgets.QPushButton` provides a command button that may
        execute some action.
    * `PyQt5.QtWidgets.QSpinBox` allows the user to choose a value by
        clicking the up/down buttons or pressing up/down on the keyboard.
        The user may also input the value manually.
    * `PyQt5.QtWidgets.QVBoxLayout` lines up widgets vertically.
    * `PyQt5.QtWidgets.QWidget` is the base class of all user interface
        objects.
"""

from __future__ import absolute_import, division

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QDesktopWidget,
    QGroupBox,
    QHBoxLayout,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from .custom_canvas import DistPlot, HistPlot, PathPlot
from .monte_carlo import MonteCarloSim


class AppWindow(QMainWindow):
    """
    The project's custom window, with responsibilities such as displaying
    graphics and handling user input.
    """

    def __init__(self):
        """
        Initializes the AppWindow object with the following attributes:

            it_box:         spin box for the number of iterations.
            rp_box:         spin box for the number of replications.
            start_button:   button that controls the entire program.
            prr_bar:        bar that displays the progress of computations.
            main_widget:    dominant widget that holds all the other ones.
            main_layout:    layout for the dominant widget.

        All the configurations for the starting window are done here, such
        as its initial size, ranges and default values for the spin boxes,
        actions and layouts for the widgets.
        """
        super().__init__(flags=Qt.WindowFlags())
        self.setWindowTitle("Random Walk Simulator")
        self.setFixedSize(QSize(225, 275))
        self.thread = None

        self.it_box = QSpinBox()
        self.it_box.setRange(1, 1 << 24)
        self.it_box.setSingleStep(100)
        self.it_box.setValue(2000)

        self.rp_box = QSpinBox()
        self.rp_box.setRange(1, 1 << 24)
        self.rp_box.setSingleStep(10)
        self.rp_box.setValue(1)

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.process_data)

        self.prr_bar = QProgressBar()
        self.prr_bar.setValue(0)

        it_group = QGroupBox("Number of iterations (i)")
        it_layout = QHBoxLayout(it_group)
        it_layout.addWidget(self.it_box, alignment=Qt.AlignBaseline)

        rp_group = QGroupBox("Number of replications (r)")
        rp_layout = QHBoxLayout(rp_group)
        rp_layout.addWidget(self.rp_box, alignment=Qt.AlignBaseline)

        pr_group = QGroupBox("Progress bar (r)")
        pr_layout = QHBoxLayout(pr_group)
        pr_layout.addWidget(self.prr_bar, alignment=Qt.AlignBaseline)
        pr_layout.addWidget(self.start_button, alignment=Qt.AlignBaseline)

        parameters = QGroupBox("Simulation info and parameters")
        param_layout = QVBoxLayout(parameters)
        param_layout.addWidget(it_group, alignment=Qt.AlignBaseline)
        param_layout.addWidget(rp_group, alignment=Qt.AlignBaseline)
        param_layout.addWidget(pr_group, alignment=Qt.AlignBaseline)

        self.main_widget = QWidget(self, flags=Qt.WindowFlags())
        self.main_layout = QHBoxLayout(self.main_widget)
        self.main_layout.addWidget(parameters, alignment=Qt.AlignAbsolute)
        self.setCentralWidget(self.main_widget)

    def keypress_event(self, event):
        """
        Handles key presses while the window is focused. One can start the
        computing by pressing Enter, and quit at any time by pressing
        Esc or Enter.

        Args:
            event:  an abstract object representing an event.
        """
        if event.key() == Qt.Key_Return:
            self.process_data()
        elif event.key() == Qt.Key_Escape:
            self.close()

    def process_data(self):
        """
        Intermission before displaying the output graphs. Shows a progress
        bar being updated with each chunk of processing from the thread after
        it is started. Also disables other elements and changes the button's
        function, to quit the program if it is pressed. When the thread ends,
        it will automatically call the next function in the control flow.
        """
        self.rp_box.setEnabled(False)
        self.it_box.setEnabled(False)
        self.start_button.setText("Abort/quit")
        self.start_button.disconnect()
        self.start_button.clicked.connect(self.close)

        rep, ite = self.rp_box.value(), self.it_box.value()
        self.thread = MonteCarloSim(rep, ite)

        if rep != 1:
            self.prr_bar.setMaximum(rep)
            self.thread.prr_signal.connect(self.prr_bar.setValue)
        else:
            self.prr_bar.setRange(0, 0)

        self.thread.pli_signal.connect(self.it_graphs)
        self.thread.plr_signal.connect(self.rp_graphs)
        self.thread.start()

    def it_graphs(self, xpos, ypos, dist, expt):
        """
        Receives the final signal emitted from the thread when there are no
        replications to be calculated and adds the graphs as widgets.

        Args:
            xpos:   list of `x` coordinates for the random points.
            ypos:   list of `y` coordinates for the random points.
            dist:   list of distances between every pair of points.
            expt:   list of distance expected at that point on the iteration.
        """
        self.main_layout.addWidget(
            PathPlot(xpos, ypos), alignment=Qt.AlignBaseline
        )
        self.main_layout.addWidget(
            DistPlot(dist, expt), alignment=Qt.AlignBaseline
        )
        self.setFixedSize(QSize(1152, 432))
        self.resize_window()

    def rp_graphs(self, rdis):
        """
        Receives the final signal emitted from the thread when there are
        replications to be calculated and adds the graph as a widget.

        Args:
            rdis:   list of differences between expected and walked distances.
        """
        self.main_layout.addWidget(HistPlot(rdis), alignment=Qt.AlignBaseline)
        self.setFixedSize(QSize(640, 432))
        self.resize_window()

    def resize_window(self):
        """
        Marks the progress bar as completed, resizes the window according
        to the graphs created and adds a help message.
        """
        self.start_button.setText("Quit")
        self.prr_bar.setRange(0, 1)
        self.prr_bar.setValue(1)
        resolution = QDesktopWidget().screenGeometry()
        self.move(
            (resolution.width() / 2) - (self.frameSize().width() / 2),
            (resolution.height() / 2) - (self.frameSize().height() / 2),
        )
        self.statusBar().showMessage(
            "Left click and drag to pan, right click and drag to zoom"
        )
