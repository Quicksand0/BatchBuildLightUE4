# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dial_SetupTab.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogSetupProject(object):
    def setupUi(self, DialogSetupProject):
        DialogSetupProject.setObjectName("DialogSetupProject")
        DialogSetupProject.resize(640, 480)
        DialogSetupProject.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(DialogSetupProject)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(DialogSetupProject)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_project = QtWidgets.QWidget()
        self.tab_project.setObjectName("tab_project")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_project)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_project)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ue4_path_label = QtWidgets.QLabel(self.groupBox)
        self.ue4_path_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ue4_path_label.setObjectName("ue4_path_label")
        self.gridLayout_3.addWidget(self.ue4_path_label, 0, 0, 1, 1)
        self.ue4_path_text = QtWidgets.QLineEdit(self.groupBox)
        self.ue4_path_text.setObjectName("ue4_path_text")
        self.gridLayout_3.addWidget(self.ue4_path_text, 0, 1, 1, 1)
        self.ue4_path_label_edit = QtWidgets.QPushButton(self.groupBox)
        self.ue4_path_label_edit.setObjectName("ue4_path_label_edit")
        self.gridLayout_3.addWidget(self.ue4_path_label_edit, 0, 2, 1, 1)
        self.project_file_label = QtWidgets.QLabel(self.groupBox)
        self.project_file_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.project_file_label.setObjectName("project_file_label")
        self.gridLayout_3.addWidget(self.project_file_label, 1, 0, 1, 1)
        self.sub_folder_label = QtWidgets.QLabel(self.groupBox)
        self.sub_folder_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sub_folder_label.setObjectName("sub_folder_label")
        self.gridLayout_3.addWidget(self.sub_folder_label, 2, 0, 1, 1)
        self.project_name_label = QtWidgets.QLabel(self.groupBox)
        self.project_name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.project_name_label.setObjectName("project_name_label")
        self.gridLayout_3.addWidget(self.project_name_label, 3, 0, 1, 1)
        self.project_file_text = QtWidgets.QLineEdit(self.groupBox)
        self.project_file_text.setObjectName("project_file_text")
        self.gridLayout_3.addWidget(self.project_file_text, 1, 1, 1, 1)
        self.sub_folder_text = QtWidgets.QLineEdit(self.groupBox)
        self.sub_folder_text.setObjectName("sub_folder_text")
        self.gridLayout_3.addWidget(self.sub_folder_text, 2, 1, 1, 1)
        self.project_name_text = QtWidgets.QLineEdit(self.groupBox)
        self.project_name_text.setEnabled(False)
        self.project_name_text.setReadOnly(False)
        self.project_name_text.setObjectName("project_name_text")
        self.gridLayout_3.addWidget(self.project_name_text, 3, 1, 1, 1)
        self.project_file_edit = QtWidgets.QPushButton(self.groupBox)
        self.project_file_edit.setObjectName("project_file_edit")
        self.gridLayout_3.addWidget(self.project_file_edit, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_project)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ProjectTreeLevels = QtWidgets.QTreeWidget(self.groupBox_2)
        self.ProjectTreeLevels.setObjectName("ProjectTreeLevels")
        self.ProjectTreeLevels.headerItem().setTextAlignment(0, QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.ProjectTreeLevels)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/Icons/package.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_project, icon, "")
        self.tab_sc = QtWidgets.QWidget()
        self.tab_sc.setObjectName("tab_sc")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_sc)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_sc)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.softwares_label = QtWidgets.QLabel(self.groupBox_3)
        self.softwares_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.softwares_label.setObjectName("softwares_label")
        self.gridLayout_9.addWidget(self.softwares_label, 0, 0, 1, 1)
        self.softwares_comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.softwares_comboBox.setObjectName("softwares_comboBox")
        self.softwares_comboBox.addItem("")
        self.softwares_comboBox.addItem("")
        self.softwares_comboBox.addItem("")
        self.softwares_comboBox.addItem("")
        self.gridLayout_9.addWidget(self.softwares_comboBox, 0, 1, 1, 2)
        self.path_sc_label = QtWidgets.QLabel(self.groupBox_3)
        self.path_sc_label.setEnabled(False)
        self.path_sc_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.path_sc_label.setObjectName("path_sc_label")
        self.gridLayout_9.addWidget(self.path_sc_label, 1, 0, 1, 1)
        self.path_sc_text = QtWidgets.QLineEdit(self.groupBox_3)
        self.path_sc_text.setEnabled(False)
        self.path_sc_text.setObjectName("path_sc_text")
        self.gridLayout_9.addWidget(self.path_sc_text, 1, 1, 1, 1)
        self.path_sc_edit = QtWidgets.QPushButton(self.groupBox_3)
        self.path_sc_edit.setEnabled(False)
        self.path_sc_edit.setObjectName("path_sc_edit")
        self.gridLayout_9.addWidget(self.path_sc_edit, 1, 2, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_sc)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.user_label = QtWidgets.QLabel(self.groupBox_4)
        self.user_label.setEnabled(False)
        self.user_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_label.setObjectName("user_label")
        self.gridLayout_7.addWidget(self.user_label, 0, 0, 1, 1)
        self.user_text = QtWidgets.QLineEdit(self.groupBox_4)
        self.user_text.setEnabled(False)
        self.user_text.setObjectName("user_text")
        self.gridLayout_7.addWidget(self.user_text, 0, 1, 1, 1)
        self.password_label = QtWidgets.QLabel(self.groupBox_4)
        self.password_label.setEnabled(False)
        self.password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_label.setObjectName("password_label")
        self.gridLayout_7.addWidget(self.password_label, 1, 0, 1, 1)
        self.password_text = QtWidgets.QLineEdit(self.groupBox_4)
        self.password_text.setEnabled(False)
        self.password_text.setObjectName("password_text")
        self.gridLayout_7.addWidget(self.password_text, 1, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.gridLayout_6.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 1, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/Icons/git-branch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_sc, icon1, "")
        self.tab_network = QtWidgets.QWidget()
        self.tab_network.setObjectName("tab_network")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_network)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_network)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_network)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_network)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 1, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/Icons/globe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_network, icon2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogSetupProject)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Open|QtWidgets.QDialogButtonBox.RestoreDefaults|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.project_file_label.setBuddy(self.project_file_label)

        self.retranslateUi(DialogSetupProject)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(DialogSetupProject)

    def retranslateUi(self, DialogSetupProject):
        _translate = QtCore.QCoreApplication.translate
        DialogSetupProject.setWindowTitle(_translate("DialogSetupProject", "Dialog"))
        self.groupBox.setTitle(_translate("DialogSetupProject", "Path Setup"))
        self.ue4_path_label.setText(_translate("DialogSetupProject", "Unreal Engine Editor :"))
        self.ue4_path_text.setPlaceholderText(_translate("DialogSetupProject", "UE4Editor.exe"))
        self.ue4_path_label_edit.setText(_translate("DialogSetupProject", "Choice File"))
        self.project_file_label.setText(_translate("DialogSetupProject", "Unreal Project File :"))
        self.sub_folder_label.setText(_translate("DialogSetupProject", "Sub folder (optionnal) :"))
        self.project_name_label.setText(_translate("DialogSetupProject", "Project Name :"))
        self.project_file_text.setPlaceholderText(_translate("DialogSetupProject", "Name.project"))
        self.project_name_text.setPlaceholderText(_translate("DialogSetupProject", "This field contain no description and name."))
        self.project_file_edit.setText(_translate("DialogSetupProject", "Open File"))
        self.groupBox_2.setTitle(_translate("DialogSetupProject", "Levels"))
        self.ProjectTreeLevels.headerItem().setText(0, _translate("DialogSetupProject", "Editable"))
        self.ProjectTreeLevels.headerItem().setText(1, _translate("DialogSetupProject", "Types"))
        self.ProjectTreeLevels.headerItem().setText(2, _translate("DialogSetupProject", "Level Names"))
        self.label_5.setText(_translate("DialogSetupProject", "Levels names"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_project), _translate("DialogSetupProject", "Project"))
        self.groupBox_3.setTitle(_translate("DialogSetupProject", "Source Control Software"))
        self.softwares_label.setText(_translate("DialogSetupProject", "Source Control Software :"))
        self.softwares_comboBox.setItemText(0, _translate("DialogSetupProject", "Disabled"))
        self.softwares_comboBox.setItemText(1, _translate("DialogSetupProject", "Perforce"))
        self.softwares_comboBox.setItemText(2, _translate("DialogSetupProject", "Subversion"))
        self.softwares_comboBox.setItemText(3, _translate("DialogSetupProject", "Git"))
        self.path_sc_label.setText(_translate("DialogSetupProject", "Path Software :"))
        self.path_sc_text.setPlaceholderText(_translate("DialogSetupProject", "p4.exe"))
        self.path_sc_edit.setText(_translate("DialogSetupProject", "Edit"))
        self.groupBox_4.setTitle(_translate("DialogSetupProject", "Sotware Setup"))
        self.user_label.setText(_translate("DialogSetupProject", "User :"))
        self.password_label.setText(_translate("DialogSetupProject", "Password :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sc), _translate("DialogSetupProject", "Source Control"))
        self.pushButton_3.setText(_translate("DialogSetupProject", "Generate file"))
        self.label_7.setText(_translate("DialogSetupProject", "Placeholder 2 :"))
        self.label_6.setText(_translate("DialogSetupProject", "Placeholder :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_network), _translate("DialogSetupProject", "Network"))

