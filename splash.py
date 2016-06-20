# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.setWindowModality(QtCore.Qt.WindowModal)
		MainWindow.resize(360, 467)
		MainWindow.setFixedSize(360, 467)
		MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.label = QtGui.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(40, 0, 211, 81))
		font = QtGui.QFont()
		font.setPointSize(24)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName(_fromUtf8("label"))
		self.label_2 = QtGui.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(260, 10, 61, 51))
		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
		brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
		self.label_2.setPalette(palette)
		font = QtGui.QFont()
		font.setPointSize(36)
		font.setBold(True)
		font.setWeight(75)
		self.label_2.setFont(font)
		self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.pushButton = QtGui.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(30, 380, 101, 41))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(230, 380, 101, 41))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
		self.plainTextEdit.setGeometry(QtCore.QRect(30, 70, 311, 291))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.plainTextEdit.setFont(font)
		self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 21))
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
		self.menubar.setSizePolicy(sizePolicy)
		self.menubar.setObjectName(_fromUtf8("menubar"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "Anti Ransom v3", None))
		self.label.setText(_translate("MainWindow", "Anti Ransom", None))
		self.label_2.setText(_translate("MainWindow", "V3", None))
		self.pushButton.setText(_translate("MainWindow", "Stop", None))
		self.pushButton.clicked.connect(b1_clicked)
		self.pushButton_2.setText(_translate("MainWindow", "Go", None))
		self.pushButton_2.clicked.connect(b2_clicked)
		self.plainTextEdit.setPlainText(_translate("MainWindow",  sys.argv[1], None))
		self.plainTextEdit.setReadOnly(True)

class MyWindow(QtGui.QMainWindow):
	print
	

def b1_clicked():
	sys.exit(10)

def b2_clicked():
	sys.exit(20)
	
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    app.setActiveWindow(MainWindow)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


