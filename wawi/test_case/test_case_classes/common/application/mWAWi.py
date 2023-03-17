from AWAWiSetting import Config
import datetime
import mBase
import mDBOperation
import mException
import mListView
import mPasswordChangerInLogin
import mRestoreDB
import mSteuervalidierung
import mSqlUpdateChangelog
import Objects_WAWi
import smtplib
import mLogin
                        
#--
#...
#--
class cWAWi(mBase.cBase):
        def __init__(self   ,Mode = 'Standard'
                            ,QProjection                                                                                                        = "USE eazybusiness;SELECT COUNT(1) FROM "
                            ,QSource                                                                                                            = 'Unbekannt'
                            ,QCondition                                                                                                         = ""
                            ,Empfanger                                                                                                          = 'Admin'
                            ,War                                                                                                                = 'Unbekannt'
                            ,Ist                                                                                                                = 'Unbekannt'
                            
                            ,CheckList_0_Ar                                                                                                     = []
                            ,CheckList_0_Ar_Antwort                                                                                             = []
                            ,CheckList_0_DIC_Antwort                                                                                            = {}
                            ,CheckList_0_DB_Att                                                                                                 = []
                            ,CheckList_0_Ar_Ext                                                                                                 = []
                            ,CheckList_0_DB_Att_Ext                                                                                             = []):

                            
                            
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
        
#--
#...
#--
        def ShutdownWAWi(self):
            
                try:  
                                       
                        while Sys.WaitProcess('JTL-Wawi').Exists:
                                Sys.WaitProcess('JTL-Wawi').Terminate()
                                Delay(2500)
                                
                                if Sys.WaitProcess('JTL-Wawi').Exists:
                                        Sys.WaitProcess('JTL-Wawi').Terminate()
                                        Delay(2500)
                                else:
                                        break
                                
                                mException.WindowDetector(self.__module__)
                                if Objects_WAWi.Parent_ToolsBar.Exists:
                                        Objects_WAWi.Parent_ToolsBar.Terminate()
                                        Log.Message(" * AQC of WAWi says: I Terminate the WAWi at: " + str(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + " * ") 
                                        Delay(2500)
                                self.MessagboxManager()
                        
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp)) 
                        raise mException.cReturn()                                
#--
#...
#--    
        def RunWAWi(self):
                Options.Run.Timeout = self.GetTimes('RegularTime')
                
                try:
                
                        if Objects_WAWi.Absturz_btnSchlie_en.Exists:
                                Objects_WAWi.Absturz_btnSchlie_en.Click()
                        
                        while Sys.WaitProcess('JTL-Wawi').Exists:
                                Log.Message(" * AQC of WAWi says: I close the WAWi in Runing at : " + str(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + " * ")
                                
                                if self.MessagboxManager():
                                        self.MessagboxManager()
                                        
                                        if self.MessagboxManager():
                                                Sys.WaitProcess('JTL-Wawi').Terminate()
                                                Delay(2200)

                                Objects_WAWi.Parent_ToolsBar.Close()
                                self.MessagboxManager()
                                
                                Delay(2500)
                                
                                mException.WindowDetector(self.__module__)
                                
                                if Objects_WAWi.Parent_ToolsBar.Exists:
                                        Sys.WaitProcess('JTL-Wawi').Terminate()
                                        Log.Message(" * AQC of WAWi says: I Terminate the WAWi in Runing at : " + str(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + " * ") 
                                        self.MessagboxManager()
                                        Delay(2500)
                                self.MessagboxManager()
                        self.PrepareEazybusiness()
                        self.StartWAWi()
                        self.Login()
                        
                        Delay(1000)
                        
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp)) 
                        raise mException.cReturn()
#--
#...
#--
        def PrepareEazybusiness(self):
                Options.Run.Timeout = self.GetTimes(500);
  
                try:
                
                        Temp = mDBOperation.cDBOperation()
                        while Temp.DBC('AC', SQLHost = Config.SQLHost, Type = 'OnePropertyQRY') != '0':
                                Temp.DBC('MU', SQLHost = Config.SQLHost, Type = 'Command')
                                Delay(3800)
                                
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp)) 
                        raise mException.cReturn()
#--
#...
#--
        def StartWAWi(self):
                Options.Run.Timeout = self.GetTimes(500);
  
                try:
                
                        import Objects_DBTools
                        
                        ExceptionCounter = 0
                        
                        TestedApps.JTL_WAWi.Run(1, True)
                        Log.Message(" * AQC of WAWi says: I Start the WAWi at: " + str(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + " * ") 

                        while not ImageRepository.WAWiStartUp.StartupIcon.Exists():
                                Delay(50)
                                
                                Temp = mLogin.cLogin()
                                if Temp.Login_IsThere():
                                        break
                                        
                                if Aliases.JTL_WAWi.ExportVorlage_0.Window("Static", "Für dieses Profil wurde keine Eazybusiness Datenbank gefunden. Soll diese erstellt werden?", 1).Exists or Objects_DBTools.Form.Exists:
                                        self.MessagboxManager()
                                        self.DBToolMainManager()
                                        
                                ExceptionCounter += 1

                                if ExceptionCounter > 30:
                                        mException.WindowDetector(self.__module__)
                                        ExceptionCounter = 0
                                        break
                                
                        while ImageRepository.WAWiStartUp.StartupIcon.Exists():
                                Delay(50)
                                
                                Temp = mLogin.cLogin()
                                if Temp.Login_IsThere():
                                        break
                                
                                if Aliases.JTL_WAWi.ExportVorlage_0.Window("Static", "Für dieses Profil wurde keine Eazybusiness Datenbank gefunden. Soll diese erstellt werden?", 1).Exists or Objects_DBTools.Form.Exists:
                                        self.MessagboxManager()
                                        self.DBToolMainManager()

                        
                        if Aliases.JTL_WAWi.ExportVorlage_0.Window("Static", "Für dieses Profil wurde keine Eazybusiness Datenbank gefunden. Soll diese erstellt werden?", 1).Exists or Objects_DBTools.Form.Exists:
                                self.MessagboxManager()
                                self.DBToolMainManager()
                                
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp)) 
                        raise mException.cReturn()
