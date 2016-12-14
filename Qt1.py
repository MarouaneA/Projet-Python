# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/eleve/IENAC/veronhu/Bureau/projetpython/untitled.ui'
#
# Created: Tue Nov 29 15:08:57 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(601, 443)
        self.slider_vertic = QtWidgets.QSlider(Dialog)
        self.slider_vertic.setGeometry(QtCore.QRect(190, 390, 160, 29))
        self.slider_vertic.setOrientation(QtCore.Qt.Horizontal)
        self.slider_vertic.setObjectName("slider_vertic")
        self.slider_horiz = QtWidgets.QSlider(Dialog)
        self.slider_horiz.setGeometry(QtCore.QRect(560, 100, 29, 160))
        self.slider_horiz.setOrientation(QtCore.Qt.Vertical)
        self.slider_horiz.setObjectName("slider_horiz")
        self.label_time = QtWidgets.QLabel(Dialog)
        self.label_time.setGeometry(QtCore.QRect(460, 300, 66, 17))
        self.label_time.setObjectName("label_time")
        self.label_carac = QtWidgets.QLabel(Dialog)
        self.label_carac.setGeometry(QtCore.QRect(460, 340, 66, 17))
        self.label_carac.setObjectName("label_carac")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 70, 46, 241))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.carac1 = QtWidgets.QLabel(self.widget)
        self.carac1.setObjectName("carac1")
        self.verticalLayout.addWidget(self.carac1)
        self.carac2 = QtWidgets.QLabel(self.widget)
        self.carac2.setObjectName("carac2")
        self.verticalLayout.addWidget(self.carac2)
        self.carac3 = QtWidgets.QLabel(self.widget)
        self.carac3.setObjectName("carac3")
        self.verticalLayout.addWidget(self.carac3)
        self.carac4 = QtWidgets.QLabel(self.widget)
        self.carac4.setObjectName("carac4")
        self.verticalLayout.addWidget(self.carac4)
        self.carac5 = QtWidgets.QLabel(self.widget)
        self.carac5.setObjectName("carac5")
        self.verticalLayout.addWidget(self.carac5)
        self.carac6 = QtWidgets.QLabel(self.widget)
        self.carac6.setObjectName("carac6")
        self.verticalLayout.addWidget(self.carac6)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(450, 90, 87, 181))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.widget1)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_2.addWidget(self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout_2.addWidget(self.comboBox_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "timeline"))
        self.label_time.setText(_translate("Dialog", "time_label"))
        self.label_carac.setText(_translate("Dialog", "carac_label"))
        self.carac1.setText(_translate("Dialog", "carac1"))
        self.carac2.setText(_translate("Dialog", "carac2"))
        self.carac3.setText(_translate("Dialog", "carac3"))
        self.carac4.setText(_translate("Dialog", "carac4"))
        self.carac5.setText(_translate("Dialog", "carac5"))
        self.carac6.setText(_translate("Dialog", "carac6"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())

