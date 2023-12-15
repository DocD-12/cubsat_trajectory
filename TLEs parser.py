from LxmlSoup import LxmlSoup
import requests

html = requests.get('https://celestrak.org/NORAD/elements/gp.php?INTDES=2023-091').text  # получаем html код сайта

polytech = html.find('POLYTECH-UNIVERSE 3')
polytechend = html.rfind('SITRO-AIS 6')
polytle = html[polytech:polytechend]
cstp = html.find('CSTP 1.1')
cstpend = html.find('UTMN 2')
cstptle = html[cstp:cstpend]

tlep = polytle.split()
tlecs = cstptle.split()



p1 = tlep.index('1')
s1 = tlecs.index('1')
p2 = tlep.index('2')
s2 = tlecs.index('2')

firstcs = tlecs[s1:s2]
secondcs =  tlecs[s2:]

firstp = tlep[p1:p2]
secondp = tlep[p2:]
print(firstcs)
def donelecs():
    print(f'Номер строки: {firstcs[0]}')
    print(f'Номер спутника в базе данных NORAD: {firstcs[1][:-1]}')
    print(f'Классификация: {firstcs[1][-1]}')
    print(f'Последние две цифры года запуска: {firstcs[2][:2]}')
    print(f'Номер запуска в этом году: {firstcs[2][2:5]}')
    print(f'Часть запуска: {firstcs[2][5:]}')
    print(f'Год эпохи: {firstcs[3][:3]}')
    print(f'Время эпохи: {firstcs[3][3:]}')
    print(f'Первая производная от среднего движения, делённая на 2: {firstcs[4]}')
    print(f'Вторая производная от среднего движения, делённая на шесть: {firstcs[5]}')
    print(f'Коэффициент торможения: {firstcs[6]}')
    print(f'Изначально — типы эфемерид, сейчас — всегда число 0: {firstcs[7]}')
    print(f'Номер элемента: {firstcs[8][:-1]}')
    print(f'Контрольная сумма по модулю 10: {firstcs[8][-1]}')
donelecs()