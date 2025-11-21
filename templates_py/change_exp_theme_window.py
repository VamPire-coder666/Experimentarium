change_exp_theme_window = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>80</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>400</width>
    <height>80</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>400</width>
    <height>80</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">QWidget {
	background-color: &quot;black&quot;;
}

/* Стиль для кнопок */
QPushButton {
    background-color: #2a3943;
    color: #a9b7c6;
    border: 1px solid #555;
    border-radius: 5px;
    padding: 5px 10px;
    font-family: &quot;monaco&quot;, monospace;
}

/* Стиль для кнопок при наведении мышки */
QPushButton:hover {
    border: 2px solid #3498db; /* Синяя рамка */
    border-radius: 10px;
}

/* Стиль для кнопок при клике мышки */
QPushButton:pressed {
    border: 2px solid #2980b9; /* Тёмно-синяя рамка */
    border-radius: 10px;
}

/* Стиль для заголовков */
QLabel {
    color: #a9b7c6;
    font-family: &quot;monaco&quot;, monospace;
}

/* Стиль для строки ввода */
QLineEdit {
    background-color: #2a3943;
    color: #a9b7c6;
    border: 1px solid #555;
    border-radius: 5px;
    padding: 5px 10px;
    font-family: &quot;monaco&quot;, monospace;
}
          
/* Стиль для строки ввода при наведении мыши */
QLineEdit:hover {
    border: 2px solid #3498db; /* Синяя рамка */
    border-radius: 10px;
}</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>341</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>Как показывать результат эксперимента?</string>
   </property>
  </widget>
  <widget class="QPushButton" name="one_btn">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>40</y>
     <width>151</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Одно окно</string>
   </property>
  </widget>
  <widget class="QPushButton" name="many_btn">
   <property name="geometry">
    <rect>
     <x>200</x>
     <y>40</y>
     <width>161</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Несколько окон</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""