#! python3
import datetime
import re
import subprocess

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget, QHBoxLayout, QFrame, QLabel, QTextEdit, \
    QLineEdit, QPushButton, QFileDialog
import messageBox


class UiMainWindow(QMainWindow):
    """Cria uma classe que representa uma janela."""
    def __init__(self):
        super().__init__()
        """Inicializa os componentes."""
        self.file = ""
        self.text = ""

        self.setWindowTitle("Expressões Regulares")
        self.resize(540, 700)

        self.centralwidget = QWidget(self)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.frmInitial = QFrame(self.centralwidget)
        self.frmInitial.setStyleSheet("background-color: rgb(0, 150, 200);\n")
        self.frmInitial.setFrameShape(QFrame.StyledPanel)
        self.frmInitial.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_frmInitial = QHBoxLayout(self.frmInitial)

        self.frmTexto = QFrame(self.frmInitial)
        self.frmTexto.setStyleSheet(
            "background-color: rgb(20, 170, 220);\n"
            "color: rgb(255, 255, 255);\n"
        )
        self.frmTexto.setFrameShape((QFrame.StyledPanel))
        self.frmTexto.setFrameShadow(QFrame.Raised)
        self.frmTexto.setMaximumWidth(400)
        self.frmTexto.setMinimumWidth(400)

        self.lblTitulo = QLabel(self.frmTexto)
        self.lblTitulo.setGeometry(QRect(
            38,  # x
            40,  # y
            400,  # width
            150  # height
        ))
        self.lblTitulo.setFont(setMyFont(28))
        self.lblTitulo.setText("Search your Regex")

        self.lblInput = QLabel(self.frmTexto)
        self.lblInput.setGeometry(QRect(
            38,  # x
            186,  # y
            400,  # width
            50  # height
        ))
        self.lblInput.setFont(setMyFont(14))
        self.lblInput.setText("Regular Expression: ")

        self.txtInput = QTextEdit(self.frmTexto)
        self.txtInput.setGeometry(
            38,
            228,
            324,
            280)
        self.txtInput.setFont(setMyFont(12))
        self.txtInput.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "color: rgba(0, 0, 0, 180);"
        )

        self.lblArch = QLabel(self.frmTexto)
        self.lblArch.setGeometry(QRect(
            38,  # x
            510,  # y
            324,  # width
            30  # height
        ))
        self.lblArch.setFont(setMyFont(12))
        self.lblArch.setText("Open file (.txt): ")

        self.ltxDir = QLineEdit(self.frmTexto)
        self.ltxDir.setGeometry(
            38,
            540,
            294,
            28
        )
        self.ltxDir.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "color: rgba(0, 0, 0, 180);"
        )
        self.ltxDir.setReadOnly(True)

        self.btnDir = QPushButton(self.frmTexto)
        self.btnDir.setGeometry(
            324,
            540,
            38,
            28
        )
        self.btnDir.setFont(setMyFont(12))
        self.btnDir.setText("...")
        self.btnDir.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 3px;\n"
            "border: 0.5px solid white }\n"
            "QPushButton:hover {\n"
            "border: 1px solid rgb(250,250,250);\n"
            "background-color: rgb(30,180,230); }\n"
        )

        self.btnSearch = QPushButton(self.frmTexto)
        self.btnSearch.setGeometry(
            150,
            600,
            102,
            42
        )
        self.btnSearch.setFont(setMyFont(14))
        self.btnSearch.setText("&Search")
        self.btnSearch.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 3px;\n"
            "border: 1px solid white }\n"
            "QPushButton:hover {\n"
            "border: 1px solid rgb(20,170,220);\n"
            "background-color: rgb(50,190,240); }\n"
            "QPushButton:pressed {\n"
            "border: 1px solid rgb(130,220,255);\n"
            "background-color: rgb(20,170,220); }\n"
        )

        # Define os layouts
        self.horizontalLayout.addWidget(self.frmInitial)
        self.horizontalLayout_frmInitial.addWidget(self.frmTexto)
        self.setCentralWidget(self.centralwidget)

        # Eventos
        self.btnSearch.clicked.connect(self.evtSearch)
        self.btnDir.clicked.connect(self.openText)

    def evtSearch(self):
        """Esse evento utiliza a regex para pesquisar no arquivo txt"""
        # TODO: Vamos chamar uma função para:
        # Pegar o input, criar um compile e pesquisar no arquivo txt
        self.serachRegex()
        # Mensagem informando que deu tudo certo
        self.joinMessage()

    def serachRegex(self):
        """Criar um compile e pesquisar no arquivo txt entao abrir um txt com o resultado"""
        self.readFile()
        tregex = re.compile(rf'{self.txtInput.toPlainText()}')
        fileResult = open(self.file+'_result.txt', 'a')

        with fileResult:
            fileResult.write('-='*30)
            fileResult.write(f"\nPesquisa: r'{self.txtInput.toPlainText()}'\nData: {datetime.datetime.now()}\nResultado:\n")
            for r in tregex.findall(self.text):
                fileResult.write(r+'\n')
        fileResult.close()
        subprocess.Popen(['start', self.file+'_result.txt'], shell=True)

    def openText(self):
        """Abrir o arquivo txt a ser analizado"""
        filenameDir, _ = QFileDialog.getOpenFileName(self, "Selecionar o arquivo de texto",
                                               "C:\\",
                                               "Arquivos de textos (*.txt)")
        self.ltxDir.setText(filenameDir)
        self.file = filenameDir
        subprocess.Popen(['start', self.file], shell=True)

    def readFile(self):
        file = open(self.file, 'r')
        with file:
            text = file.read()
            self.text = text
        file.close()

    def joinMessage(self):
        """Exibe uma caixa de mensagem"""
        messageBox.Tela(
            "Arquivo com o resultado gerado em: ",
            f"{self.file}_result.txt",
            QMessageBox.Information,
            self.returnMessage
        ).open()

    def returnMessage(self):
        """Informa qual btn foi clicado na QmessageBox"""
        pass


def setMyFont(tamanho):
    """Cria uma fonte única"""
    font = QFont()
    font.setFamily("Comic Sans MS")
    font.setPointSize(tamanho)
    return font


if __name__ == "__main__":
    """Inicia a janela principal"""
    import sys
    app = QApplication(sys.argv)
    window = UiMainWindow()
    window.show()
    sys.exit(app.exec_())
