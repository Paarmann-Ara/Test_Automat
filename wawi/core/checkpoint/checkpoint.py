from Toolboxs.mToolbox import cToolbox
import datetime
from WAWi.Setting.Core.mCheckPointConfig import cCheckPointConfig
import codecs
CheckPointResult = []

# --
# ...
# --


class cCheckPoint():
    def __init__(cls):
        super().__init__()
        cls.CheckPoint = None

    CheckPoint = [[]]  # 'name', 'war', 'ist', 'soll', 'id', IsStatus

# --
# ...
# --
    @classmethod
    def ChkPoint(cls, Object, Methode='', Soll='Nothing', ExName='', IsNotSingleMode=True):

        try:

            if Object == None:
                return

            if not Config.IsCheckPoint:
                return

            tempResult = ''
            Soll = cls.Str(Soll)

            if isinstance(Object, str):
                Id = Methode
            elif aqObject.IsSupported(Object, 'MappedName'):
                Id = Object.MappedName
            else:
                Id = Methode

            if len(cls.CheckPoint) <= 1:
                cls.CheckPoint.append(['', '', '', Soll, Id, IsNotSingleMode])
                Index = len(cls.CheckPoint) - 1

            else:
                for it in cls.CheckPoint:
                    if len(it) != 0:
                        try:
                            if it.index(Id):
                                Index = cls.CheckPoint.index(it)
                                break

                        except Exception as exp:
                            if cls.CheckPoint.index(it) == len(cls.CheckPoint) - 1:
                                cls.CheckPoint.append(
                                    ['', '', '', Soll, Id, IsNotSingleMode])
                                Index = len(cls.CheckPoint) - 1

                        finally:
                            pass

            if Object == "DB":
                pass

            else:

                if ExName == '':
                    if aqObject.IsSupported(Object, 'Exists'):
                        if Object.Exists:
                            if aqObject.IsSupported(Object, 'Name'):
                                cls.CheckPoint[Index][0] = Object.Name
                    else:
                        cls.CheckPoint[Index][0] = 'Unbekannt'
                else:
                    cls.CheckPoint[Index][0] = ExName

                tempRst = cls.__GettempResult(Object, Methode)
                tempResult = tempRst[1]

            if Soll == 'cObjects':
                if Config.CheckPointMode == 'Write':
                    cls.DBC(Type='Command', SQLCommand='USE AQC;INSERT INTO dbo.tCheckPoint([ObjectName], [Action], Property, [Value]) VALUES (' +
                            "'" + Id + "'" + ',\'' + Methode + '\', ' + "'" + tempRst[0] + "'" + ', ' + "'" + tempResult + "'" + ')', SQLHost=Config.AQCHost)
                    cls.CheckPoint.remove(cls.CheckPoint[Index])
                    return

                elif Config.CheckPointMode == 'Read':
                    if cls.DBC(SQLCommand='USE AQC;SELECT COUNT(1) FROM dbo.tCheckPoint WHERE ObjectName = ' + "'" + Id + "'", SQLHost=Config.AQCHost, Type='OnePropertyQRY') != '0':
                        temp = cls.DBC(SQLCommand='USE AQC;SELECT [Value] FROM dbo.tCheckPoint WHERE ObjectName = ' +
                                       "'" + Id + "'", SQLHost=Config.AQCHost, Type='OnePropertyQRY')
                        if temp is not None:
                            cls.CheckPoint[Index][3] = temp
                    else:
                        cls.CheckPoint[Index][3] = 'Nothing'
                    cls.CheckPoint[Index][5] = False

            if cls.CheckPoint[Index][5]:
                cls.CheckPoint[Index][1] = tempResult
                cls.CheckPoint[Index][5] = False
            else:
                cls.CheckPoint[Index][2] = tempResult
                cls.TestResult('CheckPoint: ' + cls.CheckPoint[Index][0], TypeOfResultObject='CheckPoint',
                               F0_war=cls.CheckPoint[Index][1], F0_ist=cls.CheckPoint[Index][2], F0_Soll=cls.CheckPoint[Index][3])

                cls.__BugDetectAndAlarm(Index)
                cls.CheckPoint.remove(cls.CheckPoint[Index])

        except Exception as exp:
            Log.Warning('CheckPoint: ' + str(exp))
            if Object != None and aqObject.IsSupported(Object, 'Name'):
                cls.TestResult('CheckPoint ' + Object.Name + ': ',
                               TypeOfResultObject='Info', MoreInfo=str(exp))
            else:
                cls.TestResult(
                    'CheckPoint: ', TypeOfResultObject='Info', MoreInfo=str(exp))
