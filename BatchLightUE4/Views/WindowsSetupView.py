# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowsSetupView.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(666, 317)
        self.Softwareoptions = QtWidgets.QWidget()
        self.Softwareoptions.setObjectName("Softwareoptions")
        self.formLayout = QtWidgets.QFormLayout(self.Softwareoptions)
        self.formLayout.setObjectName("formLayout")
        self.label_18 = QtWidgets.QLabel(self.Softwareoptions)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_18.setFont(font)
        self.label_18.setText("")
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/info.png"))
        self.label_18.setScaledContents(False)
        self.label_18.setWordWrap(False)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.label_17 = QtWidgets.QLabel(self.Softwareoptions)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_17.setFont(font)
        self.label_17.setWordWrap(True)
        self.label_17.setIndent(6)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_17)
        self.groupBox = QtWidgets.QGroupBox(self.Softwareoptions)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 305, 166))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.treeViewLevels = QtWidgets.QTreeView(self.scrollAreaWidgetContents)
        self.treeViewLevels.setObjectName("treeViewLevels")
        self.horizontalLayout_4.addWidget(self.treeViewLevels)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.addWidget(self.scrollArea)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.algoTreeView = QtWidgets.QComboBox(self.groupBox)
        self.algoTreeView.setObjectName("algoTreeView")
        self.algoTreeView.addItem("")
        self.algoTreeView.addItem("")
        self.algoTreeView.addItem("")
        self.algoTreeView.addItem("")
        self.horizontalLayout_5.addWidget(self.algoTreeView)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.groupBox)
        TabWidget.addTab(self.Softwareoptions, "")
        self.Path = QtWidgets.QWidget()
        self.Path.setObjectName("Path")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Path)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line = QtWidgets.QFrame(self.Path)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)
        self.buttonBoxPath = QtWidgets.QDialogButtonBox(self.Path)
        self.buttonBoxPath.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.RestoreDefaults|QtWidgets.QDialogButtonBox.Save)
        self.buttonBoxPath.setObjectName("buttonBoxPath")
        self.gridLayout_3.addWidget(self.buttonBoxPath, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.Path)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/info.png"))
        self.label_7.setScaledContents(False)
        self.label_7.setWordWrap(False)
        self.label_7.setIndent(-1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.Path)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setIndent(6)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.Path)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEditUnreal = QtWidgets.QLineEdit(self.Path)
        self.lineEditUnreal.setText("")
        self.lineEditUnreal.setObjectName("lineEditUnreal")
        self.gridLayout_2.addWidget(self.lineEditUnreal, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.Path)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEditProject = QtWidgets.QLineEdit(self.Path)
        self.lineEditProject.setObjectName("lineEditProject")
        self.gridLayout_2.addWidget(self.lineEditProject, 1, 1, 1, 1)
        self.pushPathOpenUnreal = QtWidgets.QPushButton(self.Path)
        self.pushPathOpenUnreal.setObjectName("pushPathOpenUnreal")
        self.gridLayout_2.addWidget(self.pushPathOpenUnreal, 0, 2, 1, 1)
        self.pushPathOpenProject = QtWidgets.QPushButton(self.Path)
        self.pushPathOpenProject.setObjectName("pushPathOpenProject")
        self.gridLayout_2.addWidget(self.pushPathOpenProject, 1, 2, 1, 1)
        self.pushPathDataLevels = QtWidgets.QPushButton(self.Path)
        font = QtGui.QFont()
        font.setItalic(True)
        self.pushPathDataLevels.setFont(font)
        self.pushPathDataLevels.setObjectName("pushPathDataLevels")
        self.gridLayout_2.addWidget(self.pushPathDataLevels, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(513, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 3, 0, 1, 1)
        TabWidget.addTab(self.Path, "")
        self.Network = QtWidgets.QWidget()
        self.Network.setObjectName("Network")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.Network)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.Network)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setText("")
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/info.png"))
        self.label_11.setScaledContents(False)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.Network)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_12.setFont(font)
        self.label_12.setIndent(6)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.Network)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_7.addWidget(self.line_2, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.Network)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.Network)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.buttonBoxNetwork = QtWidgets.QDialogButtonBox(self.Network)
        self.buttonBoxNetwork.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxNetwork.setObjectName("buttonBoxNetwork")
        self.gridLayout_7.addWidget(self.buttonBoxNetwork, 3, 0, 1, 1)
        TabWidget.addTab(self.Network, "")
        self.CSV = QtWidgets.QWidget()
        self.CSV.setObjectName("CSV")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.CSV)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.CSV)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_15.setFont(font)
        self.label_15.setText("")
        self.label_15.setTextFormat(QtCore.Qt.AutoText)
        self.label_15.setPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/info.png"))
        self.label_15.setScaledContents(False)
        self.label_15.setWordWrap(False)
        self.label_15.setIndent(6)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.CSV)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_16.setFont(font)
        self.label_16.setIndent(6)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.CSV)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_5.addWidget(self.line_3, 1, 0, 2, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.CSV)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.CSV)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.CSV)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.CSV)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_8.addWidget(self.lineEdit_8)
        self.pushButton_6 = QtWidgets.QPushButton(self.CSV)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_8.addWidget(self.pushButton_6)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.CSV)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.CSV)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.CSV)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 4, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.CSV)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 5, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 2, 1, 1, 1)
        self.buttonBoxCSV = QtWidgets.QDialogButtonBox(self.CSV)
        self.buttonBoxCSV.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxCSV.setObjectName("buttonBoxCSV")
        self.gridLayout_5.addWidget(self.buttonBoxCSV, 3, 0, 1, 2)
        TabWidget.addTab(self.CSV, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        self.label_17.setText(_translate("TabWidget", "All options avaible here... ho what ? Yes, i know it\'s empty, but don\'t be afraid ; it\'s a Work in Progress !"))
        self.groupBox.setTitle(_translate("TabWidget", "Levels Views"))
        self.label_6.setText(_translate("TabWidget", "Method Tree Selected : "))
        self.algoTreeView.setItemText(0, _translate("TabWidget", "Folders Contains"))
        self.algoTreeView.setItemText(1, _translate("TabWidget", "Master Levels"))
        self.algoTreeView.setItemText(2, _translate("TabWidget", "Path Levels"))
        self.algoTreeView.setItemText(3, _translate("TabWidget", "Full Random"))
        self.label.setText(_translate("TabWidget", "Levels : Name editable project"))
        self.textBrowser.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Resume levels used, the widget must be changed !</p></body></html>"))
        TabWidget.setTabText(TabWidget.indexOf(self.Softwareoptions), _translate("TabWidget", "Options"))
        self.label_8.setText(_translate("TabWidget", "This pannel define all path needed."))
        self.label_2.setText(_translate("TabWidget", "Unreal Engine Path :"))
        self.lineEditUnreal.setPlaceholderText(_translate("TabWidget", "Unreal.exe"))
        self.label_5.setText(_translate("TabWidget", "Project File Path :"))
        self.lineEditProject.setPlaceholderText(_translate("TabWidget", "file.uproject"))
        self.pushPathOpenUnreal.setText(_translate("TabWidget", "Open"))
        self.pushPathOpenProject.setText(_translate("TabWidget", "Open"))
        self.pushPathDataLevels.setText(_translate("TabWidget", "Generate Levels Data"))
        TabWidget.setTabText(TabWidget.indexOf(self.Path), _translate("TabWidget", "Path"))
        self.label_12.setText(_translate("TabWidget", "Your setup with all computer avaible on your network"))
        self.label_3.setText(_translate("TabWidget", "Network Name :"))
        self.label_9.setText(_translate("TabWidget", "TextLabel"))
        TabWidget.setTabText(TabWidget.indexOf(self.Network), _translate("TabWidget", "Network"))
        self.label_16.setText(_translate("TabWidget", "Setup your CSV software, Git, Perforce or SVN."))
        self.label_4.setText(_translate("TabWidget", "CSV Tools :"))
        self.comboBox.setItemText(0, _translate("TabWidget", "Perforce"))
        self.comboBox.setItemText(1, _translate("TabWidget", "Git"))
        self.comboBox.setItemText(2, _translate("TabWidget", "Subversion"))
        self.label_13.setText(_translate("TabWidget", "Executable File"))
        self.lineEdit_8.setPlaceholderText(_translate("TabWidget", "p4.exe"))
        self.pushButton_6.setText(_translate("TabWidget", "Open"))
        self.label_14.setText(_translate("TabWidget", "Identifiant :"))
        self.label_19.setText(_translate("TabWidget", "Password :"))
        TabWidget.setTabText(TabWidget.indexOf(self.CSV), _translate("TabWidget", "CSV"))

