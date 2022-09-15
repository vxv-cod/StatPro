import os
from time import sleep
import win32com.client
import threading
from pythoncom import CoInitializeEx as pythoncomCoInitializeEx
from PyQt5 import QtCore, QtWidgets
import sys
import traceback
from rich import print

import numpy as np
import os
import pyodbc
import time

from okno_ui import Ui_Form
from  vxv_tnnc_SQL_Pyton import Sql
import CodeGrount
import SvodTabTalue
import SvodTabMerzlue
from version import ver
os.system('CLS')

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()


_translate = QtCore.QCoreApplication.translate
Title = 'StatProc v. 1.0.1.' + str(ver)
Form.setWindowTitle(_translate("Form", Title))

'''Обертка функции в потопк (декоратор)'''
def thread(my_func):
    def wrapper():
        threading.Thread(target=my_func, daemon=True).start()
    return wrapper

def colorBar(progBar, color):
    # progBar.setStyleSheet("QProgressBar::chunk {background-color: rgb(170, 170, 170); margin: 2px;}")
    progBar.setStyleSheet("QProgressBar::chunk {background-color: rgb("f"{color[0]}, {color[1]}, {color[2]}); margin: 2px;""}")

def max_row_sheet(sheet, row, col):
    # max_row = sheet.Range(f"C{sheet.Rows.Count}").End(3).Row
    '''от нижнего края вверх до нижней крайней заполненной ячейки'''
    max_row = sheet.Cells(sheet.Rows.Count, col).End(3).Row
    '''от правого края влево до правой крайней заполненной ячейки'''
    max_col = sheet.Cells(row, sheet.Columns.Count).End(1).Column
    '''от 1ой колонки вправо до первой заполненной ячейки'''
    min_col = sheet.Cells(row, 1).End(2).Column
    if min_col == 3:
        min_col = sheet.Cells(row, 1).End(1).Column
    '''Количество занимаемых таблицей строк'''
    countTab_row = sheet.UsedRange.Rows.Count
    # '''Количество занимаемых таблицей колонок'''
    # countTab_col = sheet.UsedRange.Columns.Count

    # print(f"\"{sheet.Name}\": max_row = {max_row}")
    # print(f"\"{sheet.Name}\": max_col = {max_col}")
    # print(f"\"{sheet.Name}\": min_col = {min_col}")
    # print(f"\"{sheet.Name}\": countTab_row = {countTab_row}")
    # print(f"\"{sheet.Name}\": countTab_col = {countTab_col}")

    return max_row, max_col, min_col, countTab_row

# def importdataCode(sheet, StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl):
#     '''Собираем список из 1ой колонки'''
#     vals = sheet.Range(sheet.Cells(StartNomerRow, StartNomerColl), sheet.Cells(EndNomerRow, EndNomerColl)).Value
#     vals = [vals[i][x] for i in range(len(vals)) for x in range(len(vals[i]))]
#     return vals

"""Получаем индексы ячеек построчно с искомыми строками"""
def importdata(StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl, sheet, columnsList85, index95=1):
    proc = 0
    def funr85(columnsList85, RowList85, index95, row):
        # RowList85 = []
        for i in columnsList85:
            for j in range(0, index95 + 1):
                val = sheet.Cells(row + j, StartNomerColl + i).Value
                val = "-" if val == None else val
                RowList85.append(val)
        return RowList85
    typeGountVozmojnie = ['Песок', 'Супесь', 'Суглинок', 'Глина', 'Торф']
    TabListRow = []
    raschet85 = []
    '''Собираем список из 1ой колонки'''
    OneColumnList = sheet.Range(sheet.Cells(1, StartNomerColl), sheet.Cells(EndNomerRow, StartNomerColl)).Value
    OneColumnList = [str(OneColumnList[i][0]) for i in range(len(OneColumnList))]
    '''Ищем нужные индексы по искомым значениям и собираем список построчно из таблицы'''
    for row in range(StartNomerRow, len(OneColumnList)):
        RowList = []
        RowList85 = []
        Xn = OneColumnList[row - 1]
        for i in typeGountVozmojnie:
            if i in str(Xn):
                aaa = Xn[0 : Xn.find(i)]
                aaa = aaa.replace('ИГЭ', '')
                aaa = aaa.replace('-', '')
                aaa = aaa.replace(' ', '')
                bbb = Xn[Xn.find(i) : len(Xn)]
        text = 'Нормативное значение (Xn)'
        if Xn == text:
            for col in range(StartNomerColl, EndNomerColl + 1):
                val = sheet.Cells(row, col).Value
                val = "-" if val == None else val
                if val == text:
                    RowList.append(aaa)
                    RowList.append(bbb)
                else:
                    RowList.append(val)
            TabListRow.append(RowList)
        if Xn == 'Расчетное значение (0,85)':
            raschet85.append(funr85(columnsList85, RowList85, index95, row))
        
        proc = round(row / EndNomerRow * 100)
        if index95 == 1:
            sig.signal_1.emit(proc)
            # if ui.progressBar_1.Value() != proc:
            #     sig.signal_1.emit(proc)
        if index95 == 2:
            sig.signal_2.emit(proc)
            # if ui.progressBar_2.Value() != proc:
            #     sig.signal_2.emit(proc)

    return TabListRow, raschet85

'''Функция прорисовки граней ячеек'''
def grani(sheet, gr, StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl):
    sheet.Range(sheet.Cells(StartNomerRow, StartNomerColl), sheet.Cells(EndNomerRow, EndNomerColl)).Borders.Weight = 2
    cel = sheet.Range(sheet.Cells(StartNomerRow, StartNomerColl), sheet.Cells(EndNomerRow, EndNomerColl))
    cel.Borders(7).Weight = 3
    cel.Borders(8).Weight = 3
    cel.Borders(9).Weight = 3
    cel.Borders(10).Weight = 3
    for i in gr:
        cellLeftRightGran = sheet.Range(sheet.Cells(StartNomerRow, StartNomerColl + i[0]), sheet.Cells(EndNomerRow, StartNomerColl + i[1]))
        cellLeftRightGran.Borders(7).Weight = 3
        cellLeftRightGran.Borders(10).Weight = 3