# --
# ...
# --
# --
# ...
# --

    @classmethod
    def __GettempResult(cls, Object, Methode):

        try:

            tempResult = ['', '']  # Property, Value

            if Methode == 'Count':
                if aqObject.IsSupported(Object, 'wItemCount'):
                    tempResult[0] = 'wItemCount'
                    tempResult[1] = cls.Str(Object.wItemCount)

                elif aqObject.IsSupported(Object, 'wRowCount') and not isinstance(tempResult[1], int):
                    tempResult[0] = 'wRowCount'
                    tempResult[1] = cls.Str(Object.wRowCount)

                elif aqObject.IsSupported(Object, 'wItems') and not isinstance(tempResult[1], int):
                    tempResult[0] = 'wItems'
                    tempResult[1] = cls.Str(Object.wRowCount)

            elif Methode == 'Text':
                if aqObject.IsSupported(Object, 'wText'):
                    tempResult[0] = 'wText'
                    tempResult[1] = Object.wText

                elif aqObject.IsSupported(Object, 'WPFControlText'):
                    tempResult[0] = 'WPFControlText'
                    tempResult[1] = Object.WPFControlText

                elif aqObject.IsSupported(Object, 'WndCaption'):
                    tempResult[0] = 'WndCaption'
                    tempResult[1] = Object.WndCaption

                elif aqObject.IsSupported(Object, 'Text'):
                    tempResult[0] = 'Text'
                    tempResult[1] = Object.Text

                elif aqObject.IsSupported(Object, 'Header'):
                    tempResult[0] = 'Header'
                    tempResult[1] = Object.Header

            elif Methode == 'Enabled':
                if aqObject.IsSupported(Object, 'Enabled'):
                    tempResult[0] = 'Enabled'
                    if Object.Enabled:
                        tempResult[1] = 'True'
                    else:
                        tempResult[1] = 'False'

            # Statics Objects

            elif Methode == 'Title':
                if aqObject.IsSupported(Object, 'HeaderTitle'):
                    tempResult[0] = 'HeaderTitle'
                    tempResult[1] = Object.HeaderTitle

            elif Methode == 'TabName':
                if aqObject.IsSupported(Object, 'SelectedTab'):
                    tempResult[0] = 'SelectedTab'
                    tempResult[1] = Object.SelectedTab.Text.OleValue

            elif Methode == 'ClickButton':
                if aqObject.IsSupported(Object, 'Text'):
                    tempResult[0] = 'Text'
                    tempResult[1] = Object.Text.OleValue

            elif Methode == 'StateCheckBox':
                if aqObject.IsSupported(Object, 'WPFControlText'):
                    tempResult[0] = 'WPFControlText'
                    tempResult[1] = Object.WPFControlText
                elif aqObject.IsSupported(Object, 'get_Content'):
                    tempResult[0] = 'get_Content'
                    tempResult[1] = Object.get_Content().OleValue

            elif Methode == 'CheckBoxState':
                if aqObject.IsSupported(Object, 'wState'):
                    tempResult[0] = 'wState'
                    tempResult[1] = Object.wState
                elif aqObject.IsSupported(Object, 'get_IsChecked'):
                    tempResult[0] = 'get_IsChecked'
                    tempResult[1] = str(Object.get_IsChecked().OleValue)

            elif Methode == 'CheckRadio':
                if aqObject.IsSupported(Object, 'wChecked'):
                    tempResult[0] = 'wChecked'
                    tempResult[1] = Object.wChecked

            elif Methode == 'ClickItem':
                if aqObject.IsSupported(Object, 'wSelection'):
                    tempResult[0] = 'wSelection'
                    tempResult[1] = Object.wSelection
                elif aqObject.IsSupported(Object, 'wItemList'):
                    tempResult[0] = 'wItemList'
                    tempResult[1] = Object.wItemList
                elif aqObject.IsSupported(Object, 'wSelectedItems'):
                    tempResult[0] = 'wSelectedItems'
                    tempResult[1] = Object.wSelectedItems

            elif Methode == 'DblClickItem':
                if aqObject.IsSupported(Object, 'wSelection'):
                    tempResult[0] = 'wSelection'
                    tempResult[1] = Object.wSelection
                elif aqObject.IsSupported(Object, 'wItemList'):
                    tempResult[0] = 'wItemList'
                    tempResult[1] = Object.wItemList
                elif aqObject.IsSupported(Object, 'wSelectedItems'):
                    tempResult[0] = 'wSelectedItems'
                    tempResult[1] = Object.wSelectedItems

            elif Methode == 'Date':
                if aqObject.IsSupported(Object, 'wDate'):
                    tempResult[0] = 'wDate'
                    tempResult[1] = aqConvert.DateTimeToFormatStr(
                        Object.wDate, "%d/%m/%Y")

            elif Methode == 'SetDate':
                if aqObject.IsSupported(Object, 'WPFControlText'):
                    tempResult[0] = 'WPFControlText'
                    tempResult[1] = Object.WPFControlText

            elif Methode == 'SetText':
                if aqObject.IsSupported(Object, 'CueText.OleValue'):
                    tempResult[0] = 'CueText'
                    tempResult[1] = Object.CueText.OleValue
                elif aqObject.IsSupported(Object, 'wCueBanner'):
                    tempResult[0] = 'wCueBanner'
                    tempResult[1] = Object.wCueBanner

            elif Methode == 'CheckItem':
                if aqObject.IsSupported(Object, 'WPFControlText'):
                    tempResult[0] = 'wItems'
                    tempResult[1] = Object.WPFControlText

            elif Methode == 'Click':
                if aqObject.IsSupported(Object, 'CueText.OleValue'):
                    tempResult[0] = 'wItems'
                    tempResult[1] = Object.CueText.OleValue
                elif aqObject.IsSupported(Object, 'ClrClassName'):
                    tempResult[0] = 'wItems'
                    tempResult[1] = Object.ClrClassName

            elif Methode == 'Close':
                if aqObject.IsSupported(Object, 'WndCaption'):
                    tempResult[0] = 'WndCaption'
                    tempResult[1] = Object.WndCaption
                elif aqObject.IsSupported(Object, 'Name'):
                    tempResult[0] = 'Name'
                    tempResult[1] = Object.Name

            elif Methode == 'DblClick':
                if aqObject.IsSupported(Object, 'CueText.OleValue'):
                    tempResult[0] = 'wItems'
                    tempResult[1] = Object.CueText.OleValue
                elif aqObject.IsSupported(Object, 'ClrClassName'):
                    tempResult[0] = 'wItems'
                    tempResult[1] = Object.ClrClassName

            elif Methode == 'TreeViewClick':
                if aqObject.IsSupported(Object, 'wSelection'):
                    tempResult[0] = 'wSelection'
                    tempResult[1] = Object.wSelection

            elif Methode[:8] == 'ListView':
                Column = Methode[9:]
                if aqObject.IsSupported(Object, 'Header'):
                    HeaderControl = Object.Header
                    if aqObject.IsSupported(Object, 'wItemCount'):
                        ItemCount = HeaderControl.wItemCount
                        _ = 0
                        for _ in range(0, ItemCount):
                            if HeaderControl.wItem[_] == Column:
                                tempResult[0] = 'wItem'
                                tempResult[1] = str(Object.wItem[0, _])
                                break

                elif aqObject.IsSupported(Object, 'wValue'):
                    tempResult[0] = 'wValue'
                    if Object.wValue[0, Column] == None:
                        tempResult[1] = ''
                    else:
                        tempResult[1] = str(Object.wValue[0, Column].OleValue)

                elif aqObject.IsSupported(Object, 'wHeader'):
                    ItemCount = Object.Columns.Count
                    _ = 0
                    for _ in range(0, ItemCount):
                        if Object.wHeader.wItem[_] == Column:
                            tempResult[0] = 'wHeader'
                            tempResult[1] = str(Object.wItem[0, _])
                            break

            else:
                tempResult[0] = 'Query'
                tempResult[1] = cls.DBC(
                    SQLCommand=Methode, Type='OnePropertyQRY')

            if isinstance(tempResult[1], bool):
                if tempResult[1] == True:
                    tempResult[1] = 'True'
                else:
                    tempResult[1] = 'False'

            if isinstance(tempResult[1], float):
                tempResult[1] = FloatToStr(tempResult[1])
            elif isinstance(tempResult[1], str):
                tempResult[1] = tempResult[1]
            elif isinstance(tempResult[1], int):
                tempResult[1] = IntToStr(tempResult[1])
            else:
                tempResult[1] = 'Null'

            return tempResult

        except Exception as exp:
            Log.Warning('__GettempResult: ' + str(exp))
            cls.TestResult('__GettempResult: ',
                           TypeOfResultObject='Info', MoreInfo=str(exp))
