from PyQt5.QtWidgets import QMainWindow
from view.telaSistema import Ui_janelaPrincipal as Ui_MainWindow
import random, threading, time
from datetime import datetime

"""
Programas
 
Informações e dicas
 
Anuncie
 
Ajude
 
Sobre…
 
Início » Como ajustar o brilho da tela a partir da linha de comando no Linux

Como ajustar o brilho da tela a partir da linha de comando no Linux
18/10/2020 Por Edivaldo Brito
Se você quer ter controle completo sobre a tela do seu PC, veja como ajustar o brilho da tela a partir da linha de comando no Linux.

Ajustar o brilho da tela no modo gráfico é fácil. Já analisamos um aplicativo Brightness Controller que ajuda a controlar o brilho em sistemas operacionais Linux.

Mas, o desenvolvimento desse aplicativo parece estar parado há mais de um ano e eu não se tem certeza se ele funcionará com versões recentes do Linux.

Outra desvantagem é que o aplicativo Brightness Controller é compatível apenas com o Python2.

Como ajustar o brilho da tela a partir da linha de comando no Linux
Como ajustar o brilho da tela a partir da linha de comando no Linux
Enquanto procurava formas alternativas, descobri que podemos fazer esse trabalho facilmente com um utilitário de linha de comando chamado “xrandr“.
 
O programa xrandr é usado para definir o tamanho, orientação e/ou reflexão das saídas de uma tela.

Usando o Xrandr, também é possível exibir o estado atual da tela do sistema, alterar ou definir a resolução, desativar as saídas desconectadas e ativar as conectadas.

E o bom é que o Xrandr vem pré-instalado com a maioria das distribuições Linux, por isso não é preciso se preocupar em instalar aplicativos adicionais.

Como ajustar o brilho da tela a partir da linha de comando no Linux
Para ajustar o brilho do monitor a partir da linha de comando no Linux, primeiro, precisamos verificar o estado atual da exibição do sistema.

Para fazer isso, execute:

xrandr -q
A saída será mais ou menos assim:

Screen 0: minimum 320 x 200, current 1366 x 768, maximum 8192 x 8192
LVDS-1 connected primary 1366x768+0+0 (normal left inverted right x axis y axis) 344mm x 194mm
1366x768 60.00*+ 40.00 
1280x720 60.00 59.99 59.86 59.74 
1024x768 60.04 60.00 
960x720 60.00 
928x696 60.05 
896x672 60.01 
1024x576 59.95 59.96 59.90 59.82 
960x600 59.93 60.00 
960x540 59.96 59.99 59.63 59.82 
800x600 60.00 60.32 56.25 
840x525 60.01 59.88 
864x486 59.92 59.57 
700x525 59.98 
800x450 59.95 59.82 
640x512 60.02 
700x450 59.96 59.88 
640x480 60.00 59.94 
720x405 59.51 58.99 
684x384 59.88 59.85 
640x400 59.88 59.98 
640x360 59.86 59.83 59.84 59.32 
512x384 60.00 
512x288 60.00 59.92 
480x270 59.63 59.82 
400x300 60.32 56.34 
432x243 59.92 59.57 
320x240 60.05 
360x202 59.51 59.13 
320x180 59.84 59.32 
VGA-1 disconnected (normal left inverted right x axis y axis)
HDMI-1 disconnected (normal left inverted right x axis y axis)
DP-1 disconnected (normal left inverted right x axis y axis)
Como você pode ver, o display atualmente conectado é o LVDS-1. Essa saída exibe a resolução atual e a taxa de atualização da tela.

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
        self.tela.botaoEntrar.clicked.connect(self.exibirConteudo)
        contar = threading.Thread(target = self.contarSegundos)
        contar.daemon = True
        contar.start()

    def exibirConteudo(self):
        login = self.tela.entradaNome.toPlainText()
        senha = self.tela.entradaSenha.toPlainText()
        self.tela.labelErro.setText("logado!")

    def contarSegundos(self):
        while True:
            now = datetime.now()
            self.tela.relogio.setText(now.strftime("%H:%M:%S"))
            time.sleep(1)

