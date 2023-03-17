import array
import codecs
import inspect
import os
import datetime
from wawi.core.base.bluepages.bp_base import BluepageBase
from wawi.core.base.base_instances import BaseInstances

# --
# ...
# --

class Base(BluepageBase, BaseInstances):
    TestResultObject = [[11]]
    QSource = ''
    Empfanger = 'Admin'
    to_Adddress = ''
    to_Address_list = ''

    def __init__(self, Mode=''):
        super().__init__()
        self.TestMode = Mode
        
# --
# ...
# --

    def Setup(self, Methode='', ChangeCheckListAndAntwortMethode=''):
        pass
# --
# ...
# --

    def Prerequisite(self):
        if self.IsRunnigProcesByName(self.ConfigAQC(self, 'ProcessName')):
            self.RecoverWAWi()
        # if wawi is not awailable start wawi from module and methode
        pass
# --
# ...
# --

    def AfterSetup(self):
        pass
# --
# ...
# --

    def ChangeCheckListAndAntwortOrUseCheckListExt(self, ChangeCheckListAndAntwortMethode=''):
        pass
# --
# ...
# --

    def TestResult(self, TestName='', FensterZeit=["", ""], Empfanger='Admin', TypeOfResultObject='', QSource='', war='', ist='', F0_war='', F0_ist='', F0_Soll='', MoreInfo='', Mode=''):

        try:

            self.SetObjectsLog()

            TestName = self.GetClassName(TestName, Mode, MoreInfo)

            time.sleep(self.getTime('RefreshingTime'))

            Empfanger = Empfanger[0:15]
            QSource = self.SolveChar(QSource[0:50])
            TestName = TestName[0:99]
            war = war[0:10]
            ist = ist[0:10]

            EZeit = FensterZeit[0]
            IsFenster = FensterZeit[1]

            F0_war = self.SolveChar(F0_war[0:29])
            F0_ist = self.SolveChar(F0_ist[0:29])
            F0_Soll = self.SolveChar(F0_Soll[0:29])

            Reserved = ''  # F0_id[0:11]

            MoreInfo = self.SolveChar(MoreInfo)
            TestName = self.SolveChar(TestName)
            TestName = self.SolveWort(self.SolveChar(TestName))

            sIndicator = '>'

            if TypeOfResultObject == 'Message':
                sIndicator = '!'

            elif TypeOfResultObject == 'Bug' or TypeOfResultObject == 'Info':
                sIndicator = ':-('

            elif TypeOfResultObject == 'Information':
                sIndicator = '>>>'

            elif TypeOfResultObject == 'Bool':
                sIndicator = 'T/F'

            elif TypeOfResultObject == 'MessageManager':
                sIndicator = '(!)'

            elif TypeOfResultObject == 'Objects':
                sIndicator = '|!|'

            elif TypeOfResultObject == 'CheckPoint' and F0_Soll == F0_ist:
                sIndicator = '>^<'

            elif TypeOfResultObject == 'CheckPoint' and F0_Soll != F0_ist:
                sIndicator = '>!<'

            now = self.WaitForNow()

            self.ChkPoint(None)

            if len(MoreInfo) != 0:
                tempIndex = len(MoreInfo) // 95 + 2
                tempMoreInfo = ''
                for index in range(1, tempIndex):
                    temp = MoreInfo[(index - 1) * 95: index * 95] + '\n'
                    tempMoreInfo = temp + tempMoreInfo
                MoreInfo = tempMoreInfo

            self.TestResultObject.append([str(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")).strip(), sIndicator.strip(), TestName.strip().replace(' ', '_'), IsFenster.strip(
            ), QSource.strip(), war.strip(), ist.strip(), EZeit.strip(), F0_Soll.strip(), F0_war.strip(), F0_ist.strip(), Empfanger.strip(), MoreInfo.strip()])

        except Exception as exp:
            Log.Warning("TestResult: " + str(exp))

        finally:
            pass
