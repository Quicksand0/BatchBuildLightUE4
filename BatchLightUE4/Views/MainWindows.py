import os, json

from PyQt5 import QtWidgets, QtGui
from BatchLightUE4.Views.WindowsMainWindows import Ui_MainWindow
from BatchLightUE4.Views.WindowsSetupView import Ui_TabWidget


class SetupTab(QtWidgets.QTabWidget, Ui_TabWidget):
    """This object create a new windows"""
    def __init__(self):
        super(SetupTab, self).__init__()
        self.setupUi(self)

        json_path = os.path.abspath("BatchLightUE4/Models/setup_path.json")
        if os.path.isfile(json_path):
            data = json.loads(open(json_path).read())
            ue4_path = data['UE4 Editor']
            ue4_project = data['UE4 Project']

        else:
            ue4_path = ''
            ue4_project = ''

        # Path Panel
        self.pushPathOpenUnreal.clicked.connect(lambda: self.openSave(1))
        self.lineEditUnreal.setText(ue4_path)
        self.pushPathOpenProject.clicked.connect(lambda: self.openSave(2))
        self.lineEditProject.setText(ue4_project)

        self.buttonBoxPath.button(
            QtWidgets.QDialogButtonBox.Save).clicked.connect(self.tabSave)

    def openSave(self, state):
        if state == 1:
            file_description = 'Open the UE4 Editor'
            file_select = 'UE4Editor.exe'
            field = self.lineEditUnreal.setText

        elif state == 2:
            file_description = 'Open a Unreal Project File'
            file_select = '*.uproject'
            field = self.lineEditProject.setText

        else:
            file_description = 'Open a File'
            file_select = ''
            field = None

        (filename, filter) = QtWidgets.QFileDialog.getOpenFileName(
            self,
            file_description,
            filter=file_select)

        return field(filename)

    def tabSave(self):
        editor = self.lineEditUnreal.text()
        project = self.lineEditProject.text()

        path_dict = {
            "UE4 Editor": editor,
            "UE4 Project": project,
        }

        json_path = os.path.abspath("BatchLightUE4/Models/setup_path.json")
        with open(json_path, 'w') as f:
            json.dump(path_dict, f, indent=4)

        SetupTab.close(self)


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main Windows, principal view, this windows can be show all level,
    access on many option -path setup, network, log... """

    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

        # Triggered Menu
        #     File Menu
        self.actionLast_project.triggered.connect(self.openSave)
        self.actionExit.triggered.connect(self.closeEvent)

        #    Setup and Option Menu
        self.actionOptions.triggered.connect(self.editLevels)
        self.actionPaths.triggered.connect(lambda: self.editLevels(1))
        self.actionNetworks.triggered.connect(lambda: self.editLevels(2))
        self.actionCSV.triggered.connect(lambda: self.editLevels(3))

        self.pushLevelsSelect.clicked.connect(lambda: self.selectLevel(True))
        self.pushLevelsDeselect.clicked.connect(self.selectLevel)
        self.toolLevelsEdit.clicked.connect(self.editLevels)

        self.pushToolsBuils.clicked.connect(self.buildLevel)

    # File Menu
    def openSave(self, state):
        if state == 1:
            self.str_debug = 'First Value'
            self.file_setup = filter="Project (*.blight)"
        else:
            self.str_debug = 'Pas de status, basique way'
            self.file_setup = filter="Project (*.blight)"


        print(self.str_debug)

        (filename, filter) = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Open a previous project',
            self.file_setup)


    # Events
    def editLevels(self, id):
        print(id)
        self.dialog = SetupTab()
        self.dialog.show()
        self.dialog.setCurrentIndex(id)

    def selectLevel(self, state):
        if state:
            print('Select all Level')

        else:
            print('Deselect all Level')

    def buildLevel(self):
        print('Build Level')

    def closeEvent(self, event):
        confirmation = "Are your sur you want close this application ?"
        answer = QtWidgets.QMessageBox.question(self, "Confirmation",
                                                confirmation,
                                                QtWidgets.QMessageBox.Yes,
                                                QtWidgets.QMessageBox.No)

        if answer == QtWidgets.QMessageBox.Yes:
            event.accept()

        else:
            event.ignore()
