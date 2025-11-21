registration = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>625</width>
    <height>575</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Регистрация</string>
  </property>
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
     <item row="10" column="1">
      <widget class="QPushButton" name="help_btn">
       <property name="text">
        <string>Помощь</string>
       </property>
      </widget>
     </item>
     <item row="4" column="0">
      <widget class="QLabel" name="label_6">
       <property name="text">
        <string>Фамилия</string>
       </property>
       <property name="alignment">
        <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
       </property>
      </widget>
     </item>
     <item row="3" column="1">
      <widget class="QLineEdit" name="name_lineEdit"/>
     </item>
     <item row="3" column="0">
      <widget class="QLabel" name="label_5">
       <property name="text">
        <string>Имя</string>
       </property>
       <property name="alignment">
        <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
       </property>
      </widget>
     </item>
     <item row="6" column="1">
      <widget class="QLineEdit" name="password_lineEdit">
       <property name="inputMethodHints">
        <set>Qt::ImhHiddenText|Qt::ImhNoAutoUppercase|Qt::ImhNoPredictiveText|Qt::ImhSensitiveData</set>
       </property>
       <property name="echoMode">
        <enum>QLineEdit::Password</enum>
       </property>
      </widget>
     </item>
     <item row="11" column="1">
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
     <item row="8" column="1">
      <widget class="QPushButton" name="sign_up_btn">
       <property name="text">
        <string>Зарегистрироваться</string>
       </property>
      </widget>
     </item>
     <item row="5" column="0">
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>Логин</string>
       </property>
       <property name="alignment">
        <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
       </property>
      </widget>
     </item>
     <item row="5" column="1">
      <widget class="QLineEdit" name="login_lineEdit"/>
     </item>
     <item row="1" column="0" colspan="3">
      <widget class="QLabel" name="label_1">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:24pt;&quot;&gt;Добро пожаловать!&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
       <property name="textFormat">
        <enum>Qt::AutoText</enum>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
      </widget>
     </item>
     <item row="6" column="2">
      <widget class="QCheckBox" name="checkBoxShowPassword">
       <property name="text">
        <string>Показать пароль</string>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
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
     <item row="6" column="0">
      <widget class="QLabel" name="label_4">
       <property name="text">
        <string>Пароль</string>
       </property>
       <property name="alignment">
        <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
       </property>
      </widget>
     </item>
     <item row="4" column="1">
      <widget class="QLineEdit" name="surname_lineEdit"/>
     </item>
     <item row="2" column="0" colspan="3">
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Для использовани приложения войдите или зарегистрируйтесь</string>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
      </widget>
     </item>
     <item row="9" column="1">
      <widget class="QPushButton" name="return_btn">
       <property name="text">
        <string>Назад</string>
       </property>
      </widget>
     </item>
     <item row="12" column="0" colspan="3">
      <widget class="QLabel" name="label">
       <property name="text">
        <string>Regis Inc 2025. Все права защищены</string>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
      </widget>
     </item>
    </layout>
   </item>
  </layout>
 </widget>
 <tabstops>
  <tabstop>name_lineEdit</tabstop>
  <tabstop>surname_lineEdit</tabstop>
  <tabstop>login_lineEdit</tabstop>
  <tabstop>password_lineEdit</tabstop>
  <tabstop>sign_up_btn</tabstop>
  <tabstop>return_btn</tabstop>
 </tabstops>
 <resources/>
 <connections/>
</ui>
"""