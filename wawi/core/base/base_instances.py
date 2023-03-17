
from wawi.core.engin.TestComplete.mTestCompleteDriver import cTestCompleteDriver
from wawi.core.Measures.mPerformanceProtokoliren import cPerformanceProtokoliren
from wawi.core.CheckPoint.mCheckPoint import cCheckPoint
from wawi.Setting.core.mcoreConfig import ccoreConfig
from wawi.core.base.mbaseDescriptor import cDescriptor

'''TestCase Modules'''
from wawi.TestCase.Keys.Common.Application.mMessageManager import cMessageManager
from wawi.TestCase.Keys.Common.Application.mToolbar import cToolbar

'''Projects Modules'''
from Toolboxs.mToolbox import cToolbox
from Toolboxs.mDelay import cDelay
from Toolboxs.mProcess import cProcess
from Exception.mException import cException
import Exception.mException
from db.engin.SQLServer.mSQLExecute import cDBOperation
from Email.mSendMail import cSendMail
from Log.mLog import cLog

'''Config Modules'''
from wawi.Setting.wawi.mwawiConfig import cAQCConfig
from Toolboxs.Repository.mText import cText
from Toolboxs.Repository.mTime import cTime
from wawi.Setting.TestCase.mTestCaseConfig import cTestCaseConfig
from wawi.Setting.TestCase.mTestCaseDateiConfig import cTestCaseDateiConfig
from wawi.Setting.core.mCheckPointConfig import cCheckPointConfig
from Drivers.Setting.menginConfig import cenginConfig
from wawi.Setting.core.mcoreConfig import ccoreConfig


# --
# ...
# --


class BaseInstances():
    def __init__(self):
        
        '''Config Instance'''
        self.ConfigCheckPoint = cCheckPointConfig().instance
        self.Configengin = cenginConfig().instance
        self.Configcore = ccoreConfig().instance
        self.ConfigTestCase = cTestCaseConfig().instance
        self.ConfigTestCaseDatei = cTestCaseDateiConfig().instance
        self.ConfigAQC = cAQCConfig().instance
        self.Text = cText().instance
        self.Time = cTime().instance        