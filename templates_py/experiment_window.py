experiment_window = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>950</width>
    <height>600</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>950</width>
    <height>600</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Эксперимент</string>
  </property>
  <layout class="QGridLayout" name="gridLayout_2">
   <item row="0" column="0">
    <layout class="QGridLayout" name="gridLayout" columnstretch="2,1">
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
     <item row="1" column="0">
      <widget class="QFrame" name="frame">
       <property name="cursor">
        <cursorShape>PointingHandCursor</cursorShape>
       </property>
       <property name="styleSheet">
        <string notr="true">background: rgb(255, 255, 255)</string>
       </property>
       <property name="frameShape">
        <enum>QFrame::StyledPanel</enum>
       </property>
       <property name="frameShadow">
        <enum>QFrame::Raised</enum>
       </property>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QTabWidget" name="tabWidget">
       <property name="currentIndex">
        <number>1</number>
       </property>
       <widget class="QWidget" name="tab_3">
        <attribute name="title">
         <string>Главное</string>
        </attribute>
        <widget class="QLabel" name="label">
         <property name="geometry">
          <rect>
           <x>0</x>
           <y>20</y>
           <width>71</width>
           <height>16</height>
          </rect>
         </property>
         <property name="text">
          <string>Название</string>
         </property>
         <property name="alignment">
          <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
         </property>
        </widget>
        <widget class="QLineEdit" name="expname_lineEdit">
         <property name="geometry">
          <rect>
           <x>80</x>
           <y>10</y>
           <width>191</width>
           <height>31</height>
          </rect>
         </property>
        </widget>
        <widget class="QLabel" name="label_2">
         <property name="geometry">
          <rect>
           <x>0</x>
           <y>50</y>
           <width>51</width>
           <height>20</height>
          </rect>
         </property>
         <property name="text">
          <string>Среда</string>
         </property>
         <property name="alignment">
          <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
         </property>
        </widget>
        <widget class="QComboBox" name="env_comboBox">
         <property name="geometry">
          <rect>
           <x>80</x>
           <y>50</y>
           <width>201</width>
           <height>26</height>
          </rect>
         </property>
         <property name="cursor">
          <cursorShape>PointingHandCursor</cursorShape>
         </property>
        </widget>
        <widget class="QLabel" name="label_3">
         <property name="geometry">
          <rect>
           <x>0</x>
           <y>180</y>
           <width>60</width>
           <height>16</height>
          </rect>
         </property>
         <property name="text">
          <string>Тела:</string>
         </property>
         <property name="alignment">
          <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
         </property>
        </widget>
        <widget class="QTextBrowser" name="figures_textbrowser">
         <property name="geometry">
          <rect>
           <x>10</x>
           <y>210</y>
           <width>271</width>
           <height>251</height>
          </rect>
         </property>
        </widget>
        <widget class="QPushButton" name="add_figure_btn">
         <property name="geometry">
          <rect>
           <x>10</x>
           <y>470</y>
           <width>271</width>
           <height>32</height>
          </rect>
         </property>
         <property name="text">
          <string>Добавить тело</string>
         </property>
        </widget>
       </widget>
       <widget class="QWidget" name="tab_4">
        <attribute name="title">
         <string>Настройки</string>
        </attribute>
        <widget class="QPushButton" name="save_pushButton">
         <property name="geometry">
          <rect>
           <x>10</x>
           <y>10</y>
           <width>221</width>
           <height>32</height>
          </rect>
         </property>
         <property name="text">
          <string>Сохранить</string>
         </property>
        </widget>
        <widget class="QPushButton" name="escape_pushButton">
         <property name="geometry">
          <rect>
           <x>10</x>
           <y>130</y>
           <width>221</width>
           <height>32</height>
          </rect>
         </property>
         <property name="text">
          <string>Выйти</string>
         </property>
        </widget>
        <widget class="QPushButton" name="delete_btn">
         <property name="geometry">
          <rect>
           <x>10</x>
           <y>50</y>
           <width>221</width>
           <height>32</height>
          </rect>
         </property>
         <property name="text">
          <string>Удалить</string>
         </property>
        </widget>
        <widget class="QLabel" name="label_4">
         <property name="geometry">
          <rect>
           <x>10</x>
           <y>330</y>
           <width>101</width>
           <height>16</height>
          </rect>
         </property>
         <property name="text">
          <string>Комментарии</string>
         </property>
        </widget>
        <widget class="QPlainTextEdit" name="comments_textEdit">
         <property name="geometry">
          <rect>
           <x>10</x>
           <y>350</y>
           <width>231</width>
           <height>161</height>
          </rect>
         </property>
        </widget>
        <widget class="QPushButton" name="help_btn">
         <property name="geometry">
          <rect>
           <x>10</x>
           <y>90</y>
           <width>221</width>
           <height>32</height>
          </rect>
         </property>
         <property name="text">
          <string>Помощь</string>
         </property>
        </widget>
       </widget>
      </widget>
     </item>
     <item row="0" column="0" colspan="2">
      <widget class="QLabel" name="status">
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
    </layout>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""