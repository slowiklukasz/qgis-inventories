from qgis.PyQt.QtWidgets import *
from .dlg_errors_ui import Ui_dlg_errors


class DlgErrors(QDialog, Ui_dlg_errors):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