'''Отправляем данные в таблицу'''
def exportdata(sheet, data, StartNomerColl, EndNomerColl, StartNomerRow, EndNomerRow, gr):
    '''Вносим данные построчно в таблицу'''
    sheet.Range(sheet.Cells(StartNomerRow, StartNomerColl), sheet.Cells(EndNomerRow, EndNomerColl)).Value = data
    '''Для второй колонки устанавливаем Перенос текста и выравнивание по левому краю'''
    XCells = sheet.Range(sheet.Cells(StartNomerRow, StartNomerColl + 1), sheet.Cells(EndNomerRow, StartNomerColl + 1))
    XCells.WrapText = True
    XCells.HorizontalAlignment = 1
    grani(sheet, gr, StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl)

        
def normTalie(ishodSheet, workSheet):
    '''Активируем лист'''
    workSheet.Activate()
    '''======================================================================================================'''
    """Получаем значение ячеек построчно"""
    StartNomerRow = 7
    StartNomerColl = 1
    EndNomerColl = 47
    endcount = max_row_sheet(ishodSheet, StartNomerRow - 1, StartNomerColl)
    EndNomerRow = endcount[0]

    dataX = importdata(StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl, sheet=ishodSheet, columnsList85=[7, 34, 35], index95=1)
    data = dataX[0]
    raschet85 = dataX[1]

    for i in range(len(data)):
        del data[i][2]

    data1 = []
    data2 = []
    for i in range(len(data)):
        data1.append(data[i][ 0: 17 + 1])
        data2.append(data[i][36: 46 + 1])

    dataExp = [data1[i] + data2[i] + [data[i][31]] + [data[i][34]] + [data[i][35]] + raschet85[i] for i in range(len(data))]
    # dataExp = [data1[i] + data2[i] + [data[i][26]] + [data[i][31]] + [data[i][32]] + raschet85[i] for i in range(len(data))]

    for i in range(len(dataExp)):
        del dataExp[i][16]

    if dataExp == []:
        dataExp = [["-"]*37]
    
    if data == []:
        data = [["-"]*47]

    '''Определяем первые и последние индексы строк и колонок с данными'''
    StartNomerRow = 6
    CountRow = len(dataExp)     # 8
    EndNomerRow = StartNomerRow + CountRow - 1
    endcount = max_row_sheet(workSheet, StartNomerRow - 1, StartNomerColl)
    EndNomerColl = endcount[1]
    StartNomerColl = endcount[2]
    EndNomerRowALL = endcount[3] + StartNomerRow
    '''Удаляем строки со сдвигом вверх'''
    workSheet.Rows(f"{StartNomerRow}:{EndNomerRowALL}").Delete(1)
    '''Отправляем данные в таблицуи Рисуем грани таблицы'''
    gr = [[1, 1],  [17, 27], [31, 32], [35, 36]]
    exportdata(workSheet, dataExp, StartNomerColl, EndNomerColl, StartNomerRow, EndNomerRow, gr)
    sig.signal_1.emit(100)

    return dataExp, data

def normMerzlie(ishodSheet, workSheet):
    '''Активируем лист'''
    workSheet.Activate()
    '''======================================================================================================'''
    """Получаем значение ячеек построчно"""
    StartNomerRow = 7
    StartNomerColl = 1
    EndNomerColl = 49
    endcount = max_row_sheet(ishodSheet, StartNomerRow - 1, StartNomerColl)
    EndNomerRow = endcount[0]
    dataX = importdata(StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl, sheet=ishodSheet, columnsList85=[12, 32, 33, 34, 36, 35 ,37], index95=2)
    data = dataX[0]
    raschet85 = dataX[1]

    for i in range(len(data)):
        del data[i][2]

    dataExp = [data[i] + raschet85[i] for i in range(len(data))]

    if data == []:
        data = [["-"]*49]
    if dataExp == []:
        dataExp = [["-"]*70]

    '''Определяем первые и последние индексы строк и колонок с данными'''
    StartNomerRow = 7
    CountRow = len(dataExp)     # 8
    EndNomerRow = StartNomerRow + CountRow - 1
    endcount = max_row_sheet(workSheet, StartNomerRow - 1, StartNomerColl)
    EndNomerColl = endcount[1]
    StartNomerColl = 1
    EndNomerRowALL = endcount[3] + StartNomerRow

    '''Удаляем строки со сдвигом вверх'''
    workSheet.Rows(f"{StartNomerRow}:{EndNomerRowALL}").Delete(1)
    
    '''Отправляем данные в таблицуи Рисуем грани таблицы'''
    gr = [[0, 0], [2, 6], [11, 13], [17, 19], [28, 29], [32, 34], [38, 48], [52, 54], [58, 60], [64, 66], [67, 69]]
     
    exportdata(workSheet, dataExp, StartNomerColl, EndNomerColl, StartNomerRow, EndNomerRow, gr)
    '''======================================================================================================'''
    '''======================================================================================================'''

    sig.signal_2.emit(100)
    return data

def granPerimetr(sheet, StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl):
    cel = sheet.Range(sheet.Cells(StartNomerRow, StartNomerColl), sheet.Cells(EndNomerRow, EndNomerColl))
    cel.Borders(7).Weight = 3
    cel.Borders(8).Weight = 3
    cel.Borders(9).Weight = 3
    cel.Borders(10).Weight = 3

def perevorotTab(xxx):
    res = []
    for i in range(len(xxx[0])):
        zzz = []
        for x in range(len(xxx)):
            zzz.append(xxx[x][i])
        res.append(zzz)
    return res

