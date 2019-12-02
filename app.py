import os
import sys
import configparser
from PyQt5 import QtWidgets, uic, QtGui, QtCore

# from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
# from PyQt5.QtWidgets import QHeaderView, QPushButton, QWidget

APP_DIR = os.path.dirname(os.path.realpath(__file__))
DS = os.path.sep

config = configparser.ConfigParser()
# jkjk

# Just a small function to write the file
def write_file():
    config.write(open('config.ini', 'w'))


if not os.path.exists('config.ini'):
    config['DATABASE'] = {
        'database_server': '127.0.0.1',
        'database_port': '1433',
        'database_name': 'DbName',
        'database_username': 'sa',
        'database_password': 'pass'
    }
    config['APP'] = {
        'app_favicon': 'favicon.png'
    }
    write_file()
else:
    # Read File
    config.sections()
    config.read('config.ini')


# print(os.environ)
# config = configparser.ConfigParser()
# with open('config.ini', 'w') as configfile:
#     config.write(configfile)
#    config['DATABASE']['database_server'] = '127.0.0.1'
#    config['DATABASE']['database_port'] = '1433'
#    config['DATABASE']['database_name'] = 'DbName'
#    config['DATABASE']['database_username'] = 'sa'
#    config['DATABASE']['database_password'] = 'pass'
#    config['APP']['app_favicon'] = 'favicon.png'


# config.sections()
# config.read('config.ini')

DATABASE_SERVER = config['DATABASE']['database_server'] + ',' + config['DATABASE']['database_port']  # "127.0.0.1,1433"
DATABASE_NAME = config['DATABASE']['database_name']
USERNAME = config['DATABASE']['database_username']
PASSWORD = config['DATABASE']['database_password']
APP_FAVICON = config['APP']['app_favicon']


class UiWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UiWindow, self).__init__(parent)
        uic.loadUi('MainWidget.ui', self)
        self.btnTools = self.findChild(QtWidgets.QPushButton, 'btnTools')


class UiTool(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UiTool, self).__init__(parent)
        uic.loadUi('ToolBoxWidget.ui', self)
        self.btnWin = self.findChild(QtWidgets.QPushButton, 'btnWin')


class App(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        uic.loadUi('App.ui', self)
        self.setWindowIcon(QtGui.QIcon(APP_DIR + DS + APP_FAVICON))

        self.actionMenuMain = self.findChild(QtWidgets.QAction, 'actionMenuMain')
        self.actionMenuMain.setShortcut('Ctrl+M')
        self.actionMenuMain.triggered.connect(self.startUIWindow)
        self.actionMenuToolBox = self.findChild(QtWidgets.QAction, 'actionMenuToolBox')
        self.actionMenuToolBox.setShortcut('Ctrl+T')
        self.actionMenuToolBox.triggered.connect(self.startUIToolTab)

        self.startUIWindow()

    def startUIToolTab(self):
        self.ToolTab = UiTool(self)
        self.setWindowTitle("UI ToolTab")
        self.setCentralWidget(self.ToolTab)
        self.ToolTab.btnWin.clicked.connect(self.startUIWindow)
        self.show()

    def startUIWindow(self):
        self.Window = UiWindow(self)
        self.setWindowTitle("UI Window")
        self.setCentralWidget(self.Window)
        self.Window.btnTools.clicked.connect(self.startUIToolTab)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = App()
    sys.exit(app.exec_())
