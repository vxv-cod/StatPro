# from multiprocessing.sharedctypes import Value
# from operator import index
# import os
# import re
import win32com.client
# import threading
from pythoncom import CoInitializeEx as pythoncomCoInitializeEx
# import time
# from PyQt5 import QtCore, QtWidgets
# import sys
# os.system('CLS')

def importdataCode(sheet, StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl):
    '''Собираем список из 1ой колонки'''
    vals = sheet.Range(sheet.Cells(StartNomerRow, StartNomerColl), sheet.Cells(EndNomerRow, EndNomerColl)).Value
    vals = [vals[i][x] for i in range(len(vals)) for x in range(len(vals[i]))]
    return vals

def codeTalie(sheet, StartNomerRow):
    StartNomerColl = 1
    EndNomerColl = 49
    # Raznovidnost = ""
    RewXXX = ["####"] + importdataCode(sheet, StartNomerRow, StartNomerColl, StartNomerRow, EndNomerColl)
    RewXXX = [None if i == '' else i for i in RewXXX]
    # print(f"RewXXX = {RewXXX}")

    Ip = RewXXX[6]
    Ip = None if Ip == '' else Ip
    IL = RewXXX[7]
    IL = None if IL == '' else IL
    Sr = RewXXX[13]
    Sr = None if Sr == '' else Sr
    Ir = RewXXX[14]
    Ir = None if Ir == '' else Ir
    # Ir = None if isinstance(Ir, str) else Ir
    
    Ddp = RewXXX[15]
    Ddp = None if Ddp == '' else Ddp
    W = RewXXX[3]
    W = None if W == '' else W
    W = W * 100 if W != None else W
    eee = RewXXX[12]
    eee = None if eee == '' else eee 

    # print(f"Ip = {Ip}")
    # print(f"IL = {IL}")
    # print(f"Sr = {Sr}")
    # print(f"Ir = {Ir}")
    # print(f"Ddp = {Ddp}")
    # print(f"W = {W}")
    # print(f"eee = {eee}")

    CodeIGE = ""
    if Ip != None:
        '''Гранулометрический состав 0,05 - 2,00'''
        Dr005_2 = sum([i if i != None else 0 for i in RewXXX[40:44 + 1]])
        Dr2 = sum([i if i != None else 0 for i in RewXXX[37:39 + 1]])
        '''Б.2.9 Разновидности глинистых грунтов по числу пластичности 
        и содержанию песчаных частиц выделяют в соответствии с таблицей Б.14'''
        
        '''Супесь'''
        if Ip < 0.01:
            CodeIGE = "0000"
        if 0.01 <= Ip <= 0.07:
            '''1 - Цифра: вид грунта'''
            CodeIGE = CodeIGE + "3"
            '''2 - цифра: разновидность грунта '''
            if Dr005_2 >= 50:
                Raznovidnost = "Супесь песчанистая"
                CodeIGE = CodeIGE + "1"
            if Dr005_2 < 50:
                Raznovidnost = "Супесь пылеватая"
                CodeIGE = CodeIGE + "2"
            if 15 <= Dr2 <= 50: 
                Raznovidnost = "Супесь с гравием"
                CodeIGE = CodeIGE + "0"
            if Dr005_2 == 0:
                Raznovidnost = "Супесь"
                CodeIGE = "30"

            '''3 - цифра: консистенция'''
            if IL != None:
                if IL < 0:
                    Raznovidnost = Raznovidnost + " твердая"
                    CodeIGE = CodeIGE + "1"
                if 0 <= IL <= 1.00:
                    Raznovidnost = Raznovidnost + " пластичная"
                    CodeIGE = CodeIGE + "7"
                if IL > 1.00:
                    Raznovidnost = Raznovidnost + " текучая"
                    CodeIGE = CodeIGE + "6"
            if IL == None:
                CodeIGE = CodeIGE + "0"
        
        '''Суглинок'''
        if 0.07 < Ip <= 0.12:
            '''1 - Цифра: вид грунта'''
            CodeIGE = CodeIGE + "2"
            '''2 - цифра: разновидность грунта '''
            if Dr005_2 >= 40:
                Raznovidnost = "Суглинок легкий песчанистый"
                CodeIGE = CodeIGE + "1"
            if Dr005_2 < 40:
                Raznovidnost = "Суглинок легкий пылеватый"
                CodeIGE = CodeIGE + "2"
            if 15 <= Dr2 <= 50:
                Raznovidnost = "Суглинок с гравием"
                CodeIGE = CodeIGE + "0"
            if Dr005_2 == 0:
                Raznovidnost = "Суглинок"
                CodeIGE = "20"

        if 0.12 < Ip <= 0.17:
            '''1 - Цифра: вид грунта'''
            CodeIGE = CodeIGE + "2"
            '''2 - цифра: разновидность грунта '''
            if Dr005_2 >= 40:
                Raznovidnost = "Суглинок тяжелый песчанистый"
                CodeIGE = CodeIGE + "3"
            if Dr005_2 < 40:
                Raznovidnost = "Суглинок тяжелый пылеватый"
                CodeIGE = CodeIGE + "4"
            if 15 <= Dr2 <= 50:
                Raznovidnost = "Суглинок с гравием"
                CodeIGE = CodeIGE + "0"
            if Dr005_2 == 0:
                Raznovidnost = "Суглинок"
                CodeIGE = "20"

        '''3 - цифра: консистенция'''

        '''Б.2.11 Разновидности глинистых грунтов по показателю текучести IL
        выделяют в соответствии с таблицей Б.16'''
        if 0.07 < Ip <= 0.17: # Суглинок
            if IL != None:
                if IL < 0:
                    Raznovidnost = Raznovidnost + " твердый"
                    CodeIGE = CodeIGE + "1"
                if 0 <= IL <= 0.25:
                    Raznovidnost = Raznovidnost + " полутвердый"
                    CodeIGE = CodeIGE + "2"
                if 0.25 < IL <= 0.50:
                    Raznovidnost = Raznovidnost + " тугопластичный"
                    CodeIGE = CodeIGE + "3"
                if 0.50 < IL <= 0.75:
                    Raznovidnost = Raznovidnost + " мягкопластичный"
                    CodeIGE = CodeIGE + "4"
                if 0.75 < IL <= 1.00:
                    Raznovidnost = Raznovidnost + " текучепластичный"
                    CodeIGE = CodeIGE + "5"
                if IL > 1.00:
                    Raznovidnost = Raznovidnost + " текучий"
                    CodeIGE = CodeIGE + "6"
            if IL == None:
                CodeIGE = CodeIGE + "0"

        '''Глина'''
        if 0.17 < Ip <= 0.27:
            '''1 - Цифра: вид грунта'''
            CodeIGE = CodeIGE + "1"
            '''2 - цифра: разновидность грунта '''
            if Dr005_2 >= 40:
                Raznovidnost = "Глина легкая песчанистая"
                CodeIGE = CodeIGE + "1"
            if Dr005_2 < 40:
                Raznovidnost = "Глина легкая пылеватая"
                CodeIGE = CodeIGE + "2"
            if 15 <= Dr2 <= 50:
                Raznovidnost = "Глина с гравием"
                CodeIGE = CodeIGE + "0"
            if Dr005_2 == 0:
                Raznovidnost = "Глина"
                CodeIGE = "10"

        if Ip > 0.27:
            '''1 - Цифра: вид грунта'''
            CodeIGE = CodeIGE + "1"
            '''2 - цифра: разновидность грунта '''
            Raznovidnost = "Глина тяжелая"
            if 15 <= Dr2 <= 50:
                Raznovidnost = "Глина тяжелая с гравием"
                CodeIGE = CodeIGE + "0"
        
        '''Глина'''
        if 0.17 < Ip <= 0.27:
            if IL != None:
                '''3 - цифра: консистенция'''
                if IL < 0:
                    Raznovidnost = Raznovidnost + " твердая"
                    CodeIGE = CodeIGE + "1"
                if 0 <= IL <= 0.25:
                    Raznovidnost = Raznovidnost + " полутвердая"
                    CodeIGE = CodeIGE + "2"
                if 0.25 < IL <= 0.50:
                    Raznovidnost = Raznovidnost + " тугопластичная"
                    CodeIGE = CodeIGE + "3"
                if 0.50 < IL <= 0.75:
                    Raznovidnost = Raznovidnost + " мягкопластичная"
                    CodeIGE = CodeIGE + "4"
                if 0.75 < IL <= 1.00:
                    Raznovidnost = Raznovidnost + " текучепластичная"
                    CodeIGE = CodeIGE + "5"
                if IL > 1.00:
                    Raznovidnost = Raznovidnost + " текучая"
                    CodeIGE = CodeIGE + "6"
            if IL == None:
                CodeIGE = CodeIGE + "0"

    '''Пески'''
    if Ip == None:
        '''1 - Цифра: вид грунта'''
        Raznovidnost = "Песок"
        CodeIGE = "4"
        
        '''2 - цифра: разновидность грунта '''

        Dr = sum([i if i != None else 0 for i in RewXXX[37:39 + 1]])
        '''Размер частиц d: > 2 мм'''
        if Dr > 25:
            Raznovidnost = Raznovidnost + " гравелистый"
            CodeIGE = CodeIGE + "5"
        Dr = sum([i if i != None else 0 for i in RewXXX[37:41 + 1]])
        '''Размер частиц d: > 0.5 мм'''
        if Dr > 50:
            if " гравелистый" not in Raznovidnost:
                Raznovidnost = Raznovidnost + " крупный"
                CodeIGE = CodeIGE + "3"
        Dr = sum([i if i != None else 0 for i in RewXXX[37:42 + 1]])
        '''Размер частиц d: > 0.25 мм'''
        if Dr > 50:
            if " крупный" not in Raznovidnost:
                Raznovidnost = Raznovidnost + " средней крупности"
                CodeIGE = CodeIGE + "2"
        Dr = sum([i if i != None else 0 for i in RewXXX[37:43 + 1]])
        '''Размер частиц d: > 0.10 мм'''
        if Dr >= 75:
            if " средней крупности" not in Raznovidnost:
                Raznovidnost = Raznovidnost + " мелкий"
                CodeIGE = CodeIGE + "1"
        Dr = sum([i if i != None else 0 for i in RewXXX[37:43 + 1]])
        '''Размер частиц d: > 0.10 мм'''
        if Dr < 75:
            if " мелкий" not in Raznovidnost:
                Raznovidnost = Raznovidnost + " пылеватый"
                CodeIGE = CodeIGE + "4"
        if Dr == 0:
            CodeIGE = CodeIGE + "0"

        '''3 - цифра: консистенция_Таблица Б.10'''
        if eee != None:
            if " гравелистый"  in Raznovidnost or " крупный"  in Raznovidnost or " средней крупности" in Raznovidnost:
                if eee <= 0.55:
                    Raznovidnost = Raznovidnost + " плотный"
                    CodeIGE = CodeIGE + "4"
                if 0.55 < eee <= 0.70:
                    Raznovidnost = Raznovidnost + " средней плотности"
                    CodeIGE = CodeIGE + "5"
                if eee > 0.70:
                    Raznovidnost = Raznovidnost + " рыхлый"
                    CodeIGE = CodeIGE + "6"
            if " мелкий" in Raznovidnost:
                if eee <= 0.60:
                    Raznovidnost = Raznovidnost + " плотный"
                    CodeIGE = CodeIGE + "4"
                if 0.60 < eee <= 0.75:
                    Raznovidnost = Raznovidnost + " средней плотности"
                    CodeIGE = CodeIGE + "5"
                if eee > 0.75:
                    Raznovidnost = Raznovidnost + " рыхлый"
                    CodeIGE = CodeIGE + "6"
            if " пылеватый" in Raznovidnost:
                if eee <= 0.60:
                    Raznovidnost = Raznovidnost + " плотный"
                    CodeIGE = CodeIGE + "4"
                if 0.60 < eee <= 0.80:
                    Raznovidnost = Raznovidnost + " средней плотности"
                    CodeIGE = CodeIGE + "5"
                if eee > 0.80:
                    Raznovidnost = Raznovidnost + " рыхлый"
                    CodeIGE = CodeIGE + "6"
        if eee == None:
            CodeIGE = CodeIGE + "0"

    '''Б.2.15 По относительному содержанию органического вещества (степени заторфованности) Таблица Б.20'''
    '''4 - цифра: примеси/заполнитель'''
    if Ir == None:
            CodeIGE = CodeIGE + "0"
    if Ir != None:
        '''Частный случай для глинистых'''
        if Ip != None:
            if 0.05 < Ir <= 0.10:
                Raznovidnost = Raznovidnost + " с примесью органического вещества"
                CodeIGE = CodeIGE + "1"
            if Ir <= 0.05:
                CodeIGE = CodeIGE + "0"
        '''Частный случай для песков'''
        if Ip == None:
            if Ir != None:
                if 0.03 <= Ir <= 0.10:
                    Raznovidnost = Raznovidnost + " с примесью органического вещества"
                    CodeIGE = CodeIGE + "1"
                if Ir <= 0.03:
                    CodeIGE = CodeIGE + "0"
        
        if 0.1 < Ir <= 0.25:
            Raznovidnost = Raznovidnost + " с низким содержанием орг.вещества (слабозаторфованные)"
            CodeIGE = CodeIGE + "2"
        if 0.25 < Ir <= 0.40:
            Raznovidnost = Raznovidnost + " со средним содержанием орг. вещества (среднезаторфованные)"
            CodeIGE = CodeIGE + "3"
        if 0.40 < Ir < 0.50:
            Raznovidnost = Raznovidnost + " с высоким содержанием орг.вещества (сильнозаторфованные)"
            CodeIGE = CodeIGE + "4"

        '''Торфы'''
        if Ir >= 0.50:
            '''1 - Цифра: вид грунта'''
            Raznovidnost = "Торф"
            CodeIGE = "9"
            '''Таблица Б.21_По степени разложения'''
            '''2 - цифра: разновидность грунта '''
            if Ddp != None:
                if Ddp <= 20:
                    Raznovidnost = Raznovidnost + " слаборазложившийся"
                    CodeIGE = CodeIGE + "1"
                if 20 < Ddp <= 45:
                    Raznovidnost = Raznovidnost + " среднеразложившийся"
                    CodeIGE = CodeIGE + "2"
                if Ddp > 45:
                    Raznovidnost = Raznovidnost + " сильноразложившийся"
                    CodeIGE = CodeIGE + "3"
            if Ddp == None:
                CodeIGE = CodeIGE + "0"

            if W != None:
                '''3 - цифра: консистенция'''
                if W <= 300:
                    Raznovidnost = Raznovidnost + " осушенный (уплотненный)"
                    CodeIGE = CodeIGE + "1"
                if 300 < W <= 600:
                    Raznovidnost = Raznovidnost + " маловлажный"
                    CodeIGE = CodeIGE + "2"
                if 600 < W <= 900:
                    Raznovidnost = Raznovidnost + " средней влажности"
                    CodeIGE = CodeIGE + "3"
                if 900 < W <= 1200:
                    Raznovidnost = Raznovidnost + " очень влажный"
                    CodeIGE = CodeIGE + "4"
                if W > 1200:
                    Raznovidnost = Raznovidnost + " избыточно влажный"
                    CodeIGE = CodeIGE + "5"
                '''4 - цифра: примеси/заполнитель'''
                W = W * 0.01
                if W <= 6:
                    CodeIGE = CodeIGE + "1"
                if 6 < W <= 8:
                    CodeIGE = CodeIGE + "2"
                if 8 < W <= 12:
                    CodeIGE = CodeIGE + "3"
                if W > 12:
                    CodeIGE = CodeIGE + "4"
            if W == None:
                CodeIGE = CodeIGE + "0"
                CodeIGE = CodeIGE + "0"

    '''5 - цифра: водонасыщение песков'''
    '''Пески'''
    def vodonas(Raznovidnost, CodeIGE):
        if Sr == None:
            CodeIGE = CodeIGE + "0"
        if Sr != None:
            if 0 < Sr <= 0.5:
                Raznovidnost = Raznovidnost + " малой степени водонасыщения"
                CodeIGE = CodeIGE + "5"
            if 0.5 < Sr <= 0.8:
                Raznovidnost = Raznovidnost + " средней степени водонасыщения"
                CodeIGE = CodeIGE + "6"
            if 0.8 < Sr <= 1.0:
                Raznovidnost = Raznovidnost + " водонасыщенный"
                CodeIGE = CodeIGE + "7"
        return Raznovidnost, CodeIGE

    if Ip == None:
        if Ir != None:
            if Ir < 0.50:
                xxx = vodonas(Raznovidnost, CodeIGE)
                Raznovidnost = xxx[0]
                CodeIGE = xxx[1]
        if Ir == None:
            xxx = vodonas(Raznovidnost, CodeIGE)
            Raznovidnost = xxx[0]
            CodeIGE = xxx[1]

    return Raznovidnost, CodeIGE

    