def FMTalie(workSheet, dataExp):
    IGE = []
    for i in dataExp:
        if "Торф" not in str(i[1]):
            xxx = i[:14] + i[28:31]
            IGE.append(xxx)
    
    for i in range(len(IGE)):
        del IGE[i][1]

    '''Активируем лист'''
    workSheet.Activate()
    
    StartNomerRow = 4
    StartNomerColl = 4
    EndNomerRow = 19

    IGE = perevorotTab(IGE)
    EndNomerColl = StartNomerColl - 1 +  len(IGE[0])
    '''от правого края влево до правой крайней заполненной ячейки'''
    countTab_col = workSheet.UsedRange.Columns.Count + StartNomerColl
    '''Удаляем колонки со сдвигом влево'''
    workSheet.Range(workSheet.Columns(StartNomerColl), workSheet.Columns(countTab_col)).Delete(1)

    workSheet.Range("D3").Value = "ИГЭ"
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Value = IGE
    workSheet.Range(workSheet.Cells(3, StartNomerColl), workSheet.Cells(3, EndNomerColl)).Merge()

    '''Отправляем данные в таблицуи Рисуем грани таблицы'''
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Borders.Weight = 2
    granPerimetr(workSheet, StartNomerRow - 1, StartNomerColl, EndNomerRow, EndNomerColl)
    granPerimetr(workSheet, StartNomerRow, StartNomerColl, StartNomerRow, EndNomerColl)
    sig.signal_3.emit(100)
    return IGE

def SopostMexTal(workSheet, dataExpTalie):
    soposNeTorf = []
    for i in dataExpTalie:
        if "Торф" not in str(i[1]):
            xxx = [i[0], i[11], i[6], i[28], None, None, None, i[29], None, None, None, i[30], None, None, None]
            soposNeTorf.append(xxx)
    
    '''Активируем лист'''
    workSheet.Activate()
    
    StartNomerRow = 5
    StartNomerColl = 1
    EndNomerRow = StartNomerRow - 1 + len(soposNeTorf)
    EndNomerColl = 15
    countTab_row = workSheet.UsedRange.Rows.Count + StartNomerRow

    '''Удаляем строки со сдвигом вверх'''
    workSheet.Rows(f"{StartNomerRow}:{countTab_row}").Delete(1)
    
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Borders.Weight = 2
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Value = soposNeTorf
    gr = [[1, 1],  [3, 6], [11, 14]]
    grani(workSheet, gr, StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl)
    
    sig.signal_4.emit(100)


def RachFMTal(workSheet, dataExpTalie):
    RachFMTalList = []
    for i in dataExpTalie:
        xxx = [i[0], i[7], i[31], i[32], i[30], i[35], i[36], i[29], i[33], i[34], i[28]]
        RachFMTalList.append(xxx)
    
    '''Активируем лист'''
    workSheet.Activate()
    
    StartNomerRow = 5
    StartNomerColl = 1
    EndNomerRow = StartNomerRow - 1 + len(RachFMTalList)
    EndNomerColl = 11
    countTab_row = workSheet.UsedRange.Rows.Count + StartNomerRow

    '''Удаляем строки со сдвигом вверх'''
    workSheet.Rows(f"{StartNomerRow}:{countTab_row}").Delete(1)
    
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Borders.Weight = 2
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Value = RachFMTalList
    gr = [[1, 3],  [7, 9]]
    grani(workSheet, gr, StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl)
    
    sig.signal_5.emit(100)

def FMTorf(workSheet, data, dataM):
    '''Активируем лист'''
    workSheet.Activate()

    IGE = []
    for i in data:
        if "Торф" in str(i[1]):
            xxx = [i[0]] + i[2 : 12 + 1] + ["-", "-", "-", "-"] + [float(i[13])*100] + [i[14]] + ["-", "-", "-", None, None, None]
            IGE.append(xxx)
    for i in dataM:
        if "Торф" in str(i[1]):
            xxx = [i[0]] + i[2 : 6 + 1] + i[11 : 15 + 1] + ["-"] + i[16 : 20 + 1] + [i[21]] + [i[35]] + [i[36]] + [i[37]] + [None, None, None]
            IGE.append(xxx)
    
    # print(f"IGE = {IGE}")
    if IGE == []:
        IGE = ["-"*24]
    # print(f"IGE = {IGE}")

    IGE = perevorotTab(IGE)
    
    StartNomerRow = 4
    StartNomerColl = 4
    EndNomerRow = 27

    EndNomerColl = StartNomerColl - 1 +  len(IGE[0])
    '''от правого края влево до правой крайней заполненной ячейки'''
    countTab_col = workSheet.UsedRange.Columns.Count + StartNomerColl
    '''Удаляем колонки со сдвигом влево'''
    workSheet.Range(workSheet.Columns(StartNomerColl), workSheet.Columns(countTab_col)).Delete(1)

    workSheet.Range("D3").Value = "ИГЭ"
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Value = IGE
    workSheet.Range(workSheet.Cells(3, StartNomerColl), workSheet.Cells(3, EndNomerColl)).Merge()

    '''Отправляем данные в таблицуи Рисуем грани таблицы'''
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Borders.Weight = 2
    granPerimetr(workSheet, StartNomerRow - 1, StartNomerColl, EndNomerRow, EndNomerColl)
    granPerimetr(workSheet, StartNomerRow, StartNomerColl, StartNomerRow, EndNomerColl)

    sig.signal_6.emit(100)

def FizMMg86(workSheet, dataM):
    IGE = []
    for i in dataM:
        if "Торф" not in str(i[1]):
            xxx = [i[0]] + i[2 : 20 + 1]
            IGE.append(xxx)

    IGE = perevorotTab(IGE)
    
    '''Активируем лист'''
    workSheet.Activate()
    
    StartNomerRow = 4
    StartNomerColl = 4
    EndNomerRow = 23

    EndNomerColl = StartNomerColl - 1 +  len(IGE[0])
    '''от правого края влево до правой крайней заполненной ячейки'''
    countTab_col = workSheet.UsedRange.Columns.Count + StartNomerColl
    '''Удаляем колонки со сдвигом влево'''
    workSheet.Range(workSheet.Columns(StartNomerColl), workSheet.Columns(countTab_col)).Delete(1)

    workSheet.Range("D3").Value = "ИГЭ"
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Value = IGE
    workSheet.Range(workSheet.Cells(3, StartNomerColl), workSheet.Cells(3, EndNomerColl)).Merge()

    '''Отправляем данные в таблицуи Рисуем грани таблицы'''
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Borders.Weight = 2
    granPerimetr(workSheet, StartNomerRow - 1, StartNomerColl, EndNomerRow, EndNomerColl)
    granPerimetr(workSheet, StartNomerRow, StartNomerColl, StartNomerRow, EndNomerColl)

    sig.signal_7.emit(100)


