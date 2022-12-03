import sys

from PyQt5.QtWidgets import (
    QApplication
)

from PyQt5.QtGui import (
    QIcon
)

from PyQt5.QtCore import (
    QFile, QTextStream
)

from view.app import App
from view.resource import resource

if __name__ == "__main__":
    
    f = QFile(":css/style.css")
    stylesheet =""
    if  f.exists():
        f.open(QFile.ReadOnly | QFile.Text)
        ts = QTextStream(f)
        stylesheet = ts.readAll()
    
    app = QApplication(sys.argv)
    win = App()
    #win.showMaximized()
    win.showFullScreen()
    win.setWindowIcon(QIcon(":/img/falta.png"))
    win.setWindowTitle("SugarLM-Regress")
    win.setStyleSheet(stylesheet)
    sys.exit(app.exec())