# --
# ...
# --

    @classmethod
    def __BugDetectAndAlarm(cls, Id):

        try:

            if cls.CheckPoint[Id][3] == 'Nothing':
                return

            Message = ''

            cls.CheckPoint[Id][3] = cls.Str(cls.CheckPoint[Id][3])
            cls.CheckPoint[Id][2] = cls.Str(cls.CheckPoint[Id][2])

            if cls.CheckPoint[Id][3] != cls.CheckPoint[Id][2]:

                CheckPoint_1 = cls.SolveChar(
                    cls.CheckPoint[Id][1].strip())[0:48]
                CheckPoint_2 = cls.SolveChar(
                    cls.CheckPoint[Id][2].strip())[0:48]
                CheckPoint_3 = cls.SolveChar(
                    cls.CheckPoint[Id][3].strip())[0:48]
                CheckPoint_4 = cls.SolveChar(
                    cls.CheckPoint[Id][4].strip())[0:500]

                CheckPointResult.append(CheckPoint_1.center(50, '.') + CheckPoint_2.center(
                    50, '.') + CheckPoint_3.center(50, '.') + CheckPoint_4.ljust(500, '.') + '\n\n')

                if len(CheckPointResult) > Config.CheckPointNumberofObjectsInEmail:
                    Version = cls.DBC(
                        SQLCommand="USE eazybusiness;SELECT cValue FROM tOptions WHERE ckey = 'Revision'", Type='OnePropertyQRY')
                    Message = '<h1>Hallo zusammen, </h1><h3> nachfolgend das einen Bugpotenzial in der Version ' + \
                        Version + ' am ' + \
                        str(datetime.datetime.now().strftime(
                            "%m/%d/%Y, %H:%M:%S")) + ' gefunden.</h3><p>\n'
                    Message = Message + 'In diesem Bereich treten Fehler auf. \n\n'
                    Message = Message + 'CheckPoint>>>'.center(50, '.') + '>>>CheckPoint'.center(
                        50, '.') + 'Soll'.center(50, '.') + 'Name'.ljust(500, '.') + '\n' + 650*'-' + '\n\n'

                    for it in CheckPointResult:
                        Message = Message + it

                    cls.GetDeliveryAddress("BugAlert")

                    cls.SendEmail(Message,
                                  from_addr=Config.TC_BugAlert_Address,
                                  to_addr=cls.to_Address_list,
                                  subject='TestComplete hat vileicht einen Bug gefunden!',
                                  login=Config.TC_BugAlert_Address,
                                  password=Config.TC_BugAlert_Password, IsAttach=False)

                    CheckPointResult.clear()

        except Exception as exp:
            Log.Warning('__BugDetectAndAlarm: ' + str(exp))
            cls.TestResult('__BugDetectAndAlarm: ',
                           TypeOfResultObject='Info', MoreInfo=str(exp))
