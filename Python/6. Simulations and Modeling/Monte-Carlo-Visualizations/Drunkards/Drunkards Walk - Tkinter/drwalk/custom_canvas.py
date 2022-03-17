#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=R0903

"""custom_canvas.py

Group of classes that deal with plotting three kinds of interactive
graphs. The structure for this file was loosely based on Matplotlib's
examples [1].

    * `matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg` is the canvas
        that the figure renders into. Ultimately, a figure embedded into
        a QWidget object.
    * `matplotlib.backends.backend_qt5.NavigationToolbar2QT` is the common
        toolbar that appears when one calls `plt.show()`. Even if one does
        not want it into the widget, it can be used to interact with the
        graph through mouse actions if the object is created correctly.
    * `matplotlib.pyplot.subplots` creates a figure with a set of subplots
        already made, all with one simple call.

[1] http://matplotlib.org/examples/user_interfaces/embedding_in_qt5.html
"""

from __future__ import absolute_import

from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as Toolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FCanvas
from matplotlib.pyplot import subplots


class CustomCanvas(FCanvas):
    """
    The parent class for the figures rendered as widgets on the Qt program.
    """

    def __init__(self):
        """
        Initializes a CustomCanvas object with the following attributes:

            axes:       contains most of the figure elements ready to be
                        customized through various functions. Displays
                        scientific notation right from the start.

        The `__init__` function is then called, representing the constructor
        for the parent class. Finally, the toolbar object is created
        and a function that enables panning and zooming is called.
        """
        fig, self.axes = subplots()
        self.axes.ticklabel_format(style="sci", scilimits=(0, 0))
        super().__init__(fig)
        Toolbar(self, None).pan()


class HistPlot(CustomCanvas):
    """
    Draws a histogram with, at most, thirty classes, when there is more than
    one replication on the Monte Carlo simulation.
    """

    def __init__(self, data):
        """
        Initializes a HistPlot object with the following attributes:

            data:   represents the raw data that will be plotted.

        Calls the parent class constructor, edits the graph's title and
        draws a histogram with `data`.
        """
        super().__init__()
        self.axes.set_title("Histogram for $r \\times (d_n - \\sqrt{n})$")
        self.axes.hist(data, min(int(len(data) ** 0.5), 30), edgecolor="k")


class PathPlot(CustomCanvas):
    """
    Draws a random walk if there are no replications to be made. Plotting of
    more than a million points may be slow.
    """

    def __init__(self, *data):
        """
        Initializes a PathPlot object with the following attributes:

            data:   represents the raw data that will be plotted. Can be
                    a n-uple, in which case it should be unpacked.

        Calls the parent class constructor, edits the graph's title and
        draws various points connected by lines, as well as markers for
        the first and last points.
        """
        super().__init__()
        xpos, ypos = data
        self.axes.set_title("Random walk")
        self.axes.plot(xpos, ypos, "y-")
        self.axes.plot(xpos, ypos, "b.", markersize=2)
        self.axes.plot(xpos[0], ypos[0], color="r", marker="$S$")
        self.axes.plot(xpos[-1], ypos[-1], color="r", marker="$E$")


class DistPlot(CustomCanvas):
    """
    Draws a comparison graph between the distance walked after a random event
    and the expected distance, which is √i for 0 < `i` ≤ `n` points.
    """

    def __init__(self, *data):
        """
        Initializes a DistPlot object with the following attributes:

            data:   represents the raw data that will be plotted. Can be
                    a n-uple, in which case it should be unpacked.

        Calls the parent class constructor, edits the graph's title and
        draws the increasing distance graphs, as well as a line representing
        the difference between expected and walked distances.
        """
        super().__init__()
        dist, expt = data
        final_dist = abs(dist[-1] - expt[-1])
        self.axes.set_title("Distance comparison")
        comps, = self.axes.plot(dist, label="$d_i - d_{i-1}$")
        expct, = self.axes.plot(expt, label="$\\sqrt{i}$")
        diffs, = self.axes.plot(
            [len(dist) * 1.01, len(expt) * 1.01],
            [dist[-1], expt[-1]],
            label=f"$d_n - \\sqrt{{n}} \\approx {final_dist:.2f}$",
        )
        self.axes.legend(handles=[comps, expct, diffs], loc=0, frameon=False)
