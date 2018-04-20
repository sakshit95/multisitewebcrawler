# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_crawler.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import amazon_crawler, snapdeal_crawler

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.crawlers = QtWidgets.QComboBox(self.centralwidget)
        self.crawlers.setGeometry(QtCore.QRect(10, 100, 131, 31))
        self.crawlers.setObjectName("crawlers")
        self.crawlers.addItem("")
        self.crawlers.addItem("")
        self.crawlers.addItem("")
        self.website = QtWidgets.QLabel(self.centralwidget)
        self.website.setGeometry(QtCore.QRect(20, 80, 47, 16))
        self.website.setObjectName("website")
        self.searchname = QtWidgets.QLineEdit(self.centralwidget)
        self.searchname.setGeometry(QtCore.QRect(200, 100, 141, 31))
        self.searchname.setObjectName("searchname")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(370, 100, 101, 31))
        self.search.setObjectName("search")
        self.searchproduct = QtWidgets.QLabel(self.centralwidget)
        self.searchproduct.setGeometry(QtCore.QRect(210, 80, 81, 20))
        self.searchproduct.setObjectName("searchproduct")
        self.running = QtWidgets.QLabel(self.centralwidget)
        self.running.setGeometry(QtCore.QRect(0, 140, 531, 141))
        self.running.setObjectName("running")
        self.setting = QtWidgets.QPushButton(self.centralwidget)
        self.setting.setGeometry(QtCore.QRect(420, 290, 111, 21))
        self.setting.setObjectName("setting")
        self.traintest = QtWidgets.QPushButton(self.centralwidget)
        self.traintest.setGeometry(QtCore.QRect(300, 290, 111, 21))
        self.traintest.setObjectName("traintest")
        self.recommendation = QtWidgets.QPushButton(self.centralwidget)
        self.recommendation.setGeometry(QtCore.QRect(0, 320, 531, 41))
        self.recommendation.setObjectName("recommendation")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 521, 71))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.search.clicked.connect(self.runcode)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def runcode(self):
        pname = self.searchname.text()
        crawler_name = self.crawlers.currentText()
        if crawler_name == 'AMAZON':
            self.running.setText("Crawling amazon")
            amazon_crawler.crawl_product(pname)
        elif crawler_name== "SHOPCLUES":
            #self.running.setText("Crawling snapdeal")
            pass
        elif crawler_name== "SNAPDEAL":
            self.running.setText("Crawling snapdeal")
            snapdeal_crawler.crawl_snapdealproducts(pname)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.crawlers.setItemText(0, _translate("MainWindow", "AMAZON"))
        self.crawlers.setItemText(1, _translate("MainWindow", "SHOPCLUES"))
        self.crawlers.setItemText(2, _translate("MainWindow", "SNAPDEAL"))
        # self.crawlers.setItemText(3, _translate("MainWindow", "MYNTRA"))
        # self.crawlers.setItemText(4, _translate("MainWindow", "JABONG"))
        self.website.setText(_translate("MainWindow", "Website"))
        self.search.setText(_translate("MainWindow", "search"))
        self.searchproduct.setText(_translate("MainWindow", "Search product"))
        self.running.setText(_translate("MainWindow", "         Running...."))
        self.setting.setText(_translate("MainWindow", "Setting"))
        self.traintest.setText(_translate("MainWindow", "Train Test"))
        self.recommendation.setText(_translate("MainWindow", "Recommendations"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#00007f;\">This is a recommendation system where  we search  the product  we want and the recommended product will be shown to us. This will help us to search the products from different crawlers in order to buy  efficient and effective product hence, our shopping experience will be improved.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
