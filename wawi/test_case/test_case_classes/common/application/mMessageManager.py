from AWAWiTestCase.Objects.Common.Application import Objects_MessageManager

#--
#...
#--
class cMessageManager():
        def __init__(cls):
                pass

#         #MsgBox_Absturz
#         MsgBox_Absturz                                                      = Aliases.JTL_WAWi.MsgBox_Absturz
#         Absturz_btnSchlie_en                                                = Aliases.JTL_WAWi.MsgBox_Absturz.btnSchliessen
#         MsgBox_btnOK                                                        = Aliases.JTL_WAWi.MsgBox_Absturz.btnOK

#         #Windows_Msg_Crash
# #        Windows_Msg_Crash                                                   = Aliases.Windows_Msg_Crash.Crashed
# #        Windows_Msg_Crash_btnProgrammSchliesen                              = Aliases.Windows_Msg_Crash.Crashed.JTL_WAWi.CtrlNotifySink.btnProgrammSchliesen

#         #MsgBox_0
#         MsgBox_0                                                            = Aliases.JTL_WAWi.MsgBox_0
#         MsgBox_0_Body                                                       = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup
#         MsgBox_0_btnSpeichern                                               = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnSpeichern
#         MsgBox_0_btnNichtSpeichern                                          = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl2.btnNichtSpeichern
#         MsgBox_0_btnAbbrechen_0                                             = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl3.btnAbbrechen_0
#         MsgBox_0_btnNein_0                                                  = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl2.btnNein_0
#         MsgBox_0_btnJa_0                                                    = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnJa_0
#         MsgBox_0_btnAbbrechen_1                                             = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl3.btnAbbrechen_1
#         MsgBox_0_btnBeenden                                                 = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl2.btnBeenden
#         MsgBox_0_btnOk_0                                                    = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnOk_0
#         MsgBox_0_btnOnlineshopLSchen                                        = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnOnlineshopLSchen
#         MsgBox_0_btnAbbrechen_2                                             = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl2.btnAbbrechen_2
#         MsgBox_0_btnJa_1                                                    = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl2.btnJa_1
#         MsgBox_0_btnNein_1                                                  = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl3.btnNein_1
#         MsgBox_0_btnSchlieEn_0                                              = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl2.btnSchlieEn_0
#         MsgBox_0_btnOk_1                                                    = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnOk_1
#         MsgBox_0_btnJa_2                                                    = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnJa_2
#         MsgBox_0_btnNein_2                                                  = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl2.btnNein_2
#         MsgBox_0_btnArtikelLoscen                                           = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnArtikelLoscen
#         MsgBox_0_btnBestandAusbuchen                                        = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnBestandAusbuchen
#         MsgBox_0_btnAbbrechen_3                                             = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl2.btnAbbrechen_3
#         MsgBox_0_btnOk_2                                                    = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl2.btnOk_2
#         MsgBox_0_btnKostenfreieBetaLizenzAktiviere                          = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnKostenfreieBetaLizenzAktiviere
        
#         MsgBox_0_txtInput_0                                                 = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.txtInput_0
#         MsgBox_0_btnSpeichern_1                                             = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnSpeichern_1

#         MsgBox_0_cmbInput_0                                                 = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.cmbInput_0
        
#         MsgBox_0_btnAuthorisieren                                           = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnAuthorisieren
#         MsgBox_0_btnImportieren                                             = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl2.btnImportieren

#         MsgBox_0_btnJetztEinrichten                                         = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnJetztEinrichten
        
#         MsgBox_0_btnPostfachAnlegen                                         = Aliases.JTL_WAWi.MsgBox_0.Body.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnPostfachAnlegen

        
        
#         #MsgBox_1
#         MsgBox_1                                                            = Aliases.JTL_WAWi.MsgBox_1
#         MsgBox_1_Body                                                       = Aliases.JTL_WAWi.MsgBox_1.JTL_Wawi
#         MsgBox_1_btnJa_0                                                    = Aliases.JTL_WAWi.MsgBox_1.JTL_WAWi.CtrlNotifySink.btnJa_0
#         MsgBox_1_btnNein_0                                                  = Aliases.JTL_WAWi.MsgBox_1.JTL_WAWi.CtrlNotifySink2.btnNein_0
#         MsgBox_1_btnAbbrechen_0                                             = Aliases.JTL_WAWi.MsgBox_1.JTL_WAWi.CtrlNotifySink3.btnAbbrechen_0
#         MsgBox_1_btnAbbrechen_1                                             = Aliases.JTL_WAWi.MsgBox_1.JTL_WAWi.CtrlNotifySink2.btnAbbrechen_1
#         MsgBox_1_btnOK_0                                                    = Aliases.JTL_WAWi.MsgBox_1.JTL_WAWi.CtrlNotifySink.btnOK_0
#         MsgBox_1_Progressbar_0                                              = Aliases.JTL_WAWi.MsgBox_1.JTL_Wawi.CtrlNotifySink.Progressbar_0

        
                
#         #MsgBox_2
#         MsgBox_2                                                            = Aliases.JTL_WAWi.MsgBox_2
#         MsgBox_2_btnOK_0                                                    = Aliases.JTL_WAWi.MsgBox_2.btnOK_0
#         MsgBox_2_btnJa_0                                                    = Aliases.JTL_WAWi.MsgBox_2.btnJa_0
#         MsgBox_2_btnNein_0                                                  = Aliases.JTL_WAWi.MsgBox_2.btnNein_0
#         MsgBox_2_btnAbbrechen_0                                             = Aliases.JTL_WAWi.MsgBox_2.btnAbbrechen_0

        
        
