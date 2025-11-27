from pycode.ExperimentClasses import ExperimentWindow


class MKT_ExpWindow(ExperimentWindow):
    """ Основной класс МКТ-экспериментов """
    
    def __init__(self, parent, template):
        super().__init__(parent, template)
        self.initUI()
    
    def initUI(self):
        super().initUI()
        
        ...