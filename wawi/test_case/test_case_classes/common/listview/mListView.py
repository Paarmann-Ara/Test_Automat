from Exception.mException import cException
from WAWi.Core.Base.mBase import cBase
from WAWi.TestCase.Keys.Common.ListView import mListViewEditor
from WAWi.Setting.TestCase.mTestCaseConfig import cTestCaseConfig

# --
# ...
# --


class cListView(cBase):
    def __init__(self, Mode='Standard', QProjection="USE eazybusiness;SELECT COUNT(1) FROM ", QSource='Unbekannt', QCondition="", Empfanger='Admin', War='Unbekannt', Ist='Unbekannt', CheckList_0_Ar=[], CheckList_0_Ar_Antwort=[], CheckList_0_DIC_Antwort={}, CheckList_0_DB_Att=[], CheckList_0_Ar_Ext=[], CheckList_0_DB_Att_Ext=[], ListView=None, T1=0, T2=0, Info=' (I have no info) '):

        super().__init__(Mode)
        self.Mode = Mode
        self.IsInTestList = False
        self.Help = ''
        self.QSource = QSource
        self.Empfanger = Empfanger
        self.War = War
        self.Ist = Ist
        self.QProjection = QProjection
        self.QCondition = QCondition
        self.CheckList_0_Ar = CheckList_0_Ar
        self.CheckList_0_Ar_Antwort = CheckList_0_Ar_Antwort
        self.CheckList_0_DIC_Antwort = CheckList_0_DIC_Antwort
        self.CheckList_0_DB_Att = CheckList_0_DB_Att
        self.CheckList_0_Ar_Ext = CheckList_0_Ar_Ext
        self.CheckList_0_DB_Att_Ext = CheckList_0_DB_Att_Ext

        self.ListView = ListView
        self.T1 = T1
        self.T2 = T2
        self.Info = Info

        if Mode == 'Test':
            self.ListView = ListView


# --
# ...
# --


    def ListView_Single_WithColumnsAdjust(self):

        try:

            self.TestResult(TypeOfResultObject='Information')

            if Config.IsListViewCheck:
                self.__Check_ListView_With()

            Delay(self.getTime('SmallTime'))

        except Exception as exp:
            self.TestResult(Mode=self.Mode, Empfanger=self.Empfanger,
                            TypeOfResultObject='Info', MoreInfo=str(exp))
# --
# ...
# --

    def ListView_Single_WithoutColumnsAdjust(self):

        try:

            self.TestResult(TypeOfResultObject='Information')

            if Config.IsListViewCheck:
                self.__Check_ListView_Without()

            Delay(self.getTime('SmallTime'))

        except Exception as exp:
            self.TestResult(Mode=self.Mode, Empfanger=self.Empfanger,
                            TypeOfResultObject='Info', MoreInfo=str(exp))
# --
# ...
# --

    def LogingTime(self):
        
        try:

            self.__LogingTime(self.T1, self.T2, self.Info)

        except Exception as exp:
            self.TestResult(Mode=self.Mode, Empfanger=self.Empfanger,
                            TypeOfResultObject='Info', MoreInfo=str(exp))
# --
# ...
# --

    def __Check_ListView_With(self):

        try:

            self.WaitForAvailablity(self.ListView)

            Temp = mListViewEditor.cListViewEditor(self.Mode)
            Temp.ListView = self.ListView
            Temp.ListViewColumns_Anpassen()

            self.__Check_ListView_Without()

        except Exception as exp:
            self.TestResult(Mode=self.Mode, Empfanger=self.Empfanger,
                            TypeOfResultObject='Info', MoreInfo=str(exp))
# --
# ...
# --

    def __Check_ListView_Without(self):

        try:

            self.WaitForAvailablity(self.ListView)

            IndexItem = 0
            HeaderCount = 0
            HeaderListView = None

            if (aqObject.IsSupported(self.ListView, 'HeaderControl') and aqObject.IsSupported(self.ListView, 'Header')):
                if aqObject.IsSupported(self.ListView.Header, 'wItemCount'):
                    HeaderCount = self.ItemCount(self.ListView.Header)

                HeaderListView = self.ListView.Header

            elif aqObject.IsSupported(self.ListView, 'HeaderControl'):
                if aqObject.IsSupported(self.ListView.HeaderControl, 'wItemCount'):
                    HeaderCount = self.ItemCount(self.ListView.HeaderControl)

                HeaderListView = self.ListView.HeaderControl

            elif aqObject.IsSupported(self.ListView, 'Header'):
                if aqObject.IsSupported(self.ListView.Header, 'wItemCount'):
                    HeaderCount = self.ItemCount(self.ListView.Header)

                HeaderListView = self.ListView.Header

            if HeaderListView == None:
                return

            self.WaitForAvailablity(HeaderListView)

            for IndexItem in range(IndexItem, HeaderCount, 1):

                T1 = self.WaitForNow()
                self.__ClickOnListViewHeader(IndexItem, 0)
                self.__LogingTime(T1, self.WaitForNow(), str(
                    HeaderListView.wItem[IndexItem]))

                Delay(100)

                self.__ClickOnListViewHeader(IndexItem, 0)

                if aqObject.IsSupported(self.ListView, 'HScroll'):
                    if self.ListView.HScroll.Max > 0 and self.ListView.HScroll.Pos > 0:
                        self.ListView.HScroll.Pos = 0

                if aqObject.IsSupported(self.ListView, 'VScroll'):
                    if self.ListView.VScroll.Max > 0 and self.ListView.VScroll.Pos > 0:
                        self.ListView.VScroll.Pos = 0

                ColumnName = HeaderListView.wItem[IndexItem]
                IndexItem += IndexItem

        except Exception as exp:
            self.TestResult(Mode=self.Mode, Empfanger=self.Empfanger,
                            TypeOfResultObject='Info', MoreInfo=str(exp))
# --
# ...
# --

    def __ClickOnListViewHeader(self, TargetIndex0, TargetIndex1):

        try:

            self.WaitForAvailablity(self.ListView)

            if (aqObject.IsSupported(self.ListView, 'HeaderControl') and aqObject.IsSupported(self.ListView, 'Header')):
                self.ListView.Header.ClickItem(TargetIndex0, TargetIndex1)

            elif aqObject.IsSupported(self.ListView, 'HeaderControl'):
                self.ListView.HeaderControl.ClickItem(
                    TargetIndex0, TargetIndex1)

            elif aqObject.IsSupported(self.ListView, 'Header'):
                self.ListView.Header.ClickItem(TargetIndex0, TargetIndex1)

        except Exception as exp:
            self.TestResult(Mode=self.Mode, Empfanger=self.Empfanger,
                            TypeOfResultObject='Info', MoreInfo=str(exp))
# --
# ...
# --

    def __LogingTime(self, T1, T2, Info=' (I have no info) '):

        try:

            DT = T2 - T1
            M = (DT.days * 86400000) + (DT.seconds * 1000) + \
                (DT.microseconds / 1000)
            self.DBC("LogTime", '', '', Info, str(M), "Sorting for column " +
                     Info + " take " + str(M) + " ms", SQLHost=Config.AQCHost)

            self.TestResult(Mode=self.Mode, Empfanger=self.Empfanger, FensterZeit=[
                            IntToStr(M), '(C)'], QSource=Info)

        except Exception as exp:
            self.TestResult(Mode=self.Mode, Empfanger=self.Empfanger,
                            TypeOfResultObject='Info', MoreInfo=str(exp))
