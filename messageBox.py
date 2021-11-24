import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
#from GetWikiDesigner import *

# Classe improvisada, reformular depois

class Tela(QMainWindow):
    def __init__(self, text, textComp, icon, resultadoUtil, button=QMessageBox.Ok, ):
        super().__init__()
        #self.ui = ui_interface
        #self.ui.setupUi(self)

        self.resultadoUtil = resultadoUtil

        self.button = button
        self.icon = icon
        self.textComp = textComp
        self.text = text
        #self.ui.pushButton.clicked.connect(self.caixas)

    def open(self):
        msg = QMessageBox()
        msg.setWindowTitle("GetWiki")
        msg.setText(self.text)
        msg.setIcon(self.icon)
        msg.setInformativeText(self.textComp)
        msg.setStandardButtons(self.button)
        #msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        #msg.setDefaultButton(QMessageBox.No)
        #msg.setEscapeButton(QMessageBox.No)
        msg.buttonClicked.connect(self.resultadoUtil)
        #msg.setDetailedText("Mais informações")


        retorno = msg.exec()

    def resultado(self, clicado):
        print(clicado.text())


#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    w = Tela()
#    w.show()
#    sys.exit(app.exec_())
