import numpy as np
import win32com.client
import os
# import threading
from pythoncom import CoInitializeEx as pythoncomCoInitializeEx
from time import sleep
os.system('CLS')

'''Обертка функции в потопк (декоратор)'''
def thread(my_func):
    def wrapper():
        threading.Thread(target=my_func, daemon=True).start()
    return wrapper
print("=========================================================")

def Book():
    pythoncomCoInitializeEx(0)
    Excel = win32com.client.Dispatch("Excel.Application")
    wb = Excel.ActiveWorkbook   # Получаем доступ к активной книге
    return wb

def NFt(cells, okrug):
    try:
        cells.NumberFormat = okrug
    except:
        cells.NumberFormat = okrug.replace('.', ',')

def importdataCode(sheet, StartNomerRow, StartNomerColl, EndNomerRow, EndNomerColl):
    '''Собираем список из 1ой колонки'''
    vals = sheet.Range(sheet.Cells(StartNomerRow, StartNomerColl), sheet.Cells(EndNomerRow, EndNomerColl)).value
    # vals = [vals[i][x] for i in range(len(vals)) for x in range(len(vals[i]))]
    if isinstance(vals, float) or vals == None:
        vals = [vals]
    else:
        vals = [vals[i][x] for i in range(len(vals)) for x in range(len(vals[i]))]
    return vals

def svodTalie(sheet, StartNomerRow, EndNomerRow, StartNomerColl, EndNomerColl):

    data = []
    for i in range(StartNomerRow, EndNomerRow + 1):
        RewXXX = importdataCode(sheet, i, StartNomerColl, i, EndNomerColl)
        RewXXX = [None if i == '' or i == 0 else i for i in RewXXX]
        data.append(RewXXX)
    return data

