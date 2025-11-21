help_window = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>589</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>500</width>
    <height>400</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>800</width>
    <height>700</height>
   </size>
  </property>
  <property name="cursor">
   <cursorShape>PointingHandCursor</cursorShape>
  </property>
  <property name="windowTitle">
   <string>Справка</string>
  </property>
  <property name="layoutDirection">
   <enum>Qt::LeftToRight</enum>
  </property>
  <layout class="QGridLayout" name="gridLayout_2">
   <item row="0" column="0">
    <layout class="QGridLayout" name="gridLayout" rowstretch="1,0">
     <property name="leftMargin">
      <number>10</number>
     </property>
     <property name="topMargin">
      <number>10</number>
     </property>
     <property name="rightMargin">
      <number>10</number>
     </property>
     <property name="bottomMargin">
      <number>10</number>
     </property>
     <item row="1" column="0" colspan="2">
      <widget class="QPushButton" name="return_btn">
       <property name="text">
        <string>Назад</string>
       </property>
      </widget>
     </item>
     <item row="0" column="0" colspan="2">
      <widget class="QTextBrowser" name="textBrowser"/>
     </item>
    </layout>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""