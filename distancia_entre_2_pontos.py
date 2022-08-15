# Este código pede ao usuário para informar as coodernadas de dois pontos,
# e calcula a distância entre eles.

import PySimpleGUI as sg
import math

def calcula_distancia(x1,y1,x2,y2):
	return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


# if (__name__ == '__main__'):
# 	x1 = float(input('\nDigite a abcissa do primeiro ponto: '))
# 	y1 = float(input('Digite a ordenada do primeiro ponto: '))
# 	x2 = float(input('Digite a abcissa do segundo ponto: '))
# 	y2 = float(input('Digite a ordenada do segundo ponto: '))
# 	distancia = calcula_distancia(x1,y1,x2,y2)
# 	print(f'\nA distância entre os pontos ({x1},{y1}) e ({x2},{y2}) é de {distancia:.2f}.')


sg.theme('BluePurple')
layout = [
    [sg.Text('Primeiro ponto'), sg.Push(), sg.Text('Segundo ponto')],
    [sg.Input(size=(5,1), key='a_p1'), sg.Input(size=(5,1),key='c_p1'), sg.Push(), sg.Input(size=(5,1),key='a_p2'), sg.Input(size=(5,1),key='c_p2')],
    [sg.Button('Calcula'), sg.Text('Distância = '), sg.Text(size=(5,1),key='distancia'), sg.Button('Sair')]
        ]

window = sg.Window('Distância', layout)

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'Calcula':
        x1, y1, x2, y2 = float(values['a_p1']), float(values['c_p1']), float(values['a_p2']), float(values['c_p2'])
        distancia = round(calcula_distancia(x1,y1,x2,y2), 2)
        window['distancia'].update(distancia)

window.close()