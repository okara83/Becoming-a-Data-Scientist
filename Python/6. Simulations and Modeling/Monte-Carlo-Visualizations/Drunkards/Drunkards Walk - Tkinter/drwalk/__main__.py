#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""__main__.py

The main file for `drwalk`, a Monte Carlo method that simulates random walks
and compares those with the expected distance after a number `n` of steps.

    * `PyQt5.QtWidgets.QApplication` handles the initialization, finalization,
        control flow and main settings for the GUI application.
"""

from __future__ import absolute_import
from sys import argv

from PyQt5.QtWidgets import QApplication

from .qt_window import AppWindow

APP = QApplication(argv)
WINDOW = AppWindow()
WINDOW.show()
exit(APP.exec_())
