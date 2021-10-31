# IMPORTANDO A CLASSE MAINWINDOW
from ui.calcPy import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

# INICIANDO FUNÇÃO PRINCIPAL
def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    uiMainWindow = Ui_MainWindow()
    uiMainWindow.setupUi(mainWindow)
    
    # MOSTRANDO JANELA PRINCIPAL
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    