# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import rs

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(760, 230)
        Dialog.setMinimumSize(QSize(760, 230))
        Dialog.setMaximumSize(QSize(760, 240))
        font = QFont()
        font.setPointSize(9)
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/data.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"QDialog {\n"
"background-color: rgb(40,40,40);\n"
"}\n"
"\n"
"QLabel{\n"
"color: white;\n"
"background-color: transparent;\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(75, 75))
        self.label_2.setMaximumSize(QSize(75, 75))
        self.label_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_2.setPixmap(QPixmap(u":/icons/data.ico"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"IDX2TXT - \u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435 ", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">IDX2TXT</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u0434\u0430\u043d\u043d\u044b\u0445 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 IDX \u0438\u0437 \u0442\u0430\u0445\u0435\u043e\u043c\u0435\u0442\u0440\u0430 Leica Builder 509.\n"
"version 3.0.0\n"
"Copyrigth \u00a9 2019-2020 Pochatkov A.\n"
"All rights reserved.", None))
    # retranslateUi