def SrartSvodTalie(sig):
    wb = Book()
    '''Работа с исходной таблицей'''
    sheet = wb.Worksheets("Код_Талые")
    # sheet.Activate()
    StartNomerRow = 7
    '''от нижнего края вверх до нижней крайней заполненной ячейки'''
    EndNomerRow = sheet.Cells(sheet.Rows.Count, 1).End(3).Row
    # EndNomerRow = 15
    StartNomerColl = 1
    EndNomerColl = 49
    data = svodTalie(sheet, StartNomerRow, EndNomerRow, StartNomerColl, EndNomerColl)
    '''Сортировка списка по ключу'''
    datasort = sorted(data, key = lambda i: int(i[-1]))
    codeNomer = [int(i[-1]) for i in datasort]
    codeNomer = set(codeNomer)

    groupList = []
    for x in codeNomer:
        xxx = []
        for i in datasort:
            if i[-1] == x:
                xxx.append(i)
        groupList.append(xxx)

    '''Работа с результирующей таблицей'''
    sheet = wb.Worksheets("Талые")
    sheet.Activate()
    StartNomerRow = 8
    countTab_row = sheet.UsedRange.Rows.Count + StartNomerRow
    '''Удаляем строки со сдвигом вверх'''
    sheet.Rows(f"{StartNomerRow}:{countTab_row}").Delete(1)

    RRR = [
            ["Кол-во определений (n)", None],
            ["Минимальное значение (Xmin)", None],
            ["Максимальное значение (Xmax)", None],
            ["Нормативное значение (Xn)", None],
            ["Среднекв. отклонение (S)", None],
            ["Коэффициент вариации (V)", None],
            ["показатель точности (0,85)", None],
            ["показатель точности (0,95)", None],
            ["Коффициент надежности по грунту (0,85)", None],
            ["Коффициент надежности по грунту (0,95)", None],
            ["Расчетное значение (0,85)", None],
            ["Расчетное значение (0,95)", None]
            ]

    lenRRR = len(RRR)
    EndNomerColl = 47

    def perevorotTab(xxx):
        res = []
        for i in range(len(xxx[0])):
            zzz = []
            for x in range(len(xxx)):
                zzz.append(xxx[x][i])
            res.append(zzz)
        return res

    '''Переворачавеем списки для расчета по столбцам'''
    groupListPerevorot = []
    for i in groupList:
        xxx = perevorotTab(i)
        groupListPerevorot.append(xxx)


    Row = -1
    for i in groupList:
        iii = groupList.index(i)
        '''Отправляем название грунта с кодом'''
        Row += 1
        nameX = str(int(i[0][-1])) + " " + i[0][-2]
        IGE = sheet.Cells(StartNomerRow + Row, StartNomerColl)
        IGE.value = nameX
        IGE.Font.Size = 14
        IGE.Font.Bold = True
        IGEnd = sheet.Range(sheet.Cells(StartNomerRow + Row, StartNomerColl), sheet.Cells(StartNomerRow + Row, EndNomerColl))
        IGEnd.Merge()
        IGEnd.Borders.Weight = 2
        IGEnd.HorizontalAlignment = 3
        IGEnd.VerticalAlignment = 2
        lenX = len(i)

        '''---------------------------------------------------------------------------'''
        '''Отправляем данные'''
        '''---------------------------------------------------------------------------'''
        Row += 1
        BBB = sheet.Range(sheet.Cells(StartNomerRow + Row, StartNomerColl), sheet.Cells(StartNomerRow + Row + lenX - 1, EndNomerColl))
        BBB.value = i
        BBB.Borders.Weight = 2
        BBB.HorizontalAlignment = 3
        NFt(BBB, "0.000")
        RowSt = StartNomerRow + Row
        RowEnd = StartNomerRow + Row + lenX - 1


        ''' Е '''
        col = "AF"
        BBB = sheet.Range(f"{col}{StartNomerRow + Row}:{col}{StartNomerRow + Row + lenX - 1}")
        NFt(BBB, "0.00")

        col = "K"
        BBB = sheet.Range(f"{col}{StartNomerRow + Row}:{col}{StartNomerRow + Row + lenX - 1}")
        NFt(BBB, "0.0")
        
        ''' ϕi '''
        col = "AI"
        BBB = sheet.Range(f"{col}{StartNomerRow + Row}:{col}{StartNomerRow + Row + lenX - 1}")
        NFt(BBB, "0.0")

        col1 = "AK"
        col2 = "AU"
        BBB = sheet.Range(f"{col1}{StartNomerRow + Row}:{col2}{StartNomerRow + Row + lenX - 1}")
        NFt(BBB, "0.00")

        ''' Ci '''
        col = "AJ"
        BBB = sheet.Range(f"{col}{StartNomerRow + Row}:{col}{StartNomerRow + Row + lenX - 1}")
        NFt(BBB, "0.00")
        BBB = sheet.Range(f"{col}{StartNomerRow + Row + lenX - 1 - 1}:{col}{StartNomerRow + Row + lenRRR - 1}")
        NFt(BBB, "0.00")

        Row = Row + lenX - 1

        '''---------------------------------------------------------------------------'''
        '''Отправляем расчетные позиции'''
        '''---------------------------------------------------------------------------'''
        Row += 1
        AAA = sheet.Range(sheet.Cells(StartNomerRow + Row, StartNomerColl), sheet.Cells(StartNomerRow  + Row  + lenRRR - 1, EndNomerColl))
        sheet.Range(sheet.Cells(StartNomerRow + Row, StartNomerColl), sheet.Cells(StartNomerRow  + Row  + lenRRR - 1, StartNomerColl + 1)).value = RRR
        AAA.Borders.Weight = 2
        # AAA.WrapText = True
        AAA.HorizontalAlignment = 3
        NFt(AAA, "0,000")

        '''Выравниваем даннче "Кол-во определений (n)" и др. по левому краю в ячейке'''
        ColOne = sheet.Range(sheet.Cells(StartNomerRow + Row, StartNomerColl), sheet.Cells(StartNomerRow + Row + lenRRR - 1, StartNomerColl))
        ColOne.HorizontalAlignment = 1

        '''Собираем список с формулами из списков построчно в расчетных данных'''
        '''-----------------------------------------------------------------------------------------------'''
        ResList = []
        nnnList = []
        XminList = []
        XmasList = []
        XnList = []
        SSSList = []
        VVVList = []
        Toch085List = []
        Toch095List = []
        KKK085List = []
        KKK095List = []
        Raschet085List = []
        Raschet095List = []
        
        ggg =  groupListPerevorot[iii]
        for col in range(3, EndNomerColl + 1):
            uuu = ggg[col - 1]
            uuu = [i if i != None and not isinstance(i, str) else 0 for i in uuu]
            if sum(uuu) != 0 and len(uuu):
                xxx = f"=COUNT(R[-{lenX - 1 + 1}]C:R[-1]C)"
                nnnList.append(xxx)
                xxx = f"=MIN(R[-{lenX - 1 + 2}]C:R[-2]C)"
                XminList.append(xxx)
                xxx = f"=MAX(R[-{lenX - 1 + 3}]C:R[-3]C)"
                XmasList.append(xxx)
            else:
                xxx = None
                nnnList.append(xxx)
                XminList.append(xxx)
                XmasList.append(xxx)

            if sum(uuu) != 0 and sum(uuu) != None:
                if col not in [6, 7, 10, 11, 12, 13, 32, 35]:
                    xxx = f"=AVERAGE(R[-{lenX - 1 + 4}]C:R[-4]C)"
                if col == 6:
                    xxx = "=RC[-2]-RC[-1]"
                if col == 7:
                    xxx = "=(RC[-4]-RC[-2])/RC[-1]"
                if col == 10:
                    xxx = "=RC[-2]/(1+RC[-7])"
                if col == 11:
                    xxx = "=(RC[-2]-RC[-1])/RC[-2]*100"
                if col == 12:
                    xxx = "=(RC[-3]-RC[-2])/RC[-2]"
                if col == 13:
                    xxx = "=(RC[-10]*RC[-4])/RC[-1]"
                if col == 32:
                    xxx = "=RC[-2]*RC[-1]"
                if col == 35:
                    xxx = "=DEGREES(ATAN(RC[-1]))"
            else:
                xxx = None
            XnList.append(xxx)
            
            if sum(uuu) != 0 and len(uuu) != 1:
                if col in [3, 4, 5, 8, 30, 31, 32, 34, 35, 36]:
                    xxx = f"=STDEV(R[-{lenX - 1 + 5}]C:R[-5]C)"
                    SSSList.append(xxx)
                    xxx = f"=R[-1]C/R[-2]C"
                    VVVList.append(xxx)
                else:
                    xxx = None
                    SSSList.append(xxx)
                    VVVList.append(xxx)
            
                if col == 8:
                    xxx = "=(1.1*R[-1]C)/((R[-6]C)^0.5)"
                    Toch085List.append(xxx)
                    xxx = "=(1.83*R[-2]C)/((R[-7]C)^0.5)"
                    Toch095List.append(xxx)
                    xxx = "=1/(1-R[-2]C)"
                    KKK085List.append(xxx)
                    xxx = "=1/(1-R[-2]C)"
                    KKK095List.append(xxx)
                    xxx = "=R[-7]C/R[-2]C"
                    Raschet085List.append(xxx)
                    xxx = "=R[-8]C/R[-2]C"
                    Raschet095List.append(xxx)
                    
                if col in [32, 34, 35, 36]:
                    xxx = "=(1.16*R[-1]C)/((R[-6]C)^0.5)"
                    Toch085List.append(xxx)
                    xxx = "=(2.01*R[-2]C)/((R[-7]C)^0.5)"
                    Toch095List.append(xxx)
                    xxx = "=1/(1-R[-2]C)"
                    KKK085List.append(xxx)
                    xxx = "=1/(1-R[-2]C)"
                    KKK095List.append(xxx)
                    xxx = "=R[-7]C/R[-2]C"
                    Raschet085List.append(xxx)
                    xxx = "=R[-8]C/R[-2]C"
                    Raschet095List.append(xxx)
                    
                if col not in [8, 32, 34, 35, 36]:
                    xxx = None
                    Toch085List.append(xxx)
                    Toch095List.append(xxx)
                    KKK085List.append(xxx)
                    KKK095List.append(xxx)
                    Raschet085List.append(xxx)
                    Raschet095List.append(xxx)
            else:
                xxx = None
                SSSList.append(xxx)
                VVVList.append(xxx)
                Toch085List.append(xxx)
                Toch095List.append(xxx)
                KKK085List.append(xxx)
                KKK095List.append(xxx)
                Raschet085List.append(xxx)
                Raschet095List.append(xxx)


        ResList.append(nnnList)
        ResList.append(XminList)
        ResList.append(XmasList)
        
        ResList.append(XnList)
        ResList.append(SSSList)
        ResList.append(VVVList)

        ResList.append(Toch085List)
        ResList.append(Toch095List)
        ResList.append(KKK085List)
        ResList.append(KKK095List)
        ResList.append(Raschet085List)
        ResList.append(Raschet095List)

        sheet.Range(sheet.Cells(RowEnd + 1, 3), sheet.Cells(RowEnd + 12, EndNomerColl)).value = ResList

        ''' Е '''
        col = "AF"
        BBB = sheet.Range(f"{col}{StartNomerRow + Row}:{col}{StartNomerRow + Row + lenRRR - 1}")
        NFt(BBB, "0.00")

        ''' ϕi '''
        col = "AI"
        BBB = sheet.Range(f"{col}{StartNomerRow + Row}:{col}{StartNomerRow + Row + 3}")
        NFt(BBB, "0.0")
        BBB = sheet.Range(f"{col}{StartNomerRow + Row + lenRRR - 1 - 1}:{col}{StartNomerRow + Row + lenRRR - 1}")
        NFt(BBB, "0")

        col1 = "AK"
        col2 = "AU"
        BBB = sheet.Range(f"{col1}{StartNomerRow + Row}:{col2}{StartNomerRow + Row + lenRRR - 1}")
        NFt(BBB, "0.00")

        ''' Ci '''
        col = "AJ"
        BBB = sheet.Range(f"{col}{StartNomerRow + Row}:{col}{StartNomerRow + Row + 3}")
        NFt(BBB, "0.00")
        BBB = sheet.Range(f"{col}{StartNomerRow + Row + lenRRR - 1 - 1}:{col}{StartNomerRow + Row + lenRRR - 1}")
        NFt(BBB, "0.00")

        '''Кол-во определений (n)'''
        AAA = sheet.Range(sheet.Cells(StartNomerRow + Row, StartNomerColl), sheet.Cells(StartNomerRow + Row, EndNomerColl))
        NFt(AAA, "0")

        Row = Row + lenRRR - 1

        proc = round(groupList.index(i) / (len(groupList)) * 100)
        sig.signal_31.emit(proc)

    EndNomerRow = sheet.Cells(sheet.Rows.Count, 1).End(3).Row
    cel = sheet.Range(sheet.Cells(StartNomerRow, StartNomerColl), sheet.Cells(EndNomerRow, EndNomerColl))

    cel.VerticalAlignment = 2
    sig.signal_31.emit(100)
    sig.signal_41.emit(1)
    sleep(0.01)
    print("=========================================================")


if __name__ == "__main__":
    from StatPro import sig, app, sys, threading
    
    my_func = SrartSvodTalie
    threading.Thread(target=my_func, args=(sig, ), daemon=True).start()
    sys.exit(app.exec_())