#         #Msgbox_3
#         Msgbox_3                                                            = Aliases.JTL_WAWi.Msgbox_3
#         Msgbox_3_Body                                                       = Aliases.JTL_WAWi.Msgbox_3.JTL_Wawi
#         Msgbox_3_btnJa_0                                                    = Aliases.JTL_WAWi.Msgbox_3.JTL_WAWi.CtrlNotifySink.btnJa_0
#         Msgbox_3_btnNein_0                                                  = Aliases.JTL_WAWi.Msgbox_3.JTL_WAWi.CtrlNotifySink2.btnNein_0
#         Msgbox_3_btnOK_0                                                    = Aliases.JTL_WAWi.Msgbox_3.JTL_WAWi.CtrlNotifySink.btnOK_0
#         Msgbox_3_btnOK_1                                                    = Aliases.JTL_WAWi.Msgbox_3.JTL_WAWi.CtrlNotifySink3.btnOK_1
#         Msgbox_3_btnOK_2                                                    = Aliases.JTL_WAWi.Msgbox_3.JTL_WAWi.CtrlNotifySink2.btnOK_2
#         Msgbox_3_btnOK_3                                                    = Aliases.JTL_WAWi.Msgbox_3.JTL_Wawi.CtrlNotifySink5.btnOK_3
#         Msgbox_3_btnOK_4                                                    = Aliases.JTL_WAWi.Msgbox_3.StatisticError.CtrlNotifySink.btnOK_4
        
#         Msgbox_3_AchtungSign                                                = Aliases.JTL_WAWi.Msgbox_3.JTL_WAWi.AchtungSign
#         Msgbox_3_btnZusatzinformationenNichtSenden                          = Aliases.JTL_WAWi.Msgbox_3.JTL_WAWi.CtrlNotifySink.btnZusatzinformationenNichtSenden
#         Msgbox_3_btnZusatzinformationenSenden                               = Aliases.JTL_WAWi.Msgbox_3.JTL_WAWi.CtrlNotifySink2.btnZusatzinformationenSenden
#         Msgbox_3_Progressbar_0                                              = Aliases.JTL_WAWi.Msgbox_3.JTL_WAWi.CtrlNotifySink.Progressbar_0
        
#         Msgbox_3_StatisticError_btnOK_0                                     = Aliases.JTL_WAWi.Msgbox_3.StatisticError.CtrlNotifySink_3.btnOK_0
#         Msgbox_3_StatisticError_btnOK_1                                     = Aliases.JTL_WAWi.Msgbox_3.StatisticError.CtrlNotifySink_11.btnOK_1
        
#         Msgbox_3_btnSchliessen_0                                            = Aliases.JTL_WAWi.Msgbox_3.JTL_Wawi.CtrlNotifySink.btnSchliessen_0

        
        
#         #Msgbox_neue_0
#         Msgbox_neue_0                                                       = Aliases.JTL_WAWi.Msgbox_neue_0
#         Msgbox_neue_0_btnOk_0                                               = Aliases.JTL_WAWi.Msgbox_neue_0.JTL_Wawi_Verkaufsverwaltung_Dialoge_ErrorMessage_ErrorMessageViewModel.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnOk_0
#         Msgbox_neue_0_Data                                                  = Aliases.JTL_WAWi.Msgbox_neue_0.JTL_Wawi_Verkaufsverwaltung_Dialoge_ErrorMessage_ErrorMessageViewModel.ContentControl.zTemplateGeneratorControl.DialogContentView.LayoutGroup.ContentControl.zTemplateGeneratorControl.ErrorMessageView.Grid.ScrollViewer.ItemsControl.ContentPresenter.Grid.ItemscontrolAngebot.ContentPresenter.StackPanel
        
        
        
#         #Msgbox_neue_1
#         Msgbox_neue_1                                                       = Aliases.JTL_WAWi.MsgBox_neue_1
#         Msgbox_neue_1_btnOk_0                                               = Aliases.JTL_WAWi.MsgBox_neue_1.ViewModel.ContentControl._TemplateGeneratorControl.DialogContentView.LayoutGroup.WawiFooter.ContentControl.btnOk_0
#         Msgbox_neue_1_Data                                                  = Aliases.JTL_WAWi.MsgBox_neue_1.ViewModel.ContentControl._TemplateGeneratorControl.DialogContentView.LayoutGroup.ContentControl._TemplateGeneratorControl.ValidationErrorsDialogView.Grid.ScrollViewer.ItemsControl.ContentPresenter.Grid.ItemscontrolStammdaten.ContentPresenter.StackPanel
        
        
        
#         #MsgBox_BildHinzufugen_0
#         MsgBox_BildHinzufugen_0                                             = Aliases.JTL_WAWi.MsgBox_BildHinzufugen_0
#         MsgBox_BildHinzufugen_0_Body                                        = Aliases.JTL_WAWi.MsgBox_BildHinzufugen_0.Bild_hinzuf_gen
#         MsgBox_BildHinzufugen_0_btnOK_0                                     = Aliases.JTL_WAWi.MsgBox_BildHinzufugen_0.Bild_hinzuf_gen.CtrlNotifySink.btnOK_0

        
        
#         #MsgBox_BildHinzufugen_1
#         MsgBox_BildHinzufugen_1                                             = Aliases.JTL_WAWi.MsgBox_BildHinzufugen_1
#         MsgBox_BildHinzufugen_1_Body                                        = Aliases.JTL_WAWi.MsgBox_BildHinzufugen_1.Bilder_hinzuf_gen
#         MsgBox_BildHinzufugen_1_btnOK_0                                     = Aliases.JTL_WAWi.MsgBox_BildHinzufugen_1.Bilder_hinzuf_gen.CtrlNotifySink.btnOK_0

        
        
#         #MsgBox_BildHinzufugen_0
#         MsgBox_BildErsetzen_0                                               = Aliases.JTL_WAWi.MsgBox_BildErsetzen_0
#         MsgBox_BildErsetzen_0_Body                                          = Aliases.JTL_WAWi.MsgBox_BildErsetzen_0.Bild_BildErsetzen
#         MsgBox_BildErsetzen_0_btnOK_0                                       = Aliases.JTL_WAWi.MsgBox_BildErsetzen_0.Bild_BildErsetzen.CtrlNotifySink.btnOK_0

        
        