def MexMMG87(workSheet, dataM):
    IGE = []
    for i in dataM:
        xxx = [i[0]] + i[32 : 37 + 1]
        IGE.append(xxx)

    '''Активируем лист'''
    workSheet.Activate()
    
    StartNomerRow = 5
    StartNomerColl = 1
    EndNomerRow = StartNomerRow - 1 + len(IGE)
    EndNomerColl = 7
    countTab_row = workSheet.UsedRange.Rows.Count + StartNomerRow

    '''Удаляем строки со сдвигом вверх'''
    workSheet.Rows(f"{StartNomerRow}:{countTab_row}").Delete(1)
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Borders.Weight = 2
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Value = IGE
    gr = [[0, 0], [1, 2], [4, 5]]
    grani(workSheet, gr, StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl)

    sig.signal_8.emit(100)

def Teplofiz88(workSheet, data, dataM):
    IGE = []
    for i in data:
        xxx = [i[0]] + i[25 : 28 + 1] + [None]
        IGE.append(xxx)
    
    for i in dataM:
        xxx = [i[0]] + [i[29]] + [i[28]] + [i[31]] + [i[30]] + [None]
        IGE.append(xxx)

    '''Активируем лист'''
    workSheet.Activate()
    
    StartNomerRow = 5
    StartNomerColl = 1
    EndNomerRow = StartNomerRow - 1 + len(IGE)
    EndNomerColl = StartNomerColl - 1 + len(IGE[0])
    countTab_row = workSheet.UsedRange.Rows.Count + StartNomerRow

    '''Удаляем строки со сдвигом вверх'''
    workSheet.Rows(f"{StartNomerRow}:{countTab_row}").Delete(1)
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Borders.Weight = 2
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Value = IGE
    gr = [[0, 0], [1, 2], [5, 5]]
    grani(workSheet, gr, StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl)

    sig.signal_9.emit(100)


def Gran810(workSheet, data, dataM):
    IGE = []
    for i in data:
        if "Торф" not in str(i[1]):
            xxx = [i[0]] + i[36 : 46 + 1]
            IGE.append(xxx)
    for i in dataM:
        if "Торф" not in str(i[1]):
            xxx = [i[0]] + i[38 : 48 + 1]
            IGE.append(xxx)

    '''Активируем лист'''
    workSheet.Activate()
    
    StartNomerRow = 5
    StartNomerColl = 1
    EndNomerRow = StartNomerRow - 1 + len(IGE)
    EndNomerColl = StartNomerColl - 1 + len(IGE[0])
    countTab_row = workSheet.UsedRange.Rows.Count + StartNomerRow

    '''Удаляем строки со сдвигом вверх'''
    workSheet.Rows(f"{StartNomerRow}:{countTab_row}").Delete(1)
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Borders.Weight = 2
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Value = IGE
    gr = [[0, 0]]
    grani(workSheet, gr, StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl)

    sig.signal_10.emit(100)

def Prosad(workSheet, dataM):
    IGE = []
    for i in dataM:
        # if "Торф" not in str(i[1]):
        xxx = [i[0]] + [i[18]] + [i[2]] + [None]
        IGE.append(xxx)

    '''Активируем лист'''
    workSheet.Activate()
    
    StartNomerRow = 4
    StartNomerColl = 1
    EndNomerRow = StartNomerRow - 1 + len(IGE)
    EndNomerColl = StartNomerColl - 1 + len(IGE[0])
    countTab_row = workSheet.UsedRange.Rows.Count + StartNomerRow

    '''Удаляем строки со сдвигом вверх'''
    workSheet.Rows(f"{StartNomerRow}:{countTab_row}").Delete(1)
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Borders.Weight = 2
    workSheet.Range(workSheet.Cells(StartNomerRow, StartNomerColl), workSheet.Cells(EndNomerRow, EndNomerColl)).Value = IGE
    gr = [[0, 0], [2, 2]]
    grani(workSheet, gr, StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl)

    sig.signal_11.emit(100)

