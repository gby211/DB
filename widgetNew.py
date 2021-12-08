from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self):
        self.setObjectName("self")
        self.resize(500, 85)
        self.setMinimumSize(QtCore.QSize(500, 0))
        self.setMaximumSize(QtCore.QSize(500, 16777215))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.pushButton11 = QtWidgets.QPushButton(self)
        self.pushButton11.setObjectName("pushButton11")
        self.verticalLayout.addWidget(self.pushButton11)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Добавить запись"))
        self.pushButton11.setText(_translate("self", "Добавить запись"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
