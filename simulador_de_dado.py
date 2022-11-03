# Simulador de dados
# Simular o uso de um dado, gerando um valor de 1 até 6

import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        #self.mensagem = 'Você gostaria de gerar uma novo valor para o dado?'

        # Layout
        self.layout = [
            [sg.Text('Jogar o dados?')],
            [sg.Button('sim'), sg.Button('Não')]
        ]

    def Iniciar(self):

        # Criar uma janela
        self.janela = sg.Window('Simulador de dado', layout = self.layout)
        # Ler os valores na tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer algumas coisas com esses valores
        while True:
            try:
                if self.eventos == 'sim' or self.eventos == 's':
                    self.GerarValorDoDado()
                elif self.eventos == 'não' or self.eventos == 'n':
                    print('Agradecemos a sua participação')
                else:
                    print('Favor digitar sim ou não')
            except:
                print('ocorreu um erro ao receber a sua self.eventos')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()
