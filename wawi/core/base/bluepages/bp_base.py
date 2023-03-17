from abc import ABC, abstractmethod
 
class BluepageBase(ABC):
 
        @abstractmethod
        def Setup(self, Methode = '', ChangeCheckListAndAntwortMethode = ''):
                pass
#--
#...
#--
        @abstractmethod
        def Prerequisite(self):
                pass
#--
#...
#--
        @abstractmethod
        def AfterSetup(self):
                pass
#--
#...
#--
        @abstractmethod
        def ChangeCheckListAndAntwortOrUseCheckListExt(self, ChangeCheckListAndAntwortMethode = ''):
                pass
