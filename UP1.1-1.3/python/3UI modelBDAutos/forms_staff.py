# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.twStaffs = QtWidgets.QTableWidget(self.centralwidget)
        self.twStaffs.setGeometry(QtCore.QRect(30, 290, 631, 271))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.twStaffs.setFont(font)
        self.twStaffs.setObjectName("twStaffs")
        self.twStaffs.setColumnCount(0)
        self.twStaffs.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 251, 244))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.leFio = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leFio.setFont(font)
        self.leFio.setObjectName("leFio")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leFio)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lePhone = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lePhone.setFont(font)
        self.lePhone.setToolTip("")
        self.lePhone.setInputMask("")
        self.lePhone.setObjectName("lePhone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lePhone)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.leEmail = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leEmail.setFont(font)
        self.leEmail.setObjectName("leEmail")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.leEmail)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lePhone_2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lePhone_2.setFont(font)
        self.lePhone_2.setToolTip("")
        self.lePhone_2.setInputMask("")
        self.lePhone_2.setObjectName("lePhone_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lePhone_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.leFio_2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leFio_2.setFont(font)
        self.leFio_2.setObjectName("leFio_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leFio_2)
        self.leEmail_2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leEmail_2.setFont(font)
        self.leEmail_2.setObjectName("leEmail_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.leEmail_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(300, 30, 77, 92))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbOpen = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbOpen.sizePolicy().hasHeightForWidth())
        self.pbOpen.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbOpen.setFont(font)
        self.pbOpen.setMouseTracking(False)
        self.pbOpen.setTabletTracking(False)
        self.pbOpen.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pbOpen.setAutoDefault(False)
        self.pbOpen.setObjectName("pbOpen")
        self.verticalLayout.addWidget(self.pbOpen)
        self.pbInsert = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbInsert.sizePolicy().hasHeightForWidth())
        self.pbInsert.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbInsert.setFont(font)
        self.pbInsert.setMouseTracking(False)
        self.pbInsert.setTabletTracking(False)
        self.pbInsert.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pbInsert.setAutoDefault(False)
        self.pbInsert.setObjectName("pbInsert")
        self.verticalLayout.addWidget(self.pbInsert)
        self.pbDelete = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbDelete.sizePolicy().hasHeightForWidth())
        self.pbDelete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbDelete.setFont(font)
        self.pbDelete.setMouseTracking(False)
        self.pbDelete.setTabletTracking(False)
        self.pbDelete.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pbDelete.setAutoDefault(False)
        self.pbDelete.setObjectName("pbDelete")
        self.verticalLayout.addWidget(self.pbDelete)
        self.lblAvgAge = QtWidgets.QLabel(self.centralwidget)
        self.lblAvgAge.setGeometry(QtCore.QRect(300, 220, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblAvgAge.setFont(font)
        self.lblAvgAge.setObjectName("lblAvgAge")
        self.pbFind = QtWidgets.QPushButton(self.centralwidget)
        self.pbFind.setGeometry(QtCore.QRect(460, 117, 75, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pbFind.setFont(font)
        self.pbFind.setObjectName("pbFind")
        self.leFind = QtWidgets.QLineEdit(self.centralwidget)
        self.leFind.setEnabled(True)
        self.leFind.setGeometry(QtCore.QRect(460, 86, 167, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leFind.sizePolicy().hasHeightForWidth())
        self.leFind.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leFind.setFont(font)
        self.leFind.setObjectName("leFind")
        self.cbColNames = QtWidgets.QComboBox(self.centralwidget)
        self.cbColNames.setGeometry(QtCore.QRect(460, 55, 167, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbColNames.sizePolicy().hasHeightForWidth())
        self.cbColNames.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbColNames.setFont(font)
        self.cbColNames.setObjectName("cbColNames")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(520, 30, 44, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 841, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Автомобили"))
        self.label.setText(_translate("MainWindow", "Марка"))
        self.label_4.setText(_translate("MainWindow", "Пробег"))
        self.label_5.setText(_translate("MainWindow", "VIN"))
        self.label_6.setText(_translate("MainWindow", "Цена"))
        self.label_9.setText(_translate("MainWindow", "Дата Выпуска"))
        self.label_3.setText(_translate("MainWindow", "Модель"))
        self.pbOpen.setText(_translate("MainWindow", "Открыть"))
        self.pbInsert.setText(_translate("MainWindow", "Добавить"))
        self.pbDelete.setText(_translate("MainWindow", "Удалить"))
        self.lblAvgAge.setText(_translate("MainWindow", "Средний пробег:"))
        self.pbFind.setText(_translate("MainWindow", "Найти"))
        self.label_8.setText(_translate("MainWindow", "Поиск"))
