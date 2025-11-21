main_window = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
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
  <property name="windowTitle">
   <string>Лаборатория</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout_2">
    <item row="0" column="0">
     <layout class="QGridLayout" name="gridLayout" columnstretch="1,2,1">
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
      <item row="3" column="1">
       <widget class="QPushButton" name="my_experiments_btn">
        <property name="text">
         <string>Мои эксперименты</string>
        </property>
       </widget>
      </item>
      <item row="10" column="1">
       <spacer name="verticalSpacer">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>20</width>
          <height>40</height>
         </size>
        </property>
       </spacer>
      </item>
      <item row="6" column="1">
       <widget class="QPushButton" name="help_btn">
        <property name="text">
         <string>Помощь</string>
        </property>
       </widget>
      </item>
      <item row="9" column="1">
       <spacer name="verticalSpacer_3">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>20</width>
          <height>40</height>
         </size>
        </property>
       </spacer>
      </item>
      <item row="4" column="1">
       <widget class="QPushButton" name="new_experiment_btn">
        <property name="text">
         <string>Новый эксперимент</string>
        </property>
       </widget>
      </item>
      <item row="0" column="0" colspan="3">
       <widget class="QLabel" name="hello_label">
        <property name="styleSheet">
         <string notr="true"/>
        </property>
        <property name="text">
         <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:24pt;&quot;&gt;Добро пожаловать в лабораторию&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignCenter</set>
        </property>
       </widget>
      </item>
      <item row="7" column="1">
       <widget class="QPushButton" name="escape_btn">
        <property name="text">
         <string>Выйти из аккаунта</string>
        </property>
       </widget>
      </item>
      <item row="11" column="0" colspan="3">
       <widget class="QLabel" name="label">
        <property name="text">
         <string>Regis Inc 2025. Все права защищены</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignCenter</set>
        </property>
       </widget>
      </item>
      <item row="1" column="0">
       <spacer name="verticalSpacer_2">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>20</width>
          <height>40</height>
         </size>
        </property>
       </spacer>
      </item>
      <item row="8" column="1">
       <widget class="QPushButton" name="close_btn">
        <property name="text">
         <string>Закрыть</string>
        </property>
       </widget>
      </item>
      <item row="5" column="1">
       <widget class="QPushButton" name="music_btn">
        <property name="text">
         <string>Музыка</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>37</height>
    </rect>
   </property>
   <widget class="QMenu" name="name_menubar">
    <property name="title">
     <string>Аккаунт</string>
    </property>
    <addaction name="escape_action"/>
    <addaction name="close_action"/>
   </widget>
   <widget class="QMenu" name="experiments_menu">
    <property name="title">
     <string>Эксперименты</string>
    </property>
    <addaction name="new_exp_action"/>
    <addaction name="my_exp_action"/>
   </widget>
   <addaction name="name_menubar"/>
   <addaction name="experiments_menu"/>
  </widget>
  <action name="escape_action">
   <property name="text">
    <string>Выйти</string>
   </property>
  </action>
  <action name="new_exp_action">
   <property name="text">
    <string>Новый эксперимент</string>
   </property>
  </action>
  <action name="my_exp_action">
   <property name="text">
    <string>Мои эксперименты</string>
   </property>
  </action>
  <action name="close_action">
   <property name="text">
    <string>Закрыть</string>
   </property>
  </action>
 </widget>
 <tabstops>
  <tabstop>my_experiments_btn</tabstop>
  <tabstop>new_experiment_btn</tabstop>
  <tabstop>help_btn</tabstop>
 </tabstops>
 <resources/>
 <connections/>
</ui>
"""