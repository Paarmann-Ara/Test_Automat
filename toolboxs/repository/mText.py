from Toolboxs.Repository.Base.mBaseRepository import BaseRepository
from Toolboxs.Repository.mTextDictionary import cTextDictionary


# --
# ...
# --

class cText(BaseRepository):
        @classmethod
        def get_dictionary(cls):
                return cTextDictionary()()