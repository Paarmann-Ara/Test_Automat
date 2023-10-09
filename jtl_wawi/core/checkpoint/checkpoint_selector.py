import mException
import mBase
import mRandom
from WAWi.Setting.TestApp import Config

#--
#...
#--
class cCheckPointSelector(mBase.cBase):
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
                            ,CheckList_0_Ar_Ext                                                                                                 = [],CheckList_0_DB_Att_Ext                                                                                             = []
                            
                            ,CheckPoint_Dic                                                                                                     = {}
                            ,IsNotSingleMode                                                                                                    = True
                            ,NoShow    		    																				                = [] ):
                            
                            
                            	
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
                
                self.CheckPoint_Dic                                                                                                             = CheckPoint_Dic
                self.IsNotSingleMode                                                                                                            = IsNotSingleMode
                self.NoShow                                                                                                                     = NoShow
                
                
                
#--
#...
#--
        def CheckPointSelector(self):
                Options.Run.Timeout = self.getTime('VeryLongTime')
                
                try:
                
                        self.TestResult('CheckPointSelector', TypeOfResultObject = 'Information')        
                         		
                        self.__CheckPointSelector()
                        
                        Delay(self.getTime('SmallTime'))
        
                except Exception as exp:
                        self.TestResult(self.CheckPointSelector.__name__ , Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp))

#--
#...
#--
        def __CheckPointSelector(self):
            
                try:                      
                
                        if not Config.IsCheckPoint:
                                return
                                
                        Index = 0
                        
                        CheckList_0_Ar_Zusammenfassen = self.CheckList_0_Ar[:] + self.CheckList_0_Ar_Ext[:]
                        CheckList_0_Ar_ExtAntwort = self.CheckList_0_Ar_Antwort
                                
                        if len(self.NoShow) != 0:
                                for it in self.NoShow:
                                        CheckList_0_Ar_Zusammenfassen.remove(it)                                
                
                        CheckList_0_Ar_ExtAntwortDic = {Item[1]: Item[0] for Item in CheckList_0_Ar_ExtAntwort}
                                                                   
                        for it in CheckList_0_Ar_Zusammenfassen:
                        
                                #DB's Update 
                                try:                       
                                        if self.CheckPoint_Dic[it][0] == 'Query':
                                                _ = CheckList_0_Ar_ExtAntwortDic[it]
                                                
                                                self.CheckPoint_Dic.update({it:('Query', self.CheckPoint_Dic[it][1] + '\'' + CheckList_0_Ar_ExtAntwortDic[self.CheckPoint_Dic[it][2]] + '\'')})

                                                        
                                                        
                                except Exception as exp:
                                        pass
        
                                finally:
                                    pass                        
                        
                                for Index in range(len(CheckList_0_Ar_ExtAntwort)):
                                        if it == CheckList_0_Ar_ExtAntwort[Index][1]:
                                                                                
                                                try: 
                                                        _ = self.CheckPoint_Dic[it]
                                                        
                                                        #Object, Type of check, TabObject, TabName, Return_TabObject, Return_TabName
                                                        
                                                        if len(self.CheckPoint_Dic[it]) > 2:
                                                                if self.CheckPoint_Dic[it][3] == 'Click':
                                                                        self.Click(self.CheckPoint_Dic[it][2])
                                                                elif self.CheckPoint_Dic[it][3] == 'Tab':
                                                                        self.ClickTab(self.CheckPoint_Dic[it][2], self.CheckPoint_Dic[it][4])
                                                                elif self.CheckPoint_Dic[it][3] == 'NestedTab':
                                                                        self.ClickTab(self.CheckPoint_Dic[it][2], self.CheckPoint_Dic[it][4])
                                                                        self.ClickTab(self.CheckPoint_Dic[it][5], self.CheckPoint_Dic[it][7])
                                                               
                                                        self.ChkPoint(self.CheckPoint_Dic[it][0], self.CheckPoint_Dic[it][1], CheckList_0_Ar_ExtAntwort[Index][0], it, self.IsNotSingleMode)

                                                        if len(self.CheckPoint_Dic[it]) > 2:                                                        
                                                                if self.CheckPoint_Dic[it][3] == 'Click':
                                                                        self.Click(self.CheckPoint_Dic[it][4])
                                                                elif self.CheckPoint_Dic[it][3] == 'Tab':
                                                                        self.ClickTab(self.CheckPoint_Dic[it][5], self.CheckPoint_Dic[it][7])
                                                                elif self.CheckPoint_Dic[it][3] == 'NestedTab':
                                                                        self.ClickTab(self.CheckPoint_Dic[it][8], self.CheckPoint_Dic[it][10])
                                                                        self.ClickTab(self.CheckPoint_Dic[it][11], self.CheckPoint_Dic[it][13])

                                                        break
                                                        
                                                except Exception as exp:
                                                        pass
        
                                                finally:
                                                    break
                		                
                except Exception as exp:
                        self.TestResult(Mode = self.Mode, Empfanger = self.Empfanger, TypeOfResultObject = 'Info', MoreInfo = str(exp))                         
                        raise mException.cCheckPointSelector()