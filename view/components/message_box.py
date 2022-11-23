from PyQt5.QtWidgets import (
    QMessageBox
)

from PyQt5.QtGui import (
    QPixmap
)

from PyQt5 import QtCore

from view.resource import resource


MESSAG_QUESTION = 0   # mensaje de pregunta al usuario 
MESSAG_INFORMATION = 1 # mensaje de información al usuario 
MESSAG_WARNING = 2	    # enum mensaje de advertencia al usuario 
MESSAG_CRITICAL = 3   # enum mensaje crítico al usuario 
MESSAG_OK_DELETE = 4    # enum mensaje de autorización para borrar 

def showGenericMessage( _parent,_type,_title,_text, _informativeText = "", _detailText = "", _buttons ={}):
    messageBox = QMessageBox(_parent)
    if _parent != None :
        messageBox.setWindowModality(QtCore.Qt.WindowModal)
        
    messageBox.setWindowTitle(_title);
    messageBox.setText(_text);

    if len(_informativeText)!=0:
        messageBox.setInformativeText(_informativeText);

    if len(_detailText)!=0:
        messageBox.setDetailedText(_detailText)
        messageBox.setWindowFlags(messageBox.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
    
    px = None
    
    if _type == MESSAG_INFORMATION:
        messageBox.setIcon(QMessageBox.Information)
        px = QPixmap(":/img/informacion.png")
    elif _type == MESSAG_WARNING:
        messageBox.setIcon(QMessageBox.Warning)
        px = QPixmap(":/img/Advertencia.png")
    elif _type == MESSAG_OK_DELETE:
        pass
    elif _type == MESSAG_QUESTION:
        messageBox.setIcon(QMessageBox.Question)
        px = QPixmap(":/img/Ayuda.png")
    elif _type == MESSAG_CRITICAL:
        messageBox.setIcon(QMessageBox.Critical)
        px = QPixmap(":/img/Error.png")
    
    if px != None:
        px.scaled(150,150)
        messageBox.setIconPixmap(px)
    
    return messageBox
    

def functionalityForNextVersion( _parent):
    pass