# --
# ...
# --

    def Ergebnisprotokoll(self, exp='', Type=''):

        try:

            Log.SaveToDisk()

            Version = self.DBC(
                SQLCommand="USE eazybusiness;SELECT cValue FROM tOptions WHERE ckey = 'Revision'", Type='OnePropertyQRY')
            Node = os.environ['COMPUTERNAME']
            User = os.getlogin()
            indexItem = 0
            ReusltText = ''
            InformationText = ''

            if len(self.TestResultObject) > 1:
                ReusltText = '<h1>Hallo zusammen, </h1>\n<h3>nachfolgend das Ergebnis der durchlaufenden Testfalle am:' + \
                    self.TestResultObject[1][0] + '\n\nDie WAWi-Version:' + Version + '\nDas Host: ' + \
                    Node + '-' + self.GetPlatform() + '\nDer Benutzer: ' + User + '\n</h3> <p>\n'
                ReusltText = ReusltText + 'Datum'.ljust(21, '.') + 'Zeichen'.center(10, '.') + 'Test Name'.ljust(99, '.')+'Fenster'.center(7, '.') + 'QQuelle'.center(50, '.') + 'DB>>>'.center(10, '.') + '>>>DB'.center(
                    10, '.') + 'E-Zeit'.center(13, '.') + '>Check<'.center(30, '.') + 'Check>>>'.center(30, '.') + '>>>Check'.center(30, '.') + 'Empfanger'.center(15, '.') + 'MehrInfo'.ljust(0, '.') + 26*'.' + '\n' + 340*'*' + '\n'

            for indexItem in range(1, len(self.TestResultObject), 1):

                self.GetDeliveryAddress(self.TestResultObject[indexItem][11])

                ReusltText = ReusltText + self.TestResultObject[indexItem][0].ljust(21, '.') + self.TestResultObject[indexItem][1].center(10, '.') + self.TestResultObject[indexItem][2].ljust(99, '.') + self.TestResultObject[indexItem][3].center(7, '.') + self.TestResultObject[indexItem][4].center(50, '.') + self.TestResultObject[indexItem][5].center(10, '.') + self.TestResultObject[indexItem][6].center(
                    10, '.') + self.TestResultObject[indexItem][7].center(13, '.') + self.TestResultObject[indexItem][8].center(30, '.') + self.TestResultObject[indexItem][9].center(30, '.') + self.TestResultObject[indexItem][10].center(30, '.') + self.TestResultObject[indexItem][11].center(15, '.') + self.TestResultObject[indexItem][12].ljust(0) + 2*'\n'
            if exp != '':
                ReusltText = ReusltText + \
                    '\n>>>!!!<<<\nMad ich brauche deine Hilfe! Bitte Bitte lass mich nicht allein. \n\nDas ist mein Fehler:\n\n' + exp

            self.__WriteTestResultFile(ReusltText)

            if Type == '':
                ReusltText = ReusltText + "</p>\n" + "<h2>Ihr TC-Team</h2>"

                for indexItem in range(1, len(self.TestResultObject), 1):
                    if self.TestResultObject[indexItem][1] == '>!<' or self.TestResultObject[indexItem][1] == ':-(':
                        self.SendEmail(
                            ReusltText, to_addr=self.to_Address_list)
                        break

            self.TestResultObject.clear()
            ReusltText = ''

        except Exception as exp:
            Log.Warning("Ergebnisprotokoll: " + str(exp))

        finally:
            pass


# --
# ...
# --

    def GetDeliveryAddress(self, DeliveryGroupe):

        try:

            DeliveryGroupeListe = DeliveryGroupe.split(",")

            for Index in range(0, len(DeliveryGroupeListe), 1):
                DeliveryGroupe = DeliveryGroupeListe[Index]

                if self.to_Adddress.find(DeliveryGroupe) == -1:
                    self.to_Adddress = self.to_Adddress + ', ' + DeliveryGroupe

                    if DeliveryGroupe == 'Admin':
                        self.to_Address_list = self.Default_Admin_Address + ', ' + self.to_Address_list
                        self.to_Address_list = self.Default_Dev_Address + ', ' + self.to_Address_list

                    if DeliveryGroupe == 'Dev':
                        self.to_Address_list = self.Default_Dev_Address + ', ' + self.to_Address_list

                    if DeliveryGroupe == "BugAlert":
                        # self.to_Address_list = self.Default_Admin_Address + ', ' + self.to_Address_list
                        self.to_Address_list = self.Default_Dev_Address + ', ' + self.to_Address_list
                        self.to_Address_list = self.TC_BugAlert_Address + ', ' + self.to_Address_list

        except Exception as exp:
            Log.Warning("__GetDeliveryAddress: " + str(exp))