class Signals(QtCore.QObject):
    signal_1 = QtCore.pyqtSignal(int)
    signal_2 = QtCore.pyqtSignal(int)
    signal_3 = QtCore.pyqtSignal(int)
    signal_4 = QtCore.pyqtSignal(int)
    signal_5 = QtCore.pyqtSignal(int)
    signal_6 = QtCore.pyqtSignal(int)
    signal_7 = QtCore.pyqtSignal(int)
    signal_8 = QtCore.pyqtSignal(int)
    signal_9 = QtCore.pyqtSignal(int)
    signal_10 = QtCore.pyqtSignal(int)
    signal_11 = QtCore.pyqtSignal(int)
    signal_err = QtCore.pyqtSignal(str)

    signal_21 = QtCore.pyqtSignal(int)
    signal_22 = QtCore.pyqtSignal(int)
    
    signal_31 = QtCore.pyqtSignal(int)
    signal_32 = QtCore.pyqtSignal(int)
    
    signal_41 = QtCore.pyqtSignal(int)
    signal_42 = QtCore.pyqtSignal(int)

    signal_bool = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.signal_1.connect(self.on_change_1,QtCore.Qt.QueuedConnection)
        self.signal_2.connect(self.on_change_2,QtCore.Qt.QueuedConnection)
        self.signal_3.connect(self.on_change_3,QtCore.Qt.QueuedConnection)
        self.signal_4.connect(self.on_change_4,QtCore.Qt.QueuedConnection)
        self.signal_5.connect(self.on_change_5,QtCore.Qt.QueuedConnection)
        self.signal_6.connect(self.on_change_6,QtCore.Qt.QueuedConnection)
        self.signal_7.connect(self.on_change_7,QtCore.Qt.QueuedConnection)
        self.signal_8.connect(self.on_change_8,QtCore.Qt.QueuedConnection)
        self.signal_9.connect(self.on_change_9,QtCore.Qt.QueuedConnection)
        self.signal_10.connect(self.on_change_10,QtCore.Qt.QueuedConnection)
        self.signal_11.connect(self.on_change_11,QtCore.Qt.QueuedConnection)
        self.signal_err.connect(self.on_change_err,QtCore.Qt.QueuedConnection)
        
        self.signal_21.connect(self.on_change_21,QtCore.Qt.QueuedConnection)
        self.signal_22.connect(self.on_change_22,QtCore.Qt.QueuedConnection)
        
        self.signal_31.connect(self.on_change_31,QtCore.Qt.QueuedConnection)
        self.signal_32.connect(self.on_change_32,QtCore.Qt.QueuedConnection)
        
        self.signal_41.connect(self.on_change_41,QtCore.Qt.QueuedConnection)
        self.signal_42.connect(self.on_change_42,QtCore.Qt.QueuedConnection)

        self.signal_bool.connect(self.on_change_bool,QtCore.Qt.QueuedConnection)

    '''Отправляем сигналы в элементы окна'''
    def on_change_1(self, s):
        ui.progressBar_1.setValue(s)
    def on_change_2(self, s):
        ui.progressBar_2.setValue(s)
    def on_change_3(self, s):
        ui.progressBar_3.setValue(s)
    def on_change_4(self, s):
        ui.progressBar_4.setValue(s)
    def on_change_5(self, s):
        ui.progressBar_5.setValue(s)
    def on_change_6(self, s):
        ui.progressBar_6.setValue(s)
    def on_change_7(self, s):
        ui.progressBar_7.setValue(s)
    def on_change_8(self, s):
        ui.progressBar_8.setValue(s)
    def on_change_9(self, s):
        ui.progressBar_9.setValue(s)
    def on_change_10(self, s):
        ui.progressBar_10.setValue(s)
    def on_change_11(self, s):
        ui.progressBar_11.setValue(s)
    def on_change_err(self, s):
        QtWidgets.QMessageBox.information(Form, 'Excel не отвечает...', s)
    
    def on_change_21(self, s):
        ui.progressBar_12.setValue(s)
    def on_change_22(self, s):
        ui.progressBar_13.setValue(s)
    
    def on_change_31(self, s):
        ui.progressBar_14.setValue(s)
    def on_change_32(self, s):
        ui.progressBar_15.setValue(s)
    
    def on_change_41(self, s=1):
        colorBar(ui.progressBar_14, color = [170, 170, 170])
    def on_change_42(self, s=1):
        colorBar(ui.progressBar_15, color = [170, 170, 170])

    def on_change_bool(self, s):
        ui.pushButton_3.setDisabled(s)
        ui.pushButton_4.setDisabled(s)
        ui.pushButton.setDisabled(s)

sig = Signals()

@thread
def obrabotka():
    try:
        for i in range(1, 12): eval(f"colorBar(ui.progressBar_{i}, color = [100, 150, 150])")
        sig.signal_1.emit(0)
        sig.signal_2.emit(0)
        sig.signal_3.emit(0)
        sig.signal_4.emit(0)
        sig.signal_5.emit(0)
        sig.signal_6.emit(0)
        sig.signal_7.emit(0)
        sig.signal_8.emit(0)
        sig.signal_9.emit(0)
        sig.signal_10.emit(0)
        sig.signal_11.emit(0)

        """Создаем COM объект"""
        pythoncomCoInitializeEx(0)
        Excel = win32com.client.Dispatch("Excel.Application")
        # Excel.Visible=1
        """Открываем определенный файл"""
        # wb = Excel.Workbooks.Open(r"C:\vxvproj\tnnc-StaticProcess\Static.xlsx")
        """Получаем доступ к активной книге"""
        wb = Excel.ActiveWorkbook
        """Получаем доступ к активному листу"""
        # sheet1 = wb.ActiveSheet
        # sheet1 = wb.Worksheets(1)
        sheet1 = wb.Worksheets("Талые")
        sheet2 = wb.Worksheets("Мерзлые")
        sheet3 = wb.Worksheets("1.норм тал")
        sheet4 = wb.Worksheets("2.норм мерзлые")
        sheet5 = wb.Worksheets("8.2 ФМ тал")
        sheet6 = wb.Worksheets("8.3 Сопост мех тал")
        sheet7 = wb.Worksheets("8.4 Расч ФМ тал")
        sheet8 = wb.Worksheets("8.5 ФМ торф")
        sheet9 = wb.Worksheets("8.6 Физ ММГ")
        sheet10 = wb.Worksheets("8.7 Мех ММГ")
        sheet11 = wb.Worksheets("8.8 Теплофиз")
        sheet12 = wb.Worksheets("8.10 Гран")
        sheet13 = wb.Worksheets("Просадочность")
        '''Добавление листа'''
        # sheet5 = wb.Sheets.Add().Name = "xxxxx"
        
        startdata = normTalie(sheet1, sheet3)
        dataExpTalie = startdata[0]
        data = startdata[1]

        dataM = normMerzlie(sheet2, sheet4)

        FMTalie(sheet5, dataExpTalie)
        SopostMexTal(sheet6, dataExpTalie)
        RachFMTal(sheet7, dataExpTalie)
        FMTorf(sheet8, data, dataM)
        FizMMg86(sheet9, dataM)
        MexMMG87(sheet10, dataM)
        Teplofiz88(sheet11, data, dataM)
        Gran810(sheet12, data, dataM)
        Prosad(sheet13, dataM)

        for i in range(1, 12): 
            eval(f"colorBar(ui.progressBar_{i}, color = [170, 170, 170])")
    except Exception as e:
        text = f"Формирование таблиц не выполнено, повторите попытку \n\n{traceback.format_exc()}"
        sig.signal_err.emit(text)
    sig.signal_bool.emit(False)


