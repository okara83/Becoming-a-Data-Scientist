#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=R0903

"""monte_carlo.py

A number crunching class that simulates the drunken sailor's random walk [1]
in a separate thread.

    * `PyQt5.QtCore.QThread` is a class that provides platform-independent
        management of threads within the program.
    * `PyQt5.QtCore.pyqtSignal` is a class attribute that is bound to a
        class instance whenever it is called, allowing data transfer
        between threads.

[1] http://blog.wolfram.com/2011/06/08/
"""

from __future__ import absolute_import
from math import cos, sin

import numpy.random
from PyQt5.QtCore import QThread, pyqtSignal


class MonteCarloSim(QThread):
    """
    A QThread reimplementation that may emit three signals, discussed below:

        prr_signal: progress bar signal for replications (r), an integer
                    emitted every time a replication is calculated.
        pli_signal: plotting signal, a tuple of lists with the final data:
                    `x` and `y` coordinates for the random points, estimated
                    and walked distances.
        plr_signal: plotting signal, a list containing the absolute value
                    of the differences between estimated and walked distances.
    """

    prr_signal = pyqtSignal(int)
    pli_signal = pyqtSignal(list, list, list, list)
    plr_signal = pyqtSignal(list)

    def __init__(self, replications, iterations):
        """
        Initializes a MonteCarloSim object with the following attributes:

            replications:   number of times the experiment must be repeated.
            iterations:     number of steps taken on the random walk.
        """
        super().__init__()
        self.repl = replications
        self.iter = iterations

    def run(self):
        """
        The starting point for the thread. Returning from this method will
        end the execution of the thread. Takes the attributes and creates
        lists that will be populated with random data and calculations
        derived from it. Emits signals on every replication.
        """
        if self.repl == 1:
            xpos, ypos, dist, expt = ([0] * self.iter for _ in range(4))
            angles = numpy.random.randint(0, 361, self.iter)

            for i in range(self.iter):
                xpos[i] = xpos[i - 1] + cos(angles[i])
                ypos[i] = ypos[i - 1] + sin(angles[i])
                dist[i] = (xpos[i] ** 2 + ypos[i] ** 2) ** 0.5
                expt[i] = i ** 0.5

            self.pli_signal.emit(xpos, ypos, dist, expt)

        else:
            rdis = [0] * self.repl
            angles = numpy.random.randint(0, 361, self.repl * self.iter)

            for i in range(0, self.repl * self.iter, self.iter):
                xpos = sum(map(cos, angles[i : i + self.iter]))
                ypos = sum(map(sin, angles[i : i + self.iter]))
                rdis[i // self.iter] = (xpos ** 2 + ypos ** 2) ** 0.5
                self.prr_signal.emit((i // self.iter) + 1)

            self.plr_signal.emit(rdis)
