from AWAWiTestCase.Objects.Common.Startup import Objects_Steuervalidierung
from WAWi.Core.Base import mBase
from Exception.mException import cException
from WAWi.TestCase.Keys.Common.ListView.mListView import cListView

#--
#...
#--
class cSteuervalidierung(mBase.cBase):
        def __init__(self	,Mode = 'Standard'
                            ,QProjection                                                                                                        = "USE eazybusiness;SELECT COUNT(1) FROM "
                            ,QSource                                                                                                            = 'Unbekannt'
                            ,QCondition                                                                                                         = ""
                            ,Empfanger                                                                                                          = 'Admin'
                            ,War                                                                                                                = 'Unbekannt'
                            ,Ist                                                                                                                = 'Unbekannt'
                            
                            ,CheckList_0_Ar                                                                                                     = ['BenutzerCount']
                            ,CheckList_0_Ar_Antwort                                                                                             = []
                            ,CheckList_0_DIC_Antwort                                                                                            = {}
                            ,CheckList_0_DB_Att                                                                                                 = ['BenutzerCount']
                            ,CheckList_0_Ar_Ext                                                                                                 = []
                            ,CheckList_0_DB_Att_Ext                                                                                             = []
                            ):
			
                            
                 
                super().__init__(Mode)           
                self.Mode                                              						        							                = Mode
                self.IsInTestList                                     						        							                = False
                self.Help                                             						        							                = ''
                self.QSource                                                                                                                    = QSource
                self.Empfanger                                                                                                                  = Empfanger				
                self.War                                                                                              		                    = War						
                self.Ist                                                                                              		                    = Ist	 
                self.QProjection																							                    = QProjection
                self.QCondition    																							                    = QCondition 
                
                self.CheckList_0_Ar      																							            = CheckList_0_Ar   
                self.CheckList_0_Ar_Antwort      																							    = CheckList_0_Ar_Antwort   
                self.CheckList_0_DIC_Antwort                                                                                                    = CheckList_0_DIC_Antwort   
                self.CheckList_0_DB_Att      																							        = CheckList_0_DB_Att   
                self.CheckList_0_Ar_Ext      																							        = CheckList_0_Ar_Ext
                self.CheckList_0_DB_Att_Ext   																							        = CheckList_0_DB_Att_Ext
                
									
									
                if Mode == 'Test':
                        pass
                        
                        
                        
                #Object, Type of check, TabObject, TabName, Return_TabObject, Return_TabName
                #Object, Type of check-Column
                self.CheckPoint_Dic = {
#                'BenutzerCount'                                                                                                                 : (Objects_NeuerBenutzer.lvBenutzer, 'Count'), 
                }                             
   

           
#--
#...
#--

        def Steuervalidierung_Test(self):
                
                try:
                        self.Sleep(self, self.GetDefinedTime(self, 'SmallTime'))
                        
                        self.TestResult(TypeOfResultObject = 'Information')        
                        
                        self.Setup()
                        
                        self.__Test()
                        
                        self.sleep(self.getTime('SmallTime'))
                
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp))
#--
#...
#--
        def Setup(self, Methode = '', ChangeCheckListAndAntwortMethode = ''):
            
                try:
                                
                        self.Prerequisite()
            
                        self.AfterSetup()
                        
                        self.ChangeCheckListAndAntwortOrUseCheckListExt(ChangeCheckListAndAntwortMethode)
                                         
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp)) 
                        raise mException.cSetup()
#--
#...
#--
        def AfterSetup(self):
            
                try:
                        pass
                        
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp))
                        raise mException.cAfterSetup()
#--
#...
#--
        def ChangeCheckListAndAntwortOrUseCheckListExt(self, ChangeCheckListAndAntwortMethode = ''):
            
                try:
                        
                        if ChangeCheckListAndAntwortMethode == '':
                                pass
                                        
                                        
                        self.CheckList_0_DIC_Antwort = {Item[1] : Item[0] for Item in self.CheckList_0_Ar_Antwort}                                
                        
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp))
                        raise mException.cChangeCheckListAndAntwortOrUseCheckListExt()
#--
#...
#--
        def __CheckPointSelector(self, NoShow = [], IsNotSingleMode = True, ChangeCheckListAndAntwortMethode = ''):
            
                try:                      
                
                        if ChangeCheckListAndAntwortMethode != '':
                                self.ChangeCheckListAndAntwortOrUseCheckListExt(ChangeCheckListAndAntwortMethode)

                        Temp = mCheckPointSelector.cCheckPointSelector(self.Mode)
                        Temp.CheckList_0_Ar = self.CheckList_0_Ar
                        Temp.CheckList_0_Ar_Antwort = self.CheckList_0_Ar_Antwort
                        Temp.CheckList_0_DIC_Antwort = self.CheckList_0_DIC_Antwort
                        Temp.CheckList_0_DB_Att = self.CheckList_0_DB_Att
                        Temp.CheckList_0_Ar_Ext = self.CheckList_0_Ar_Ext
                        Temp.CheckPoint_Dic = self.CheckPoint_Dic
                        Temp.IsNotSingleMode = IsNotSingleMode
                        Temp.NoShow = NoShow
                        Temp.CheckPointSelector()
                		                
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp))                         
                        raise mException.cCheckPointSelector()                        
#--
#...
#--
        def __Test(self):
                Options.Run.Timeout = self.getTime('VeryLargTime');
  
                try:
                
                        if self.QSource == 'Unbekannt':
                                self.QSource = 'dbo.tRechtBenutzerGruppe'
                                
                        if self.QCondition == '':
                                self.QCondition = " "
								
                        self.War = self.DBC(SQLCommand = self.QProjection + self.QSource + self.QCondition, Type = 'OnePropertyQRY')
                        
                        if self.WaitForAvailablity(Objects_Steuervalidierung.Form):

                                Temp = mListView.cListView(self.Mode)
                                Temp.ListView = Objects_Steuervalidierung.lv
                                Temp.ListView_Single_WithColumnsAdjust()
                                
                                #time.sleep(self.getTime('StartupWarnung'))
                                #Temp = mSteuerverwaltung.cSteuerverwaltung()
                                #Temp.Steuerverwaltung_behobenFehler()
                                #Check_Steuerverwaltung.Steuerverwaltung_behobenFehler()
                                #time.sleep(self.getTime('StartupWarnung'))
                
                                FensterZeit = self.FensterZeit(Objects_Steuervalidierung.btnSchliessen, Objects_Steuervalidierung.Form)

                                self.Ist = self.DBC(SQLCommand = self.QProjection + self.QSource + self.QCondition, Type = 'OnePropertyQRY')   
                        
                                self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, FensterZeit = FensterZeit, QSource = self.QSource, war = self.War, ist = self.Ist)                       

                                time.sleep(self.getTime('StartupWarnung'))
                                                
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp))
                        Objects_Steuervalidierung.Form.Close()
                        raise mException.cReturn()