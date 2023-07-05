from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QInputDialog
import cx_Oracle
import os

class Ui_TabWidget(QtCore.QObject):

    row_selected = QtCore.pyqtSignal(list)
    previous_selected_row = None
    
    def setupUi(self, tabWidget):
        self.tabWidget = tabWidget
        tabWidget.setObjectName("tabWidget")
        tabWidget.resize(618, 455)
        self.accountingTab = QtWidgets.QWidget()
        self.accountingTab.setObjectName("accountingTab")
        self.accountingTable = QtWidgets.QTableWidget(self.accountingTab)
        self.accountingTable.setGeometry(QtCore.QRect(10, 160, 591, 251))
        self.accountingTable.setObjectName("accountingTable")
        self.accountingTable.setColumnCount(0)
        self.accountingTable.setRowCount(0)
        self.accountingUpdateBtn = QtWidgets.QPushButton(self.accountingTab)
        self.accountingUpdateBtn.setGeometry(QtCore.QRect(310, 120, 141, 32))
        self.accountingUpdateBtn.setObjectName("accountingUpdateBtn")
        self.accountingInsertBtn = QtWidgets.QPushButton(self.accountingTab)
        self.accountingInsertBtn.setGeometry(QtCore.QRect(460, 120, 141, 32))
        self.accountingInsertBtn.setObjectName("accountingInsertBtn")
        self.accountingIdTxt = QtWidgets.QTextEdit(self.accountingTab)
        self.accountingIdTxt.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.accountingIdTxt.setObjectName("accountingIdTxt")
        self.accountingAccLvlTxt = QtWidgets.QTextEdit(self.accountingTab)
        self.accountingAccLvlTxt.setGeometry(QtCore.QRect(10, 80, 141, 31))
        self.accountingAccLvlTxt.setObjectName("accountingAccLvlTxt")
        self.accountingDescTxt = QtWidgets.QTextEdit(self.accountingTab)
        self.accountingDescTxt.setGeometry(QtCore.QRect(160, 20, 141, 31))
        self.accountingDescTxt.setObjectName("accountingDescTxt")
        self.accountingGnlAccTxt = QtWidgets.QTextEdit(self.accountingTab)
        self.accountingGnlAccTxt.setGeometry(QtCore.QRect(160, 80, 141, 31))
        self.accountingGnlAccTxt.setObjectName("accountingGnlAccTxt")
        self.accountingAccTypeTxt = QtWidgets.QTextEdit(self.accountingTab)
        self.accountingAccTypeTxt.setGeometry(QtCore.QRect(310, 20, 141, 31))
        self.accountingAccTypeTxt.setObjectName("accountingAccTypeTxt")
        self.accountingTrxAllwTxt = QtWidgets.QTextEdit(self.accountingTab)
        self.accountingTrxAllwTxt.setGeometry(QtCore.QRect(460, 20, 141, 31))
        self.accountingTrxAllwTxt.setObjectName("accountingTrxAllwTxt")
        self.accountingBlnTxt = QtWidgets.QTextEdit(self.accountingTab)
        self.accountingBlnTxt.setGeometry(QtCore.QRect(310, 80, 141, 31))
        self.accountingBlnTxt.setObjectName("accountingBlnTxt")
        self.accountingStsTxt = QtWidgets.QTextEdit(self.accountingTab)
        self.accountingStsTxt.setGeometry(QtCore.QRect(460, 80, 141, 31))
        self.accountingStsTxt.setObjectName("accountingStsTxt")
        self.accountingIdLbl = QtWidgets.QLabel(self.accountingTab)
        self.accountingIdLbl.setGeometry(QtCore.QRect(10, 0, 60, 16))
        self.accountingIdLbl.setObjectName("accountingIdLbl")
        self.accountingDescLbl = QtWidgets.QLabel(self.accountingTab)
        self.accountingDescLbl.setGeometry(QtCore.QRect(160, 0, 91, 16))
        self.accountingDescLbl.setObjectName("accountingDescLbl")
        self.accountingAccTypeLbl = QtWidgets.QLabel(self.accountingTab)
        self.accountingAccTypeLbl.setGeometry(QtCore.QRect(310, 0, 121, 16))
        self.accountingAccTypeLbl.setObjectName("accountingAccTypeLbl")
        self.accountingTrxAllowedLbl = QtWidgets.QLabel(self.accountingTab)
        self.accountingTrxAllowedLbl.setGeometry(QtCore.QRect(460, 0, 111, 16))
        self.accountingTrxAllowedLbl.setObjectName("accountingTrxAllowedLbl")
        self.accountingAccLvlLbl = QtWidgets.QLabel(self.accountingTab)
        self.accountingAccLvlLbl.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.accountingAccLvlLbl.setObjectName("accountingAccLvlLbl")
        self.accountingGnlAccLbl = QtWidgets.QLabel(self.accountingTab)
        self.accountingGnlAccLbl.setGeometry(QtCore.QRect(160, 60, 121, 16))
        self.accountingGnlAccLbl.setObjectName("accountingGnlAccLbl")
        self.accountingBlncLbl = QtWidgets.QLabel(self.accountingTab)
        self.accountingBlncLbl.setGeometry(QtCore.QRect(310, 60, 101, 16))
        self.accountingBlncLbl.setObjectName("accountingBlncLbl")
        self.accountingStatusLbl = QtWidgets.QLabel(self.accountingTab)
        self.accountingStatusLbl.setGeometry(QtCore.QRect(460, 60, 111, 16))
        self.accountingStatusLbl.setObjectName("accountingStatusLbl")
        self.accountingFilterBtn = QtWidgets.QPushButton(self.accountingTab)
        self.accountingFilterBtn.setGeometry(QtCore.QRect(160, 120, 141, 32))
        self.accountingFilterBtn.setObjectName("accountingFilterBtn")
        self.accountingDeleteBtn = QtWidgets.QPushButton(self.accountingTab)
        self.accountingDeleteBtn.setGeometry(QtCore.QRect(10, 120, 141, 32))
        self.accountingDeleteBtn.setObjectName("accountingDeleteBtn")
        tabWidget.addTab(self.accountingTab, "")
        self.acctypesTab = QtWidgets.QWidget()
        self.acctypesTab.setObjectName("acctypesTab")
        self.acctypeTable = QtWidgets.QTableWidget(self.acctypesTab)
        self.acctypeTable.setGeometry(QtCore.QRect(80, 140, 451, 261))
        self.acctypeTable.setObjectName("acctypeTable")
        self.acctypeTable.setColumnCount(0)
        self.acctypeTable.setRowCount(0)
        self.acctypeIdLbl = QtWidgets.QLabel(self.acctypesTab)
        self.acctypeIdLbl.setGeometry(QtCore.QRect(80, 10, 60, 16))
        self.acctypeIdLbl.setObjectName("acctypeIdLbl")
        self.acctypeDescTxt = QtWidgets.QTextEdit(self.acctypesTab)
        self.acctypeDescTxt.setGeometry(QtCore.QRect(80, 90, 141, 31))
        self.acctypeDescTxt.setObjectName("acctypeDescTxt")
        self.acctypeOrgTxt = QtWidgets.QTextEdit(self.acctypesTab)
        self.acctypeOrgTxt.setGeometry(QtCore.QRect(230, 30, 141, 31))
        self.acctypeOrgTxt.setObjectName("acctypeOrgTxt")
        self.acctypeOrigLbl = QtWidgets.QLabel(self.acctypesTab)
        self.acctypeOrigLbl.setGeometry(QtCore.QRect(230, 10, 60, 16))
        self.acctypeOrigLbl.setObjectName("acctypeOrigLbl")
        self.acctypeIdTxt = QtWidgets.QTextEdit(self.acctypesTab)
        self.acctypeIdTxt.setGeometry(QtCore.QRect(80, 30, 141, 31))
        self.acctypeIdTxt.setObjectName("acctypeIdTxt")
        self.acctypeDescLbl = QtWidgets.QLabel(self.acctypesTab)
        self.acctypeDescLbl.setGeometry(QtCore.QRect(80, 70, 91, 16))
        self.acctypeDescLbl.setObjectName("acctypeDescLbl")
        self.acctypeStatusLbl = QtWidgets.QLabel(self.acctypesTab)
        self.acctypeStatusLbl.setGeometry(QtCore.QRect(230, 70, 60, 16))
        self.acctypeStatusLbl.setObjectName("acctypeStatusLbl")
        self.acctypeStsTxt = QtWidgets.QTextEdit(self.acctypesTab)
        self.acctypeStsTxt.setGeometry(QtCore.QRect(230, 90, 141, 31))
        self.acctypeStsTxt.setObjectName("acctypeStsTxt")
        self.acctypeInsertBtn = QtWidgets.QPushButton(self.acctypesTab)
        self.acctypeInsertBtn.setGeometry(QtCore.QRect(390, 100, 141, 32))
        self.acctypeInsertBtn.setObjectName("acctypeInsertBtn")
        self.acctypeFilterBtn = QtWidgets.QPushButton(self.acctypesTab)
        self.acctypeFilterBtn.setGeometry(QtCore.QRect(390, 40, 141, 32))
        self.acctypeFilterBtn.setObjectName("acctypeFilterBtn")
        self.acctypeUpdateBtn = QtWidgets.QPushButton(self.acctypesTab)
        self.acctypeUpdateBtn.setGeometry(QtCore.QRect(390, 70, 141, 32))
        self.acctypeUpdateBtn.setObjectName("acctypeUpdateBtn")
        self.acctypeDeleteBtn = QtWidgets.QPushButton(self.acctypesTab)
        self.acctypeDeleteBtn.setGeometry(QtCore.QRect(390, 10, 141, 32))
        self.acctypeDeleteBtn.setObjectName("acctypeDeleteBtn")
        tabWidget.addTab(self.acctypesTab, "")
        self.currencyTab = QtWidgets.QWidget()
        self.currencyTab.setObjectName("currencyTab")
        self.currencyRateLbl = QtWidgets.QLabel(self.currencyTab)
        self.currencyRateLbl.setGeometry(QtCore.QRect(230, 10, 60, 16))
        self.currencyRateLbl.setObjectName("currencyRateLbl")
        self.currencyTable = QtWidgets.QTableWidget(self.currencyTab)
        self.currencyTable.setGeometry(QtCore.QRect(80, 140, 451, 261))
        self.currencyTable.setObjectName("currencyTable")
        self.currencyTable.setColumnCount(0)
        self.currencyTable.setRowCount(0)
        self.currencyRateTxt = QtWidgets.QTextEdit(self.currencyTab)
        self.currencyRateTxt.setGeometry(QtCore.QRect(230, 30, 141, 31))
        self.currencyRateTxt.setObjectName("currencyRateTxt")
        self.currencyFetchBtn = QtWidgets.QPushButton(self.currencyTab)
        self.currencyFetchBtn.setGeometry(QtCore.QRect(390, 40, 141, 32))
        self.currencyFetchBtn.setObjectName("currencyFetchBtn")
        self.currencyIdTxt = QtWidgets.QTextEdit(self.currencyTab)
        self.currencyIdTxt.setGeometry(QtCore.QRect(80, 30, 141, 31))
        self.currencyIdTxt.setObjectName("currencyIdTxt")
        self.currencyStatusLbl = QtWidgets.QLabel(self.currencyTab)
        self.currencyStatusLbl.setGeometry(QtCore.QRect(230, 70, 60, 16))
        self.currencyStatusLbl.setObjectName("currencyStatusLbl")
        self.currencyIdLbl = QtWidgets.QLabel(self.currencyTab)
        self.currencyIdLbl.setGeometry(QtCore.QRect(80, 10, 60, 16))
        self.currencyIdLbl.setObjectName("currencyIdLbl")
        self.currencyStsTxt = QtWidgets.QTextEdit(self.currencyTab)
        self.currencyStsTxt.setGeometry(QtCore.QRect(230, 90, 141, 31))
        self.currencyStsTxt.setObjectName("currencyStsTxt")
        self.currencyDescTxt = QtWidgets.QTextEdit(self.currencyTab)
        self.currencyDescTxt.setGeometry(QtCore.QRect(80, 90, 141, 31))
        self.currencyDescTxt.setObjectName("currencyDescTxt")
        self.currencyDeleteBtn = QtWidgets.QPushButton(self.currencyTab)
        self.currencyDeleteBtn.setGeometry(QtCore.QRect(390, 10, 141, 32))
        self.currencyDeleteBtn.setObjectName("currencyDeleteBtn")
        self.currencyUpdateBtn = QtWidgets.QPushButton(self.currencyTab)
        self.currencyUpdateBtn.setGeometry(QtCore.QRect(390, 70, 141, 32))
        self.currencyUpdateBtn.setObjectName("currencyUpdateBtn")
        self.currencyInsertBtn = QtWidgets.QPushButton(self.currencyTab)
        self.currencyInsertBtn.setGeometry(QtCore.QRect(390, 100, 141, 32))
        self.currencyInsertBtn.setObjectName("currencyInsertBtn")
        self.currencyDescLbl = QtWidgets.QLabel(self.currencyTab)
        self.currencyDescLbl.setGeometry(QtCore.QRect(80, 70, 91, 16))
        self.currencyDescLbl.setObjectName("currencyDescLbl")
        tabWidget.addTab(self.currencyTab, "")
        self.usersTab = QtWidgets.QWidget()
        self.usersTab.setObjectName("usersTab")
        self.auxDeleteBtn = QtWidgets.QPushButton(self.usersTab)
        self.auxDeleteBtn.setGeometry(QtCore.QRect(390, 20, 141, 32))
        self.auxDeleteBtn.setObjectName("auxDeleteBtn")
        self.auxStatusTxt = QtWidgets.QTextEdit(self.usersTab)
        self.auxStatusTxt.setGeometry(QtCore.QRect(230, 40, 141, 31))
        self.auxStatusTxt.setObjectName("auxStatusTxt")
        self.auxUpdateBtn = QtWidgets.QPushButton(self.usersTab)
        self.auxUpdateBtn.setGeometry(QtCore.QRect(390, 80, 141, 32))
        self.auxUpdateBtn.setObjectName("auxUpdateBtn")
        self.auxDescLbl = QtWidgets.QLabel(self.usersTab)
        self.auxDescLbl.setGeometry(QtCore.QRect(80, 80, 91, 16))
        self.auxDescLbl.setObjectName("auxDescLbl")
        self.auxDescTxt = QtWidgets.QTextEdit(self.usersTab)
        self.auxDescTxt.setGeometry(QtCore.QRect(80, 100, 291, 31))
        self.auxDescTxt.setObjectName("auxDescTxt")
        self.auxIdLbl = QtWidgets.QLabel(self.usersTab)
        self.auxIdLbl.setGeometry(QtCore.QRect(80, 20, 60, 16))
        self.auxIdLbl.setObjectName("auxIdLbl")
        self.auxInsertBtn = QtWidgets.QPushButton(self.usersTab)
        self.auxInsertBtn.setGeometry(QtCore.QRect(390, 110, 141, 32))
        self.auxInsertBtn.setObjectName("auxInsertBtn")
        self.auxIdTxt = QtWidgets.QTextEdit(self.usersTab)
        self.auxIdTxt.setGeometry(QtCore.QRect(80, 40, 141, 31))
        self.auxIdTxt.setObjectName("auxIdTxt")
        self.auxStatusLbl = QtWidgets.QLabel(self.usersTab)
        self.auxStatusLbl.setGeometry(QtCore.QRect(230, 20, 60, 16))
        self.auxStatusLbl.setObjectName("auxStatusLbl")
        self.auxFetchBtn = QtWidgets.QPushButton(self.usersTab)
        self.auxFetchBtn.setGeometry(QtCore.QRect(390, 50, 141, 32))
        self.auxFetchBtn.setObjectName("auxFetchBtn")
        self.auxTable = QtWidgets.QTableWidget(self.usersTab)
        self.auxTable.setGeometry(QtCore.QRect(80, 150, 451, 261))
        self.auxTable.setObjectName("auxTable")
        self.auxTable.setColumnCount(0)
        self.auxTable.setRowCount(0)
        tabWidget.addTab(self.usersTab, "")
        self.entriesTab = QtWidgets.QWidget()
        self.entriesTab.setObjectName("entriesTab")
        self.entriesAccTypeTxt = QtWidgets.QTextEdit(self.entriesTab)
        self.entriesAccTypeTxt.setGeometry(QtCore.QRect(460, 30, 141, 31))
        self.entriesAccTypeTxt.setObjectName("entriesAccTypeTxt")
        self.entriesIdLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesIdLbl.setGeometry(QtCore.QRect(10, 10, 60, 16))
        self.entriesIdLbl.setObjectName("entriesIdLbl")
        self.entriesStatusLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesStatusLbl.setGeometry(QtCore.QRect(460, 70, 111, 16))
        self.entriesStatusLbl.setObjectName("entriesStatusLbl")
        self.entriesDescTxt = QtWidgets.QTextEdit(self.entriesTab)
        self.entriesDescTxt.setGeometry(QtCore.QRect(160, 30, 141, 31))
        self.entriesDescTxt.setObjectName("entriesDescTxt")
        self.entriesAmountLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesAmountLbl.setGeometry(QtCore.QRect(310, 70, 101, 16))
        self.entriesAmountLbl.setObjectName("entriesAmountLbl")
        self.entriesTable = QtWidgets.QTableWidget(self.entriesTab)
        self.entriesTable.setGeometry(QtCore.QRect(10, 170, 591, 251))
        self.entriesTable.setObjectName("entriesTable")
        self.entriesTable.setColumnCount(0)
        self.entriesTable.setRowCount(0)
        self.entriesAccOrigTxt = QtWidgets.QTextEdit(self.entriesTab)
        self.entriesAccOrigTxt.setGeometry(QtCore.QRect(310, 30, 141, 31))
        self.entriesAccOrigTxt.setObjectName("entriesAccOrigTxt")
        self.entriesUpdateBtn = QtWidgets.QPushButton(self.entriesTab)
        self.entriesUpdateBtn.setGeometry(QtCore.QRect(310, 130, 141, 32))
        self.entriesUpdateBtn.setObjectName("entriesUpdateBtn")
        self.entriesAccTypeLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesAccTypeLbl.setGeometry(QtCore.QRect(460, 10, 121, 16))
        self.entriesAccTypeLbl.setObjectName("entriesAccTypeLbl")
        self.entriesAccNumTxt = QtWidgets.QTextEdit(self.entriesTab)
        self.entriesAccNumTxt.setGeometry(QtCore.QRect(10, 90, 141, 31))
        self.entriesAccNumTxt.setObjectName("entriesAccNumTxt")
        self.entriesInsertBtn = QtWidgets.QPushButton(self.entriesTab)
        self.entriesInsertBtn.setGeometry(QtCore.QRect(460, 130, 141, 32))
        self.entriesInsertBtn.setObjectName("entriesInsertBtn")
        self.entriesStsTxt = QtWidgets.QTextEdit(self.entriesTab)
        self.entriesStsTxt.setGeometry(QtCore.QRect(460, 90, 141, 31))
        self.entriesStsTxt.setObjectName("entriesStsTxt")
        self.entriesFilterBtn = QtWidgets.QPushButton(self.entriesTab)
        self.entriesFilterBtn.setGeometry(QtCore.QRect(160, 130, 141, 32))
        self.entriesFilterBtn.setObjectName("entriesFilterBtn")
        self.entriesIdTxt = QtWidgets.QTextEdit(self.entriesTab)
        self.entriesIdTxt.setGeometry(QtCore.QRect(10, 30, 141, 31))
        self.entriesIdTxt.setObjectName("entriesIdTxt")
        self.entriesDeleteBtn = QtWidgets.QPushButton(self.entriesTab)
        self.entriesDeleteBtn.setGeometry(QtCore.QRect(10, 130, 141, 32))
        self.entriesDeleteBtn.setObjectName("entriesDeleteBtn")
        self.entriesDescLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesDescLbl.setGeometry(QtCore.QRect(160, 10, 91, 16))
        self.entriesDescLbl.setObjectName("entriesDescLbl")
        self.entriesAccNumLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesAccNumLbl.setGeometry(QtCore.QRect(10, 70, 121, 16))
        self.entriesAccNumLbl.setObjectName("entriesAccNumLbl")
        self.entriesAmountTxt = QtWidgets.QTextEdit(self.entriesTab)
        self.entriesAmountTxt.setGeometry(QtCore.QRect(310, 90, 141, 31))
        self.entriesAmountTxt.setObjectName("entriesAmountTxt")
        self.entriesDateLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesDateLbl.setGeometry(QtCore.QRect(160, 70, 121, 16))
        self.entriesDateLbl.setObjectName("entriesDateLbl")
        self.entriesAccOrigLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesAccOrigLbl.setGeometry(QtCore.QRect(310, 10, 121, 16))
        self.entriesAccOrigLbl.setObjectName("entriesAccOrigLbl")
        self.entriesDateTxt = QtWidgets.QTextEdit(self.entriesTab)
        self.entriesDateTxt.setGeometry(QtCore.QRect(160, 90, 141, 31))
        self.entriesDateTxt.setObjectName("entriesDateTxt")
        tabWidget.addTab(self.entriesTab, "")

        self.retranslateUi(tabWidget)
        tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(tabWidget)

    def retranslateUi(self, tabWidget):
        _translate = QtCore.QCoreApplication.translate
        tabWidget.setWindowTitle(_translate("tabWidget", "Gestión de Contabilidad para ISO8XX"))
        self.accountingUpdateBtn.setText(_translate("tabWidget", "Modificar"))
        self.accountingInsertBtn.setText(_translate("tabWidget", "Crear"))
        self.accountingIdLbl.setText(_translate("tabWidget", "ID"))
        self.accountingDescLbl.setText(_translate("tabWidget", "Descripción"))
        self.accountingAccTypeLbl.setText(_translate("tabWidget", "Tipo de cuenta"))
        self.accountingTrxAllowedLbl.setText(_translate("tabWidget", "¿Permite trans.?"))
        self.accountingAccLvlLbl.setText(_translate("tabWidget", "Nivel de cuenta"))
        self.accountingGnlAccLbl.setText(_translate("tabWidget", "Cuenta general"))
        self.accountingBlncLbl.setText(_translate("tabWidget", "Balance"))
        self.accountingStatusLbl.setText(_translate("tabWidget", "Estatus"))
        self.accountingFilterBtn.setText(_translate("tabWidget", "Filtrar"))
        self.accountingDeleteBtn.setText(_translate("tabWidget", "Eliminar"))
        self.accountingDeleteBtn.setStyleSheet("color: rgb(255, 0, 0);")
        tabWidget.setTabText(tabWidget.indexOf(self.accountingTab), _translate("tabWidget", "Cuentas contables"))
        self.acctypeIdLbl.setText(_translate("tabWidget", "ID"))
        self.acctypeOrigLbl.setText(_translate("tabWidget", "Origen"))
        self.acctypeDescLbl.setText(_translate("tabWidget", "Descripción"))
        self.acctypeStatusLbl.setText(_translate("tabWidget", "Estatus"))
        self.acctypeInsertBtn.setText(_translate("tabWidget", "Crear"))
        self.acctypeFilterBtn.setText(_translate("tabWidget", "Filtrar"))
        self.acctypeUpdateBtn.setText(_translate("tabWidget", "Modificar"))
        self.acctypeDeleteBtn.setText(_translate("tabWidget", "Eliminar"))
        self.acctypeDeleteBtn.setStyleSheet("color: rgb(255, 0, 0);")
        tabWidget.setTabText(tabWidget.indexOf(self.acctypesTab), _translate("tabWidget", "Tipos de cuentas"))
        self.currencyRateLbl.setText(_translate("tabWidget", "Tasa"))
        self.currencyFetchBtn.setText(_translate("tabWidget", "Actualizar tasas"))
        self.currencyStatusLbl.setText(_translate("tabWidget", "Estatus"))
        self.currencyIdLbl.setText(_translate("tabWidget", "ID"))
        self.currencyDeleteBtn.setText(_translate("tabWidget", "Eliminar"))
        self.currencyDeleteBtn.setStyleSheet("color: rgb(255, 0, 0);")
        self.currencyUpdateBtn.setText(_translate("tabWidget", "Modificar"))
        self.currencyInsertBtn.setText(_translate("tabWidget", "Crear"))
        self.currencyDescLbl.setText(_translate("tabWidget", "Descripción"))
        tabWidget.setTabText(tabWidget.indexOf(self.currencyTab), _translate("tabWidget", "Monedas"))
        self.auxDeleteBtn.setText(_translate("tabWidget", "Eliminar"))
        self.auxDeleteBtn.setStyleSheet("color: rgb(255, 0, 0);")
        self.auxUpdateBtn.setText(_translate("tabWidget", "Modificar"))
        self.auxDescLbl.setText(_translate("tabWidget", "Descripción"))
        self.auxIdLbl.setText(_translate("tabWidget", "ID"))
        self.auxInsertBtn.setText(_translate("tabWidget", "Crear"))
        self.auxStatusLbl.setText(_translate("tabWidget", "Estatus"))
        self.auxFetchBtn.setText(_translate("tabWidget", "Actualizar tasas"))
        tabWidget.setTabText(tabWidget.indexOf(self.usersTab), _translate("tabWidget", "Auxiliares"))
        self.entriesIdLbl.setText(_translate("tabWidget", "ID"))
        self.entriesStatusLbl.setText(_translate("tabWidget", "Estatus"))
        self.entriesAmountLbl.setText(_translate("tabWidget", "Monto"))
        self.entriesUpdateBtn.setText(_translate("tabWidget", "Modificar"))
        self.entriesAccTypeLbl.setText(_translate("tabWidget", "Tipo de cuenta"))
        self.entriesInsertBtn.setText(_translate("tabWidget", "Crear"))
        self.entriesFilterBtn.setText(_translate("tabWidget", "Filtrar"))
        self.entriesDeleteBtn.setText(_translate("tabWidget", "Eliminar"))
        self.entriesDeleteBtn.setStyleSheet("color: rgb(255, 0, 0);")
        self.entriesDescLbl.setText(_translate("tabWidget", "Descripción"))
        self.entriesAccNumLbl.setText(_translate("tabWidget", "Número de cuenta"))
        self.entriesDateLbl.setText(_translate("tabWidget", "Fecha de registro"))
        self.entriesAccOrigLbl.setText(_translate("tabWidget", "Cuenta origen"))
        tabWidget.setTabText(tabWidget.indexOf(self.entriesTab), _translate("tabWidget", "Entradas contables"))
        
    def insert_accounting_data(self):
    # Retrieve values from text fields
        accounting_id = int(self.accountingIdTxt.toPlainText())
        accounting_description = str(self.accountingDescTxt.toPlainText())
        accounting_acc_type = self.accountingAccTypeTxt.toPlainText()
        accounting_trx_allowed = self.accountingTrxAllwTxt.toPlainText()
        accounting_acc_lvl = int(self.accountingAccLvlTxt.toPlainText())
        accounting_gnl_acc = self.accountingGnlAccTxt.toPlainText()
        accounting_balance = float(self.accountingBlnTxt.toPlainText())
        accounting_status = self.accountingStsTxt.toPlainText()

        try:
            # Establish a connection to the Oracle database
            os.environ['TNS_ADMIN'] = '/Users/fernandez/instantclient_19_8/network/admin'
            connection = cx_Oracle.connect('ADMIN', 'Iso815810unapec', 'iso8xx_low')
            cursor = connection.cursor()

            # Call the stored procedure
            cursor.callproc("proc_insert_accounting_accs", (accounting_id, accounting_description, accounting_acc_type, accounting_trx_allowed, accounting_acc_lvl, accounting_gnl_acc, accounting_balance, accounting_status))
            connection.commit()
            cursor.close()
            connection.close()

            # Show a pop-up alert
            QMessageBox.information(None, "Éxito", "¡El registro se ha creado con éxito!")

            # Clear the text fields after successful insertion
            self.accountingIdTxt.clear()
            self.accountingDescTxt.clear()
            self.accountingAccTypeTxt.clear()
            self.accountingTrxAllwTxt.clear()
            self.accountingAccLvlTxt.clear()
            self.accountingGnlAccTxt.clear()
            self.accountingBlnTxt.clear()
            self.accountingStsTxt.clear()

            self.query_accounting_accs()

            try:
                self.accountingTable.itemClicked.disconnect()
            except TypeError:
                pass

            self.accountingTable.itemClicked.connect(self.on_table_item_clicked)
            ui.accountingTable.itemSelectionChanged.connect(handle_row_deselected)

        except Exception as e:
            # Show a pop-up alert
            QMessageBox.critical(None, "Error", f"Error al momento de eliminar el registro: {str(e)}")
            import traceback
            traceback.print_exc()

    def query_accounting_accs(self):
        # Establish a connection to the Oracle database
        os.environ['TNS_ADMIN'] = '/path/to/instantclient_19_8/network/admin'
        connection = cx_Oracle.connect('username', 'password', 'tnsname')

        self.accountingDeleteBtn.setEnabled(False)

        # Fetch all rows from the result set
        cursor = connection.cursor()
        cursor.execute("""SELECT id, 
                        description,
                        (SELECT b.description FROM accounting_accs b WHERE b.id = a.acc_types) as acc_type,
                        CASE trx_allowed WHEN 'Y' THEN 'Si' ELSE 'No' END AS trx_allowed, 
                        acc_level,
                        COALESCE((SELECT b.description FROM accounting_accs b WHERE b.id = a.general_acc), a.description) as general,
                        balance, 
                        CASE status WHEN '1' THEN 'Activado' ELSE 'Desactivado' END AS status
                        FROM accounting_accs a""")
        
        rows = cursor.fetchall()
        num_rows = len(rows)
        num_columns = len(cursor.description)
        #print(rows)

        self.accountingTable.setRowCount(num_rows)
        self.accountingTable.setColumnCount(num_columns)
        self.accountingTable.verticalHeader().setVisible(False)

        #headers = [desc[0] for desc in cursor.description]
        header_names = ["ID","Descripción", "Tipo de cuenta", "Trans. permitidas", "Nivel", "Cuenta general","Balance", "Estado"]
        self.accountingTable.setHorizontalHeaderLabels(header_names)

        #self.accountingTable.setHorizontalHeaderLabels(headers)
        for i, row in enumerate(rows):
            for j, value in enumerate(row[0:]):
                item = QtWidgets.QTableWidgetItem(str(value) if value is not None else "")
                self.accountingTable.setItem(i, j, item)

        cursor.close()
        connection.close()
        self.accountingTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.accountingTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        try:
            self.accountingTable.itemClicked.disconnect()
        except TypeError:
            pass 

        self.accountingTable.itemClicked.connect(self.on_table_item_clicked)

    def delete_accounting_data(self):
        # Retrieve the selected accounting ID
        accounting_id = self.accountingIdTxt.toPlainText()

        # Check if the accounting ID is empty
        if not accounting_id:
            # Disable the delete button and return
            self.accountingDeleteBtn.setEnabled(False)
            return

        # Convert the accounting ID to an integer
        try:
            accounting_id = int(accounting_id)
        except ValueError:
            # Show a pop-up alert for invalid input
            QMessageBox.critical(None, "Error", "ID inválido.")
            return

        # Show a confirmation pop-up
        #confirmation, ok = QInputDialog.getInt(self.tabWidget, "Confirmation", "¿Seguro que quieres eliminar este registro?", min=0, max=1)
        confirmation = QMessageBox.question(self.tabWidget, "Confirmación", 
                                        "¿Seguro que quieres eliminar este registro?", 
                                        QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            try:
                # Establish a connection to the Oracle database
                os.environ['TNS_ADMIN'] = '/path/to/instantclient_19_8/network/admin'
                connection = cx_Oracle.connect('username', 'password', 'tnsname')
                cursor = connection.cursor()

                # Execute the deletion query
                cursor.execute("DELETE FROM accounting_accs WHERE id = :accounting_id", accounting_id=accounting_id)
                connection.commit()
                cursor.close()
                connection.close()

                # Show a pop-up alert
                QMessageBox.information(None, "Éxito", "¡El registro se ha eliminado con éxito!")

                # Clear the text fields
                self.clear_text_fields()

                # Reload the table view with updated data
                self.query_accounting_accs()
            except Exception as e:
                # Show a pop-up alert
                QMessageBox.critical(None, "Error", f"Error al momento de eliminar el registro: {str(e)}")
        else:
            # User canceled the deletion
            QMessageBox.information(None, "Abortado", "Eliminación cancelada.")

    def on_table_item_clicked(self, item):
        row_index = item.row()
        row = []
        for column in range(self.accountingTable.columnCount()):
            table_item = self.accountingTable.item(row_index, column)
            if table_item is not None:
                row.append(table_item.text())
            else:
                row.append("")

        if self.previous_selected_row == row:
            # Same row selected again (deselecting)
            self.clear_text_fields()
            self.previous_selected_row = None
            self.accountingDeleteBtn.setEnabled(False)
        else:
            # New row selected
            self.accountingIdTxt.setText(row[0])
            self.accountingDescTxt.setText(row[1])
            self.accountingAccTypeTxt.setText(row[2])
            self.accountingTrxAllwTxt.setText(row[3])
            self.accountingAccLvlTxt.setText(row[4])
            self.accountingGnlAccTxt.setText(row[5])
            self.accountingBlnTxt.setText(row[6])
            self.accountingStsTxt.setText(row[7])
            self.previous_selected_row = row
            self.accountingDeleteBtn.setEnabled(True)

        self.row_selected.emit(row)

    def clear_text_fields(self):
        self.accountingIdTxt.clear()
        self.accountingDescTxt.clear()
        self.accountingAccTypeTxt.clear()
        self.accountingTrxAllwTxt.clear()
        self.accountingBlnTxt.clear()
        self.accountingStsTxt.clear()
        ui.accountingAccLvlTxt.clear()
        ui.accountingGnlAccTxt.clear()
        ui.previous_selected_row = None
        self.accountingDeleteBtn.setEnabled(False)

def handle_row_deselected():
    ui.previous_selected_row = None

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(tabWidget)
    ui.query_accounting_accs()

    try:
        ui.accountingTable.itemSelectionChanged.disconnect()
    except TypeError:
        pass
    ui.accountingTable.itemSelectionChanged.connect(handle_row_deselected)
    ui.accountingInsertBtn.clicked.connect(ui.insert_accounting_data)
    ui.accountingDeleteBtn.clicked.connect(ui.delete_accounting_data)

    tabWidget.show()
    sys.exit(app.exec_())
