# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import rs

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 485)
        MainWindow.setMinimumSize(QSize(880, 485))
        icon = QIcon()
        icon.addFile(u":/icons/data.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"background-color: grey;\n"
"}\n"
"\n"
"QLabel {\n"
"font: 63 20pt \"Yu Gothic UI Semibold\";\n"
"color: white;\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background: rgb(40,40,40);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"border-radius: 5px;\n"
"height: 35px;\n"
"width: 105 px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: black;\n"
"background: #bcbdbb;\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"border-radius: 5px;\n"
"height: 35px;\n"
"width: 105 px;\n"
"border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #741B10;\n"
"    color: #000;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background-color: transparent;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    border: none;\n"
"	min-width: 100px;\n"
"    background-color: #9b9b9b;\n"
"}\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:hor"
                        "izontal, \n"
"QScrollBar::sub-page:horizontal {\n"
"    width: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"QScrollBar:vertical {\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    border: none;\n"
"	min-height: 100px;\n"
"    background-color: #9b9b9b;\n"
"}\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical {\n"
"    height: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"QTableView{\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"background-color: grey;\n"
"border: 1px solid grey;\n"
"color: #f0f0f0;\n"
"gridline-color: rgb(40,40,40);\n"
"outline : 0;\n"
"}\n"
"QTableView::item:hover{\n"
"background-color: #bcbdbb;\n"
"color: #000;\n"
"}\n"
"QTableView::item:selected {\n"
"background-color: #741B10;\n"
"color: #000;\n"
"}\n"
"QTableView::item:selected:disabled{\n"
"background-color: #1a1b1c;\n"
"border: 2px solid #"
                        "525251;\n"
"color: #656565;\n"
"}\n"
"QTableCornerButton::section{\n"
"background-color: rgb(40,40,40);\n"
"}\n"
"QHeaderView{\n"
"background-color: rgb(40,40,40);\n"
"}\n"
"QHeaderView::section:vertical{\n"
"padding-left: 10px;\n"
"}\n"
"QHeaderView::section:horizontal{\n"
"padding-left: 0px;\n"
"}\n"
"QHeaderView::section{\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"color: #fff;\n"
"border-top: 0px;\n"
"border-bottom: 1px solid gray;\n"
"border-right: 1px solid gray;\n"
"background-color: rgb(40,40,40);\n"
"}\n"
"QHeaderView::section:checked{\n"
"color: #000;\n"
"background-color: #741B10;\n"
"}\n"
"QHeaderView::section:checked:disabled{\n"
"color: #656565;\n"
"background-color: #525251;\n"
"}\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one{\n"
"border-top: 1px solid #353635;\n"
"}\n"
"QHeaderView::section::vertical{\n"
"border-top: 1px solid #353635;\n"
"}\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one{\n"
"border-left"
                        ": 1px solid #353635;\n"
"}\n"
"QHeaderView::section::horizontal{\n"
"border-left: 1px solid #353635;\n"
"}")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Button_load = QPushButton(self.centralwidget)
        self.Button_load.setObjectName(u"Button_load")
        self.Button_load.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_load.sizePolicy().hasHeightForWidth())
        self.Button_load.setSizePolicy(sizePolicy)
        self.Button_load.setMinimumSize(QSize(50, 30))
        font = QFont()
        font.setFamily(u"Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.Button_load.setFont(font)
        self.Button_load.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.Button_load)

        self.horizontalSpacer = QSpacerItem(400, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Button_save = QPushButton(self.centralwidget)
        self.Button_save.setObjectName(u"Button_save")
        self.Button_save.setEnabled(True)
        self.Button_save.setMinimumSize(QSize(50, 30))
        self.Button_save.setFont(font)
        self.Button_save.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.Button_save)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 880, 29))
        self.menubar.setStyleSheet(u"QMenuBar{\n"
"background: rgb(40,40,40);\n"
"color: white;\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"QMenuBar::item:pressed {\n"
"  	background-color: #741B10;\n"
"    color: #000;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  	background-color: #bcbdbb;\n"
"    color: #000;\n"
"}\n"
"\n"
"QMenu{\n"
"background: rgb(40,40,40);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"QMenu::item{\n"
"color: white;\n"
"background: rgb(40,40,40);\n"
"}\n"
"QMenu::item:selected{\n"
"  	  	background-color: #bcbdbb;\n"
"    color: #000;\n"
"}\n"
"QMenu::item:pressed{\n"
"	background-color: #741B10;\n"
"    color: #000;\n"
"}")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"IDX2TXT", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IDX2TXT", None))
        self.Button_load.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.Button_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

