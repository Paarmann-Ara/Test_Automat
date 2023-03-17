from Toolboxs.Repository.Base.mBaseRepository import BaseRepository
from Toolboxs.Repository.mTimeDictionary import cTimeDictionary


# --
# ...
# --

class cTime(BaseRepository):
        @classmethod
        def get_dictionary(cls):
                return cTimeDictionary()()