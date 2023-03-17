# import Objects_WAWi
# import Objects_ArtikelMainListViewControl
# import Objects_Toolsbar
from Exception.mException import cException

#--
#...
#--
class cToolbar():
        ParsChildResult = []
        
        def __init__(cls):
                pass

                
                
#--
#...
#--
        def GoToToolsbar(cls, PageName):
                Options.Run.Timeout = cls.getTime('VeryLargTime')
        
                try:
                
                        cls.WaitForAvailablity(Objects_WAWi.ToolsBar)
                        Objects_WAWi.Parent_ToolsBar.WaitChild('toolbar') 
                        Objects_WAWi.ToolsBar.CheckItem(PageName, True, False)
                        Delay(1500)
                        cls.WaitForAvailablity(Objects_WAWi.ToolsBar)
                        Delay(1500)
                        while not Objects_WAWi.ToolsBar.wChecked[PageName, False]:
                                Delay(1500)
                                Objects_WAWi.ToolsBar.CheckItem(PageName, True, False)
                        Delay(cls.getTime('SmallTime'))
                        if PageName == 'Artikel':
                                while not Objects_ArtikelMainListViewControl.ArtikelSuchen_cmbGlobal.Exists:
                                        Delay(cls.getTime('SmallTime'))
                        else:
                                cls.WaitForAvailablity(Objects_Toolsbar.optPage(PageName))
                            
                except Exception as exp:
                        Log.Warning("GoToToolsbar: " + str(exp))
                        mException.RecoverWAWi('cToolbar')
#--
#...
#--        
        def WaitForToolsbarAvailablity(cls, Object, ObjectName = " Nothing "):
                Options.Run.Timeout = cls.getTime('TinyTime')
        
                try:
        
                        Delay(cls.getTime('SmallTime'))
                        if Object is None or Object == 'nothing' or type(Object) == str:
                                Object = None
                                return False
        
                        if not aqObject.IsSupported(Object, 'Enabled'):  
                                Object = None    
                                return False
            
                        if aqObject.IsSupported(Object, 'Exists'):
                                while True:
                                    if Object.Exists :
                                        break
                                    Delay(cls.getTime('TinyTime'))
        
                        if aqObject.IsSupported(Object, 'Header') or aqObject.IsSupported(Object, 'HeaderControl'):
                                Delay(cls.getTime('RegularTime'))
                                Counter = 0
                                while True:
                                        if not ImageRepository.Waiting.Wait.Exists(Object) or Counter > 40:
                                                break
                                        Delay(4000)
                                        Counter +=1
                        
                        if aqObject.IsSupported(Object, 'Visible'):
                                Counter = 0
                                while not Object.Visible:
                                        Counter += 1
                                        Delay(cls.getTime('SmallTime'))
                                        if Counter > 50:
                                                Object = None
                                                Counter = None
                                                return False  
                                                      
                        if not Object.Enabled:
                                Counter = None
                                Object = None
                                return False
                        Counter = None
                        Object = None
                        return True    
                            
                except Exception as exp:
                        Log.Warning("mToolbar-WaitForToolsbarAvailablity: " + str(exp))
#--
#...
#--
        def WaitForProgressBar(cls, ProgressBar, WaitFor = 99, MCounter = 2000):
                
                try:
                
                        Delay(250)
                        
                        if ProgressBar == None:
                                return
                                
                        if not ProgressBar.Exists:
                                return
                
                        if not aqObject.IsSupported(ProgressBar, 'Value'):
                                Log.Message(" * AQC of WAWi says: The Progressbar is not available *")
                                return
                
                        while ProgressBar.Value < WaitFor :	
                                
                                Delay(cls.getTime('SmallTime'))
                                
                                mException.WindowDetector()
                                
                                if MCounter == 0:
                                        Log.Message(" * AQC of WAWi says: I have waited for Progressbar too much but his not finished, I will go *") 
                                        break
                                        
                                if MCounter < 1950 and not ProgressBar.Exists:
                                        Log.Message(" * AQC of WAWi says: The Progressbar is not more available *")
                                        break
                                        
                                MCounter -= 1
                                
                                if not aqObject.IsSupported(ProgressBar, 'Value'):
                                        break
                                        
                                if not ProgressBar.Exists:
                                        break
                
                        Delay(cls.getTime('SmallTime'))
                
                except Exception as exp:
                        Log.Warning("WaitForProgressBar " + str(exp))
#--
#...
#--
        #Get class Attribute ParsChildResult
        def GetAllChildNameList(cls, Child):

                try:
                        
                        cls.ParsChildResult.clear()
                        
                        cls.__ParsChild(Child)
                        
                        return cls.ParsChildResult
                
                except Exception as exp:
                        Log.Message('GetAllChildNameList: ' + str(exp))
#--
#...
#--
        #Give Me TreeView then I Get You All Child name in FullPathNode forexample: TreeView = Aliases.JTL_WAWi.ToolbarPages.ZahlungsverwaltungForm.spMain.SplitterPanel2.tlpTree.tvBereiche.SelectedNode
        def __ParsChild(cls, Child):

                try:
                        
                        if Child == None:
                            return
            
                        Child.ExpandAll()
                        FullPathNode = "|" + Child.FullPath.OleValue.replace("\\", "|")
  
                        #Do Somthing for example a function that save a node name
                        cls.ParsChildResult.append(FullPathNode)
  
                        if Child.FirstNode != None:
                            Child = Child.FirstNode
                        elif Child.NextNode != None and Child.LastNode == None:
                            Child = Child.NextNode
                        else:
                            Child = Child.Parent.NextNode
    
                        cls.__ParsChild(Child)
                
                except Exception as exp:
                        Log.Message('ParsChild: ' + str(exp))

                        
                        
