
from jtl_wawi.core.engin.TestComplete.mTestCompleteDriver import cTestCompleteDriver
from jtl_wawi.core.Measures.mPerformanceProtokoliren import cPerformanceProtokoliren
from jtl_wawi.core.CheckPoint.mCheckPoint import cCheckPoint
from jtl_wawi.Setting.core.mcoreConfig import ccoreConfig
from jtl_wawi.core.base.mbaseDescriptor import cDescriptor

'''TestCase Modules'''
from jtl_wawi.TestCase.Keys.Common.Application.mMessageManager import cMessageManager
from jtl_wawi.TestCase.Keys.Common.Application.mToolbar import cToolbar

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
from jtl_wawi.Setting.wawi.mwawiConfig import cAQCConfig
from Toolboxs.Repository.mText import cText
from Toolboxs.Repository.mTime import cTime
from jtl_wawi.Setting.TestCase.mTestCaseConfig import cTestCaseConfig
from jtl_wawi.Setting.TestCase.mTestCaseDateiConfig import cTestCaseDateiConfig
from jtl_wawi.Setting.core.mCheckPointConfig import cCheckPointConfig
from Drivers.Setting.menginConfig import cenginConfig
from jtl_wawi.Setting.core.mcoreConfig import ccoreConfig


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