from PyQt5.QtWidgets import QTableWidgetItem
from mysql.connector import connect, Error

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 720)
        MainWindow.setMinimumSize(QtCore.QSize(850, 720))
        MainWindow.setMaximumSize(QtCore.QSize(850, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStatusTip("")
        self.centralwidget.setAccessibleDescription("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setMinimumSize(QtCore.QSize(550, 0))
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout.setContentsMargins(3, 30, 0, -1)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")

        self.comboBox.addItem("warehouse")
        self.comboBox.addItem("review")
        self.comboBox.addItem("customer")
        self.comboBox.addItem("product")
        self.comboBox.addItem("order")
        self.comboBox.addItem("delivery")
        self.comboBox.addItem("brigade")
        self.comboBox.addItem("employee")


        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.comboBox)
        self.pushButtonTable = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonTable.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButtonTable.setObjectName("pushButtonTable")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButtonTable)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lineEditMen = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMen.setMinimumSize(QtCore.QSize(85, 0))
        self.lineEditMen.setMaximumSize(QtCore.QSize(85, 16777215))
        self.lineEditMen.setObjectName("lineEditMen")
        self.horizontalLayout_3.addWidget(self.lineEditMen)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.pushButtonMen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMen.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButtonMen.setObjectName("pushButtonMen")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButtonMen)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.lineEditBol = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditBol.setMinimumSize(QtCore.QSize(85, 0))
        self.lineEditBol.setMaximumSize(QtCore.QSize(85, 16777215))
        self.lineEditBol.setObjectName("lineEditBol")
        self.horizontalLayout_4.addWidget(self.lineEditBol)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_4)
        self.pushButtonBol = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBol.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButtonBol.setObjectName("pushButtonBol")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButtonBol)
        self.lineEditRabName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRabName.setObjectName("lineEditRabName")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lineEditRabName)
        self.pushButtonRabName = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRabName.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButtonRabName.setObjectName("pushButtonRabName")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButtonRabName)
        self.lineEditZakazchik = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditZakazchik.setObjectName("lineEditZakazchik")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lineEditZakazchik)
        self.pushButtonZakazchik = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonZakazchik.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButtonZakazchik.setObjectName("pushButtonZakazchik")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButtonZakazchik)
        self.lineEditRabTel = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditRabTel.setObjectName("lineEditRabTel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lineEditRabTel)
        self.pushButtonRabTel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRabTel.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButtonRabTel.setObjectName("pushButtonRabTel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButtonRabTel)
        self.lineEditSklad = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSklad.setObjectName("lineEditSklad")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lineEditSklad)
        self.pushButtonSklad = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSklad.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButtonSklad.setObjectName("pushButtonSklad")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pushButtonSklad)
        self.lineEditProd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditProd.setText("")
        self.lineEditProd.setObjectName("lineEditProd")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lineEditProd)
        self.pushButtonProd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonProd.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButtonProd.setObjectName("pushButtonProd")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pushButtonProd)



        self.pushButtonNew = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNew.setMaximumSize(QtCore.QSize(500, 16777215))
        self.pushButtonNew.setObjectName("pushButtonNew")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.pushButtonNew)

        self.comboBoxNew = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxNew.setObjectName("comboBox")
        self.comboBoxNew.addItem("warehouse")
        self.comboBoxNew.addItem("review")
        self.comboBoxNew.addItem("customer")
        self.comboBoxNew.addItem("product")
        self.comboBoxNew.addItem("order")
        self.comboBoxNew.addItem("delivery")
        self.comboBoxNew.addItem("brigade")
        self.comboBoxNew.addItem("employee")

        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.comboBoxNew)




        self.horizontalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tikhonov DBMS"))
        self.pushButtonTable.setText(_translate("MainWindow", "Отобразить таблицу"))

        self.pushButtonTable.clicked.connect(self.on_click_pushButtonTable)

        self.label.setText(_translate("MainWindow", "Меньше"))
        self.pushButtonMen.setText(_translate("MainWindow", "Отобразить заказы где цена"))

        self.pushButtonMen.clicked.connect(self.on_click_pushButtonMen)

        self.label_2.setText(_translate("MainWindow", "Больше"))
        self.pushButtonBol.setText(_translate("MainWindow", "Отобразить заказы где цена"))

        self.pushButtonBol.clicked.connect(self.on_click_pushButtonBol)

        self.lineEditRabName.setPlaceholderText(_translate("MainWindow", "Имя"))
        self.pushButtonRabName.setText(_translate("MainWindow", "Найти работника по имени"))

        self.pushButtonRabName.clicked.connect(self.on_click_pushButtonRabName)

        self.lineEditZakazchik.setPlaceholderText(_translate("MainWindow", "Телефон"))
        self.pushButtonZakazchik.setText(_translate("MainWindow", "Найти заказчика по телефону"))

        self.pushButtonZakazchik.clicked.connect(self.on_click_pushButtonZakazchik)

        self.lineEditRabTel.setPlaceholderText(_translate("MainWindow", "Телефон"))
        self.pushButtonRabTel.setText(_translate("MainWindow", "Найти работника по телефону"))

        self.pushButtonRabTel.clicked.connect(self.on_click_pushButtonRabTel)

        self.lineEditSklad.setPlaceholderText(_translate("MainWindow", "Название"))
        self.pushButtonSklad.setText(_translate("MainWindow", "Найти склад по названию"))

        self.pushButtonSklad.clicked.connect(self.on_click_pushButtonSklad)

        self.lineEditProd.setPlaceholderText(_translate("MainWindow", "Название"))
        self.pushButtonProd.setText(_translate("MainWindow", "Найти продукт по названию"))


        #кнопка new
        self.pushButtonNew.setText(_translate("MainWindow", "Добавить в таблиу"))


        self.pushButtonProd.clicked.connect(self.on_click_pushButtonProd)


    def on_click_pushButtonTable(self):

        self.tableView.clear()
        self.tableView.setRowCount(0)
        self.tableView.setColumnCount(0)

        text =self.comboBox.currentText()
        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="123456",
            ) as connection:
                show_db_query = "SELECT * FROM vegetable_production_db." + str(text) + ";"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    # self.tableView.setRowCount(len(cursor.column_names))
                    self.tableView.setColumnCount(len(cursor.description))
                    i = 0
                    self.tableView.setHorizontalHeaderLabels(cursor.column_names)#.setStretchLastSection(True)
                    self.tableView.verticalHeader().setVisible(False)

                    for r,db in enumerate(cursor):
                        print(db)
                        print(type(db))
                        self.tableView.insertRow(r)
                        for c,data in enumerate(db):
                            self.tableView.setItem(r,c,QTableWidgetItem(str(data)))
                        # self.tableView.resizeRowToContents()

                connect().disconnect #TODO
        except Error as e:
            print(e)


    def on_click_pushButtonMen(self):

        self.tableView.clear()
        self.tableView.setRowCount(0)
        self.tableView.setColumnCount(0)
        text = self.lineEditMen.text()

        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="123456",
            ) as connection:
                show_db_query = "SELECT * FROM vegetable_production_db.order where price < "+ str(text) +";"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    # self.tableView.setRowCount(len(cursor.column_names))
                    self.tableView.setColumnCount(len(cursor.description))
                    i = 0
                    self.tableView.setHorizontalHeaderLabels(cursor.column_names)#.setStretchLastSection(True)
                    self.tableView.verticalHeader().setVisible(False)

                    for r,db in enumerate(cursor):
                        print(db)
                        print(type(db))
                        self.tableView.insertRow(r)
                        for c,data in enumerate(db):
                            self.tableView.setItem(r,c,QTableWidgetItem(str(data)))
                        # self.tableView.resizeRowToContents()
        except Error as e:
            print(e)


    def on_click_pushButtonBol(self):

        self.tableView.clear()
        self.tableView.setRowCount(0)
        self.tableView.setColumnCount(0)
        text = self.lineEditBol.text()

        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="123456",
            ) as connection:
                show_db_query = "SELECT * FROM vegetable_production_db.order where price > "+ str(text) +";"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    # self.tableView.setRowCount(len(cursor.column_names))
                    self.tableView.setColumnCount(len(cursor.description))
                    i = 0
                    self.tableView.setHorizontalHeaderLabels(cursor.column_names)#.setStretchLastSection(True)
                    self.tableView.verticalHeader().setVisible(False)

                    for r,db in enumerate(cursor):
                        print(db)
                        print(type(db))
                        self.tableView.insertRow(r)
                        for c,data in enumerate(db):
                            self.tableView.setItem(r,c,QTableWidgetItem(str(data)))
                        # self.tableView.resizeRowToContents()
        except Error as e:
            print(e)


    def on_click_pushButtonRabName(self):

        self.tableView.clear()
        self.tableView.setRowCount(0)
        self.tableView.setColumnCount(0)
        text = self.lineEditRabName.text()

        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="123456",
            ) as connection:
                show_db_query = "SELECT * FROM vegetable_production_db.employee where employee.name like '"+ str(text) +"';"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    self.tableView.setColumnCount(len(cursor.description))
                    i = 0
                    self.tableView.setHorizontalHeaderLabels(cursor.column_names)
                    self.tableView.verticalHeader().setVisible(False)

                    for r,db in enumerate(cursor):
                        print(db)
                        print(type(db))
                        self.tableView.insertRow(r)
                        for c,data in enumerate(db):
                            self.tableView.setItem(r,c,QTableWidgetItem(str(data)))
                        # self.tableView.resizeRowToContents()
        except Error as e:
            print(e)


    def on_click_pushButtonZakazchik(self):

        self.tableView.clear()
        self.tableView.setRowCount(0)
        self.tableView.setColumnCount(0)
        text = self.lineEditZakazchik.text()

        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="123456",
            ) as connection:
                show_db_query = "SELECT * FROM vegetable_production_db.customer where customer.phone_number like '"+ str(text) +"';"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    self.tableView.setColumnCount(len(cursor.description))
                    i = 0
                    self.tableView.setHorizontalHeaderLabels(cursor.column_names)
                    self.tableView.verticalHeader().setVisible(False)

                    for r,db in enumerate(cursor):
                        print(db)
                        print(type(db))
                        self.tableView.insertRow(r)
                        for c,data in enumerate(db):
                            self.tableView.setItem(r,c,QTableWidgetItem(str(data)))
                        # self.tableView.resizeRowToContents()
        except Error as e:
            print(e)


    def on_click_pushButtonRabTel(self):

        self.tableView.clear()
        self.tableView.setRowCount(0)
        self.tableView.setColumnCount(0)
        text = self.lineEditRabTel.text()

        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="123456",
            ) as connection:
                show_db_query = "SELECT * FROM vegetable_production_db.employee where employee.phone like '"+ str(text) +"';"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    self.tableView.setColumnCount(len(cursor.description))
                    i = 0
                    self.tableView.setHorizontalHeaderLabels(cursor.column_names)
                    self.tableView.verticalHeader().setVisible(False)

                    for r,db in enumerate(cursor):
                        print(db)
                        print(type(db))
                        self.tableView.insertRow(r)
                        for c,data in enumerate(db):
                            self.tableView.setItem(r,c,QTableWidgetItem(str(data)))
                        # self.tableView.resizeRowToContents()
        except Error as e:
            print(e)

    def on_click_pushButtonSklad(self):

        self.tableView.clear()
        self.tableView.setRowCount(0)
        self.tableView.setColumnCount(0)
        text = self.lineEditSklad.text()

        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="123456",
            ) as connection:
                show_db_query = "SELECT * FROM vegetable_production_db.warehouse where warehouse.name like '"+ str(text) +"';"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    self.tableView.setColumnCount(len(cursor.description))
                    i = 0
                    self.tableView.setHorizontalHeaderLabels(cursor.column_names)
                    self.tableView.verticalHeader().setVisible(False)

                    for r,db in enumerate(cursor):
                        print(db)
                        print(type(db))
                        self.tableView.insertRow(r)
                        for c,data in enumerate(db):
                            self.tableView.setItem(r,c,QTableWidgetItem(str(data)))
                        # self.tableView.resizeRowToContents()
        except Error as e:
            print(e)

    def on_click_pushButtonProd(self):

        self.tableView.clear()
        self.tableView.setRowCount(0)
        self.tableView.setColumnCount(0)
        text = self.lineEditProd.text()

        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="123456",
            ) as connection:
                show_db_query = "SELECT * FROM vegetable_production_db.product where product.name like '"+ str(text) +"';"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    self.tableView.setColumnCount(len(cursor.description))
                    i = 0
                    self.tableView.setHorizontalHeaderLabels(cursor.column_names)
                    self.tableView.verticalHeader().setVisible(False)

                    for r,db in enumerate(cursor):
                        print(db)
                        print(type(db))
                        self.tableView.insertRow(r)
                        for c,data in enumerate(db):
                            self.tableView.setItem(r,c,QTableWidgetItem(str(data)))
                        # self.tableView.resizeRowToContents()
        except Error as e:
            print(e)


def on_click_pushButtonNew(self):

    self.widget = QtWidgets.QWidget()
    self.widget.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