def codeMerz(sheet, StartNomerRow):
    StartNomerColl = 1
    EndNomerColl = 49
    RewXXX = ["####"] + importdataCode(sheet, StartNomerRow, StartNomerColl, StartNomerRow, EndNomerColl)
    RewXXX = [None if i == '' else i for i in RewXXX]

    ValueNone = 0
    Ip = RewXXX[10]
    IL = RewXXX[11]
    TTT = RewXXX[27]
    Srf = RewXXX[17]
    Ir = RewXXX[21]
    Ir = 0 if Ir == None else Ir
    # Ir = 0 if isinstance(Ir, str) else Ir
    Ddp = RewXXX[22]
    Itot = RewXXX[18]
    Itot = 0 if Itot == None else Itot
    II = RewXXX[19]
    
    # print(f"Ip = {Ip}")
    # print(f"IL = {IL}")
    # print(f"TTT = {TTT}")
    # print(f"Srf = {Srf}")
    # print(f"Ir = {Ir}")
    # print(f"Ddp = {Ddp}")
    # print(f"Itot = {Itot}")
    # print(f"II = {II}")

    CodeIGE = ""
    if Ip != None:
        '''Гранулометрический состав 0,05 - 2,00'''
        Dr005_2 = sum([i if i != None else 0 for i in RewXXX[42:46 + 1]])
        Dr2 = sum([i if i != None else 0 for i in RewXXX[39:41 + 1]])
        '''Б.2.9 Разновидности глинистых грунтов по числу пластичности 
        и содержанию песчаных частиц выделяют в соответствии с таблицей Б.14'''

        '''Супесь'''
        if 0.01 <= Ip <= 0.07:
            '''1 - Цифра: вид грунта'''
            CodeIGE = CodeIGE + "3"
            '''2 - цифра: разновидность грунта '''
            if Dr005_2 >= 50:
                Raznovidnost = "Супесь песчанистая"
                CodeIGE = CodeIGE + "1"
            if Dr005_2 < 50:
                Raznovidnost = "Супесь пылеватая"
                CodeIGE = CodeIGE + "2"
            if 15 <= Dr2 <= 50: 
                Raznovidnost = "Супесь с гравием"
                CodeIGE = CodeIGE + "3"
            if Dr005_2 == 0:
                Raznovidnost = "Супесь"
                CodeIGE = "30"

        '''Суглинок'''
        if 0.07 < Ip <= 0.12:
            '''1 - Цифра: вид грунта'''
            CodeIGE = CodeIGE + "2"
            '''2 - цифра: разновидность грунта '''
            if Dr005_2 >= 40:
                Raznovidnost = "Суглинок легкий песчанистый"
                CodeIGE = CodeIGE + "1"
            if Dr005_2 < 40:
                Raznovidnost = "Суглинок легкий пылеватый"
                CodeIGE = CodeIGE + "2"
            if 15 <= Dr2 <= 50:
                Raznovidnost = "Суглинок с гравием"
                CodeIGE = CodeIGE + "0"
            if Dr005_2 == 0:
                Raznovidnost = "Суглинок"
                CodeIGE = "20"

        if 0.12 < Ip <= 0.17:
            '''1 - Цифра: вид грунта'''
            CodeIGE = CodeIGE + "2"
            '''2 - цифра: разновидность грунта '''
            if Dr005_2 >= 40:
                Raznovidnost = "Суглинок тяжелый песчанистый"
                CodeIGE = CodeIGE + "3"
            if Dr005_2 < 40:
                Raznovidnost = "Суглинок тяжелый пылеватый"
                CodeIGE = CodeIGE + "4"
            if 15 <= Dr2 <= 50:
                Raznovidnost = "Суглинок с гравием"
                CodeIGE = CodeIGE + "0"
            if Dr005_2 == 0:
                Raznovidnost = "Суглинок"
                CodeIGE = "20"
    
        '''Глина'''
        if 0.17 < Ip <= 0.27:
            '''1 - Цифра: вид грунта'''
            CodeIGE = CodeIGE + "1"
            '''2 - цифра: разновидность грунта '''
            if Dr005_2 >= 40:
                Raznovidnost = "Глина легкая песчанистая"
                CodeIGE = CodeIGE + "1"
            if Dr005_2 < 40:
                Raznovidnost = "Глина легкая пылеватая"
                CodeIGE = CodeIGE + "2"
            if 15 <= Dr2 <= 50:
                Raznovidnost = "Глина с гравием"
                CodeIGE = CodeIGE + "0"
            if Dr005_2 == 0:
                Raznovidnost = "Глина"
                CodeIGE = "10"

        if Ip > 0.27:
            '''1 - Цифра: вид грунта'''
            CodeIGE = CodeIGE + "1"
            '''2 - цифра: разновидность грунта '''
            Raznovidnost = "Глина тяжелая"
            if 15 <= Dr2 <= 50:
                Raznovidnost = "Глина тяжелая с гравием"
                CodeIGE = CodeIGE + "0"

        '''3 - цифра: тип ММГ_Таблица B.12'''

        def opo(Raznovidnost, CodeIGE, Th, Tbf, tver, plast, sipu):
            text = ""
            cifr = "0"
            if TTT != None:
                if TTT <= Th:
                    text = tver
                    cifr = "8"
                if Th < TTT <= Tbf:
                    text = plast
                    cifr = "9"
                if TTT > Tbf:
                    cifr = "0"
                if Srf != None:
                    if Tbf < TTT < 0 and Srf <= 0.15:
                        text = sipu
                        cifr = "7"
                    if Tbf < TTT < 0 and Srf > 0.15:
                        text = ""
                        cifr = "0"
                if TTT > 0:
                    text = ""
                    cifr = "0"
            Raznovidnost = Raznovidnost + text
            CodeIGE = CodeIGE + cifr
            return Raznovidnost, CodeIGE
        
        '''Супесь'''
        if 0.01 <= Ip <= 0.07:
            Th = -0.6
            Tbf = -0.15
            xxx = opo(Raznovidnost, CodeIGE, Th, Tbf, " твердомерзлая", " пластичномерзлая", " сыпучемерзлая")
            Raznovidnost = xxx[0]
            CodeIGE = xxx[1]

        '''Суглинок'''
        if 0.07 < Ip <= 0.17:
            Th = -1.0
            Tbf = -0.20
            xxx = opo(Raznovidnost, CodeIGE, Th, Tbf, " твердомерзлый", " пластичномерзлый", " сыпучемерзлый")
            Raznovidnost = xxx[0]
            CodeIGE = xxx[1]            

        '''Глина'''
        if 0.17 < Ip <= 0.27:
            Th = -1.5
            Tbf = -0.25
            xxx = opo(Raznovidnost, CodeIGE, Th, Tbf, " твердомерзлая", " пластичномерзлая", " сыпучемерзлая")
            Raznovidnost = xxx[0]
            CodeIGE = xxx[1]          

    '''Пески'''
    if Ip == None and not isinstance(Ir, str) and Ir < 0.5:
        '''1 - Цифра: вид грунта'''
        Raznovidnost = "Песок"
        CodeIGE = "4"
        
        '''2 - цифра: разновидность грунта '''

        Dr = sum([i if i != None else 0 for i in RewXXX[39:41 + 1]])
        '''Размер частиц d: > 2 мм'''
        if Dr > 25:
            Raznovidnost = Raznovidnost + " гравелистый"
            CodeIGE = CodeIGE + "5"
        Dr = sum([i if i != None else 0 for i in RewXXX[39:43 + 1]])
        '''Размер частиц d: > 0.5 мм'''
        if Dr > 50:
            if " гравелистый" not in Raznovidnost:
                Raznovidnost = Raznovidnost + " крупный"
                CodeIGE = CodeIGE + "3"
        Dr = sum([i if i != None else 0 for i in RewXXX[39:44 + 1]])
        '''Размер частиц d: > 0.25 мм'''
        if Dr > 50:
            if " крупный" not in Raznovidnost:
                Raznovidnost = Raznovidnost + " средней крупности"
                CodeIGE = CodeIGE + "2"
        Dr = sum([i if i != None else 0 for i in RewXXX[39:45 + 1]])
        '''Размер частиц d: > 0.10 мм'''
        if Dr >= 75:
            if " средней крупности" not in Raznovidnost:
                Raznovidnost = Raznovidnost + " мелкий"
                CodeIGE = CodeIGE + "1"
        Dr = sum([i if i != None else 0 for i in RewXXX[39:45 + 1]])
        '''Размер частиц d: > 0.10 мм'''
        if Dr < 75 and Dr != 0:
            if " мелкий" not in Raznovidnost:
                Raznovidnost = Raznovidnost + " пылеватый"
                CodeIGE = CodeIGE + "4"
        if Dr == 0:
            CodeIGE = CodeIGE + "0"

        '''3 - цифра: тип ММГ_Таблица B.12'''
        '''Пески'''

        if " мелкий" in Raznovidnost or " пылеватый" in Raznovidnost:
            Th = -0.3
            Tbf = -0.10
            if " пылеватый" in Raznovidnost:
                Tbf = -0.15
        if " крупный" in Raznovidnost or " средней крупности" in Raznovidnost or " гравелистый" in Raznovidnost:
            Th = -0.10
            Tbf = -0.10
        else: Th, Tbf = 100, 100

        def opoPesok(Raznovidnost, CodeIGE, Th, Tbf, tver, plast, sipu):
            text = ""
            cifr = "0"
            if TTT != None:
                if TTT <= Th:
                    text = tver
                    cifr = "8"
                if Srf != None:
                    if Th < TTT <= Tbf and Srf < 0.8:
                        text = plast
                        cifr = "9"
                    if Tbf < TTT < 0 and Srf <= 0.15:
                        text = sipu
                        cifr = "7"
                    if Tbf < TTT < 0 and Srf > 0.15:
                        text = ""
                        cifr = "0"
                if TTT > 0:
                    text = ""
                    cifr = "0"
            Raznovidnost = Raznovidnost + text
            CodeIGE = CodeIGE + cifr
            return Raznovidnost, CodeIGE
        
        xxx = opoPesok(Raznovidnost, CodeIGE, Th, Tbf, " твердомерзлый", " пластичномерзлый", " сыпучемерзлый")
        Raznovidnost = xxx[0]
        CodeIGE = xxx[1]         

    '''4 - цифра: примеси/заполнитель'''
    '''Б.2.15 По относительному содержанию органического вещества (степени заторфованности) Таблица Б.20'''
    
    '''Частный случай для глинистых'''
    if Ip != None:
        if Ir == 0:
            CodeIGE = CodeIGE + "0"
            ValueNone = 1
        if 0 < Ir <= 0.05:
            CodeIGE = CodeIGE + "0"
        if 0.05 < Ir <= 0.10:
            Raznovidnost = Raznovidnost + " с примесью органического вещества"
            CodeIGE = CodeIGE + "1"
    
    '''Частный случай для песков'''
    if Ip == None:
        if Ir == 0:
            CodeIGE = CodeIGE + "0"
            ValueNone = 1
        if Ir == '':
            CodeIGE = CodeIGE + "0"
        if Ir != '':
            if 0 < Ir <= 0.03:
                CodeIGE = CodeIGE + "0"
            if 0.03 <= Ir <= 0.10:
                Raznovidnost = Raznovidnost + " с примесью органического вещества"
                CodeIGE = CodeIGE + "1"
    
    if 0.1 < Ir <= 0.25:
        Raznovidnost = Raznovidnost + " с низким содержанием орг.вещества (слабозаторфованные)"
        CodeIGE = CodeIGE + "2"
    if 0.25 < Ir <= 0.40:
        Raznovidnost = Raznovidnost + " со средним содержанием орг. вещества (среднезаторфованные)"
        CodeIGE = CodeIGE + "3"
    if 0.40 < Ir < 0.50:
        Raznovidnost = Raznovidnost + " с высоким содержанием орг.вещества (сильнозаторфованные)"
        CodeIGE = CodeIGE + "4"

    '''5 - цифра: криотекстура'''
    if Ir < 0.5:
        CodeIGE = CodeIGE + "0"
    
    '''6 - цифра: льдистость'''

    '''Глинистые льдистость'''
    if Ip != None and Ir < 0.5:
        if II == None:
            CodeIGE = CodeIGE + "0"
            ValueNone = 1
        if II != None:
            '''6 - цифра: льдистость Таблица Б.26'''
            if II <= 0.03:
                if Ip > 0.17:
                    Raznovidnost = Raznovidnost + " нельдистая"
                else:
                    Raznovidnost = Raznovidnost + " нельдистый"
                CodeIGE = CodeIGE + "0"  
            if 0.03 < II <= 0.20:
                if Ip > 0.17:
                    Raznovidnost = Raznovidnost + " слабольдистая"
                else:
                    Raznovidnost = Raznovidnost + " слабольдистый"
                CodeIGE = CodeIGE + "1"  
            if 0.20 < II <= 0.40:
                if Ip > 0.17:
                    Raznovidnost = Raznovidnost + " льдистая"
                else:
                    Raznovidnost = Raznovidnost + " льдистый"
                CodeIGE = CodeIGE + "2"  
            if 0.40 < II <= 0.80:
                if Ip > 0.17:
                    Raznovidnost = Raznovidnost + " сильнольдистая"
                else:
                    Raznovidnost = Raznovidnost + " сильнольдистый"
                CodeIGE = CodeIGE + "3"  
            if II > 0.80:
                Raznovidnost = Raznovidnost + " ледогрунт"
                CodeIGE = CodeIGE + "4"  
    
    '''Пески льдистость'''
    if Ip == None and Ir < 0.5:
        if Itot == None:
            CodeIGE = CodeIGE + "0"
            ValueNone = 1
        if Itot != None:
            '''6 - цифра: льдистость Таблица Б.27'''
            if Itot <= 0.20:
                Raznovidnost = Raznovidnost + " нельдистый"
                CodeIGE = CodeIGE + "0"
            if 0.20 < Itot <= 0.40:
                Raznovidnost = Raznovidnost + " слабольдистый"
                CodeIGE = CodeIGE + "1"  
            if 0.40 < Itot <= 0.60:
                Raznovidnost = Raznovidnost + " льдистый"
                CodeIGE = CodeIGE + "2"  
            if 0.60 < Itot <= 0.80:
                Raznovidnost = Raznovidnost + " сильнольдистый"
                CodeIGE = CodeIGE + "3"  
            if Itot > 0.80:
                Raznovidnost = Raznovidnost + " ледогрунт"
                CodeIGE = CodeIGE + "4"

    '''Торф'''
    if Ir >= 0.50:
        '''1 - Цифра: вид грунта'''
        Raznovidnost = "Торф"
        CodeIGE = "9"
        '''Таблица Б.21_По степени разложения'''
        '''2 - цифра: разновидность грунта '''
        if Ddp != None:
            if Ddp <= 20:
                Raznovidnost = Raznovidnost + " слаборазложившийся"
                CodeIGE = CodeIGE + "1"
            if 20 < Ddp <= 45:
                Raznovidnost = Raznovidnost + " среднеразложившийся"
                CodeIGE = CodeIGE + "2"
            if Ddp > 45:
                Raznovidnost = Raznovidnost + " сильноразложившийся"
                CodeIGE = CodeIGE + "3"

        if TTT == None:
            '''3 - цифра: консистенция (мерзлость)'''
            CodeIGE = CodeIGE + "0"
            ValueNone = 1
            '''4 - цифра:'''
            CodeIGE = CodeIGE + "0"
            '''5 - цифра:'''
            Raznovidnost = Raznovidnost + " атакситовой криотекстуры"
            CodeIGE = CodeIGE + "4"

        if TTT != None:
            if TTT <= -0.13:
                '''3 - цифра: консистенция (мерзлость)'''
                Raznovidnost = Raznovidnost + " мерзлый"
                CodeIGE = CodeIGE + "9"
            else:
                CodeIGE = CodeIGE + "0"

            '''4 - цифра:'''
            CodeIGE = CodeIGE + "0"
            '''5 - цифра:'''
            Raznovidnost = Raznovidnost + " атакситовой криотекстуры"
            CodeIGE = CodeIGE + "4"

        '''6 - цифра: льдистость Таблица Б.26'''
        if II == None:
            CodeIGE = CodeIGE + "0"
            ValueNone = 1
        if II != None:
            if II <= 0.03:
                Raznovidnost = Raznovidnost + " нельдистый"
                CodeIGE = CodeIGE + "0"  
            if 0.03 < II <= 0.20:
                Raznovidnost = Raznovidnost + " слабольдистый"
                CodeIGE = CodeIGE + "1"  
            if 0.20 < II <= 0.40:
                Raznovidnost = Raznovidnost + " льдистый"
                CodeIGE = CodeIGE + "2"  
            if 0.40 < II <= 0.80:
                Raznovidnost = Raznovidnost + " сильнольдистый"
                CodeIGE = CodeIGE + "3"  
            if II > 0.80:
                Raznovidnost = Raznovidnost + " ледогрунт"
                CodeIGE = CodeIGE + "4"
    # print(f"ValueNone = {ValueNone}")
    return Raznovidnost, CodeIGE, ValueNone

