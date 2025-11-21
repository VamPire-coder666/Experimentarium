ballistic_search = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>450</width>
    <height>200</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>450</width>
    <height>200</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>450</width>
    <height>200</height>
   </size>
  </property>
  <property name="cursor">
   <cursorShape>PointingHandCursor</cursorShape>
  </property>
  <property name="windowTitle">
   <string>Введите координату или время</string>
  </property>
  <widget class="QComboBox" name="key_comboBox">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>241</width>
     <height>26</height>
    </rect>
   </property>
   <item>
    <property name="text">
     <string>Координата X</string>
    </property>
   </item>
   <item>
    <property name="text">
     <string>Время</string>
    </property>
   </item>
  </widget>
  <widget class="QSpinBox" name="value_spinBox">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>40</y>
     <width>411</width>
     <height>24</height>
    </rect>
   </property>
   <property name="maximum">
    <number>1000000000</number>
   </property>
  </widget>
  <widget class="QPushButton" name="search_btn">
   <property name="geometry">
    <rect>
     <x>160</x>
     <y>70</y>
     <width>113</width>
     <height>32</height>
    </rect>
   </property>
   <property name="text">
    <string>Посмотреть</string>
   </property>
  </widget>
  <widget class="QTextBrowser" name="result_textBrowser">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>110</y>
     <width>421</width>
     <height>81</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""