#         #MsgBox_SpeichernUnterBestatigen_0
#         MsgBox_SpeichernUnterBestatigen_0                                   = Aliases.JTL_WAWi.MsgBox_SpeichernUnterBestatigen_0
#         MsgBox_SpeichernUnterBestatigen_0_Body                              = Aliases.JTL_WAWi.MsgBox_SpeichernUnterBestatigen_0.Speichern_unter_best_tigen
#         MsgBox_SpeichernUnterBestatigen_0_btnJa_0                           = Aliases.JTL_WAWi.MsgBox_SpeichernUnterBestatigen_0.Speichern_unter_best_tigen.CtrlNotifySink.btnJa_0
#         MsgBox_SpeichernUnterBestatigen_0_btnNein_0                         = Aliases.JTL_WAWi.MsgBox_SpeichernUnterBestatigen_0.Speichern_unter_best_tigen.CtrlNotifySink2.btnNein_0
        
        
        
#         #MsgBox_PositionLoschen
#         MsgBox_PositionLoschen                                              = Aliases.JTL_WAWi.MsgBox_PositionLoschen
#         MsgBox_PositionLoschen_btnJa                                        = Aliases.JTL_WAWi.MsgBox_PositionLoschen.btnJa
#         MsgBox_PositionLoschen_btnNein                                      = Aliases.JTL_WAWi.MsgBox_PositionLoschen.btnNein
        
        
        
#         #ExportVorlage_0        
#         ExportVorlage_0                                                     = Aliases.JTL_WAWi.ExportVorlage_0
#         ExportVorlage_0_btnJa                                               = Aliases.JTL_WAWi.ExportVorlage_0.btnJa
#         ExportVorlage_0_btnOk_0                                             = Aliases.JTL_WAWi.ExportVorlage_0.btnOk_0
        
        
        
#         #OffnenFile_0
#         OffnenFile_0                                                        = Aliases.JTL_WAWi.OffnenFile_0
#         OffnenFile_0_btnOk                                                  = Aliases.JTL_WAWi.OffnenFile_0.ffnen.CtrlNotifySink.btnOK