# --
# ...
# --

    def __WriteTestResultFile(ReusltText):

        try:

            ReusltText = ReusltText.replace("<h1>", "")
            ReusltText = ReusltText.replace("</h1>", "")
            ReusltText = ReusltText.replace("<h2>", "")
            ReusltText = ReusltText.replace("</h2>", "")
            ReusltText = ReusltText.replace("<h3>", "")
            ReusltText = ReusltText.replace("</h3>", "")
            ReusltText = ReusltText.replace("<p>", "")
            ReusltText = ReusltText.replace("</p>", "")
            ReusltText = ReusltText.replace(".", " ")

            aqFile.WriteToTextFile(
                self.TestResult_Address, ReusltText, aqFile.ctANSI, True)

            TempFile = open(self.ServerResult_Address, 'a')
            TempFile.write(4*'\n' + ReusltText)
            TempFile.close()

        except Exception as exp:
            Log.Warning("WriteTestResultFile: " + str(exp))
# --
# ...
# --

    def SolveChar(Message):
        try:

            Message = Message.replace("Ö", "O")
            Message = Message.replace("ö", "o")
            Message = Message.replace("Ü", "U")
            Message = Message.replace("ü", "u")
            Message = Message.replace("Ä", "A")
            Message = Message.replace("ä", "a")
            Message = Message.replace("ß", "ss")

            return Message

        except Exception as exp:
            Log.Message('SolveChar: ' + str(exp))
# --
# ...
# --

    def SolveWort(Message):

        try:

            Message = Message.replace('WinFormsObject', '')
            Message = Message.replace('SimpleButton', '')
            Message = Message.replace('WPFObject', '')
            Message = Message.replace('"', '')
            Message = Message.replace('(', '')
            Message = Message.replace(')', '')
            Message = Message.replace(':', '')
            Message = Message.replace(', ', '')
            Message = Message.replace('1', '')
            Message = Message.replace('2', '')
            Message = Message.replace('3', '')

            return Message

        except Exception as exp:
            Log.Message('SolveWort: ' + str(exp))
# --
# ...
# --

    def GetClassName(self, TestName='', Mode='', MoreInfo=''):

        try:

            returnValue = inspect.stack()[2][3] + ' ' + Mode

            if MoreInfo == '':
                if returnValue[0:2] == '__':
                    returnValue = returnValue[2:]

            if TestName != '':
                returnValue = TestName

            return returnValue

        except Exception as exp:
            Log.Warning("Name: " + str(exp))
# --
# ...
# --

    def GetMethodName(self):

        try:

            returnValue = inspect.stack()[2][3]

            return returnValue

        except Exception as exp:
            Log.Warning("GetMethodName: " + str(exp))
# --
# ...
# --

    def GetDocument(self, document):

        try:

            return self.GetMethodName() + ', ' + document

        except Exception as exp:
            Log.Warning("GetDocument: " + str(exp))
# --
# ...
# --

    def GetPlatform(self, TestName='', Mode='', MoreInfo='') -> str:

        try:

            Platform = 'TestExecute'

            if WMI.ProcessExists('TestComplete.exe'):
                Platform = 'TestComplete'

            return Platform

        except Exception as exp:
            Log.Warning("GetPlatform: " + str(exp))
# --
# ...
# --

    def SetObjectsLog(self):

        try:

            self.ObjectsLog = self.ConfigTestCaseDatei(self, 'TC_Sample_Datei_Directory') + '\\' + self.GetPlatform() + '_ObjectsLog.txt'

        except Exception as exp:
            Log.Warning("SetObjectsLog: " + str(exp))
# --
# ...
# --

    def Exception_In_Class_Methode_Operation(self, Object_0=None, Operate_0='Close', Messagbox_0=False, YesOrNo_0='YES', Mode='', Empfanger='', TypeOfResultObject='Info', MoreInfo=''):

        try:

            if Object_0 != None:
                if Operate_0 == 'Close':
                    while Object_0.Exists:
                        self.Close(Object_0)

                        if Messagbox_0:
                            self.MessagboxManager(YesOrNo=YesOrNo_0)

                elif Operate_0 == 'ClickButton':
                    self.ClickButton(Object_0)

                    if Messagbox_0:
                        self.MessagboxManager(YesOrNo=YesOrNo_0)

            self.TestResult(Mode=Mode, Empfanger=Empfanger,
                            TypeOfResultObject=TypeOfResultObject,  MoreInfo=MoreInfo)

        except Exception as exp:
            self.TestResult(Mode=Mode, Empfanger=Empfanger, TypeOfResultObject='Info',
                            MoreInfo='Exception IM Exception!!!!!!!!')