#--
#...
#--
        def ExitError0(self):
                Options.Run.Timeout = self.GetTimes('ExitError0')
                Delay(2500)
                return
#--
#...
#--
        def FinishWAWi(self):
                Options.Run.Timeout = self.GetTimes('LargTime');
                self.GoToToolsbar('Artikel')
#--
#...
#--
        def Login(self):
                Options.Run.Timeout = self.GetTimes('MediumTime')
                
                try:
                
                        Temp = mLogin.cLogin()
                        Temp.Login_Test()

                        Delay(self.GetTimes('StartupWarnung'))
                        
                        import mJTL_Einrichten
                        Temp = mJTL_Einrichten.cJTL_Einrichten()
                        if Temp.JTL_EinrichtenManager():
                                Delay(self.GetTimes('StartupWarnung')*3)
                                Temp = mLogin.cLogin()
                                if Temp.Login_IsThere():
                                        Temp.Login_Test()
                        
                        Options.Run.Timeout = self.GetTimes('SmallTime');
                        self.MessagboxManager('WaitToFinish')
                        
                        Temp = mRestoreDB.cRestoreDB()
                        if Temp.RestoreDB_Test():
                                Delay(self.GetTimes('StartupWarnung'))
                                Temp = mLogin.cLogin()
                                if Temp.Login_IsThere():
                                        Temp.Login_Test()
                        
                        if self.RechtVerwaltung():                               
                                self.RechtVerwaltung()
                                Temp = mLogin.cLogin()
                                if Temp.Login_IsThere():
                                        Temp.Login_Test()
        
                        Temp = mSqlUpdateChangelog.cSqlUpdateChangelog()
                        Temp.Update_Test()
                        
                        Delay(self.GetTimes('StartupWarnung'))
                        self.MessagboxManager()
                        self.DefinePrinter()
                        self.MessagboxManager()
                        
                        Temp = mSteuervalidierung.cSteuervalidierung()
                        Temp.Steuervalidierung_Test()
                        
                        self.MessagboxManager()
                        
                        if Config.IsSolveRevisionBugInWAWi:
                                self.SolveWAWiRevisionBug()
                        
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp)) 
                        raise mException.cReturn()
#--
#...
#--                              
        def DefinePrinter(self):
                Options.Run.Timeout = self.GetTimes('SmallTime');
        
                try:
                        
                        import Objects_Drucker
                        import mDrucker
                        
                        if Objects_Drucker.Form.Exists:
                                Temp = mDrucker.cDrucker(self.Mode)
                                Temp.anlegen()
                
                        Delay(self.GetTimes('StartupWarnung'))
                
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp)) 
                        raise mException.cReturn()                
#--
#...
#--
        def RechtVerwaltung(self):
                Options.Run.Timeout = self.GetTimes('SmallTime')
        
                try:
                
                        import Objects_Benutzer
                        import mNeueBenutzer
                
                        if self.WaitForAvailablity(Objects_Benutzer.Form, MCounter = 4, IsReport = False):
                                Objects_Benutzer.lv.ClickItem(Config.WAWizugang_Benutzername)
                                
                                self.ClickButton(Objects_Benutzer.btnBearbeiten)
                                
                                Temp = mNeueBenutzer.cNeueBenutzer(self.Mode)
                                Temp.Neue_Benutzer_Beaschtaetigen()
                                
                                self.ClickButton(Objects_Benutzer.btnSchlissen, delay = 1000)
                
                                Delay(self.GetTimes('StartupWarnung'))
                                return True

                        Temp = mPasswordChangerInLogin.cPasswordChangerInLogin()
                        return Temp.PasswordChangerInLogin_Test()
                
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp)) 
                        raise mException.cReturn()                                     
#--
#...
#--  
        def DBToolMainManager(self):
                Options.Run.Timeout = self.GetTimes('RegularTime')
                
                try:
                
                        import mDBTools
                        Temp = mDBTools.cDBTools()
                        Temp.DBToolMainManager
                                        
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp)) 
                        raise mException.cReturn() 
#--
#...
#--
        def SolveWAWiRevisionBug(self):
                Options.Run.Timeout = self.GetTimes('MediumTime')
                
                try:
                
                        Temp = mDBOperation.cDBOperation()
                        WAWiVersion = Temp.DBC(SQLCommand = "USE eazybusiness;UPDATE tOptions SET cValue = '" + Config.AktualVersion + "' WHERE ckey = 'Revision'", Type = 'Command')
                        
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp)) 
                        raise mException.cReturn() 
