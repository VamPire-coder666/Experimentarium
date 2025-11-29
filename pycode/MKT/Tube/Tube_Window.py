from pycode.MKT.MKT_ExpWindow import MKT_ExpWindow
from templates.MKT_Tube_window import MKT_Tube_window
from PyQt6.QtWidgets import QSlider, QSpinBox, QLCDNumber, QTabWidget
from pycode.MKT.Ideal_Gas import Ideal_Gas
from .Animation.Tube import Tube
from .NotAllParametrsError import NotAllParametrsError


class Tube_Window(MKT_ExpWindow):
    """ Класс для МКТ-экспериментов типа "Труба" """
    
    def __init__(self, parent):
        super().__init__(parent, MKT_Tube_window)
        self.initUI()
    
    def initUI(self):
        super().initUI()
        
        self.gas = Ideal_Gas(self.Mr_spinBox.value(), self.expname_lineEdit.text())
        self.T_Slider.valueChanged.connect(self.update_T)
        self.Mr_spinBox.valueChanged.connect(self.edit_gas)
        self.start_btn.clicked.connect(self.start)
        
        self.tube_tabWidget.setStyleSheet('''background-color: "black";
                                          border: 1px solid #555;
                                          border-radius: 5px;
                                          padding: 5px 10px;''')
    
    def edit_gas(self):
        self.gas = Ideal_Gas(self.Mr_spinBox.value(), self.expname_lineEdit.text())
    
    def update_T(self):
        self.T_lcdNumber.display(self.T_Slider.value())
        self.avgV_lcdNumber.display(self.gas.get_avgV(self.T_Slider.value()))
    
    def start(self):
        error_parametrs = []
        if not self.Mr_spinBox.value():
            error_parametrs.append('Mr')
        if not self.m_spinBox.value():
            error_parametrs.append('m')
        if not self.V_spinBox.value():
            error_parametrs.append('V')
        if error_parametrs:
            raise NotAllParametrsError(self, *error_parametrs)
        else:
            self.status.setText('')
            self.status.setStyleSheet('opacity: 1;')
            if len(self.tube_tabWidget):
                self.tube_tabWidget.removeTab(0)
            self.tube_tabWidget.addTab(Tube(self), "Труба")
            p = self.gas.get_P(
                self.V_spinBox.value(),
                self.T_Slider.value(),
                mode='VT'
            )
            self.P_lcdNumber.display(p)
