ballistic_show = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>800</width>
    <height>600</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>100000</width>
    <height>100000</height>
   </size>
  </property>
  <property name="cursor">
   <cursorShape>ArrowCursor</cursorShape>
  </property>
  <property name="windowTitle">
   <string>Полёт</string>
  </property>
  <property name="styleSheet">
   <string notr="true">QWidget {
	background-color: rgb(255, 255, 255)
}</string>
  </property>
  <layout class="QGridLayout" name="gridLayout_2">
   <item row="0" column="0">
    <layout class="QGridLayout" name="gridLayout">
     <item row="0" column="0">
      <widget class="QTabWidget" name="tabWidget">
       <property name="cursor">
        <cursorShape>ArrowCursor</cursorShape>
       </property>
       <property name="currentIndex">
        <number>3</number>
       </property>
       <widget class="QWidget" name="tab_1">
        <attribute name="title">
         <string>Полёт</string>
        </attribute>
       </widget>
       <widget class="QWidget" name="tab_2">
        <attribute name="title">
         <string>График</string>
        </attribute>
        <layout class="QGridLayout" name="gridLayout_4">
         <item row="0" column="0">
          <widget class="PlotWidget" name="graphic"/>
         </item>
        </layout>
       </widget>
       <widget class="QWidget" name="tab_3">
        <attribute name="title">
         <string>Результаты</string>
        </attribute>
        <widget class="QTextBrowser" name="result_textBrowser">
         <property name="geometry">
          <rect>
           <x>5</x>
           <y>11</y>
           <width>721</width>
           <height>531</height>
          </rect>
         </property>
        </widget>
       </widget>
       <widget class="QWidget" name="tab_4">
        <attribute name="title">
         <string>Функции</string>
        </attribute>
        <widget class="QComboBox" name="key_comboBox">
         <property name="geometry">
          <rect>
           <x>10</x>
           <y>20</y>
           <width>691</width>
           <height>26</height>
          </rect>
         </property>
        </widget>
        <widget class="QSpinBox" name="value_spinBox">
         <property name="geometry">
          <rect>
           <x>10</x>
           <y>60</y>
           <width>381</width>
           <height>24</height>
          </rect>
         </property>
        </widget>
        <widget class="QPushButton" name="search_btn">
         <property name="geometry">
          <rect>
           <x>330</x>
           <y>100</y>
           <width>113</width>
           <height>32</height>
          </rect>
         </property>
         <property name="cursor">
          <cursorShape>PointingHandCursor</cursorShape>
         </property>
         <property name="text">
          <string>Посмотреть</string>
         </property>
        </widget>
        <widget class="QTextBrowser" name="search_textBrowser">
         <property name="geometry">
          <rect>
           <x>5</x>
           <y>151</y>
           <width>751</width>
           <height>381</height>
          </rect>
         </property>
        </widget>
       </widget>
      </widget>
     </item>
    </layout>
   </item>
  </layout>
 </widget>
 <customwidgets>
  <customwidget>
   <class>PlotWidget</class>
   <extends>QGraphicsView</extends>
   <header>pyqtgraph</header>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
"""