from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib as mplt
from PyQt5 import QtWidgets


class ConfirmScenario(QtWidgets.QDialog):
    """
    Takes in keyworded arguments to plot function and shows corresponding plot in dialog
    """

    def __init__(self, parent=None, window_title="3di scenario regen", **kwargs):
        super(ConfirmScenario, self).__init__(parent)
        self.figure = Figure()
        self.setWindowTitle(window_title)
        layout = QtWidgets.QVBoxLayout()
        self.canvas = FigureCanvas(self.figure)
        self.button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        )
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button_box)
        self.setLayout(layout)
        self.plot(**kwargs)

    def plot(
        self,
        plot_list,
        polygon_patch_list=None,
        title=None,
        xlabel=None,
        ylabel=None,
        legend=None,
    ):
        # clearing old figure
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot()
        ax.grid()

        # plot data
        for plot in plot_list:
            ax.plot(plot.x, plot.y, **plot.keyword_args)

        # plot patches
        if polygon_patch_list:
            for patch in polygon_patch_list:
                ax.add_patch(mplt.patches.Polygon(patch.coords, **patch.keyword_args))
        if title:
            self.figure.suptitle(title)
        if xlabel:
            ax.set_xlabel(xlabel, fontsize=10)
        if ylabel:
            ax.set_ylabel(ylabel, fontsize=10)
        if legend:
            plt.legend(*legend.args, **legend.keyword_args)
        # refresh canvas
        self.canvas.draw()