def errS(sheet, StartNomerRow, EndNomerRow, col, countRow, ValueNone):
    for i in range(StartNomerRow, EndNomerRow + 1):
        aaa = str(sheet.Cells(i, col).Value)
        bbb = sheet.Cells(i, col + 1).Value
        bbb = int(bbb)
        bbb = str(bbb)

        if sheet.Name == "Код_Талые":
            if "Песок" not in aaa:
                xxx =  bbb[:3]
            if "Песок" in aaa:
                xxx =  bbb[:3] + bbb[-1]
            if "0" in xxx:
                sheet.Cells(i, col).Font.Color = -16776961
            proc = 50 + round(i / countRow * 100) * 0.5
            sig.signal_21.emit(proc)

        if sheet.Name == "Код_Мерзлые":
            if "Торф" not in aaa:
                xxx =  bbb[:3]
            if "Торф" in aaa:
                xxx =  bbb[:3] + bbb[-2]
            if "0" in xxx or ValueNone[i - StartNomerRow] == 1:
                sheet.Cells(i, col).Font.Color = -16776961
            proc = 50 + round(i / countRow * 100) * 0.5
            sig.signal_22.emit(proc)

def CelOne(cel):
    cel.Borders(7).Weight = 3
    cel.Borders(8).Weight = 3
    cel.Borders(9).Weight = 3
    cel.Borders(10).Weight = 3
    cel.VerticalAlignment = 2
    cel.HorizontalAlignment = 3

def ifErr(formula):
    iferror = f"IFERROR({formula},\"\")"
    text = f"=IF({iferror}=0,\"\",{iferror})"
    # print(text)
    return text

def EndIndexRowCol(sheet):
    # EndRow, EndCol = EndIndexRowCol(sheet)
    '''Определяем позиции первой и последней ячейки'''
    UsedRange = sheet.UsedRange
    # '''Количество занимаемых таблицей строк'''
    count_row = UsedRange.Rows.Count
    # '''Количество занимаемых таблицей колонок'''
    count_col = UsedRange.Columns.Count
    # '''Номер первой занимаемой строчки'''
    StartRow = UsedRange.Row
    # '''Номер первой занимаемой колонки'''
    StartCol = UsedRange.Column
    # '''Номер последней занимаемой строчки'''
    EndRow = StartRow + count_row - 1
    # '''Номер последней занимаемой колонки'''
    EndCol = StartCol + count_col - 1
    return EndRow, EndCol

def NFt(cells, okrug):
    try:
        cells.NumberFormat = okrug
    except:
        cells.NumberFormat = okrug.replace('.', ',')


