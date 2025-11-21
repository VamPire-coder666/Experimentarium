ballistic_exp_window = """<?xml version="1.0" encoding="UTF-8"?>
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
  <property name="maximumSize">
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
    <layout class="QGridLayout" name="gridLayout" columnstretch="2,0">
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
     <item row="0" column="0" colspan="2">
      <widget class="QLabel" name="status">
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
     <item row="1" column="0" colspan="2">
      <widget class="QTabWidget" name="tabWidget">
       <property name="currentIndex">
        <number>0</number>
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
        <widget class="QLabel" name="figure_label">
         <property name="geometry">
          <rect>
           <x>620</x>
           <y>10</y>
           <width>60</width>
           <height>16</height>
          </rect>
         </property>
         <property name="text">
          <string>Тело:</string>
         </property>
        </widget>
        <widget class="QLabel" name="label_5">
         <property name="geometry">
          <rect>
           <x>10</x>
           <y>100</y>
           <width>60</width>
           <height>16</height>
          </rect>
         </property>
         <property name="text">
          <string>Тела:</string>
         </property>
        </widget>
        <widget class="QTextBrowser" name="figures_textbrowser">
         <property name="geometry">
          <rect>
           <x>15</x>
           <y>131</y>
           <width>291</width>
           <height>311</height>
          </rect>
         </property>
        </widget>
        <widget class="QPushButton" name="add_figure_btn">
         <property name="geometry">
          <rect>
           <x>10</x>
           <y>450</y>
           <width>301</width>
           <height>32</height>
          </rect>
         </property>
         <property name="text">
          <string>Добавить тело</string>
         </property>
        </widget>
        <widget class="QLabel" name="mass_label">
         <property name="geometry">
          <rect>
           <x>520</x>
           <y>40</y>
           <width>60</width>
           <height>16</height>
          </rect>
         </property>
         <property name="text">
          <string>масса:</string>
         </property>
        </widget>
        <widget class="QSpinBox" name="mass_spinBox">
         <property name="geometry">
          <rect>
           <x>580</x>
           <y>40</y>
           <width>161</width>
           <height>24</height>
          </rect>
         </property>
         <property name="maximum">
          <number>999999999</number>
         </property>
        </widget>
        <widget class="QLabel" name="speed_label">
         <property name="geometry">
          <rect>
           <x>490</x>
           <y>70</y>
           <width>71</width>
           <height>20</height>
          </rect>
         </property>
         <property name="text">
          <string>скорость:</string>
         </property>
        </widget>
        <widget class="QSpinBox" name="speed_spinBox">
         <property name="geometry">
          <rect>
           <x>580</x>
           <y>70</y>
           <width>161</width>
           <height>24</height>
          </rect>
         </property>
         <property name="maximum">
          <number>300000000</number>
         </property>
        </widget>
        <widget class="QLabel" name="corner_label">
         <property name="geometry">
          <rect>
           <x>400</x>
           <y>100</y>
           <width>171</width>
           <height>20</height>
          </rect>
         </property>
         <property name="text">
          <string>угол (скорость к ОХ):</string>
         </property>
        </widget>
        <widget class="QSpinBox" name="corner_spinBox">
         <property name="geometry">
          <rect>
           <x>580</x>
           <y>100</y>
           <width>161</width>
           <height>24</height>
          </rect>
         </property>
         <property name="maximum">
          <number>360</number>
         </property>
        </widget>
        <widget class="QLabel" name="color_label">
         <property name="geometry">
          <rect>
           <x>520</x>
           <y>130</y>
           <width>41</width>
           <height>16</height>
          </rect>
         </property>
         <property name="text">
          <string>цвет:</string>
         </property>
        </widget>
        <widget class="QLineEdit" name="color_lineEdit">
         <property name="geometry">
          <rect>
           <x>580</x>
           <y>130</y>
           <width>161</width>
           <height>31</height>
          </rect>
         </property>
         <property name="readOnly">
          <bool>true</bool>
         </property>
        </widget>
        <widget class="QPlainTextEdit" name="comments_textEdit">
         <property name="geometry">
          <rect>
           <x>510</x>
           <y>310</y>
           <width>231</width>
           <height>161</height>
          </rect>
         </property>
        </widget>
        <widget class="QLabel" name="label_3">
         <property name="geometry">
          <rect>
           <x>510</x>
           <y>280</y>
           <width>101</width>
           <height>16</height>
          </rect>
         </property>
         <property name="text">
          <string>Комментарии:</string>
         </property>
        </widget>
        <widget class="QPushButton" name="start_btn">
         <property name="geometry">
          <rect>
           <x>320</x>
           <y>10</y>
           <width>113</width>
           <height>81</height>
          </rect>
         </property>
         <property name="text">
          <string>Пуск</string>
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
           <x>300</x>
           <y>20</y>
           <width>291</width>
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
           <x>300</x>
           <y>220</y>
           <width>291</width>
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
           <x>300</x>
           <y>60</y>
           <width>291</width>
           <height>32</height>
          </rect>
         </property>
         <property name="text">
          <string>Удалить</string>
         </property>
        </widget>
        <widget class="QPushButton" name="help_btn">
         <property name="geometry">
          <rect>
           <x>300</x>
           <y>180</y>
           <width>291</width>
           <height>32</height>
          </rect>
         </property>
         <property name="text">
          <string>Помощь</string>
         </property>
        </widget>
        <widget class="QPushButton" name="open_exp_btn">
         <property name="geometry">
          <rect>
           <x>300</x>
           <y>100</y>
           <width>291</width>
           <height>32</height>
          </rect>
         </property>
         <property name="text">
          <string>Открыть эксперимент</string>
         </property>
        </widget>
        <widget class="QPushButton" name="change_view_btn">
         <property name="geometry">
          <rect>
           <x>300</x>
           <y>140</y>
           <width>291</width>
           <height>32</height>
          </rect>
         </property>
         <property name="text">
          <string>Внешний вид</string>
         </property>
        </widget>
       </widget>
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