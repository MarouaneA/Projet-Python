__author__ = 'veronhu'


import sys

from PyQt5 import QtWidgets, QtCore
from Qt1 import Ui_Dialog
import action
import inspectormoi
import visumarouane

if __name__ == "__main__":

    MUSIC_FILE='essai_donnees_2.txt'
    act= action.load_actions(MUSIC_FILE)

    # Initialize Qt
    app = QtWidgets.QApplication([])

    # create the radar view and the time navigation interface
    View = visumarouane.View(act)

    # create the inspector
    the_inspector_window = inspectormoi.Inspector()

    # create a QDockWidget for the inspector
    the_inspector_dock = QtWidgets.QDockWidget()
    the_inspector_dock.setWidget(the_inspector_window)

    # create the QMainWindow and add both widgets
    win = QtWidgets.QMainWindow()
    win.setWindowTitle("AirPort Sim Qt MainWindow & Dock")
    win.setCentralWidget(View)
    win.addDockWidget(1, the_inspector_dock)
    win.resize(1000, 600)
    win.show()
    # win.showMaximized()
    print(QtCore.Qt.DockWidgetArea(2))
    # enter the main loop
    result = app.exec_()

    # shut down nicely if main loop has exited, passing the 'result' i.e. the status or error code
    sys.exit(result)
