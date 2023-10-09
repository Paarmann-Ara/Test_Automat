from AWAWiCore.Base.mBase import cBase
from WAWi.TestCase.Objects.Common.ListView import Objects_ListViewEditor
from WAWi.TestCase.Objects.Common.WAWI import Objects_ContextMenu
from Exception.mException import cException

# --
# ...
# --


class cListViewEditor(cBase):
    def __init__(self, Mode='Standard', QProjection="USE eazybusiness;SELECT COUNT(1) FROM ", QSource='Unbekannt', QCondition="", Empfanger='Admin', War='Unbekannt', Ist='Unbekannt', CheckList_0_Ar=[], CheckList_0_Ar_Antwort=[], CheckList_0_DIC_Antwort={}, CheckList_0_DB_Att=[], CheckList_0_Ar_Ext=[], CheckList_0_DB_Att_Ext=[], IsAlleAktive=True, IsAlleDeAktive=False, ListView=None, Header=None):

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

        self.IsAlleAktive = IsAlleAktive
        self.IsAlleDeAktive = IsAlleDeAktive
        self.ListView = ListView
        self.Header = Header

        if Mode == 'Test':
            self.IsAlleAktive = IsAlleAktive
            self.IsAlleDeAktive = IsAlleDeAktive
            self.ListView = ListView
            self.Header = Header


# --
# ...
# --

    def ListViewColumns_Anpassen(self):

        try:

            self.TestResult(TypeOfResultObject='Information')

            self.__ListViewColumns_Anpassen()

            Delay(self.getTime('SmallTime'))

        except Exception as exp:
            self.TestResult(Mode=self.Mode, Empfanger=self.Empfanger,
                            TypeOfResultObject='Info', MoreInfo=str(exp))