#--
#...
#--
        def MessagboxManager(cls, Type = 'IfVisible', YesOrNo = 'YES', MCounter = 50, InputeValue = 'Give me something', MessageToCheck = '', MessageObject = None, IndexObject = 2, IsWaitingToMessagsProgressbarInvisibleCheckMessagebox = False):
                Options.Run.Timeout = cls.getTime('TinyTime')
                
                try:
                
                        Counter = 0
                        ResultValue = False
                                
                        Delay(cls.getTime('SmallTime') * MCounter / 25)
                        
                        if MessageToCheck != '':
                                if not MessageObject.Window("Static", MessageToCheck, IndexObject).Exists:
                                        ResultValue = False
                        
                                        
                
                        if Type == 'WaitToFinish':
                                while cls.MsgBox_0.Exists or cls.MsgBox_1.Exists or cls.MsgBox_2.Exists or cls.Msgbox_3.Exists or cls.MsgBox_BildHinzufugen_0.Exists or cls.MsgBox_BildHinzufugen_1.Exists or cls.MsgBox_BildErsetzen_0.Exists or cls.MsgBox_SpeichernUnterBestatigen_0.Exists or cls.Msgbox_neue_0.Exists or cls.Msgbox_neue_1.Exists or cls.MsgBox_PositionLoschen.Exists or cls.ExportVorlage_0.Exists or cls.MsgBox_Absturz.Exists or cls.OffnenFile_0.Exists:
                                        if Counter > MCounter :
                                                break
                                        
                                
                                
                                        if YesOrNo == 'YES':
                                                if cls.MsgBox_0.Exists:        
                                                        if cls.MessagWriter(cls.MsgBox_0):
                                                                if cls.MsgBox_0_btnJa_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnJa_0) 
                                                                        ResultValue = True           
                                                                elif cls.MsgBox_0_btnOk_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnOk_0) 
                                                                        ResultValue = True      
                                                                elif cls.MsgBox_0_btnJa_1.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnJa_1) 
                                                                        ResultValue = True
                                                                elif cls.MsgBox_0_btnSpeichern.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnSpeichern) 
                                                                        ResultValue = True
                                                                elif cls.MsgBox_0_btnBeenden.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnBeenden) 
                                                                        ResultValue = True
                                                                elif cls.MsgBox_0_btnOnlineshopLSchen.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnOnlineshopLSchen) 
                                                                        ResultValue = True                                         
                                                                elif cls.MsgBox_0_btnSchlieEn_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnSchlieEn_0) 
                                                                        ResultValue = True  
                                                                elif cls.MsgBox_0_btnOk_1.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnOk_1) 
                                                                        ResultValue = True
                                                                elif cls.MsgBox_0_btnOk_2.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnOk_2)
                                                                elif cls.MsgBox_0_btnKostenfreieBetaLizenzAktiviere.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnKostenfreieBetaLizenzAktiviere)
                                                                        ResultValue = True                                                                        
                                                                elif cls.MsgBox_0_btnJa_2.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnJa_2) 
                                                                        ResultValue = True  
                                                                elif cls.MsgBox_0_btnArtikelLoscen.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnArtikelLoscen) 
                                                                        ResultValue = True
                                                                elif cls.MsgBox_0_btnBestandAusbuchen.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnBestandAusbuchen) 
                                                                        ResultValue = True
                                                                elif cls.MsgBox_0_btnSpeichern_1.Exists:
                                                                        cls.MsgBox_0_txtInput_0.Keys(InputeValue)
                                                                        Delay(2500)
                                                                        cls.ClickButton(cls.MsgBox_0_btnSpeichern_1)
                                                                        ResultValue = True

                                                                                                                       
                                                                        
                                                elif cls.MsgBox_1.Exists:        
                                                        if cls.MessagWriter(cls.MsgBox_1):
                                                                if cls.MsgBox_1_btnJa_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_1_btnJa_0) 
                                                                        ResultValue = True  
                                                                elif cls.MsgBox_1_btnOK_0: 
                                                                        cls.ClickButton(cls.MsgBox_1_btnOK_0) 
                                                                        ResultValue = True   
                                             
                                                elif cls.MsgBox_2.Exists:   
                                                        if cls.MessagWriter(cls.MsgBox_2):
                                                                if cls.MsgBox_2_btnOK_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_2_btnOK_0) 
                                                                        ResultValue = True
                                                                elif cls.MsgBox_2_btnJa_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_2_btnJa_0) 
                                                                        ResultValue = True                                                
                                                
                                       
                                                elif cls.Msgbox_3.Exists:
                                                        if cls.MessagWriter(cls.Msgbox_3):
                                                                if cls.Msgbox_3_btnJa_0.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnJa_0) 
                                                                        ResultValue = True                                
                                                                elif cls.Msgbox_3_btnOK_0.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnOK_0) 
                                                                        ResultValue = True        
                                                                elif cls.Msgbox_3_btnOK_1.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnOK_1) 
                                                                        ResultValue = True
                                                                elif cls.Msgbox_3_btnOK_2.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnOK_2) 
                                                                        ResultValue = True
                                                                elif cls.Msgbox_3_btnOK_3.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnOK_3) 
                                                                        ResultValue = True
                                                                elif cls.Msgbox_3_btnOK_4.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnOK_4) 
                                                                        ResultValue = True                                                                        
                                                                elif cls.Msgbox_3_StatisticError_btnOK_0.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_StatisticError_btnOK_0) 
                                                                        cls.TestResult('AQC of WAWi says: Ich get Static Error. Position Unknown', TypeOfResultObject = 'Bug')
                                                                        ResultValue = True
                                                                elif cls.Msgbox_3_StatisticError_btnOK_1.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_StatisticError_btnOK_1) 
                                                                        cls.TestResult('AQC of WAWi says: Ich get Static Error. Position Unknown', TypeOfResultObject = 'Bug')
                                                                        ResultValue = True
                                                                elif cls.Msgbox_3_btnSchliessen_0.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnSchliessen_0) 
                                                                        ResultValue = True
                                                                                                 
                                                        
                                                elif cls.Msgbox_neue_0.Exists:
                                                        if cls.MessagWriter(cls.Msgbox_neue_0):
                                                                if cls.Msgbox_neue_0_btnOk_0.Exists:
                                                                        cls.ClickButton(cls.Msgbox_neue_0_btnOk_0) 
                                                                        ResultValue = True                                                 
                                                        
                                                elif cls.Msgbox_neue_1.Exists:
                                                        if cls.MessagWriter(cls.Msgbox_neue_1):
                                                                if cls.Msgbox_neue_1_btnOk_0.Exists:
                                                                        cls.ClickButton(cls.Msgbox_neue_1_btnOk_0) 
                                                                        ResultValue = True                                                           
                                                        
                                                elif cls.MsgBox_BildHinzufugen_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_BildHinzufugen_0):
                                                                if cls.MsgBox_BildHinzufugen_0_btnOK_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_BildHinzufugen_0_btnOK_0) 
                                                                        ResultValue = True                                 
                                                
                                                elif cls.MsgBox_BildHinzufugen_1.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_BildHinzufugen_1):
                                                                if cls.MsgBox_BildHinzufugen_1_btnOK_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_BildHinzufugen_1_btnOK_0) 
                                                                        ResultValue = True     
                                                
                                                elif cls.MsgBox_BildErsetzen_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_BildErsetzen_0):
                                                                if cls.MsgBox_BildErsetzen_0_btnOK_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_BildErsetzen_0_btnOK_0) 
                                                                        ResultValue = True                                                                                                  
                                                
                                                elif cls.MsgBox_SpeichernUnterBestatigen_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_SpeichernUnterBestatigen_0):
                                                                if cls.MsgBox_SpeichernUnterBestatigen_0_btnJa_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_SpeichernUnterBestatigen_0_btnJa_0) 
                                                                        ResultValue = True
                                                                                                           
                                                        
                                                elif cls.ExportVorlage_0.Exists:
                                                        if cls.MessagWriter(cls.ExportVorlage_0):
                                                                if cls.ExportVorlage_0_btnJa.Exists:
                                                                        cls.ClickButton(cls.ExportVorlage_0_btnJa) 
                                                                        ResultValue = True                                                        
                                                                elif cls.ExportVorlage_0_btnOk_0.Exists:
                                                                        cls.ClickButton(cls.ExportVorlage_0_btnOk_0) 
                                                                        ResultValue = True                                                                                                                
                                                                        
                                                        
                                                if cls.MsgBox_PositionLoschen.Exists:        
                                                        if cls.MessagWriter(cls.MsgBox_PositionLoschen):
                                                                if cls.MsgBox_PositionLoschen_btnJa.Exists:
                                                                        cls.ClickButton(cls.MsgBox_PositionLoschen_btnJa) 
                                                                        ResultValue = True
                                                                        
                                                                        
                                                if cls.MsgBox_Absturz.Exists:        
                                                        if cls.MessagWriter(cls.MsgBox_Absturz):
                                                                if cls.MsgBox_btnOK.Exists:
                                                                        cls.ClickButton(cls.MsgBox_btnOK) 
                                                                        ResultValue = True

                                                elif cls.OffnenFile_0.Exists:
                                                        if cls.MessagWriter(cls.OffnenFile_0):
                                                                if cls.OffnenFile_0_btnOk.Exists:
                                                                        cls.ClickButton(cls.OffnenFile_0_btnOk) 
                                                                        ResultValue = True
 
                                                                        
                                                
                                        elif YesOrNo == 'NO':
                                                if cls.MsgBox_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_0):
                                                                if cls.MsgBox_0_btnNichtSpeichern.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnNichtSpeichern)
                                                                        ResultValue = True
                                                                elif cls.MsgBox_0_btnNein_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnNein_0)
                                                                        ResultValue = True
                                                                elif cls.MsgBox_0_btnNein_1.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnNein_1)
                                                                        ResultValue = True       
                                                                elif cls.MsgBox_0_btnNein_2.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnNein_2)
                                                                        ResultValue = True                                                                                           
                                                
                                                
                                                elif cls.MsgBox_1.Exists:  
                                                        if cls.MessagWriter(cls.MsgBox_1):
                                                                if cls.MsgBox_1_btnNein_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_1_btnNein_0) 
                                                                        ResultValue = True      
                                                
                                                        
                                                elif cls.MsgBox_2.Exists:        
                                                        if cls.MessagWriter(cls.MsgBox_2):
                                                                if cls.MsgBox_2_btnNein_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_2_btnNein_0) 
                                                                        ResultValue = True      
                                                
                                                        
                                                elif cls.Msgbox_3.Exists:
                                                        if cls.MessagWriter(cls.Msgbox_3):
                                                                if cls.Msgbox_3_btnNein_0.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnNein_0) 
                                                                        ResultValue = True
                                                
                                                        
                                                elif cls.MsgBox_SpeichernUnterBestatigen_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_SpeichernUnterBestatigen_0):
                                                                if cls.MsgBox_SpeichernUnterBestatigen_0_btnNein_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_SpeichernUnterBestatigen_0_btnNein_0) 
                                                                        ResultValue = True
                                                
                                                if cls.MsgBox_PositionLoschen.Exists:        
                                                        if cls.MessagWriter(cls.MsgBox_PositionLoschen):
                                                                if cls.MsgBox_PositionLoschen_btnNein.Exists:
                                                                        cls.ClickButton(cls.MsgBox_PositionLoschen_btnNein) 
                                                                        ResultValue = True                                                        
                                                                     
                                                                        
                                                                        
                                                
                                        elif YesOrNo == 'Abbrechen':  
                                                if cls.MsgBox_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_0):
                                                                if  cls.MsgBox_0_btnAbbrechen_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnAbbrechen_0)
                                                                        ResultValue = True     
                                                                elif  cls.MsgBox_0_btnAbbrechen_1.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnAbbrechen_1)
                                                                        ResultValue = True   
                                                                elif  cls.MsgBox_0_btnAbbrechen_2.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnAbbrechen_2)
                                                                        ResultValue = True    
                                                                elif  cls.MsgBox_0_btnAbbrechen_3.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnAbbrechen_3)
                                                                        ResultValue = True
                                                
                                                
                                                elif cls.MsgBox_1.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_1):
                                                                if  cls.MsgBox_1_btnAbbrechen_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_1_btnAbbrechen_0)
                                                                        ResultValue = True  
                                                                elif  cls.MsgBox_1_btnAbbrechen_1.Exists:
                                                                        cls.ClickButton(cls.MsgBox_1_btnAbbrechen_1)
                                                                        ResultValue = True     
                                                
                                                        
                                                elif cls.MsgBox_2.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_2):
                                                                if  cls.MsgBox_2_btnAbbrechen_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_1_btnAbbrechen_0)
                                                                        ResultValue = True  



                                        elif YesOrNo == 'Authorisieren':  
                                                if cls.MsgBox_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_0):
                                                                if cls.MsgBox_0_btnAuthorisieren.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnAuthorisieren)
                                                                        ResultValue = True
                                                                        
                                                                        
                                                                        
                                        elif YesOrNo == 'Importieren':  
                                                if cls.MsgBox_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_0):
                                                                if cls.MsgBox_0_btnImportieren.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnImportieren)
                                                                        ResultValue = True

                                                                        
                                        elif YesOrNo == 'JetztEinrichten':  
                                                if cls.MsgBox_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_0):
                                                                if cls.MsgBox_0_btnJetztEinrichten.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnJetztEinrichten)
                                                                        ResultValue = True

                                                                        
                                        elif YesOrNo == 'PostfachAnlegen':  
                                                if cls.MsgBox_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_0):
                                                                if cls.MsgBox_0_btnPostfachAnlegen.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnPostfachAnlegen)
                                                                        ResultValue = True
                                                                                  
                                                                        
                                                                        
                                        Delay(cls.getTime('SmallTime'))
                                        Counter +=1
                                Delay(cls.getTime('SmallTime'))
                        

                
                        elif Type == 'IfVisible':
                                if cls.MsgBox_0.Exists or cls.MsgBox_1.Exists or cls.MsgBox_2.Exists or cls.Msgbox_3.Exists or cls.MsgBox_BildHinzufugen_0.Exists or cls.MsgBox_BildHinzufugen_1.Exists or cls.MsgBox_BildErsetzen_0.Exists or cls.MsgBox_SpeichernUnterBestatigen_0.Exists or cls.Msgbox_neue_0.Exists or cls.Msgbox_neue_1.Exists or cls.MsgBox_PositionLoschen.Exists or cls.ExportVorlage_0.Exists or cls.MsgBox_Absturz.Exists or cls.OffnenFile_0.Exists:
                                        if YesOrNo == 'YES':
                                                if cls.MsgBox_0.Exists:        
                                                        if cls.MessagWriter(cls.MsgBox_0):
                                                                if cls.MsgBox_0_btnJa_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnJa_0) 
                                                                        ResultValue = True      
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.MsgBox_0_btnOk_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnOk_0) 
                                                                        ResultValue = True      
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.MsgBox_0_btnJa_1.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnJa_1)
                                                                        ResultValue = True      
                                                                        Delay(cls.getTime('SmallTime'))                                                 
                                                                        return ResultValue
                                                                elif cls.MsgBox_0_btnJa_2.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnJa_2)
                                                                        ResultValue = True      
                                                                        Delay(cls.getTime('SmallTime'))                                                 
                                                                        return ResultValue                                                
                                                                elif cls.MsgBox_0_btnSpeichern.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnSpeichern) 
                                                                        ResultValue = True      
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.MsgBox_0_btnBeenden.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnBeenden) 
                                                                        ResultValue = True      
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue                                                
                                                                elif cls.MsgBox_0_btnOnlineshopLSchen.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnOnlineshopLSchen) 
                                                                        ResultValue = True                                                 
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.MsgBox_0_btnSchlieEn_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnSchlieEn_0) 
                                                                        ResultValue = True                                                 
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.MsgBox_0_btnOk_1.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnOk_1) 
                                                                        ResultValue = True                                                 
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.MsgBox_0_btnOk_2.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnOk_2) 
                                                                        ResultValue = True                                                 
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.MsgBox_0_btnKostenfreieBetaLizenzAktiviere.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnKostenfreieBetaLizenzAktiviere) 
                                                                        ResultValue = True                                                 
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.MsgBox_0_btnArtikelLoscen.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnArtikelLoscen) 
                                                                        ResultValue = True                                                 
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue 
                                                                elif cls.MsgBox_0_btnBestandAusbuchen.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnBestandAusbuchen) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.MsgBox_0_btnSpeichern_1.Exists:
                                                                        cls.MsgBox_0_txtInput_0.Keys(InputeValue)
                                                                        Delay(2500)
                                                                        cls.ClickButton(cls.MsgBox_0_btnSpeichern_1)
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime'))
                                                                        return ResultValue                                                
                                                                        
                                                                        
                                                elif cls.MsgBox_1.Exists:        
                                                        if cls.MessagWriter(cls.MsgBox_1):
                                                                if cls.MsgBox_1_btnJa_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_1_btnJa_0) 
                                                                        ResultValue = True      
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.MsgBox_1_btnOK_0.Exists: 
                                                                        cls.ClickButton(cls.MsgBox_1_btnOK_0) 
                                                                        ResultValue = True      
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue                                                 
                                                
                                                        
                                                elif cls.MsgBox_2.Exists:   
                                                        if cls.MessagWriter(cls.MsgBox_2):
                                                                if cls.MsgBox_2_btnOK_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_2_btnOK_0) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue  
                                                                elif cls.MsgBox_2_btnJa_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_2_btnJa_0) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue 
                                                
                                                
                                                                             
                                                elif cls.Msgbox_3.Exists:
                                                        if cls.MessagWriter(cls.Msgbox_3):
                                                                if cls.Msgbox_3_btnJa_0.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnJa_0) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue  
                                                                elif cls.Msgbox_3_btnOK_0.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnOK_0) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue           
                                                                elif cls.Msgbox_3_btnOK_1.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnOK_1) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.Msgbox_3_btnOK_2.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnOK_2) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.Msgbox_3_btnOK_3.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnOK_3) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.Msgbox_3_btnOK_4.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnOK_4) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue                                                                        
                                                                elif cls.Msgbox_3_StatisticError_btnOK_0.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_StatisticError_btnOK_0) 
                                                                        cls.TestResult('AQC of WAWi says: Ich get Static Error. Position UnKown', TypeOfResultObject = 'Bug')
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.Msgbox_3_StatisticError_btnOK_1.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_StatisticError_btnOK_1) 
                                                                        cls.TestResult('AQC of WAWi says: Ich get Static Error. Position UnKown', TypeOfResultObject = 'Bug')
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.Msgbox_3_btnSchliessen_0.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnSchliessen_0) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                                                                                                
                                                                                                                
                                                        
                                                elif cls.Msgbox_neue_0.Exists:
                                                        if cls.MessagWriter(cls.Msgbox_neue_0):
                                                                if cls.Msgbox_neue_0_btnOk_0.Exists:
                                                                        cls.ClickButton(cls.Msgbox_neue_0_btnOk_0) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue    
                                                        
                                                elif cls.Msgbox_neue_1.Exists:
                                                        if cls.MessagWriter(cls.Msgbox_neue_1):
                                                                if cls.Msgbox_neue_1_btnOk_0.Exists:
                                                                        cls.ClickButton(cls.Msgbox_neue_1_btnOk_0) 
                                                                        ResultValue = True  
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue                                                         
                                                                                                                                                                        
                                                elif cls.MsgBox_BildHinzufugen_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_BildHinzufugen_0):
                                                                if cls.MsgBox_BildHinzufugen_0_btnOK_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_BildHinzufugen_0_btnOK_0) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue                                                   
                                                
                                                        
                                                elif cls.MsgBox_BildHinzufugen_1.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_BildHinzufugen_1):
                                                                if cls.MsgBox_BildHinzufugen_1_btnOK_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_BildHinzufugen_1_btnOK_0) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue               
                                                
                                                        
                                                elif cls.MsgBox_BildErsetzen_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_BildErsetzen_0):
                                                                if cls.MsgBox_BildErsetzen_0_btnOK_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_BildErsetzen_0_btnOK_0) 
                                                                        ResultValue = True  
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue                                                                                                                                      
                                                
                                                        
                                                elif cls.MsgBox_SpeichernUnterBestatigen_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_SpeichernUnterBestatigen_0):
                                                                if cls.MsgBox_SpeichernUnterBestatigen_0_btnJa_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_SpeichernUnterBestatigen_0_btnJa_0) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                        
                                                elif cls.ExportVorlage_0.Exists:
                                                        if cls.MessagWriter(cls.ExportVorlage_0):
                                                                if cls.ExportVorlage_0_btnJa.Exists:
                                                                        cls.ClickButton(cls.ExportVorlage_0_btnJa) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.ExportVorlage_0_btnOk_0.Exists:
                                                                        cls.ClickButton(cls.ExportVorlage_0_btnOk_0) 
                                                                        ResultValue = True
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                            
                                                        
                                                if cls.MsgBox_PositionLoschen.Exists:        
                                                        if cls.MessagWriter(cls.MsgBox_PositionLoschen):
                                                                if cls.MsgBox_PositionLoschen_btnJa.Exists:
                                                                        cls.ClickButton(cls.MsgBox_PositionLoschen_btnJa) 
                                                                        ResultValue = True   
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                        
                                                if cls.MsgBox_Absturz.Exists:        
                                                        if cls.MessagWriter(cls.MsgBox_Absturz):
                                                                if cls.MsgBox_btnOK.Exists:
                                                                        cls.ClickButton(cls.MsgBox_btnOK) 
                                                                        ResultValue = True                                                                        
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue                                                                        
                                                                               
                                                                        
                                                elif cls.OffnenFile_0.Exists:
                                                        if cls.MessagWriter(cls.OffnenFile_0):
                                                                if cls.OffnenFile_0_btnOk.Exists:
                                                                        cls.ClickButton(cls.OffnenFile_0_btnOk) 
                                                                        ResultValue = True
                                                
                                        elif YesOrNo == 'NO':
                                                if cls.MsgBox_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_0):
                                                                if cls.MsgBox_0_btnNichtSpeichern.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnNichtSpeichern)
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.MsgBox_0_btnNein_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnNein_0)
                                                                        ResultValue = True 
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.MsgBox_0_btnNein_1.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnNein_1)
                                                                        ResultValue = True 
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif cls.MsgBox_0_btnNein_2.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnNein_2)
                                                                        ResultValue = True 
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue                                                
                                                
                                                        
                                                elif cls.MsgBox_1.Exists:       
                                                        if cls.MessagWriter(cls.MsgBox_1):
                                                                if cls.MsgBox_1_btnNein_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_1_btnNein_0) 
                                                                        ResultValue = True      
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue                                                
                                                

                                                elif cls.MsgBox_2.Exists:    
                                                        if cls.MessagWriter(cls.MsgBox_2):
                                                                if cls.MsgBox_2_btnNein_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_2_btnNein_0) 
                                                                        ResultValue = True      
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue                                                                                                 
                                                
                                                                                                
                                                elif cls.Msgbox_3.Exists:
                                                        if cls.MessagWriter(cls.Msgbox_3):
                                                                if cls.Msgbox_3_btnNein_0.Exists:
                                                                        cls.ClickButton(cls.Msgbox_3_btnNein_0) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue                                                 
                                                
                                                        
                                                elif cls.MsgBox_SpeichernUnterBestatigen_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_SpeichernUnterBestatigen_0):
                                                                if cls.MsgBox_SpeichernUnterBestatigen_0_btnNein_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_SpeichernUnterBestatigen_0_btnNein_0) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue 
                                                        
                                                if cls.MsgBox_PositionLoschen.Exists:        
                                                        if cls.MessagWriter(cls.MsgBox_PositionLoschen):
                                                                if cls.MsgBox_PositionLoschen_btnNein.Exists:
                                                                        cls.ClickButton(cls.MsgBox_PositionLoschen_btnNein) 
                                                                        ResultValue = True   
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue                                                                                                          
                                                
                                                
                                        elif YesOrNo == 'Abbrechen':  
                                                if cls.MsgBox_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_0):
                                                                if  cls.MsgBox_0_btnAbbrechen_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnAbbrechen_0)
                                                                        ResultValue = True     
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue 
                                                                elif  cls.MsgBox_0_btnAbbrechen_1.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnAbbrechen_1)
                                                                        ResultValue = True     
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue  
                                                                elif  cls.MsgBox_0_btnAbbrechen_2.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnAbbrechen_2)
                                                                        ResultValue = True     
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif  cls.MsgBox_0_btnAbbrechen_3.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnAbbrechen_3)
                                                                        ResultValue = True     
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue                                                

                                                
                                                elif cls.MsgBox_1.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_1):
                                                                if  cls.MsgBox_1_btnAbbrechen_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_1_btnAbbrechen_0)
                                                                        ResultValue = True     
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                elif  cls.MsgBox_1_btnAbbrechen_1.Exists:
                                                                        cls.ClickButton(cls.MsgBox_1_btnAbbrechen_1)
                                                                        ResultValue = True  
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue    
                                                
                                                        
                                                elif cls.MsgBox_2.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_2):
                                                                if  cls.MsgBox_2_btnAbbrechen_0.Exists:
                                                                        cls.ClickButton(cls.MsgBox_1_btnAbbrechen_0)
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                        
                                                                        
                                        elif YesOrNo == 'Authorisieren':  
                                                if cls.MsgBox_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_0):
                                                                if cls.MsgBox_0_btnAuthorisieren.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnAuthorisieren) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                        
                                                                        
                                                                        
                                        elif YesOrNo == 'Importieren':  
                                                if cls.MsgBox_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_0):
                                                                if cls.MsgBox_0_btnImportieren.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnImportieren) 
                                                                        ResultValue = True
                                                                        Delay(cls.getTime('SmallTime')) 
                                                                        return ResultValue
                                                                        
                                                                        
                                                                       
                                        elif YesOrNo == 'JetztEinrichten':  
                                                if cls.MsgBox_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_0):
                                                                if cls.MsgBox_0_btnJetztEinrichten.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnJetztEinrichten)
                                                                        ResultValue = True
                                                                        
                                                                        
                                                                        
                                        elif YesOrNo == 'PostfachAnlegen':  
                                                if cls.MsgBox_0.Exists:
                                                        if cls.MessagWriter(cls.MsgBox_0):
                                                                if cls.MsgBox_0_btnPostfachAnlegen.Exists:
                                                                        cls.ClickButton(cls.MsgBox_0_btnPostfachAnlegen)
                                                                        ResultValue = True
                                                                        
                                                                        
                                                                         
                        elif Type == 'WaitForMsgBox': 
                                MCounter = MCounter * 10
                                while not (cls.MsgBox_0.Exists or cls.MsgBox_1.Exists or cls.MsgBox_2.Exists or cls.Msgbox_3.Exists or cls.MsgBox_BildHinzufugen_0.Exists or cls.MsgBox_BildHinzufugen_1.Exists or cls.MsgBox_BildErsetzen_0.Exists or cls.MsgBox_SpeichernUnterBestatigen_0.Exists or cls.Msgbox_neue_0.Exists or cls.Msgbox_neue_1.Exists or cls.MsgBox_PositionLoschen.Exists or cls.ExportVorlage_0.Exists or cls.Msgbox_3_StatisticError_btnOK_0.Exists or cls.Msgbox_3_StatisticError_btnOK_1.Exists or cls.MsgBox_Absturz.Exists  or cls.OffnenFile_0.Exists):
                                        if Counter > MCounter :
                                                break
                                        Delay(cls.getTime())
                                        Counter +=1
                                 
                                ResultValue = True          
                        
                         
                        elif Type == 'WaitingToMsgBoxInVisible': 
                                MCounter = MCounter * 10  
                                Delay(cls.getTime('SmallTime'))                                              
                                while (cls.MsgBox_0.Exists or cls.MsgBox_1.Exists or cls.MsgBox_2.Exists or cls.Msgbox_3.Exists or cls.MsgBox_BildHinzufugen_0.Exists or cls.MsgBox_BildHinzufugen_1.Exists or cls.MsgBox_BildErsetzen_0.Exists or cls.MsgBox_SpeichernUnterBestatigen_0.Exists or cls.Msgbox_neue_0.Exists or cls.Msgbox_neue_1.Exists or cls.MsgBox_PositionLoschen.Exists or cls.ExportVorlage_0.Exists or cls.Msgbox_3_StatisticError_btnOK_0.Exists or cls.Msgbox_3_StatisticError_btnOK_1.Exists or cls.MsgBox_Absturz.Exists  or cls.OffnenFile_0.Exists):
                                        if Counter > MCounter :
                                                break
                                        Delay(cls.getTime())
                                        Counter +=1 
                                   
                                ResultValue = True                                                                                       
        
                        
                        elif Type == 'WaitingToMessagsProgressbarInvisible': 
                                while cls.MsgBox_1_Progressbar_0.Exists or cls.Msgbox_3_Progressbar_0.Exists:
                                        Delay(cls.getTime())
                                        if IsWaitingToMessagsProgressbarInvisibleCheckMessagebox:
                                                cls.MessagboxManager()
                                ResultValue = True
                        
                        return ResultValue         

                except Exception as exp:
                        cls.TestResult(TypeOfResultObject = 'Info', MoreInfo = str(exp))
