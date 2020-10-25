from PyQt5.QtWidgets import QMainWindow
from view.telaSistema import Ui_janelaPrincipal as Ui_MainWindow
import random, threading, time, os, subprocess
from datetime import datetime

"""
para saber quais telas estão conectadas use:
xrandr -q | grep ' connected' | head -n 1 | cut -d ' ' -f1


para ajustar o brilho use
xrandr --output VGA-1 --brightness 0.7
"""
class ControllerTelaSistema(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)
        self.tela.brilho.valueChanged.connect(self.exibirValor)


    def exibirValor(self):
        atual = str((self.tela.brilho.value()+50)/100)
        self.tela.valor.setText(atual)
        os.system("xrandr --output VGA-1 --brightness {}".format(atual))