def Book():
    pythoncomCoInitializeEx(0)
    Excel = win32com.client.Dispatch("Excel.Application")
    wb = Excel.ActiveWorkbook   # Получаем доступ к активной книге
    return wb

def SrartTalie():
    wb = Book()
    sheet = wb.Worksheets("Код_Талые")
    sheet.Activate()
    
    # vals = importdataCode(sheet, 1, 1, 10, 1)
    # Row_NVirabotki = vals.index('№ выработки') + 1
    # StartNomerRow = Row_NVirabotki + 5
    StartNomerRow = 7
    '''от нижнего края вверх до нижней крайней заполненной ячейки'''
    EndNomerRow = sheet.Cells(sheet.Rows.Count, 1).End(3).Row
    data = [codeTalie(sheet, i) for i in range(StartNomerRow, EndNomerRow + 1)]
    sheet.Range(sheet.Cells(StartNomerRow, 48), sheet.Cells(EndNomerRow, 49)).Value = data


def SrartMerz():
    wb = Book()
    sheet = wb.Worksheets("Код_Мерзлые")
    sheet.Activate()
            
    StartNomerRow = 7
    '''от нижнего края вверх до нижней крайней заполненной ячейки'''
    EndNomerRow = sheet.Cells(sheet.Rows.Count, 1).End(3).Row
    
    # aaa = 55
    # StartNomerRow = aaa
    # EndNomerRow = aaa
    
    data = [codeMerz(sheet, i) for i in range(StartNomerRow, EndNomerRow + 1)]
    sheet.Range(sheet.Cells(StartNomerRow, 50), sheet.Cells(EndNomerRow, 51)).Value = data


if __name__ == "__main__":
    SrartTalie()
    # SrartMerz()
    print("THE END !!!")