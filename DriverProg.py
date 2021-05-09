# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 01:43:17 2020

@author: evren
"""

from PyQt5 import QtWidgets

from Design import Ui_Form

import sys

class mywindow(QtWidgets.QWidget):
    
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
app=QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())