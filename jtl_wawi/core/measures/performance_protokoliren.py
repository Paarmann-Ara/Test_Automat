import datetime
from Exception.mException import cException
from WAWi.Core.Base.BluePages.bpPerformanceProtokoliren import PerformanceProtokoliren

#--
#...
#--
class cPerformanceProtokoliren(PerformanceProtokoliren):
        def __init__(cls):
                pass
        
        
        
#--
#...
#--
        def FensterZeitFallback(cls):
    
                Result = ["Unbekannt", "-"] 
                return Result
#--
#...
#--
        def FensterZeitFormNotAvailable(cls):
    
                Result = ["FormNotAvailable", "-"] 
                return Result   
#--
#...
#--
        def FensterZeit(cls, Button, Form, Messagbox = 'NO', Antwort ='YES', SecoundSign = None, IsSetFocus = False, SecoundClickOnButton = False, IsDoubleCheckException = False):
                Options.Run.Timeout = cls.getTime('LargTime')
                
                Result = ["Unbekannt", "-"] 
                Counter = 2400
                temp = ''
        
                if not Button.Enabled:
                        Delay(250)
                        
                if Button.Enabled:
                        cls.WaitForAvailablity(Button)
                        Delay(50)
                        
                        T1 = datetime.datetime.now()

                        cls.ClickButton(Button, IsSetFocus = IsSetFocus)

                        if Messagbox == 'YES':
                                if mException.WindowDetector(cls.__module__):
                                        Form.Close()
                                        cls.MessagboxManager()
                                        return Result

                                if Antwort =='YES':
                                        cls.MessagboxManager(YesOrNo = Antwort)
                                        cls.MessagboxManager(YesOrNo = Antwort)
                                elif Antwort =='WaitToFinish':
                                        cls.MessagboxManager(YesOrNo = Antwort)
                                elif Antwort !='NO':
                                        cls.MessagboxManager(YesOrNo = Antwort)
                                        cls.MessagboxManager()
                                        Result.append(Antwort)
                                else:
                                        cls.MessagboxManager(YesOrNo = 'NO')
                                        return None                               
                                
                                if SecoundClickOnButton:
                                        cls.ClickButton(Button, IsSetFocus = IsSetFocus)       
                                        
                                T1 = datetime.datetime.now()       
                                                 
                        if SecoundSign == None:
                                while Form.Exists and Counter > 0:
                                        Delay(50)
                                        if Counter < 2395:
                                                if mException.WindowDetector(cls.__module__):
                                                        Form.Close()
                                                        cls.MessagboxManager()
                                                        raise mException.cEingabeIstFalsch()
                                                
                                                if cls.MessagboxManager():
                                                        Form.Close()
                                                        raise mException.cEingabeIstFalsch()
                                                
                                                if Counter < 2390:
                                                        Form.Close() 
                                                        Log.Message('I Have a Big Problem')
                                                        raise mException.cTestAgin()
                                                        break
                                                         
                                        Counter -= 1
                        else:
                                Delay(2000)
                                Log.Message('I Have a SecoundSign')
                                
                        if IsDoubleCheckException:
                                if mException.WindowDetector(cls.__module__):
                                        Form.Close()
                                        cls.MessagboxManager()
                                        if mException.WindowDetector(cls.__module__):
                                                Form.Close()
                                                cls.MessagboxManager(YesOrNo = 'NO')
                                        raise mException.cTestAgin()
                        
                        T2 = datetime.datetime.now()
                        DT = T2 - T1;  
                
                        temp = IntToStr((DT.days * 86400000) + (DT.seconds * 1000) + (DT.microseconds / 1000))
                        if temp != 60000:
                                Result[0] = temp[0:14]
                
                        if not Form.Exists:
                                Result[1] = '+'
                        
                        return Result
                        
                else:
                        raise mException.cObjectIsDisabled()
                                
