# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help.ui'
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
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(500, 165)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(500, 165))
        Dialog.setMaximumSize(QSize(150000, 150000))
        Dialog.setBaseSize(QSize(500, 165))
        Dialog.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u":/icons/data.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"#Dialog{\n"
"background: rgb(40,40,40);\n"
"}\n"
"\n"
"QLabel{\n"
"color: white;\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(480, 150))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"IDX2TXT - \u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b:</span></p><p><span style=\" font-size:10pt;\">1)\u041d\u0430\u0436\u0430\u0442\u044c \u043a\u043d\u043e\u043f\u043a\u0443 &quot;</span><span style=\" font-size:10pt; font-weight:600;\">\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c</span><span style=\" font-size:10pt;\">&quot; \u0438 \u0432\u044b\u0431\u0440\u0430\u0442\u044c IDX \u0444\u0430\u0439\u043b \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438</span></p><p><span style=\" font-size:10pt;\">2)\u0423\u0431\u0435\u0434\u0438\u0432\u0448\u0438\u0441\u044c \u0432 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u043e\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0445 \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435, \u043d\u0430\u0436\u0430\u0442\u044c \u043a\u043d\u043e\u043f\u043a\u0443 &quot;</span><span style=\" font-size:10pt; font-weight:600;\">\u0421"
                        "\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c</span><span style=\" font-size:10pt;\">&quot; \u0438 \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0443\u0442\u044c \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f</span></p></body></html>", None))
    # retranslateUi

