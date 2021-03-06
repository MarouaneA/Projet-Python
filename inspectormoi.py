__author__ = 'veronhu'
"""
    Class displaying flight information
    wraps a widget designed with Qt Designer
    Version integrated in the airport simulator
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QListWidgetItem

import action
from Qt1 import Ui_Dialog


class Inspector(QWidget):
    """ Widget displaying information about a Flight """

    def __init__(self):
        super(Inspector, self).__init__()

        # sets up instance variables

        self.ui_flightInspector = Ui_Dialog()

        # sets up the widget created with Qt Designer and pyuic
        self.ui_flightInspector.setupUi(self)

        # populates the 'filter by type' combobox
        types = ["penis", "Departures", "Arrivals"]
        self.ui_flightInspector.comboBox_2.addItems(types)

        # populates the 'filter by runway' combobox
        runways = ["penis", "09L-27R", "09R-27L", "08L-26R", "08R-26L"]
        self.ui_flightInspector.comboBox.addItems(runways)


        self.show()