#--
#...
#--
        def FensterZeitBool(cls, Button, Messagbox = 'NO', IsSetFocus = False):
                Options.Run.Timeout = cls.getTime('LargTime')
    
                Result = ["Unbekannt", "-"] 
                Counter = 2400
                temp = ''
        
                if Button.Enabled:
                        cls.WaitForAvailablity(Button)
                        T1 = datetime.datetime.now()

                        cls.ClickButton(Button, IsSetFocus = IsSetFocus)

                        if Messagbox == 'YES':
                                if mException.WindowDetector(cls.__module__):
                                        cls.MessagboxManager()
                                        return Result
                                
                                cls.MessagboxManager()
                                T1 = datetime.datetime.now()                        
                        
                        while cls.MessagboxManager() and Counter > 0:
                                Delay(50)
                                if Counter < 2350:
                                        if mException.WindowDetector(cls.__module__):
                                                cls.MessagboxManager()
                                                break
                                Counter -= 1
                        
                        T2 = datetime.datetime.now()
                        DT = T2 - T1;  
                
                        temp = IntToStr((DT.days * 86400000) + (DT.seconds * 1000) + (DT.microseconds / 1000))
                        if temp != 60000:
                                Result[0] = temp[0:14]
                
                        Result[1] = '+'
                        
                        return Result          
#--
#...
#--
        def FensterZeitMessageBox(cls, Antwort = 'Yes'):
                Options.Run.Timeout = cls.getTime('LargTime')
    
                Result = ["Unbekannt", "-"] 
                Counter = 2400
                temp = ''
        
                T1 = datetime.datetime.now()

                while cls.MessagboxManager() and Counter > 0:
                        Delay(50)
                        if Counter < 2350:
                                if mException.WindowDetector(cls.__module__):
                                        cls.MessagboxManager()
                                        break
                        Counter -= 1
                        
                T2 = datetime.datetime.now()
                DT = T2 - T1;  
                
                temp = IntToStr((DT.days * 86400000) + (DT.seconds * 1000) + (DT.microseconds / 1000))
                if temp != 60000:
                        Result[0] = temp[0:14]
                
                Result[1] = '+'
        
                cls.MessagboxManager()
                        
                return Result                      
#--
#...
#--
        def FensterZeitWaitForAvailablity(cls, Button, Object, Messagbox = 'NO', IsSetFocus = False):
                Options.Run.Timeout = cls.getTime('LargTime')
    
                Result = ["Unbekannt", "-"] 
                Counter = 2400
                temp = ''
        
                if Button.Enabled:
                        cls.WaitForAvailablity(Button)
                        T1 = datetime.datetime.now()

                        cls.ClickButton(Button, IsSetFocus = IsSetFocus)

                        if Messagbox == 'YES':
                                if mException.WindowDetector(cls.__module__):
                                        cls.MessagboxManager()
                                        return Result
                                
                                cls.MessagboxManager()
                                T1 = datetime.datetime.now()                        
                        
                        while not cls.WaitForAvailablity(Object) and Counter > 0:
                                Delay(50)
                                if Counter < 2350:
                                        if mException.WindowDetector(cls.__module__):
                                                cls.MessagboxManager()
                                                break
                                Counter -= 1
                        
                        T2 = datetime.datetime.now()
                        DT = T2 - T1;  
                
                        temp = IntToStr((DT.days * 86400000) + (DT.seconds * 1000) + (DT.microseconds / 1000))
                        if temp != 60000:
                                Result[0] = temp[0:14]
                
                        Result[1] = '+'
                        
                        return Result