OKRTal = ["0.000", "0.000", "0.000", "0.00", "0.00", "0.00", "0.00", "0.00", "0", "0.00", "0.00", "0.000", "0.0", "0.000", 
        "0.000", "0.0", "0.00", "0", "0", "0.00", "0.00", "0.00", "0.000", "0.00", "0.00", "0.00", "0.00", "0.0", "0.0", 
        "0.0", "0.0", "0.000", "0", "0.000", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.00"]
        

# @thread
def CodeTalie():
    try:
        proc = 0
        wb = CodeGrount.Book()
        sheet = wb.Worksheets("Код_Талые")
        sheet.Activate()

        StartNomerRow = 7
        '''от нижнего края вверх до нижней крайней заполненной ячейки'''
        EndNomerRow = sheet.Cells(sheet.Rows.Count, 1).End(3).Row
        countRow = EndNomerRow - StartNomerRow + 1

        '''Формулы (при вставке значений по вертикали использовать кортежи с пустым 2ым значением)
        пример: ("=формула", )"'''
        formula1 = ifErr("RC[-2]-RC[-1]")
        formula2 = ifErr("(RC[-4]-RC[-2])/RC[-1]")

        formula12 = [(formula1, formula2)]*countRow
        cell = sheet.Range(sheet.Cells(StartNomerRow, 6), sheet.Cells(EndNomerRow, 7))
        cell.ClearContents()
        cell.Value = formula12
        cell.Font.Color = -1179134

        formula3 = ifErr("RC[-2]/(1+RC[-7])")
        formula4 = ifErr("(RC[-2]-RC[-1])/RC[-2]*100")
        formula5 = ifErr("(RC[-3]-RC[-2])/RC[-2]")
        formula6 = ifErr("(RC[-10]*RC[-4])/RC[-1]")
        formula36 = [(formula3, formula4, formula5, formula6)]*countRow

        cell = sheet.Range(sheet.Cells(StartNomerRow, 10), sheet.Cells(EndNomerRow, 13))
        cell.ClearContents()
        # cell.Interior.Pattern = 0
        cell.Value = formula36
        cell.Font.Color = -1179134

        formula7 = ifErr("RC[-2]*RC[-1]")
        cell = sheet.Range(sheet.Cells(StartNomerRow, 32), sheet.Cells(EndNomerRow, 32))
        cell.ClearContents()
        cell.Value = formula7
        cell.Font.Color = -1179134
        
        formula8 = ifErr("DEGREES(ATAN(RC[-1]))")
        cell = sheet.Range(sheet.Cells(StartNomerRow, 35), sheet.Cells(EndNomerRow, 35))
        cell.ClearContents()
        cell.Value = formula8
        cell.Font.Color = -1179134
        # cell.NumberFormat = "0,0"

        '''Округления ячеек Код Талые'''
        EndRow, EndCol = EndIndexRowCol(sheet)
        RowSt = 7
        NFt(sheet.Range(sheet.Cells(RowSt, 1), sheet.Cells(EndRow, EndCol)), "0.000")
        NFt(sheet.Range(sheet.Cells(RowSt, 1), sheet.Cells(EndRow, 1)), "0")
        NFt(sheet.Range(sheet.Cells(RowSt, 2), sheet.Cells(EndRow, 2)), "0.0")
        for ok in range(3, 47 + 1):
            if OKRTal[ok-3] != "0.000":
                NFt(sheet.Range(sheet.Cells(RowSt, ok), sheet.Cells(EndRow, ok)), OKRTal[ok-3])


        '''Создаем колонки для вставки'''
        sheet.Columns("AV:AW").Delete(1)
        
        coll = sheet.Columns("AV")
        coll.HorizontalAlignment = 1
        coll.VerticalAlignment = 2

        coll = sheet.Columns("AW")
        coll.HorizontalAlignment = 3
        coll.VerticalAlignment = 2
        
        cel = sheet.Range("AV2:AV6")
        cel.HorizontalAlignment = 3
        cel.VerticalAlignment = 2
        cel.Merge()
        cel.ColumnWidth = 45
        cel.Borders.Weight = 2

        cel = sheet.Range("AW2:AW6")
        cel.HorizontalAlignment = 3
        cel.VerticalAlignment = 2
        cel.Merge()
        cel.ColumnWidth = 10
        cel.Borders.Weight = 2

        cel = sheet.Range("AV2:AW2").Value = ["Классификация грунтов согласно ГОСТ 25100", "Код грунта"]
        sheet.Range(sheet.Cells(StartNomerRow, 48), sheet.Cells(EndNomerRow, 48)).Font.Color = 0

        data = []
        for i in range(StartNomerRow, EndNomerRow + 1):
            data.append(CodeGrount.codeTalie(sheet, i))
            proc = round(i / countRow * 100) * 0.5
            sig.signal_21.emit(proc)
        
        XCells = sheet.Range(sheet.Cells(StartNomerRow, 48), sheet.Cells(EndNomerRow, 49))
        XCells.Value = data
        XCells.WrapText = True
        XCells.Borders.Weight = 2

        errS(sheet, StartNomerRow, EndNomerRow, 48, countRow, ["0"*countRow])
        colorBar(ui.progressBar_12, color = [170, 170, 170])
    except Exception as e:
        error = traceback.format_exc()
        text = f"Кодировка талых крунтов не выполнена, повторите попытку \n\n{error}"
        print(error)
        sig.signal_err.emit(text)
    sig.signal_bool.emit(False)
    ui.checkBox_3.setEnabled(True)
    ui.checkBox_4.setEnabled(True)





'''Округление ячеек (данные Мерзлые)'''
OKRMerz = [
        "0.000", "0.000", "0.000", "0.000", "0.000", "0.000", "0.000", "0.00", "0.00", "0.00", "0.00", "0.00", "0", "0.00", "0.00", 
        "0.000", "0.000", "0.000", "0.000", "0.0", "0.000", "0.000", "0.0", "0.00", "0.00", "0.00", "0.00", "0.00", "0.00", "0.00", 
        "0.000", "0.000", "0.000", "0.000", "0.000", "0.000", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0"
        ]


@thread
def CodetMerz():
    try:
        # sleep(0.1)
        wb = CodeGrount.Book()
        sheet = wb.Worksheets("Код_Мерзлые")
        sheet.Activate()
        StartNomerRow = 7
        '''от нижнего края вверх до нижней крайней заполненной ячейки'''
        EndNomerRow = sheet.Cells(sheet.Rows.Count, 1).End(3).Row
        countRow = EndNomerRow - StartNomerRow + 1

        '''Формулы (при вставке значений по вертикали использовать кортежи с пустым 2ым значением)
        пример: ("=формула", )"'''
        formula0 = ifErr("RC[-2]-RC[-1]")
        # formula1 = ifErr("RC[-3]-RC[-1]")
        # formula1 = ifErr("RC[22]*RC[3]")
        formula1 = f"=IFERROR(RC[22]*RC[3],0)"

        formula12 = [(formula0, formula1)]*countRow
        cell = sheet.Range(sheet.Cells(StartNomerRow, 5), sheet.Cells(EndNomerRow, 6))
        cell.ClearContents()
        cell.Value = formula12
        cell.Font.Color = -1179134

        formula2 = ifErr("RC[-2]-RC[-1]")
        formula3 = ifErr("(RC[-8]-RC[-2])/RC[-1]")
        formula12 = [(formula2, formula3)]*countRow
        cell = sheet.Range(sheet.Cells(StartNomerRow, 10), sheet.Cells(EndNomerRow, 11))
        cell.ClearContents()
        cell.Value = formula12
        cell.Font.Color = -1179134
        
        formula4 = ifErr("RC[-1]/(1+RC[-11])")
        formula5 = ifErr("((RC[-3]-RC[-1])/RC[-3])*100")
        formula6 = ifErr("(RC[-4]-RC[-2])/RC[-2]")
        formula7 = ifErr("(1.1*RC[-10]+RC[-11])*RC[-5]/RC[-1]")
        formula8 = ifErr("RC[-5]*(RC[-15]-RC[-12])/(0.9*(1+RC[-15]))")
        formula9 = ifErr("(RC[-7]*(RC[-16]-RC[-15]))/(0.9+RC[-7]*(RC[-16]-0.1*RC[-13]))")
        formula10 = ifErr("RC[-2]-RC[-1]")
        formula12 = [(formula4, formula5, formula6, formula7, formula8, formula9, formula10)]*countRow
        cell = sheet.Range(sheet.Cells(StartNomerRow, 14), sheet.Cells(EndNomerRow, 20))
        cell.ClearContents()
        cell.Value = formula12
        cell.Font.Color = -1179134

        '''Округления ячеек Код Мерзлые'''
        EndRow, EndCol = EndIndexRowCol(sheet)
        RowSt = 7
        NFt(sheet.Range(sheet.Cells(RowSt, 1), sheet.Cells(EndRow, EndCol)), "0.000")
        NFt(sheet.Range(sheet.Cells(RowSt, 1), sheet.Cells(EndRow, 1)), "0")
        NFt(sheet.Range(sheet.Cells(RowSt, 2), sheet.Cells(EndRow, 2)), "0.0")
        for ok in range(3, 49 + 1):
            if OKRMerz[ok-3] != "0.000":
                NFt(sheet.Range(sheet.Cells(RowSt, ok), sheet.Cells(EndRow, ok)), OKRMerz[ok-3])


        '''Создаем колонки для вставки'''
        sheet.Columns("AX:AY").Delete(1)
        
        coll = sheet.Columns("AX")
        coll.HorizontalAlignment = 1
        coll.VerticalAlignment = 2
        
        coll = sheet.Columns("AY")
        coll.HorizontalAlignment = 3
        coll.VerticalAlignment = 2

        cel = sheet.Range("AX2:AX6")
        cel.HorizontalAlignment = 3
        cel.VerticalAlignment = 2
        cel.Merge()
        cel.ColumnWidth = 45
        cel.Borders.Weight = 2

        cel = sheet.Range("AY2:AY6")
        cel.HorizontalAlignment = 3
        cel.VerticalAlignment = 2
        cel.Merge()
        cel.ColumnWidth = 10
        cel.Borders.Weight = 2

        cel = sheet.Range("AX2:AY2").Value = ["Классификация грунтов согласно ГОСТ 25100", "Код грунта"]
        sheet.Range(sheet.Cells(StartNomerRow, 50), sheet.Cells(EndNomerRow, 50)).Font.Color = 0

        data = []
        ValueNone = []
        for i in range(StartNomerRow, EndNomerRow + 1):
            xxx = CodeGrount.codeMerz(sheet, i)
            data.append(xxx[:2])
            ValueNone.append(xxx[-1])
            proc = round(i / countRow * 100) * 0.5
            sig.signal_22.emit(proc)

        XCells = sheet.Range(sheet.Cells(StartNomerRow, 50), sheet.Cells(EndNomerRow, 51))
        XCells.Value = data
        XCells.WrapText = True
        XCells.Borders.Weight = 2
        
        errS(sheet, StartNomerRow, EndNomerRow, 50, countRow, ValueNone)
        colorBar(ui.progressBar_13, color = [170, 170, 170])
    except Exception as e:
        text = f"Кодировка мерзлых крунтов не выполнена, повторите попытку \n\n{traceback.format_exc()}"
        print(traceback.format_exc())
        sig.signal_err.emit(text)
    sig.signal_bool.emit(False)
    ui.checkBox_3.setEnabled(True)
    ui.checkBox_4.setEnabled(True)

@thread
def startCode():
    Sql("StatPro")
    for i in [12, 13]: eval(f"colorBar(ui.progressBar_{i}, color = [100, 150, 150])")
    sig.signal_21.emit(0)
    sig.signal_22.emit(0)
    if ui.checkBox_1.isChecked() == True:
        if ui.checkBox_2.isChecked() == False:
            ui.checkBox_2.setEnabled(False)
        sig.signal_bool.emit(True)
        ui.checkBox_3.setEnabled(False)
        ui.checkBox_4.setEnabled(False)
        CodeTalie()
        ui.checkBox_2.setEnabled(True)

    if ui.checkBox_2.isChecked() == True:
        if ui.checkBox_1.isChecked() == False:
            ui.checkBox_1.setEnabled(False)
        sig.signal_bool.emit(True)
        ui.checkBox_3.setEnabled(False)
        ui.checkBox_4.setEnabled(False)
        CodetMerz()
        ui.checkBox_1.setEnabled(True)

# @thread
def potoktSortTal():
    try:
        SvodTabTalue.SrartSvodTalie(sig)
    except Exception as e:
        print(traceback.format_exc())
        text = f"Сотрировка талых грунтов не выполнена, повторите попытку \n\n{traceback.format_exc()}"
        sig.signal_err.emit(text)
    sig.signal_bool.emit(False)
    ui.checkBox_1.setEnabled(True)
    ui.checkBox_2.setEnabled(True)
        
# @thread
def potoktSortMerz():
    try:
        SvodTabMerzlue.SrartSvodMerz(sig)
    # except:
    except Exception as e:
        print(traceback.format_exc())
        text = f"Сотрировка мерзлых грунтов не выполнена, повторите попытку \n\n{traceback.format_exc()}"
        # text = str(traceback.print_tb(e))
        sig.signal_err.emit(text)
    sig.signal_bool.emit(False)
    ui.checkBox_1.setEnabled(True)
    ui.checkBox_2.setEnabled(True)

@thread
def startSort():
    Sql("StatPro")
    for i in [14, 15]: eval(f"colorBar(ui.progressBar_{i}, color = [100, 150, 150])")
    sig.signal_31.emit(0)
    sig.signal_32.emit(0)
    if ui.checkBox_3.isChecked() == True:
        if ui.checkBox_4.isChecked() == False:
            ui.checkBox_4.setEnabled(False)
        sig.signal_bool.emit(True)
        ui.checkBox_1.setEnabled(False)
        ui.checkBox_2.setEnabled(False)
        potoktSortTal()
        ui.checkBox_4.setEnabled(True)

    if ui.checkBox_4.isChecked() == True:
        if ui.checkBox_3.isChecked() == False:
            ui.checkBox_3.setEnabled(False)
        sig.signal_bool.emit(True)
        ui.checkBox_1.setEnabled(False)
        ui.checkBox_2.setEnabled(False)
        potoktSortMerz()
        ui.checkBox_3.setEnabled(True)


@thread
def startObrabotka():
    sig.signal_bool.emit(True)
    Sql("StatPro")
    obrabotka()

def openShablon():
    '''открытие файла как при двойном клике'''
    os.startfile('Шаблон_Статобработка.xltx')

ui.pushButton.clicked.connect(startObrabotka)
ui.pushButton_2.clicked.connect(openShablon)
ui.pushButton_3.clicked.connect(startCode)
ui.pushButton_4.clicked.connect(startSort)

if __name__ == "__main__":
    sys.exit(app.exec_())