#--
#...
#--
        def MessagWriter(cls,MsgBox):
            
                try: 
                
                        Message = 'Unbekannt Massage'
                        
                        if MsgBox == cls.MsgBox_0:
                                if cls.MsgBox_0_Body.WPFObject("ContentControl", "", 1).WPFObject("_TemplateGeneratorControl", "", 1).WPFObject("MessageBoxDialogContentView", "", 1).WPFObject("LayoutGroup", "", 1).WPFObject("ContentControl", "", 1).WPFObject("LayoutGroup", "", 1).WPFObject("MarkdownContentControl", "", 1).Exists:
                                        Message = cls.MsgBox_0_Body.WPFObject("ContentControl", "", 1).WPFObject("_TemplateGeneratorControl", "", 1).WPFObject("MessageBoxDialogContentView", "", 1).WPFObject("LayoutGroup", "", 1).WPFObject("ContentControl", "", 1).WPFObject("LayoutGroup", "", 1).WPFObject("MarkdownContentControl", "", 1).MarkdownText.OleValue
                                elif cls.MsgBox_0_Body.WPFObject("ContentControl", "", 1).WPFObject("_TemplateGeneratorControl", "", 1).WPFObject("MessageBoxDialogContentView", "", 1).WPFObject("Grid", "", 1).WPFObject("ContentControl", "", 1).WPFObject("LayoutGroup", "", 1).WPFObject("MarkdownContentControl", "", 1).Exists:
                                        Message = cls.MsgBox_0_Body.WPFObject("ContentControl", "", 1).WPFObject("_TemplateGeneratorControl", "", 1).WPFObject("MessageBoxDialogContentView", "", 1).WPFObject("Grid", "", 1).WPFObject("ContentControl", "", 1).WPFObject("LayoutGroup", "", 1).WPFObject("MarkdownContentControl", "", 1).MarkdownText.OleValue
                                 
                        elif MsgBox == cls.MsgBox_1:
                                Message = cls.MsgBox_1_Body.Find('AutomationId', 'ContentText',10).ObjectIdentifier   

                        elif MsgBox == cls.MsgBox_2:
                                MessageObjects = cls.MsgBox_2.FindAll('WndClass', 'Static', 10) 
                        
                                for ItemIndex in range(0,len(MessageObjects), 1):
                                    if MessageObjects[ItemIndex].WndCaption != '':
                                            Message = MessageObjects[ItemIndex].WndCaption

                        elif MsgBox == cls.Msgbox_3:
                                Message = cls.Msgbox_3_Body.Find('AutomationId', 'ContentText',10).ObjectIdentifier

                        elif MsgBox == cls.Msgbox_neue_0:
                                if aqObject.IsSupported(cls.Msgbox_neue_0_Data.DataContext, 'OleValue'):
                                        Message = cls.Msgbox_neue_0_Data.DataContext.OleValue
                                        
                                elif aqObject.IsSupported(cls.Msgbox_neue_0_Data.DataContext.Message, 'OleValue'):
                                        Message = cls.Msgbox_neue_0_Data.DataContext.Message.OleValue
                        
                        elif MsgBox == cls.Msgbox_neue_1:
                                Message = cls.Msgbox_neue_1_Data.FindChild('ClrClassName', 'TextBlock', 2).Text.OleValue                       
                        
                        elif MsgBox == cls.MsgBox_BildHinzufugen_0:
                                Message = cls.MsgBox_BildHinzufugen_0_Body.Find('AutomationId', 'ContentText',10).ObjectIdentifier  
                
                        elif MsgBox == cls.MsgBox_BildHinzufugen_1:
                                Message = cls.MsgBox_BildHinzufugen_1_Body.Find('AutomationId', 'ContentText',10).ObjectIdentifier 
                                                
                        elif MsgBox == cls.MsgBox_BildErsetzen_0:
                                Message = cls.MsgBox_BildErsetzen_0_Body.Find('AutomationId', 'ContentText',10).ObjectIdentifier  
                
                        elif MsgBox == cls.MsgBox_SpeichernUnterBestatigen_0:
                                Message = cls.MsgBox_SpeichernUnterBestatigen_0_Body.Find('AutomationId', 'ContentText',10).ObjectIdentifier
                                
                        elif MsgBox == cls.MsgBox_Absturz:
                                Message = cls.MsgBox_Absturz.Window('Static', '',2).WndCaption
                

                        
                        if str(type(Message)) == "<class '__main__.IDispatchWrapper_AnyUsageStub'>":
                                        Message = 'Unbekannt Massage'
                        
                        Message = Message.replace("Ö", "O")
                        Message = Message.replace("ö", "o")
                        Message = Message.replace("Ü", "U")
                        Message = Message.replace("ü", "u")
                        Message = Message.replace("Ä", "A")
                        Message = Message.replace("ä", "a")
                        Message = Message.replace("ß", "ss")
                        Message = Message.replace("_", " ")
                
                        cls.TestResult(TypeOfResultObject = 'MessageManager', MoreInfo = ' ! ' + Message)          

                        return True

                except Exception as exp:
                        cls.TestResult(TypeOfResultObject = 'Info', MoreInfo = str(exp)) 
                

                        
