import os
import sys
def ajustaBrilho():
    try:
        valor = float(sys.argv[1])
        if valor <.1 or valor > 2:
            print("Valor invalido")
            return
        comando = "xrandr --output HDMI-A-0 --brightness {}".format(valor)
        os.system(comando)
    except:
        print("Erro, voce deve passar um parametro de 0.1 até 2.0 ")
        print("Exemplo: python ajustaBrilho.py 0.5")) 
ajustaBrilho()