import sys

def te():
    print("ich bin te")
    
methode = "MainMenu_Start_" + "BenutzerWechseln" + "_Test"
val = te
setattr(sys.modules[__name__], methode,val)

MainMenu_Start_BenutzerWechseln_Test()