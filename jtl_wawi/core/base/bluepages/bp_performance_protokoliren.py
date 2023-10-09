from abc import ABC, abstractmethod
 
class PerformanceProtokoliren(ABC):

#--
#...
#--
        @abstractmethod
        def FensterZeitFallback(cls):
                pass
#--
#...
#--
        @abstractmethod
        def FensterZeitFormNotAvailable(cls):
                pass
#--
#...
#--
        @abstractmethod
        def FensterZeit(cls):
                pass
#--
#...
#--
        @abstractmethod
        def FensterZeitBool(cls):
                pass
#--
#...
#--
        @abstractmethod
        def FensterZeitMessageBox(cls):
                pass
#--
#...
#--
        @abstractmethod
        def FensterZeitWaitForAvailablity(cls):
                pass
#--
#...
#--
        @abstractmethod
        def FensterZeitWaitForCloseFenster(cls):
                pass
#--
#...
#--
        @abstractmethod
        def FensterZeitIfMessageReleaseNoPermitToCloseFenster(cls):
                pass