#--
#...
#--
        def FensterZeitWaitForCloseFenster(cls, Form, Messagbox = 'NO', Antwort ='YES' ):
                Options.Run.Timeout = cls.getTime('LargTime')
    
                Result = ["Unbekannt", "-"] 
                Counter = 2400
                temp = ''
        
                T1 = datetime.datetime.now() 
        
                if Messagbox == 'YES':
                        if mException.WindowDetector(cls.__module__):
                                Form.Close()
                                cls.MessagboxManager()
                                return Result

                                if Antwort =='YES':
                                        cls.MessagboxManager(YesOrNo = Antwort)
                                        cls.MessagboxManager(YesOrNo = Antwort)
                                elif Antwort =='WaitToFinish':
                                        cls.MessagboxManager(YesOrNo = Antwort)
                                elif Antwort !='NO':
                                        cls.MessagboxManager(YesOrNo = Antwort)
                                        cls.MessagboxManager()
                                        Result.append(Antwort)
                                else:
                                        cls.MessagboxManager(YesOrNo = 'NO')
                                        return None
                                        
                        Form.Close()
                        cls.MessagboxManager()
        
                T1 = datetime.datetime.now()                        
                
                if Form.Exists:                
                        Form.Close()
                        while Form.Exists and Counter > 0:
                                Delay(50)
                                if Counter < 2350:
                                        if mException.WindowDetector(cls.__module__):
                                                Form.Close()
                                                cls.MessagboxManager()
                                                break
                                Counter -= 1
                        
                T2 = datetime.datetime.now()
                DT = T2 - T1;  
                
                temp = IntToStr((DT.days * 86400000) + (DT.seconds * 1000) + (DT.microseconds / 1000))
                if temp != 60000:
                        Result[0] = temp[0:14]
                
                if not Form.Exists:
                        Result[1] = '+'
                        
                return Result        
#--
#...
#--
        def FensterZeitIfMessageReleaseNoPermitToCloseFenster(cls, Button, Form, Messagbox = 'YES', Antwort ='WaitToFinish', IsSetFocus = False ):
                Options.Run.Timeout = cls.getTime('LargTime')
                
                Result = ["Unbekannt", "-"] 
                Counter = 2400
                temp = ''
        
                if not Button.Enabled:
                        Delay(250)
                        
                if Button.Enabled:
                        cls.WaitForAvailablity(Button)
                        Delay(100)
                        
                        T1 = datetime.datetime.now()

                        cls.ClickButton(Button, IsSetFocus = IsSetFocus)

                        if Messagbox == 'YES':
                                if mException.WindowDetector(cls.__module__):
                                        Form.Close()
                                        cls.MessagboxManager()
                                        return Result

                                if Antwort =='YES':
                                        cls.MessagboxManager()
                                        cls.MessagboxManager()
                                elif Antwort =='WaitToFinish':
                                        cls.MessagboxManager(YesOrNo = Antwort)
                                        if Form.Exists:
                                                Form.Close()
                                                cls.MessagboxManager()
                                                return Result
                                elif Antwort !='NO':
                                        cls.MessagboxManager(YesOrNo = Antwort)
                                        cls.MessagboxManager()
                                        Result.append(Antwort)
                                else:
                                        cls.MessagboxManager(YesOrNo = 'NO')
                                        return None                               
                                        
                                T1 = datetime.datetime.now()                        
                        
                        while Form.Exists and Counter > 0:
                                Delay(50)
                                if Counter < 2395:
                                        if mException.WindowDetector(cls.__module__):
                                                Form.Close()
                                                cls.MessagboxManager()
                                                raise mException.cEingabeIstFalsch()
                                                
                                        if cls.MessagboxManager():
                                                Form.Close()
                                                raise mException.cEingabeIstFalsch()
                                                
                                Counter -= 1
                        
                        T2 = datetime.datetime.now()
                        DT = T2 - T1;  
                
                        temp = IntToStr((DT.days * 86400000) + (DT.seconds * 1000) + (DT.microseconds / 1000))
                        if temp != 60000:
                                Result[0] = temp[0:14]
                
                        if not Form.Exists:
                                Result[1] = '+'
                        
                        return Result
                        
                else:
                        raise mException.cObjectIsDisabled()