# --
# ...
# --

    def __ListViewColumns_Anpassen(self):
        Options.Run.Timeout = self.getTime()

        try:

            if self.QSource == 'Unbekannt':
                self.QSource = 'dbo.tArtikel'

            if self.QCondition == '':
                self.QCondition = " "

            # self.War = self.DBC(SQLCommand = self.QProjection + self.QSource + self.QCondition, Type = 'OnePropertyQRY')

            Index = 0

            if aqObject.IsSupported(self.ListView, 'HScroll'):
                if self.ListView.HScroll.Max > 0 and self.ListView.HScroll.Pos > 0:
                    self.ListView.HScroll.Pos = 0

            Delay(500)

            if self.ListView.ClrClassName == 'TableView' or self.ListView.ClrClassName == 'SqlListViewControl':

                IndexObjectCounter = 1

                for IndexObjectCounter in range(1, 5):
                    HeaderControl = self.ListView.WPFObject(
                        "GridColumnHeader", "", IndexObjectCounter)
                    if self.WaitForAvailablity(HeaderControl):
                        break
                    IndexObjectCounter += 1
                else:
                    return

                if aqObject.IsSupported(HeaderControl, 'ClickR'):
                    self.ClickR(HeaderControl, IsJustClickR=True)

                    if not self.WaitForAvailablity(Objects_ContextMenu.ColumnControl_0):
                        return

                    self.Click(Objects_ContextMenu.SpalteneditorAnzeigen)

                    mException.WindowDetector(self.__module__)

                    self.WaitForAvailablity(Objects_ListViewEditor.Form)

                    self.ClickButton(
                        Objects_ListViewEditor.btnMoveAllToInvisibleColumns, Condition=self.IsAlleDeAktive)

                    self.ClickButton(
                        Objects_ListViewEditor.btnMoveAllToVisibleColumns, Condition=self.IsAlleAktive)

                    FensterZeit = self.FensterZeit(
                        Objects_ListViewEditor.btnSpeichern, Objects_ListViewEditor.Form)

            elif self.ListView.ClrClassName == 'GridControl':

                HeaderControl = self.ListView.WPFObject(
                    "TreeListView").WPFObject("GridColumnHeader", "", 1)

                if not self.WaitForAvailablity(HeaderControl):
                    return

                if aqObject.IsSupported(HeaderControl, 'ClickR'):
                    self.ClickR(HeaderControl, IsJustClickR=True)

                    if not self.WaitForAvailablity(Objects_ContextMenu.ColumnControl_0):
                        return

                    self.Click(Objects_ContextMenu.SpalteneditorAnzeigen)

                    mException.WindowDetector(self.__module__)

                    self.WaitForAvailablity(Objects_ListViewEditor.Form)

                    self.ClickButton(
                        Objects_ListViewEditor.btnMoveAllToInvisibleColumns, Condition=self.IsAlleDeAktive)

                    self.ClickButton(
                        Objects_ListViewEditor.btnMoveAllToVisibleColumns, Condition=self.IsAlleAktive)

                    FensterZeit = self.FensterZeit(
                        Objects_ListViewEditor.btnSpeichern, Objects_ListViewEditor.Form)

            elif aqObject.IsSupported(self.ListView, 'Header') and aqObject.IsSupported(self.ListView, 'HeaderControl'):

                HeaderControl = self.ListView.WPFObject(
                    "GridColumnHeader", "", 1)

                if not self.WaitForAvailablity(HeaderControl):
                    return

                if aqObject.IsSupported(HeaderControl, 'ClickR'):
                    self.ClickR(HeaderControl, IsJustClickR=True)

                    if not self.WaitForAvailablity(Objects_ContextMenu.ColumnControl_0):
                        return

                    self.Click(Objects_ContextMenu.SpalteneditorAnzeigen)

                    mException.WindowDetector(self.__module__)

                    self.WaitForAvailablity(Objects_ListViewEditor.Form)

                    self.ClickButton(
                        Objects_ListViewEditor.btnMoveAllToInvisibleColumns, Condition=self.IsAlleDeAktive)

                    self.ClickButton(
                        Objects_ListViewEditor.btnMoveAllToVisibleColumns, Condition=self.IsAlleAktive)

                    FensterZeit = self.FensterZeit(
                        Objects_ListViewEditor.btnSpeichern, Objects_ListViewEditor.Form)

            elif aqObject.IsSupported(self.ListView, 'HeaderControl'):

                HeaderControl = self.ListView.HeaderControl

                if aqObject.IsSupported(HeaderControl, 'Height'):
                    if HeaderControl.Height < 1:
                        return

                ContextMenu = Objects_ContextMenu.Generalcms_0

                if not self.WaitForAvailablity(HeaderControl):
                    if aqObject.IsSupported(self.ListView, 'wHeader'):
                        HeaderControl = self.ListView.wHeader
                    else:
                        return

                if aqObject.IsSupported(HeaderControl, 'ClickItemR'):
                    HeaderControl.ClickItemR(0)
                    if not self.WaitForAvailablity(ContextMenu, MCounter=3):
                        if not self.WaitForAvailablity(Objects_ContextMenu.Generalcms_0):
                            return
                        else:
                            ContextMenu = Objects_ContextMenu.ContextMenu_0

                    Position = self.FindLastItemPositionInContextMenu(
                        ContextMenu)

                    self.Click(ContextMenu, Position[0], Position[1])

                    mException.WindowDetector(self.__module__)

                    self.WaitForAvailablity(
                        Objects_ListViewEditor.ColumnDialog_Header)
                    self.Click(Objects_ListViewEditor.ColumnDialog_Header)

                    FensterZeit = self.FensterZeit(
                        Objects_ListViewEditor.ColumnDialog_btnOk, Objects_ListViewEditor.ColumnDialog)

            elif aqObject.IsSupported(self.ListView, 'Header'):

                HeaderControl = self.ListView.Header
                ContextMenu = Objects_ContextMenu.Generalcms_0

                if not self.WaitForAvailablity(HeaderControl):
                    return

                if aqObject.IsSupported(HeaderControl, 'ClickItemR'):
                    HeaderControl.ClickItemR(0)

                    if not self.WaitForAvailablity(ContextMenu, MCounter=3):
                        if not self.WaitForAvailablity(Objects_ContextMenu.Generalcms_0):
                            return
                        else:
                            ContextMenu = Objects_ContextMenu.Generalcms_0

                    Position = self.FindFirstItemPositionInContextMenu(
                        ContextMenu)
                    self.Click(ContextMenu, Position[0], Position[1])

                    mException.WindowDetector(self.__module__)

                    self.WaitForAvailablity(
                        Objects_ListViewEditor.JTL_Column_Dialog)

                    RowCount = self.ItemCount(
                        Objects_ListViewEditor.lvJTLHeadersAvailable)

                    for Index in range(0, RowCount):
                        self.ClickItem(
                            Objects_ListViewEditor.lvJTLHeadersAvailable, Index)
                        self.ClickButton(
                            Objects_ListViewEditor.btnJTL_Column_MoveAllToVisibleColumns)

                    FensterZeit = self.FensterZeit(
                        Objects_ListViewEditor.btnJTL_Column_Speichern, Objects_ListViewEditor.JTL_Column_Dialog, Messagbox='YES')

            elif self.ListView.ClrClassName == 'TreeListView':

                DevExpress.Xpf.Grid.TreeListView

            self.Header = HeaderControl

            self.Ist = self.DBC(SQLCommand=self.QProjection +
                                self.QSource + self.QCondition, Type='OnePropertyQRY')

            self.TestResult(Mode=self.Mode, Empfanger=self.Empfanger,
                            FensterZeit=FensterZeit, QSource=self.QSource, war=self.War, ist=self.Ist)

        except Exception as exp:
            self.TestResult(Mode=self.Mode, Empfanger=self.Empfanger,
                            TypeOfResultObject='Info', MoreInfo=str(exp))
            Objects_ListViewEditor.Form.Close()
            Objects_ListViewEditor.ColumnDialog.Close()
