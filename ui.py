# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(467, 669)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #222")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 561, 201))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: #fb5b5d")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 0, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(160, 30, 151, 161))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("exchange.png"))
        self.label_2.setObjectName("label_2")
        self.input_amount1 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount1.setGeometry(QtCore.QRect(50, 220, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_amount1.setFont(font)
        self.input_amount1.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"")
        self.input_amount1.setText("")
        self.input_amount1.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount1.setObjectName("input_amount1")
        self.output_amount1 = QtWidgets.QLineEdit(self.centralwidget)
        self.output_amount1.setGeometry(QtCore.QRect(50, 380, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_amount1.setFont(font)
        self.output_amount1.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"")
        self.output_amount1.setAlignment(QtCore.Qt.AlignCenter)
        self.output_amount1.setObjectName("output_amount1")
        self.output_amount2 = QtWidgets.QLineEdit(self.centralwidget)
        self.output_amount2.setGeometry(QtCore.QRect(50, 460, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_amount2.setFont(font)
        self.output_amount2.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"")
        self.output_amount2.setAlignment(QtCore.Qt.AlignCenter)
        self.output_amount2.setObjectName("output_amount2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 580, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"   color: white;\n"
"   background-color: #fb5b5d;\n"
"    border-radius: 30;\n"
"}\n"
"\n"
"QpushButton:Pressed{\n"
"    background-color: #fa4244\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.input_amount2 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount2.setGeometry(QtCore.QRect(50, 300, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_amount2.setFont(font)
        self.input_amount2.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"")
        self.input_amount2.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount2.setObjectName("input_amount2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "  CURRENCY CONVERTER"))
        self.pushButton.setText(_translate("MainWindow", "CONVERT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
