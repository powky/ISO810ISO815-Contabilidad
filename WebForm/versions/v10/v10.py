from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QInputDialog
import cx_Oracle
import os
import datetime

class Ui_TabWidget(QtCore.QObject):

    # Conexión de DB
    os.environ['TNS_ADMIN'] = '/Users/fernandez/instantclient_19_8/network/admin'
    connection = cx_Oracle.connect('ADMIN', 'Iso815810unapec', 'iso8xx_high')
    row_selected = QtCore.pyqtSignal(list)

    # Declarar variables para manejo de UI
    previous_selected_row = None
    select_fields = None
    is_filtered = False
    data_modified = False
    
    # Definición del UI 

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
        self.accountingInsertBtn.setStyleSheet("color: blue;")
        self.accountingIdTxt = QtWidgets.QTextEdit(self.accountingTab)
        self.accountingIdTxt.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.accountingIdTxt.setObjectName("accountingIdTxt")
        self.accountingAccLvlTxt = QtWidgets.QComboBox(self.accountingTab)
        self.accountingAccLvlTxt.setGeometry(QtCore.QRect(10, 80, 141, 31))
        self.accountingAccLvlTxt.setObjectName("accountingAccLvlTxt")
        self.accountingDescTxt = QtWidgets.QTextEdit(self.accountingTab)
        self.accountingDescTxt.setGeometry(QtCore.QRect(160, 20, 141, 31))
        self.accountingDescTxt.setObjectName("accountingDescTxt")
        self.accountingGnlAccTxt = QtWidgets.QTextEdit(self.accountingTab)
        self.accountingGnlAccTxt.setGeometry(QtCore.QRect(160, 80, 141, 31))
        self.accountingGnlAccTxt.setObjectName("accountingGnlAccTxt")
        self.accountingAccTypeTxt = QtWidgets.QComboBox(self.accountingTab)
        self.accountingAccTypeTxt.setGeometry(QtCore.QRect(310, 20, 141, 31))
        self.accountingAccTypeTxt.setObjectName("accountingAccTypeTxt")
        self.accountingTrxAllwTxt = QtWidgets.QComboBox(self.accountingTab)
        self.accountingTrxAllwTxt.setGeometry(QtCore.QRect(460, 20, 141, 31))
        self.accountingTrxAllwTxt.setObjectName("accountingTrxAllwTxt")
        self.accountingBlnTxt = QtWidgets.QTextEdit(self.accountingTab)
        self.accountingBlnTxt.setGeometry(QtCore.QRect(310, 80, 141, 31))
        self.accountingBlnTxt.setObjectName("accountingBlnTxt")
        self.accountingStsTxt = QtWidgets.QComboBox(self.accountingTab)
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

        self.accountingIdTxt.textChanged.connect(self.update_button_enabled)
        self.accountingDescTxt.textChanged.connect(self.update_button_enabled)
        self.accountingAccTypeTxt.currentIndexChanged.connect(self.update_button_enabled)
        self.accountingTrxAllwTxt.currentIndexChanged.connect(self.update_button_enabled)
        self.accountingAccLvlTxt.currentIndexChanged.connect(self.update_button_enabled)
        self.accountingGnlAccTxt.textChanged.connect(self.update_button_enabled)
        self.accountingBlnTxt.textChanged.connect(self.update_button_enabled)
        self.accountingStsTxt.currentIndexChanged.connect(self.update_button_enabled)

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
        self.acctypeOrgTxt = QtWidgets.QComboBox(self.acctypesTab)
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
        self.acctypeStsTxt = QtWidgets.QComboBox(self.acctypesTab)
        self.acctypeStsTxt.setGeometry(QtCore.QRect(230, 90, 141, 31))
        self.acctypeStsTxt.setObjectName("acctypeStsTxt")
        self.acctypeInsertBtn = QtWidgets.QPushButton(self.acctypesTab)
        self.acctypeInsertBtn.setGeometry(QtCore.QRect(390, 100, 141, 32))
        self.acctypeInsertBtn.setObjectName("acctypeInsertBtn")
        self.acctypeInsertBtn.setStyleSheet("color: blue;")
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

        self.acctypeIdTxt.textChanged.connect(self.update_button_enabled)
        self.acctypeDescTxt.textChanged.connect(self.update_button_enabled)
        self.acctypeOrgTxt.currentIndexChanged.connect(self.update_button_enabled)
        self.acctypeStsTxt.currentIndexChanged.connect(self.update_button_enabled)
        
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
        self.currencyRateTxt.setGeometry(QtCore.QRect(230, 30, 131, 31))
        self.currencyRateTxt.setObjectName("currencyRateTxt")
        self.currencyFetchBtn = QtWidgets.QPushButton(self.currencyTab)
        self.currencyFetchBtn.setGeometry(QtCore.QRect(370, 100, 161, 32))
        self.currencyFetchBtn.setObjectName("currencyFetchBtn")
        self.currencyIdTxt = QtWidgets.QTextEdit(self.currencyTab)
        self.currencyIdTxt.setGeometry(QtCore.QRect(80, 30, 131, 31))
        self.currencyIdTxt.setObjectName("currencyIdTxt")
        self.currencyStatusLbl = QtWidgets.QLabel(self.currencyTab)
        self.currencyStatusLbl.setGeometry(QtCore.QRect(230, 70, 60, 16))
        self.currencyStatusLbl.setObjectName("currencyStatusLbl")
        self.currencyIdLbl = QtWidgets.QLabel(self.currencyTab)
        self.currencyIdLbl.setGeometry(QtCore.QRect(80, 10, 60, 16))
        self.currencyIdLbl.setObjectName("currencyIdLbl")
        self.currencyStsTxt = QtWidgets.QComboBox(self.currencyTab)
        self.currencyStsTxt.setGeometry(QtCore.QRect(230, 90, 131, 31))
        self.currencyStsTxt.setObjectName("currencyStsTxt")
        self.currencyDescTxt = QtWidgets.QTextEdit(self.currencyTab)
        self.currencyDescTxt.setGeometry(QtCore.QRect(80, 90, 131, 31))
        self.currencyDescTxt.setObjectName("currencyDescTxt")
        self.currencyDeleteBtn = QtWidgets.QPushButton(self.currencyTab)
        self.currencyDeleteBtn.setGeometry(QtCore.QRect(370, 10, 81, 32))
        self.currencyDeleteBtn.setObjectName("currencyDeleteBtn")
        self.currencyUpdateBtn = QtWidgets.QPushButton(self.currencyTab)
        self.currencyUpdateBtn.setGeometry(QtCore.QRect(370, 40, 161, 32))
        self.currencyUpdateBtn.setObjectName("currencyUpdateBtn")
        self.currencyInsertBtn = QtWidgets.QPushButton(self.currencyTab)
        self.currencyInsertBtn.setGeometry(QtCore.QRect(450, 10, 81, 32))
        self.currencyInsertBtn.setObjectName("currencyInsertBtn")
        self.currencyDescLbl = QtWidgets.QLabel(self.currencyTab)
        self.currencyDescLbl.setGeometry(QtCore.QRect(80, 70, 91, 16))
        self.currencyDescLbl.setObjectName("currencyDescLbl")
        self.currencyFilterBtn = QtWidgets.QPushButton(self.currencyTab)
        self.currencyFilterBtn.setGeometry(QtCore.QRect(370, 70, 161, 32))
        self.currencyFilterBtn.setObjectName("currencyFilterBtn")

        tabWidget.addTab(self.currencyTab, "")

        self.currencyIdTxt.textChanged.connect(self.update_button_enabled)
        self.currencyDescTxt.textChanged.connect(self.update_button_enabled)
        self.currencyRateTxt.textChanged.connect(self.update_button_enabled)
        self.currencyStsTxt.currentIndexChanged.connect(self.update_button_enabled)

        self.usersTab = QtWidgets.QWidget()
        self.usersTab.setObjectName("usersTab")
        self.auxDeleteBtn = QtWidgets.QPushButton(self.usersTab)
        self.auxDeleteBtn.setGeometry(QtCore.QRect(390, 10, 141, 32))
        self.auxDeleteBtn.setObjectName("auxDeleteBtn")
        self.auxStatusTxt = QtWidgets.QComboBox(self.usersTab)
        self.auxStatusTxt.setGeometry(QtCore.QRect(230, 30, 141, 31))
        self.auxStatusTxt.setObjectName("auxStatusTxt")
        self.auxUpdateBtn = QtWidgets.QPushButton(self.usersTab)
        self.auxUpdateBtn.setGeometry(QtCore.QRect(390, 70, 141, 32))
        self.auxUpdateBtn.setObjectName("auxUpdateBtn")
        self.auxDescLbl = QtWidgets.QLabel(self.usersTab)
        self.auxDescLbl.setGeometry(QtCore.QRect(80, 70, 91, 16))
        self.auxDescLbl.setObjectName("auxDescLbl")
        self.auxDescTxt = QtWidgets.QTextEdit(self.usersTab)
        self.auxDescTxt.setGeometry(QtCore.QRect(80, 90, 291, 31))
        self.auxDescTxt.setObjectName("auxDescTxt")
        self.auxIdLbl = QtWidgets.QLabel(self.usersTab)
        self.auxIdLbl.setGeometry(QtCore.QRect(80, 10, 60, 16))
        self.auxIdLbl.setObjectName("auxIdLbl")
        self.auxInsertBtn = QtWidgets.QPushButton(self.usersTab)
        self.auxInsertBtn.setGeometry(QtCore.QRect(390, 100, 141, 32))
        self.auxInsertBtn.setObjectName("auxInsertBtn")
        self.auxInsertBtn.setStyleSheet("color: blue;")
        self.auxIdTxt = QtWidgets.QTextEdit(self.usersTab)
        self.auxIdTxt.setGeometry(QtCore.QRect(80, 30, 141, 31))
        self.auxIdTxt.setObjectName("auxIdTxt")
        self.auxStatusLbl = QtWidgets.QLabel(self.usersTab)
        self.auxStatusLbl.setGeometry(QtCore.QRect(230, 10, 60, 16))
        self.auxStatusLbl.setObjectName("auxStatusLbl")
        self.auxFetchBtn = QtWidgets.QPushButton(self.usersTab)
        self.auxFetchBtn.setGeometry(QtCore.QRect(390, 40, 141, 32))
        self.auxFetchBtn.setObjectName("auxFetchBtn")
        self.auxTable = QtWidgets.QTableWidget(self.usersTab)
        self.auxTable.setGeometry(QtCore.QRect(80, 140, 451, 261))
        self.auxTable.setObjectName("auxTable")
        self.auxTable.setColumnCount(0)
        self.auxTable.setRowCount(0)
        tabWidget.addTab(self.usersTab, "")

        self.auxIdTxt.textChanged.connect(self.update_button_enabled)
        self.auxDescTxt.textChanged.connect(self.update_button_enabled)
        self.auxStatusTxt.currentIndexChanged.connect(self.update_button_enabled)

        self.entriesTab = QtWidgets.QWidget()
        self.entriesTab.setObjectName("entriesTab")
        self.entriesAccTypeTxt = QtWidgets.QComboBox(self.entriesTab)
        self.entriesAccTypeTxt.setGeometry(QtCore.QRect(460, 20, 141, 31))
        self.entriesAccTypeTxt.setObjectName("entriesAccTypeTxt")
        self.entriesIdLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesIdLbl.setGeometry(QtCore.QRect(10, 0, 60, 16))
        self.entriesIdLbl.setObjectName("entriesIdLbl")
        self.entriesStatusLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesStatusLbl.setGeometry(QtCore.QRect(460, 60, 111, 16))
        self.entriesStatusLbl.setObjectName("entriesStatusLbl")
        self.entriesDescTxt = QtWidgets.QTextEdit(self.entriesTab)
        self.entriesDescTxt.setGeometry(QtCore.QRect(160, 20, 141, 31))
        self.entriesDescTxt.setObjectName("entriesDescTxt")
        self.entriesAmountLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesAmountLbl.setGeometry(QtCore.QRect(310, 60, 101, 16))
        self.entriesAmountLbl.setObjectName("entriesAmountLbl")
        self.entriesTable = QtWidgets.QTableWidget(self.entriesTab)
        self.entriesTable.setGeometry(QtCore.QRect(10, 160, 591, 251))
        self.entriesTable.setObjectName("entriesTable")
        self.entriesTable.setColumnCount(0)
        self.entriesTable.setRowCount(0)
        self.entriesAccOrigTxt = QtWidgets.QComboBox(self.entriesTab)
        self.entriesAccOrigTxt.setGeometry(QtCore.QRect(310, 20, 141, 31))
        self.entriesAccOrigTxt.setObjectName("entriesAccOrigTxt")
        self.entriesUpdateBtn = QtWidgets.QPushButton(self.entriesTab)
        self.entriesUpdateBtn.setGeometry(QtCore.QRect(370, 120, 111, 32))
        self.entriesUpdateBtn.setObjectName("entriesUpdateBtn")
        self.entriesAccTypeLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesAccTypeLbl.setGeometry(QtCore.QRect(460, 0, 121, 16))
        self.entriesAccTypeLbl.setObjectName("entriesAccTypeLbl")
        self.entriesAccNumTxt = QtWidgets.QComboBox(self.entriesTab)
        self.entriesAccNumTxt.setGeometry(QtCore.QRect(10, 80, 141, 31))
        self.entriesAccNumTxt.setObjectName("entriesAccNumTxt")
        self.entriesInsertBtn = QtWidgets.QPushButton(self.entriesTab)
        self.entriesInsertBtn.setGeometry(QtCore.QRect(490, 120, 111, 32))
        self.entriesInsertBtn.setObjectName("entriesInsertBtn")
        self.entriesStsTxt = QtWidgets.QTextEdit(self.entriesTab)
        self.entriesStsTxt.setGeometry(QtCore.QRect(460, 80, 141, 31))
        self.entriesStsTxt.setObjectName("entriesStsTxt")
        self.entriesFilterBtn = QtWidgets.QPushButton(self.entriesTab)
        self.entriesFilterBtn.setGeometry(QtCore.QRect(130, 120, 111, 32))
        self.entriesFilterBtn.setObjectName("entriesFilterBtn")
        self.entriesIdTxt = QtWidgets.QTextEdit(self.entriesTab)
        self.entriesIdTxt.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.entriesIdTxt.setObjectName("entriesIdTxt")
        self.entriesDeleteBtn = QtWidgets.QPushButton(self.entriesTab)
        self.entriesDeleteBtn.setGeometry(QtCore.QRect(10, 120, 111, 32))
        self.entriesDeleteBtn.setObjectName("entriesDeleteBtn")
        self.entriesDescLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesDescLbl.setGeometry(QtCore.QRect(160, 0, 91, 16))
        self.entriesDescLbl.setObjectName("entriesDescLbl")
        self.entriesAccNumLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesAccNumLbl.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.entriesAccNumLbl.setObjectName("entriesAccNumLbl")
        self.entriesAmountTxt = QtWidgets.QTextEdit(self.entriesTab)
        self.entriesAmountTxt.setGeometry(QtCore.QRect(310, 80, 141, 31))
        self.entriesAmountTxt.setObjectName("entriesAmountTxt")
        self.entriesDateLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesDateLbl.setGeometry(QtCore.QRect(160, 60, 121, 16))
        self.entriesDateLbl.setObjectName("entriesDateLbl")
        self.entriesAccOrigLbl = QtWidgets.QLabel(self.entriesTab)
        self.entriesAccOrigLbl.setGeometry(QtCore.QRect(310, 0, 121, 16))
        self.entriesAccOrigLbl.setObjectName("entriesAccOrigLbl")
        self.entriesDateTxt = QtWidgets.QTextEdit(self.entriesTab)
        self.entriesDateTxt.setGeometry(QtCore.QRect(160, 80, 141, 31))
        self.entriesDateTxt.setObjectName("entriesDateTxt")
        self.entriesFetchBtn = QtWidgets.QPushButton(self.entriesTab)
        self.entriesFetchBtn.setGeometry(QtCore.QRect(250, 120, 111, 32))
        self.entriesFetchBtn.setObjectName("entriesFetchBtn")
        tabWidget.addTab(self.entriesTab, "")

        self.entriesIdTxt.textChanged.connect(self.update_button_enabled)
        self.entriesDescTxt.textChanged.connect(self.update_button_enabled)
        self.entriesAccOrigTxt.currentIndexChanged.connect(self.update_button_enabled)
        self.entriesAccNumTxt.currentIndexChanged.connect(self.update_button_enabled)
        self.entriesAccTypeTxt.currentIndexChanged.connect(self.update_button_enabled)
        self.entriesDateTxt.textChanged.connect(self.update_button_enabled)
        self.entriesAmountTxt.textChanged.connect(self.update_button_enabled)
        self.entriesStsTxt.textChanged.connect(self.update_button_enabled)

        self.retranslateUi(tabWidget)
        tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(tabWidget)

    def retranslateUi(self, tabWidget):
        _translate = QtCore.QCoreApplication.translate
        tabWidget.setWindowTitle(_translate("tabWidget", "Gestión de Contabilidad para ISO8XX"))

        self.accountingUpdateBtn.setText(_translate("tabWidget", "Guardar cambios"))
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
        self.acctypeUpdateBtn.setText(_translate("tabWidget", "Guardar cambios"))
        self.acctypeDeleteBtn.setText(_translate("tabWidget", "Eliminar"))
        self.acctypeDeleteBtn.setStyleSheet("color: rgb(255, 0, 0);")
        tabWidget.setTabText(tabWidget.indexOf(self.acctypesTab), _translate("tabWidget", "Tipos de cuentas"))

        self.currencyRateLbl.setText(_translate("tabWidget", "Tasa"))
        self.currencyFetchBtn.setText(_translate("tabWidget", "Actualizar tasas"))
        self.currencyStatusLbl.setText(_translate("tabWidget", "Estatus"))
        self.currencyIdLbl.setText(_translate("tabWidget", "ID"))
        self.currencyDeleteBtn.setText(_translate("tabWidget", "Eliminar"))
        self.currencyDeleteBtn.setStyleSheet("color: rgb(255, 0, 0);")
        self.currencyUpdateBtn.setText(_translate("tabWidget", "Guardar cambios"))
        self.currencyInsertBtn.setText(_translate("tabWidget", "Crear"))
        self.currencyDescLbl.setText(_translate("tabWidget", "Descripción"))
        self.currencyFilterBtn.setText(_translate("tabWidget", "Filtrar"))
        self.currencyInsertBtn.setStyleSheet("color: blue;")
        self.currencyFetchBtn.setStyleSheet("color: green;")
        tabWidget.setTabText(tabWidget.indexOf(self.currencyTab), _translate("tabWidget", "Monedas"))

        self.auxDeleteBtn.setText(_translate("tabWidget", "Eliminar"))
        self.auxDeleteBtn.setStyleSheet("color: rgb(255, 0, 0);")
        self.auxUpdateBtn.setText(_translate("tabWidget", "Guardar cambios"))
        self.auxDescLbl.setText(_translate("tabWidget", "Nombre"))
        self.auxIdLbl.setText(_translate("tabWidget", "ID"))
        self.auxInsertBtn.setText(_translate("tabWidget", "Crear"))
        self.auxStatusLbl.setText(_translate("tabWidget", "Estatus"))
        self.auxFetchBtn.setText(_translate("tabWidget", "Filtrar"))
        tabWidget.setTabText(tabWidget.indexOf(self.usersTab), _translate("tabWidget", "Auxiliares"))

        self.entriesIdLbl.setText(_translate("tabWidget", "ID"))
        self.entriesStatusLbl.setText(_translate("tabWidget", "Estatus"))
        self.entriesAmountLbl.setText(_translate("tabWidget", "Monto"))
        self.entriesUpdateBtn.setText(_translate("tabWidget", "Guardar"))
        self.entriesAccTypeLbl.setText(_translate("tabWidget", "Movimiento"))
        self.entriesInsertBtn.setText(_translate("tabWidget", "Crear"))
        self.entriesFilterBtn.setText(_translate("tabWidget", "Filtrar"))
        self.entriesDeleteBtn.setText(_translate("tabWidget", "Eliminar"))
        self.entriesDeleteBtn.setStyleSheet("color: rgb(255, 0, 0);")
        self.entriesDescLbl.setText(_translate("tabWidget", "Descripción"))
        self.entriesAccNumLbl.setText(_translate("tabWidget", "Cta.\u00A0contable"))
        self.entriesDateLbl.setText(_translate("tabWidget", "Fecha de registro"))
        self.entriesAccOrigLbl.setText(_translate("tabWidget", "Auxiliar"))
        self.entriesFetchBtn.setText(_translate("tabWidget", "Refrescar"))
        self.entriesInsertBtn.setStyleSheet("color: blue;")
        self.entriesFetchBtn.setStyleSheet("color: green;")
        tabWidget.setTabText(tabWidget.indexOf(self.entriesTab), _translate("tabWidget", "Entradas contables"))

    # Funciones que consultan data 

    def query_accounting_accs(self):

        # Query inicial
        cursor = self.connection.cursor()
        cursor.execute("""SELECT id, 
                        description,
                        (SELECT b.description FROM acc_types b WHERE b.id = a.acc_types) as acc_type,
                        CASE trx_allowed WHEN 'Y' THEN 'Si' ELSE 'No' END AS trx_allowed, 
                        acc_level,
                        COALESCE((SELECT b.description FROM accounting_accs b WHERE b.id = a.general_acc), a.description) as general,
                        balance, 
                        CASE status WHEN '1' THEN 'Activado' ELSE 'Desactivado' END AS status
                        FROM accounting_accs a""")
        
        # Preparar la tabla para recibir los datos
        rows = cursor.fetchall()
        num_rows = len(rows)
        num_columns = len(cursor.description)
        self.accountingTable.setRowCount(num_rows)
        self.accountingTable.setColumnCount(num_columns)
        header_names = ["ID","Descripción", "Tipo de cuenta", "Trans.\u00A0permitidas", "Nivel", "Cuenta general","Balance", "Estado"]
        self.accountingTable.setHorizontalHeaderLabels(header_names)

        # Llenar la tabla con los datos del query
        for i, row in enumerate(rows):
            for j, value in enumerate(row[0:]):
                item = QtWidgets.QTableWidgetItem(str(value) if value is not None else "")
                self.accountingTable.setItem(i, j, item)

        cursor.close()

        # Parámetros de UI
        self.accountingTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.accountingTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.accountingTable.verticalHeader().setVisible(False)
        self.accountingDeleteBtn.setEnabled(False)
        self.accountingInsertBtn.setEnabled(False)
        self.accountingFilterBtn.setEnabled(False)
        self.accountingUpdateBtn.setEnabled(False)
        self.accountingTrxAllwTxt.clear()
        self.accountingAccLvlTxt.clear()
        self.accountingStsTxt.clear()
        self.accountingStsTxt.addItems(['','Activado','Desactivado'])
        self.accountingTrxAllwTxt.addItems(['','Si','No'])
        self.accountingAccLvlTxt.addItems(['','1','2','3'])
        try:
            self.accountingTable.itemClicked.disconnect()
        except TypeError:
            pass 

        # Iniciar función de selección de datos de la tabla
        self.accountingTable.itemClicked.connect(lambda item: self.on_table_item_clicked(item, self.accountingTable))

        # ComboBox de tipo de cuenta tiene que llenarse a partir de la base de datos
        cursor = self.connection.cursor()
        cursor.execute("SELECT description FROM acc_types")
        acc_types_rows = cursor.fetchall()
        combobox_items = [''] + [row[0] for row in acc_types_rows]
        self.accountingAccTypeTxt.clear()
        self.accountingAccTypeTxt.addItems(combobox_items)
        self.accountingAccTypeTxt.setCurrentIndex(-1)
        cursor.close()

    def query_acctypes(self):

        # Conexión de DB
        cursor = self.connection.cursor()
        cursor.execute("""SELECT id, description, orig, CASE status WHEN '1' THEN 'Activado' ELSE 'Desactivado' END AS status FROM acc_types""")
        
        # Preparar la tabla para recibir los datos
        rows = cursor.fetchall()
        num_rows = len(rows)
        num_columns = len(cursor.description)
        self.acctypeTable.setRowCount(num_rows)
        self.acctypeTable.setColumnCount(num_columns)
        header_names = ["ID","Descripción", "Movimiento", "Estado"]
        self.acctypeTable.setHorizontalHeaderLabels(header_names)

        # Llenar la tabla con los datos del query
        for i, row in enumerate(rows):
            for j, value in enumerate(row[0:]):
                item = QtWidgets.QTableWidgetItem(str(value) if value is not None else "")
                self.acctypeTable.setItem(i, j, item)

        cursor.close()

        # Parámetros de UI
        self.acctypeTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.acctypeTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.acctypeTable.verticalHeader().setVisible(False)
        self.acctypeDeleteBtn.setEnabled(False)
        self.acctypeInsertBtn.setEnabled(False)
        self.acctypeFilterBtn.setEnabled(False)
        self.acctypeUpdateBtn.setEnabled(False)
        self.acctypeStsTxt.clear()
        self.acctypeOrgTxt.clear()
        self.acctypeStsTxt.addItems(['','Activado','Desactivado'])
        self.acctypeOrgTxt.addItems(['','DB','CR'])
        try:
            self.acctypeTable.itemClicked.disconnect()
        except TypeError:
            pass 

        # Iniciar función de selección de datos de la tabla
        self.acctypeTable.itemClicked.connect(lambda item: self.on_table_item_clicked(item, self.acctypeTable))

    def query_currency(self):

        # Conexión de DB
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, description, rate, CASE status WHEN '1' THEN 'Activado' ELSE 'Desactivado' END AS status FROM currency")
        
        # Preparar la tabla para recibir los datos
        rows = cursor.fetchall()
        num_rows = len(rows)
        num_columns = len(cursor.description)
        self.currencyTable.setRowCount(num_rows)
        self.currencyTable.setColumnCount(num_columns)
        header_names = ["ID","Descripción", "Tasa", "Estado"]
        self.currencyTable.setHorizontalHeaderLabels(header_names)
        
        # Llenar la tabla con los datos del query
        for i, row in enumerate(rows):
            for j, value in enumerate(row[0:]):
                item = QtWidgets.QTableWidgetItem(str(value) if value is not None else "")
                self.currencyTable.setItem(i, j, item)

        cursor.close()

        # Parámetros de UI
        self.currencyTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.currencyTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.currencyTable.verticalHeader().setVisible(False)
        self.currencyDeleteBtn.setEnabled(False)
        self.currencyInsertBtn.setEnabled(False)
        self.currencyUpdateBtn.setEnabled(False)
        self.currencyFetchBtn.setEnabled(False)
        self.currencyFilterBtn.setEnabled(False)
        self.currencyStsTxt.clear()
        self.currencyStsTxt.addItems(['','Activado','Desactivado'])
        try:
            self.currencyTable.itemClicked.disconnect()
        except TypeError:
            pass 

        # Iniciar función de selección de datos de la tabla
        self.currencyTable.itemClicked.connect(lambda item: self.on_table_item_clicked(item, self.currencyTable))

    def query_auxsys(self):

        # Conexión de DB
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, CASE status WHEN '1' THEN 'Activado' ELSE 'Desactivado' END AS status FROM aux_systems")
        
        # Preparar la tabla para recibir los datos
        rows = cursor.fetchall()
        num_rows = len(rows)
        num_columns = len(cursor.description)
        self.auxTable.setRowCount(num_rows)
        self.auxTable.setColumnCount(num_columns)
        header_names = ["ID","Nombre", "Estado"]
        self.auxTable.setHorizontalHeaderLabels(header_names)
        
        # Llenar la tabla con los datos del query
        for i, row in enumerate(rows):
            for j, value in enumerate(row[0:]):
                item = QtWidgets.QTableWidgetItem(str(value) if value is not None else "")
                self.auxTable.setItem(i, j, item)

        cursor.close()
        
        # Parámetros de UI
        self.auxTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.auxTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.auxTable.verticalHeader().setVisible(False)
        self.auxDeleteBtn.setEnabled(False)
        self.auxInsertBtn.setEnabled(False)
        self.auxFetchBtn.setEnabled(False)
        self.auxUpdateBtn.setEnabled(False)
        self.auxStatusTxt.clear()
        self.auxStatusTxt.addItems(['','Activado','Desactivado'])
        try:
            self.auxTable.itemClicked.disconnect()
        except TypeError:
            pass 

        # Iniciar función de selección de datos de la tabla
        self.auxTable.itemClicked.connect(lambda item: self.on_table_item_clicked(item, self.auxTable))

    def query_entries(self): 

        # Conexión de DB
        cursor = self.connection.cursor()
        cursor.execute("""SELECT id, descrip,
                        (SELECT b.name FROM aux_systems b WHERE b.id = a.aux_id) as aux_id,
                        (SELECT c.description FROM accounting_accs c WHERE c.id = a.accs_id) as accs_id,
                        mov_type, entry_date, amount, status
                        FROM accounting_entries a""")
        
        # Preparar la tabla para recibir los datos
        rows = cursor.fetchall()
        num_rows = len(rows)
        num_columns = len(cursor.description)
        self.entriesTable.setRowCount(num_rows)
        self.entriesTable.setColumnCount(num_columns)
        header_names = ["ID","Descripción", "Auxiliar", "Cta.\u00A0contable","Movimiento","Fecha Reg.","Monto", "Estado"]
        self.entriesTable.setHorizontalHeaderLabels(header_names)
        
        # Llenar la tabla con los datos del query
        for i, row in enumerate(rows):
            for j, value in enumerate(row[0:]):
                item = QtWidgets.QTableWidgetItem(str(value) if value is not None else "")
                self.entriesTable.setItem(i, j, item)

        cursor.close()
        
        # Parámetros de UI
        self.entriesTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.entriesTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.entriesTable.verticalHeader().setVisible(False)
        self.entriesDeleteBtn.setEnabled(False)
        self.entriesInsertBtn.setEnabled(False)
        self.entriesFilterBtn.setEnabled(False)
        self.entriesUpdateBtn.setEnabled(False)
        self.entriesAccTypeTxt.clear()
        self.entriesAccTypeTxt.addItems(['','CR','DB'])

        try:
            self.entriesTable.itemClicked.disconnect()
        except TypeError:
            pass 

        # Iniciar función de selección de datos de la tabla
        self.entriesTable.itemClicked.connect(lambda item: self.on_table_item_clicked(item, self.entriesTable))

        # ComboBox de auxiliares tiene que llenarse a partir de la base de datos
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM aux_systems")
        aux_rows = cursor.fetchall()
        aux_combobox_items = [''] + [row[0] for row in aux_rows]
        self.entriesAccOrigTxt.clear()
        self.entriesAccOrigTxt.addItems(aux_combobox_items)
        self.entriesAccOrigTxt.setCurrentIndex(-1)
        cursor.close()

        # ComboBox de cuentas contables tiene que llenarse a partir de la base de datos
        cursor = self.connection.cursor()
        cursor.execute("SELECT description FROM accounting_accs")
        accs_rows = cursor.fetchall()
        accs_combobox_items = [''] + [row[0] for row in accs_rows]
        self.entriesAccNumTxt.clear()
        self.entriesAccNumTxt.addItems(accs_combobox_items)
        self.entriesAccNumTxt.setCurrentIndex(-1)
        cursor.close()

    # Funciones que insertan data

    def insert_accounting_data(self):
        
        # Almacenar los valores de los campos de texto en variables
        accounting_id = int(self.accountingIdTxt.toPlainText())
        accounting_description = str(self.accountingDescTxt.toPlainText())
        accounting_acc_type = self.accountingAccTypeTxt.currentText()
        accounting_trx_allowed = self.accountingTrxAllwTxt.currentText()
        accounting_acc_lvl = int(self.accountingAccLvlTxt.currentText())
        accounting_gnl_acc = self.accountingGnlAccTxt.toPlainText()
        accounting_balance = float(self.accountingBlnTxt.toPlainText())
        accounting_status = self.accountingStsTxt.currentText()

        # Correr el SP de Oracle para Insert
        try:
            cursor = self.connection.cursor()
            cursor.callproc("proc_insert_accounting_accs", (accounting_id, accounting_description, accounting_acc_type, accounting_trx_allowed, accounting_acc_lvl, accounting_gnl_acc, accounting_balance, accounting_status))
            self.connection.commit()
            cursor.close()

            # Pop up de confirmación
            QMessageBox.information(None, "Éxito", "¡El registro se ha creado con éxito!")

            # Llama función de borrado de datos de los campos de texto
            self.clear_text_fields()

            try:
                self.accountingTable.itemClicked.disconnect()
            except TypeError:
                pass

            # Llamada a función de query inicial para refrescar la tabla
            self.query_accounting_accs()

        # Excepción si el SP retorna un error
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al momento de crear el registro: {str(e)}")

    def insert_acctype(self):
        
        # Almacenar los valores de los campos de texto en variables
        acctype_description = str(self.acctypeDescTxt.toPlainText())
        acctype_orig = self.acctypeOrgTxt.currentText()
        acctype_estatus = self.acctypeStsTxt.currentText()

        # Correr el SP de Oracle para Insert
        try:
            cursor = self.connection.cursor()
            cursor.callproc("proc_insert_acctypes", (acctype_description, acctype_orig, acctype_estatus))
            self.connection.commit()
            cursor.close()

            # Pop up de confirmación
            QMessageBox.information(None, "Éxito", "¡El registro se ha creado con éxito!")

            # Llama función de borrado de datos de los campos de texto
            self.clear_text_fields()

            try:
                self.accountingTable.itemClicked.disconnect()
            except TypeError:
                pass

            # Llamada a función de query inicial para refrescar la tabla
            self.query_acctypes()

        # Excepción si el SP retorna un error
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al momento de crear el registro: {str(e)}")

    def insert_currency(self):
        
        # Almacenar los valores de los campos de texto en variables
        currency_description = str(self.currencyDescTxt.toPlainText())
        currency_rate = self.currencyRateTxt.toPlainText()
        currency_estatus = self.currencyStsTxt.currentText()

        # Correr el SP de Oracle para Insert
        try:
            cursor = self.connection.cursor()
            cursor.callproc("proc_insert_currency", (currency_description, currency_rate, currency_estatus))
            self.connection.commit()
            cursor.close()

            # Pop up de confirmación
            QMessageBox.information(None, "Éxito", "¡El registro se ha creado con éxito!")

            # Llama función de borrado de datos de los campos de texto
            self.clear_text_fields()

            try:
                self.currencyTable.itemClicked.disconnect()
            except TypeError:
                pass

            # Llamada a función de query inicial para refrescar la tabla
            self.query_currency()

        # Excepción si el SP retorna un error
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al momento de crear el registro: {str(e)}")

    def insert_aux(self):
        
        # Almacenar los valores de los campos de texto en variables
        aux_name = str(self.auxDescTxt.toPlainText())
        aux_estatus = self.auxStatusTxt.currentText()

        # Correr el SP de Oracle para Insert
        try:
            cursor = self.connection.cursor()
            cursor.callproc("proc_insert_aux", (aux_name, aux_estatus))
            self.connection.commit()
            cursor.close()

            # Pop up de confirmación
            QMessageBox.information(None, "Éxito", "¡El registro se ha creado con éxito!")

            # Llama función de borrado de datos de los campos de texto
            self.clear_text_fields()

            try:
                self.auxTable.itemClicked.disconnect()
            except TypeError:
                pass

            # Llamada a función de query inicial para refrescar la tabla
            self.query_auxsys()

        # Excepción si el SP retorna un error
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al momento de crear el registro: {str(e)}")

    def insert_entries(self): 
        
        # Almacenar los valores de los campos de texto en variables
        entries_description = str(self.entriesDescTxt.toPlainText())
        entries_aux = self.entriesAccOrigTxt.currentText()
        entries_mov = self.entriesAccTypeTxt.currentText()
        entries_accaccs = self.entriesAccNumTxt.currentText()
        entries_balance = float(self.entriesAmountTxt.toPlainText())

        # Correr el SP de Oracle para Insert
        try:
            cursor = self.connection.cursor()
            cursor.callproc("proc_insert_entries_gui", (entries_description, entries_aux, entries_accaccs, entries_mov, entries_balance))
            self.connection.commit()
            cursor.close()

            # Pop up de confirmación
            QMessageBox.information(None, "Éxito", "¡El registro se ha creado con éxito!")

            # Llama función de borrado de datos de los campos de texto
            self.clear_text_fields()

            try:
                self.entriesTable.itemClicked.disconnect()
            except TypeError:
                pass

            # Llamada a función de query inicial para refrescar la tabla
            self.query_entries()

        # Excepción si el SP retorna un error
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al momento de crear el registro: {str(e)}")

    # Funciones que eliminan data

    def delete_accounting_data(self):
        # Almaceno el ID de la fila seleccionada
        accounting_id = self.accountingIdTxt.toPlainText()

        # Revisar si el ID está vacío y si está vacío mostrar error
        if not accounting_id:
            QMessageBox.information(None, "Error", "Debes ingresar un número de ID.")
            return

        # Convertir el ID a entero porque se captura como texto
        try:
            accounting_id = int(accounting_id)
        except ValueError:
            # Pop up si el ID no es un número o está vacío
            QMessageBox.critical(None, "Error", "ID inválido, debes ingresar solamente números.")
            return

        # Pop up de confirmación con aceptar o cancelar
        confirmation = QMessageBox.question(self.tabWidget, "Confirmación", 
                                        "¿Seguro que quieres eliminar este registro?", 
                                        QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            try:
                # Concetarme a la DB
                cursor = self.connection.cursor()

                # Ejecución del comando DELETE filtrando solo por ID.
                cursor.execute("DELETE FROM accounting_accs WHERE id = :accounting_id", accounting_id=accounting_id)
                self.connection.commit()
                cursor.close()

                # Pop up de éxito
                QMessageBox.information(None, "Éxito", "¡El registro se ha eliminado con éxito!")

                # Llamar función de borrar datos de los campos de textos y refrescar la tabla
                self.clear_text_fields()
                self.query_accounting_accs()
            except Exception as e:
                # Si el DELETE retorna error, mostrar pop up de error con el problema
                QMessageBox.critical(None, "Error", f"Error al momento de eliminar el registro: {str(e)}")
        else:
            # Pop up si el usuario cancela la eliminación
            QMessageBox.information(None, "Abortado", "Eliminación cancelada.")

    def delete_acctype(self):
        # Almaceno el ID de la fila seleccionada
        acctype_id = self.acctypeIdTxt.toPlainText()

        # Revisar si el ID está vacío y si está vacío mostrar error
        if not acctype_id:
            QMessageBox.information(None, "Error", "Debes ingresar un número de ID.")
            return

        # Convertir el ID a entero porque se captura como texto
        try:
            acctype_id = int(acctype_id)
        except ValueError:
            # Pop up si el ID no es un número o está vacío
            QMessageBox.critical(None, "Error", "ID inválido, debes ingresar solamente números.")
            return

        # Pop up de confirmación con aceptar o cancelar
        confirmation = QMessageBox.question(self.tabWidget, "Confirmación", 
                                        "¿Seguro que quieres eliminar este registro?", 
                                        QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            try:
                # Concetarme a la DB
                cursor = self.connection.cursor()
                
                # Ejecución del comando DELETE filtrando solo por ID.
                cursor.execute("DELETE FROM acc_types WHERE id = :acctype_id", acctype_id=acctype_id)
                self.connection.commit()
                cursor.close()

                # Pop up de éxito
                QMessageBox.information(None, "Éxito", "¡El registro se ha eliminado con éxito!")

                # Llamar función de borrar datos de los campos de textos y refrescar la tabla
                self.clear_text_fields()
                self.query_acctypes()
            except Exception as e:
                # Si el DELETE retorna error, mostrar pop up de error con el problema
                QMessageBox.critical(None, "Error", f"Error al momento de eliminar el registro: {str(e)}")
        else:
            # Pop up si el usuario cancela la eliminación
            QMessageBox.information(None, "Abortado", "Eliminación cancelada.")

    def delete_currency(self):
        # Almaceno el ID de la fila seleccionada
        currency_id = self.currencyIdTxt.toPlainText()

        # Revisar si el ID está vacío y si está vacío mostrar error
        if not currency_id:
            QMessageBox.information(None, "Error", "Debes ingresar un número de ID.")
            return

        # Convertir el ID a entero porque se captura como texto
        try:
            currency_id = int(currency_id)
        except ValueError:
            # Pop up si el ID no es un número o está vacío
            QMessageBox.critical(None, "Error", "ID inválido, debes ingresar solamente números.")
            return

        # Pop up de confirmación con aceptar o cancelar
        confirmation = QMessageBox.question(self.tabWidget, "Confirmación", 
                                        "¿Seguro que quieres eliminar este registro?", 
                                        QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            try:
                # Concetarme a la DB
                cursor = self.connection.cursor()

                # Ejecución del comando DELETE filtrando solo por ID.
                cursor.execute("DELETE FROM currency WHERE id = :currency_id", currency_id=currency_id)
                self.connection.commit()
                cursor.close()

                # Pop up de éxito
                QMessageBox.information(None, "Éxito", "¡El registro se ha eliminado con éxito!")

                # Llamar función de borrar datos de los campos de textos y refrescar la tabla
                self.clear_text_fields()
                self.query_currency()
            except Exception as e:
                # Si el DELETE retorna error, mostrar pop up de error con el problema
                QMessageBox.critical(None, "Error", f"Error al momento de eliminar el registro: {str(e)}")
        else:
            # Pop up si el usuario cancela la eliminación
            QMessageBox.information(None, "Abortado", "Eliminación cancelada.")

    def delete_aux(self):
        # Almaceno el ID de la fila seleccionada
        aux_id = self.auxIdTxt.toPlainText()

        # Revisar si el ID está vacío y si está vacío mostrar error
        if not aux_id:
            QMessageBox.information(None, "Error", "Debes ingresar un número de ID.")
            return

        # Convertir el ID a entero porque se captura como texto
        try:
            aux_id = int(aux_id)
        except ValueError:
            # Pop up si el ID no es un número o está vacío
            QMessageBox.critical(None, "Error", "ID inválido, debes ingresar solamente números.")
            return

        # Pop up de confirmación con aceptar o cancelar
        confirmation = QMessageBox.question(self.tabWidget, "Confirmación", 
                                        "¿Seguro que quieres eliminar este registro?", 
                                        QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            try:
                # Concetarme a la DB
                cursor = self.connection.cursor()

                # Ejecución del comando DELETE filtrando solo por ID.
                cursor.execute("DELETE FROM aux_systems WHERE id = :aux_id", aux_id=aux_id)
                self.connection.commit()
                cursor.close()

                # Pop up de éxito
                QMessageBox.information(None, "Éxito", "¡El registro se ha eliminado con éxito!")

                # Llamar función de borrar datos de los campos de textos y refrescar la tabla
                self.clear_text_fields()
                self.query_auxsys()
            except Exception as e:
                # Si el DELETE retorna error, mostrar pop up de error con el problema
                QMessageBox.critical(None, "Error", f"Error al momento de eliminar el registro: {str(e)}")
        else:
            # Pop up si el usuario cancela la eliminación
            QMessageBox.information(None, "Abortado", "Eliminación cancelada.")

    def delete_entries(self):
        # Almaceno el ID de la fila seleccionada
        entries_id = self.entriesIdTxt.toPlainText()

        # Revisar si el ID está vacío y si está vacío mostrar error
        if not entries_id:
            QMessageBox.information(None, "Error", "Debes ingresar un número de ID.")
            return

        # Convertir el ID a entero porque se captura como texto
        try:
            entries_id = int(entries_id)
        except ValueError:
            # Pop up si el ID no es un número o está vacío
            QMessageBox.critical(None, "Error", "ID inválido, debes ingresar solamente números.")
            return

        # Pop up de confirmación con aceptar o cancelar
        confirmation = QMessageBox.question(self.tabWidget, "Confirmación", 
                                        "¿Seguro que quieres eliminar este registro?", 
                                        QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            try:
                # Concetarme a la DB
                cursor = self.connection.cursor()

                # Ejecución del comando DELETE filtrando solo por ID.
                cursor.execute("DELETE FROM accounting_entries WHERE id = :entries_id", entries_id=entries_id)
                self.connection.commit()
                cursor.close()

                # Pop up de éxito
                QMessageBox.information(None, "Éxito", "¡El registro se ha eliminado con éxito!")

                # Llamar función de borrar datos de los campos de textos y refrescar la tabla
                self.clear_text_fields()
                self.query_entries()
            except Exception as e:
                # Si el DELETE retorna error, mostrar pop up de error con el problema
                QMessageBox.critical(None, "Error", f"Error al momento de eliminar el registro: {str(e)}")
        else:
            # Pop up si el usuario cancela la eliminación
            QMessageBox.information(None, "Abortado", "Eliminación cancelada.")

    # Funciones que filtran data

    def filter_accounting_accs(self):

        accounting_filter_id = self.accountingIdTxt.toPlainText().strip()
        accounting_filter_description = self.accountingDescTxt.toPlainText().strip()
        accounting_filter_acc_type = self.accountingAccTypeTxt.currentText().strip()
        accounting_filter_trx_allowed = self.accountingTrxAllwTxt.currentText().strip()
        accounting_filter_acc_lvl = self.accountingAccLvlTxt.currentText().strip()
        accounting_filter_gnl_acc = self.accountingGnlAccTxt.toPlainText().strip()
        accounting_filter_balance = self.accountingBlnTxt.toPlainText().strip()
        accounting_filter_status = self.accountingStsTxt.currentText().strip()

        # Construct the SQL query
        query = "SELECT id, description, (SELECT b.description FROM acc_types b WHERE b.id = a.acc_types) as acc_type, " \
                "CASE trx_allowed WHEN 'Y' THEN 'Si' ELSE 'No' END AS trx_allowed, acc_level, " \
                "COALESCE((SELECT b.description FROM accounting_accs b WHERE b.id = a.general_acc), a.description) as general, " \
                "balance, CASE status WHEN '1' THEN 'Activado' ELSE 'Desactivado' END AS status " \
                "FROM accounting_accs a WHERE 1=1"

        params = []

        acc_type_mapping = {
            "Activos": 1, "activos": 1, "Pasivos": 2, "pasivos": 2, "Capital": 3, "capital": 3, 
            "Ingresos": 4, "ingresos": 4, "Costos": 5, "costos": 5, "Gastos": 6, "gastos": 6,
            "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6
        }

        trx_allowed_mapping = {
            "No": "N", "no": "N", "si": "Y", "Si": "Y", "Sí": "Y", "sí": "Y", "N": "N", "Y": "Y"
        }

        status_mapping = {
            "activado": "1", "Activado": "1", "Desactivado": "0", "desactivado": "0", "1": "1", "0": "0", "off": "0", 
            "on": "1", "Off": "0", "On": "1", "activo": "1", "Activo": "1", "Inactivo": "0", "inactivo": "0"
        }

        # Add filter conditions dynamically
        if accounting_filter_id:
            try:
                params.append(int(accounting_filter_id))
                query += " AND id = :id"
            except ValueError:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para ID.")
                return
            
        if accounting_filter_description:
            params.append(accounting_filter_description)
            query += " AND description = :description"

        if accounting_filter_acc_type:
            if accounting_filter_acc_type in acc_type_mapping:
                acc_type_value = acc_type_mapping[accounting_filter_acc_type]
                params.append(acc_type_value)
                query += " AND acc_types = :acc_type"
            else:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para tipo de cuenta.")
                return
            
        if accounting_filter_trx_allowed:
            if accounting_filter_trx_allowed in trx_allowed_mapping:
                trx_allw_value = trx_allowed_mapping[accounting_filter_trx_allowed]
                params.append(trx_allw_value)
                query += " AND trx_allowed = :trx_allowed"
            else:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para permite transacción.")
                return
            
        if accounting_filter_acc_lvl:
            try:
                params.append(int(accounting_filter_acc_lvl))
                query += " AND acc_level = :acc_level"
            except ValueError:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para nivel de cuenta.")
                return
            
        if accounting_filter_gnl_acc:
            params.append(accounting_filter_gnl_acc)
            query += " AND general_acc = :general_acc"

        if accounting_filter_balance:
            try:
                params.append(float(accounting_filter_balance))
                query += " AND balance = :balance"
            except ValueError:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para balance, introduce un número válido.")
                return
            
        if accounting_filter_status:
            if accounting_filter_status in status_mapping:
                status_value = status_mapping[accounting_filter_status]
                params.append(status_value)
                query += " AND status = :status"
            else:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para estatus.")
                return

        # Fetch filtered rows from the database
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        num_rows = len(rows)
        num_columns = len(cursor.description)
        self.accountingTable.setRowCount(num_rows)
        self.accountingTable.setColumnCount(num_columns)
        self.is_filtered = True

        header_names = ["ID", "Descripción", "Tipo de cuenta", "Trans. permitidas", "Nivel", "Cuenta general", "Balance", "Estado"]
        self.accountingTable.setHorizontalHeaderLabels(header_names)

        for i, row in enumerate(rows):
            for j, value in enumerate(row[0:]):
                item = QtWidgets.QTableWidgetItem(str(value) if value is not None else "")
                self.accountingTable.setItem(i, j, item)

        cursor.close()

        if self.accountingFilterBtn.text() == "Borrar filtros" and self.is_filtered:
            self.clear_text_fields()
            self.accountingFilterBtn.setText("Filtrar")
            self.query_accounting_accs()
            self.is_filtered = False

    def filter_acctype(self):

        acctype_filter_id = self.acctypeIdTxt.toPlainText().strip()
        acctype_filter_description = self.acctypeDescTxt.toPlainText().strip()
        acctype_filter_orig = self.acctypeOrgTxt.currentText().strip()
        acctype_filter_status = self.acctypeStsTxt.currentText().strip()

        # Construct the SQL query
        query = "SELECT id, description, orig, CASE status WHEN '1' THEN 'Activado' ELSE 'Desactivado' END AS status FROM acc_types WHERE 1=1"

        params = []

        status_mapping = {
            "activado": "1", "Activado": "1", "Desactivado": "0", "desactivado": "0", "1": "1", "0": "0", "off": "0", 
            "on": "1", "Off": "0", "On": "1", "activo": "1", "Activo": "1", "Inactivo": "0", "inactivo": "0"
        }

        # Add filter conditions dynamically
        if acctype_filter_id:
            try:
                params.append(int(acctype_filter_id))
                query += " AND id = :id"
            except ValueError:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para ID.")
                return
            
        if acctype_filter_description:
            params.append(acctype_filter_description)
            query += " AND description = :description"
            
        if acctype_filter_orig:
            params.append(acctype_filter_orig)
            query += " AND orig = :orig"
            
        if acctype_filter_status:
            if acctype_filter_status in status_mapping:
                status_value = status_mapping[acctype_filter_status]
                params.append(status_value)
                query += " AND status = :status"
            else:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para estatus.")
                return

        # Fetch filtered rows from the database
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        num_rows = len(rows)
        num_columns = len(cursor.description)
        self.acctypeTable.setRowCount(num_rows)
        self.acctypeTable.setColumnCount(num_columns)
        self.is_filtered = True

        header_names = ["ID", "Descripción", "Movimiento", "Estado"]
        self.acctypeTable.setHorizontalHeaderLabels(header_names)

        for i, row in enumerate(rows):
            for j, value in enumerate(row[0:]):
                item = QtWidgets.QTableWidgetItem(str(value) if value is not None else "")
                self.acctypeTable.setItem(i, j, item)

        cursor.close()

        if self.acctypeFilterBtn.text() == "Borrar filtros" and self.is_filtered:
            self.clear_text_fields()
            self.acctypeFilterBtn.setText("Filtrar")
            self.query_acctypes()
            self.is_filtered = False

    def filter_currency(self):

        currency_filter_id = self.currencyIdTxt.toPlainText().strip()
        currency_filter_description = self.currencyDescTxt.toPlainText().strip()
        currency_filter_rate = self.currencyRateTxt.toPlainText().strip()
        currency_filter_status = self.currencyStsTxt.currentText().strip()

        # Construct the SQL query
        query = "SELECT id, description, rate, CASE status WHEN '1' THEN 'Activado' ELSE 'Desactivado' END AS status FROM currency WHERE 1=1"

        params = []

        status_mapping = {
            "activado": "1", "Activado": "1", "Desactivado": "0", "desactivado": "0", "1": "1", "0": "0", "off": "0", 
            "on": "1", "Off": "0", "On": "1", "activo": "1", "Activo": "1", "Inactivo": "0", "inactivo": "0"
        }

        # Add filter conditions dynamically
        if currency_filter_id:
            try:
                params.append(int(currency_filter_id))
                query += " AND id = :id"
            except ValueError:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para ID.")
                return
            
        if currency_filter_description:
            params.append(currency_filter_description)
            query += " AND description = :description"
            
        if currency_filter_rate:
            params.append(currency_filter_rate)
            query += " AND rate = :rate"
            
        if currency_filter_status:
            if currency_filter_status in status_mapping:
                status_value = status_mapping[currency_filter_status]
                params.append(status_value)
                query += " AND status = :status"
            else:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para estatus.")
                return

        # Fetch filtered rows from the database
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        num_rows = len(rows)
        num_columns = len(cursor.description)
        self.currencyTable.setRowCount(num_rows)
        self.currencyTable.setColumnCount(num_columns)
        self.is_filtered = True

        header_names = ["ID", "Descripción", "Tasa", "Estado"]
        self.currencyTable.setHorizontalHeaderLabels(header_names)

        for i, row in enumerate(rows):
            for j, value in enumerate(row[0:]):
                item = QtWidgets.QTableWidgetItem(str(value) if value is not None else "")
                self.currencyTable.setItem(i, j, item)

        cursor.close()

        if self.currencyFilterBtn.text() == "Borrar filtros" and self.is_filtered:
            self.clear_text_fields()
            self.currencyFilterBtn.setText("Filtrar")
            self.query_currency()
            self.is_filtered = False

    def filter_aux(self):

        aux_filter_id = self.auxIdTxt.toPlainText().strip()
        aux_filter_name = self.auxDescTxt.toPlainText().strip()
        aux_filter_status = self.auxStatusTxt.currentText().strip()

        # Construct the SQL query
        query = "SELECT id, name, CASE status WHEN '1' THEN 'Activado' ELSE 'Desactivado' END AS status FROM aux_systems WHERE 1=1"

        params = []

        status_mapping = {
            "activado": "1", "Activado": "1", "Desactivado": "0", "desactivado": "0", "1": "1", "0": "0", "off": "0", 
            "on": "1", "Off": "0", "On": "1", "activo": "1", "Activo": "1", "Inactivo": "0", "inactivo": "0"
        }

        # Add filter conditions dynamically
        if aux_filter_id:
            try:
                params.append(int(aux_filter_id))
                query += " AND id = :id"
            except ValueError:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para ID.")
                return
            
        if aux_filter_name:
            params.append(aux_filter_name)
            query += " AND name = :name"
            
        if aux_filter_status:
            if aux_filter_status in status_mapping:
                status_value = status_mapping[aux_filter_status]
                params.append(status_value)
                query += " AND status = :status"
            else:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para estatus.")
                return

        # Fetch filtered rows from the database
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        num_rows = len(rows)
        num_columns = len(cursor.description)
        self.auxTable.setRowCount(num_rows)
        self.auxTable.setColumnCount(num_columns)
        self.is_filtered = True

        header_names = ["ID", "Descripción", "Movimiento", "Estado"]
        self.auxTable.setHorizontalHeaderLabels(header_names)

        for i, row in enumerate(rows):
            for j, value in enumerate(row[0:]):
                item = QtWidgets.QTableWidgetItem(str(value) if value is not None else "")
                self.auxTable.setItem(i, j, item)

        cursor.close()

        if self.auxFetchBtn.text() == "Borrar filtros" and self.is_filtered:
            self.clear_text_fields()
            self.auxFetchBtn.setText("Filtrar")
            self.query_auxsys()
            self.is_filtered = False

    def filter_entries(self):

        entries_filter_id = self.entriesIdTxt.toPlainText()
        entries_filter_description = self.entriesDescTxt.toPlainText()
        entries_filter_aux = self.entriesAccOrigTxt.currentText()
        entries_filter_mov = self.entriesAccTypeTxt.currentText()
        entries_filter_accaccs = self.entriesAccNumTxt.currentText()
        entries_filter_date = self.entriesDateTxt.toPlainText()
        entries_filter_balance = self.entriesAmountTxt.toPlainText()
        entries_filter_status = self.entriesStsTxt.toPlainText()

        # Construct the SQL query
        query = """SELECT id, descrip,
                    (SELECT b.name FROM aux_systems b WHERE b.id = a.aux_id) as aux_id,
                    (SELECT c.description FROM accounting_accs c WHERE c.id = a.accs_id) as accs_id,
                    mov_type, entry_date, amount, status
                    FROM accounting_entries a WHERE 1=1"""
        
        params = []

        aux_mapping = {}
        accaccs_mapping = {}

        # Fetch the data from the table
        cursor = self.connection.cursor()
        cursor.execute("SELECT name, id FROM aux_systems")
        aux_rows = cursor.fetchall()
        for row in aux_rows:
            description = row[0]
            id_value = row[1]
            aux_mapping[description] = id_value
            aux_mapping[description.lower()] = id_value
        for i in range(1, 7):
            aux_mapping[str(i)] = i
        cursor.close()

        # Fetch the data from the table
        cursor = self.connection.cursor()
        cursor.execute("SELECT description, id FROM accounting_accs")
        accaccs_rows = cursor.fetchall()
        for row in accaccs_rows:
            description = row[0]
            id_value = row[1]
            accaccs_mapping[description] = id_value
            accaccs_mapping[description.lower()] = id_value
        for i in range(1, 7):
            accaccs_mapping[str(i)] = i
        cursor.close()

        # Add filter conditions dynamically
        if entries_filter_id:
            try:
                params.append(int(entries_filter_id))
                query += " AND id = :id"
            except ValueError:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para ID.")
                return
            
        if entries_filter_description:
            params.append(entries_filter_description)
            query += " AND descrip = :descrip"

        if entries_filter_aux:
            if entries_filter_aux in aux_mapping:
                aux_value = aux_mapping[entries_filter_aux]
                params.append(aux_value)
                query += " AND aux_id = :aux_id"
            else:
                QMessageBox.warning(None, "Advertencia", "Valor inválido auxiliar.")
                return
            
        if entries_filter_accaccs:
            if entries_filter_accaccs in accaccs_mapping:
                accaccsvalue = accaccs_mapping[entries_filter_accaccs]
                params.append(accaccsvalue)
                query += " AND accs_id = :accs_id"
            else:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para cuenta contable.")
                return
            
        if entries_filter_mov:
            params.append(entries_filter_mov)
            query += " AND mov_type = :mov_type"
            
        if entries_filter_date:
            params.append(entries_filter_date)
            query += " AND entry_date = :entry_date"

        if entries_filter_balance:
            try:
                params.append(float(entries_filter_balance))
                query += " AND balance = :balance"
            except ValueError:
                QMessageBox.warning(None, "Advertencia", "Valor inválido para balance, introduce un número válido.")
                return
            
        if entries_filter_status:
            params.append(entries_filter_status)
            query += " AND status = :status"

        # Fetch filtered rows from the database
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        num_rows = len(rows)
        num_columns = len(cursor.description)
        self.entriesTable.setRowCount(num_rows)
        self.entriesTable.setColumnCount(num_columns)
        self.is_filtered = True

        header_names = ["ID","Descripción", "Tipo de cuenta", "Trans. permitidas", "Nivel", "Cuenta general","Balance", "Estado"]
        self.entriesTable.setHorizontalHeaderLabels(header_names)

        for i, row in enumerate(rows):
            for j, value in enumerate(row[0:]):
                item = QtWidgets.QTableWidgetItem(str(value) if value is not None else "")
                self.entriesTable.setItem(i, j, item)

        cursor.close()

        if self.entriesFilterBtn.text() == "Borrar filtros" and self.is_filtered:
            self.clear_text_fields()
            self.entriesFilterBtn.setText("Filtrar")
            self.query_entries()
            self.is_filtered = False

    # Funciones que actualizan data

    def update_accounting_data(self):
        # Retrieve the selected row's data
        row_id = str(self.previous_selected_row[0])
        description = self.previous_selected_row[1]
        acc_type = self.previous_selected_row[2]
        trx_allowed = self.previous_selected_row[3]
        acc_level = self.previous_selected_row[4]
        general_acc = self.previous_selected_row[5]
        balance = str(self.previous_selected_row[6])
        status = self.previous_selected_row[7]

        # Retrieve the updated values from the text fields
        updated_description = self.accountingDescTxt.toPlainText().strip()
        updated_acc_type = self.accountingAccTypeTxt.currentText().strip()
        updated_trx_allowed = self.accountingTrxAllwTxt.currentText().strip()
        updated_acc_level = self.accountingAccLvlTxt.currentText().strip()
        updated_general_acc = self.accountingGnlAccTxt.toPlainText().strip()
        updated_balance = self.accountingBlnTxt.toPlainText().strip()
        updated_status = self.accountingStsTxt.currentText().strip()

        # Check if any value has changed
        if (description == updated_description and
            acc_type == updated_acc_type and
            trx_allowed == updated_trx_allowed and
            acc_level == updated_acc_level and
            general_acc == updated_general_acc and
            balance == updated_balance and
            status == updated_status):
            QMessageBox.warning(None, "Advertencia", "No se presentan cambios.")
            return

        try:

            acc_type_mapping = {
                "Activos": 1, "activos": 1, "Pasivos": 2, "pasivos": 2, "Capital": 3, "capital": 3, 
                "Ingresos": 4, "ingresos": 4, "Costos": 5, "costos": 5, "Gastos": 6, "gastos": 6,
                "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6
            }

            trx_allowed_mapping = {
                "No": "N", "no": "N", "si": "Y", "Si": "Y", "Sí": "Y", "sí": "Y", "N": "N", "Y": "Y"
            }

            status_mapping = {
                "activado": "1", "Activado": "1", "Desactivado": "0", "desactivado": "0", "1": "1", "0": "0", "off": "0", 
                "on": "1", "Off": "0", "On": "1", "activo": "1", "Activo": "1", "Inactivo": "0", "inactivo": "0"
            }

            update_query = "UPDATE accounting_accs SET "
            update_params = {}

            if description != updated_description:
                update_query += "description = :description, "
                update_params["description"] = updated_description
            if acc_type != updated_acc_type:
                update_query += "acc_types = :acc_type, "
                update_params["acc_type"] = acc_type_mapping.get(updated_acc_type, acc_type)
            if trx_allowed != updated_trx_allowed:
                update_query += "trx_allowed = :trx_allowed, "
                update_params["trx_allowed"] = trx_allowed_mapping.get(updated_trx_allowed, trx_allowed)
            if acc_level != updated_acc_level:
                update_query += "acc_level = :acc_level, "
                update_params["acc_level"] = updated_acc_level
            if general_acc != updated_general_acc:
                update_query += "general_acc = :general_acc, "
                update_params["general_acc"] = updated_general_acc
            if balance != updated_balance:
                update_query += "balance = :balance, "
                update_params["balance"] = updated_balance
            if status != updated_status:
                update_query += "status = :status, "
                update_params["status"] = status_mapping.get(updated_status, status)


            # Remove the trailing comma and space
            update_query = update_query.rstrip(", ")

            # Add the WHERE clause
            update_query += " WHERE id = :id"

            # Create a dictionary of parameters for the update query
            update_params["id"] = row_id

            # Execute the update query
            cursor = self.connection.cursor()
            cursor.execute(update_query, update_params)
            self.connection.commit()
            cursor.close()

            QMessageBox.information(None, "Completado", "¡Se actualizaron los datos exitosamente!")

            # Clear the text fields after successful update
            self.clear_text_fields()

            # Refresh the table to reflect the updated data
            self.query_accounting_accs()

        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al actualizar: {str(e)}")

    def update_acctype(self):
        # Retrieve the selected row's data
        row_id = str(self.previous_selected_row[0])
        description = self.previous_selected_row[1]
        orig = self.previous_selected_row[2]
        status = self.previous_selected_row[3]

        # Retrieve the updated values from the text fields
        updated_description = self.acctypeDescTxt.toPlainText().strip()
        updated_orig = self.acctypeOrgTxt.currentText().strip()
        updated_status = self.acctypeStsTxt.currentText().strip()

        # Check if any value has changed
        if (description == updated_description and
            orig == updated_orig and
            status == updated_status):
            QMessageBox.warning(None, "Advertencia", "No se presentan cambios.")
            return

        try:

            update_query = "UPDATE acc_types SET "
            update_params = {}

            status_mapping = {
                "activado": "1", "Activado": "1", "Desactivado": "0", "desactivado": "0", "1": "1", "0": "0", "off": "0", 
                "on": "1", "Off": "0", "On": "1", "activo": "1", "Activo": "1", "Inactivo": "0", "inactivo": "0"
            }

            if description != updated_description:
                update_query += "description = :description, "
                update_params["description"] = updated_description
            if orig != updated_orig:
                update_query += "orig = :orig, "
                update_params["orig"] = updated_orig
            if status != updated_status:
                update_query += "status = :status, "
                update_params["status"] = status_mapping.get(updated_status, status)


            # Remove the trailing comma and space
            update_query = update_query.rstrip(", ")

            # Add the WHERE clause
            update_query += " WHERE id = :id"

            # Create a dictionary of parameters for the update query
            update_params["id"] = row_id

            # Execute the update query
            cursor = self.connection.cursor()
            cursor.execute(update_query, update_params)
            self.connection.commit()
            cursor.close()

            QMessageBox.information(None, "Completado", "¡Se actualizaron los datos exitosamente!")

            # Clear the text fields after successful update
            self.clear_text_fields()

            # Refresh the table to reflect the updated data
            self.query_acctypes()

        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al actualizar: {str(e)}")

    def update_currency(self):
        # Retrieve the selected row's data
        row_id = str(self.previous_selected_row[0])
        description = self.previous_selected_row[1]
        rate = self.previous_selected_row[2]
        status = self.previous_selected_row[3]

        # Retrieve the updated values from the text fields
        updated_description = self.currencyDescTxt.toPlainText().strip()
        updated_rate = self.currencyRateTxt.toPlainText().strip()
        updated_status = self.currencyStsTxt.currentText().strip()

        # Check if any value has changed
        if (description == updated_description and
            rate == updated_rate and
            status == updated_status):
            QMessageBox.warning(None, "Advertencia", "No se presentan cambios.")
            return

        try:

            update_query = "UPDATE currency SET "
            update_params = {}

            status_mapping = {
                "activado": "1", "Activado": "1", "Desactivado": "0", "desactivado": "0", "1": "1", "0": "0", "off": "0", 
                "on": "1", "Off": "0", "On": "1", "activo": "1", "Activo": "1", "Inactivo": "0", "inactivo": "0"
            }

            if description != updated_description:
                update_query += "description = :description, "
                update_params["description"] = updated_description
            if rate != updated_rate:
                update_query += "rate = :rate, "
                update_params["rate"] = updated_rate
            if status != updated_status:
                update_query += "status = :status, "
                update_params["status"] = status_mapping.get(updated_status, status)


            # Remove the trailing comma and space
            update_query = update_query.rstrip(", ")

            # Add the WHERE clause
            update_query += " WHERE id = :id"

            # Create a dictionary of parameters for the update query
            update_params["id"] = row_id

            # Execute the update query
            cursor = self.connection.cursor()
            cursor.execute(update_query, update_params)
            self.connection.commit()
            cursor.close()

            QMessageBox.information(None, "Completado", "¡Se actualizaron los datos exitosamente!")

            # Clear the text fields after successful update
            self.clear_text_fields()

            # Refresh the table to reflect the updated data
            self.query_currency()

        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al actualizar: {str(e)}")

    def update_aux(self):
        # Retrieve the selected row's data
        row_id = str(self.previous_selected_row[0])
        name = self.previous_selected_row[1]
        status = self.previous_selected_row[2]

        # Retrieve the updated values from the text fields
        updated_name = self.auxDescTxt.toPlainText().strip()
        updated_status = self.auxStatusTxt.currentText().strip()

        # Check if any value has changed
        if (name == updated_name and
            status == updated_status):
            QMessageBox.warning(None, "Advertencia", "No se presentan cambios.")
            return

        try:

            update_query = "UPDATE aux_systems SET "
            update_params = {}

            status_mapping = {
                "activado": "1", "Activado": "1", "Desactivado": "0", "desactivado": "0", "1": "1", "0": "0", "off": "0", 
                "on": "1", "Off": "0", "On": "1", "activo": "1", "Activo": "1", "Inactivo": "0", "inactivo": "0"
            }

            if name != updated_name:
                update_query += "name = :name, "
                update_params["name"] = updated_name
            if status != updated_status:
                update_query += "status = :status, "
                update_params["status"] = status_mapping.get(updated_status, status)


            # Remove the trailing comma and space
            update_query = update_query.rstrip(", ")

            # Add the WHERE clause
            update_query += " WHERE id = :id"

            # Create a dictionary of parameters for the update query
            update_params["id"] = row_id

            # Execute the update query
            cursor = self.connection.cursor()
            cursor.execute(update_query, update_params)
            self.connection.commit()
            cursor.close()

            QMessageBox.information(None, "Completado", "¡Se actualizaron los datos exitosamente!")

            # Clear the text fields after successful update
            self.clear_text_fields()

            # Refresh the table to reflect the updated data
            self.query_auxsys()

        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al actualizar: {str(e)}")

    def update_entries(self): 
        # Retrieve the selected row's data
        row_id = str(self.previous_selected_row[0])
        description = self.previous_selected_row[1]
        aux = self.previous_selected_row[2]
        accaccs = self.previous_selected_row[3]
        mov = self.previous_selected_row[4]
        date = self.previous_selected_row[5]
        balance = str(self.previous_selected_row[6])
        status = self.previous_selected_row[7]

        updated_entries_description = self.entriesDescTxt.toPlainText()
        updated_entries_aux = self.entriesAccOrigTxt.currentText()
        updated_entries_mov = self.entriesAccTypeTxt.currentText()
        updated_entries_accaccs = self.entriesAccNumTxt.currentText()
        updated_entries_date = self.entriesDateTxt.toPlainText()
        updated_entries_balance = self.entriesAmountTxt.toPlainText()
        updated_entries_status = self.entriesStsTxt.toPlainText()

        # Check if any value has changed
        if (description == updated_entries_description and
            aux == updated_entries_aux and
            mov == updated_entries_mov and
            accaccs == updated_entries_accaccs and
            date == updated_entries_date and
            balance == updated_entries_balance and
            status == updated_entries_status):
            QMessageBox.warning(None, "Advertencia", "No se presentan cambios.")
            return

        try:

            aux_mapping = {}
            accaccs_mapping = {}

            # Fetch the data from the table
            cursor = self.connection.cursor()
            cursor.execute("SELECT name, id FROM aux_systems")
            aux_rows = cursor.fetchall()
            for row in aux_rows:
                description = row[0]
                id_value = row[1]
                aux_mapping[description] = id_value
                aux_mapping[description.lower()] = id_value
            for i in range(1, 7):
                aux_mapping[str(i)] = i
            cursor.close()

            # Fetch the data from the table
            cursor = self.connection.cursor()
            cursor.execute("SELECT description, id FROM accounting_accs")
            accaccs_rows = cursor.fetchall()
            for row in accaccs_rows:
                description = row[0]
                id_value = row[1]
                accaccs_mapping[description] = id_value
                accaccs_mapping[description.lower()] = id_value
            for i in range(1, 7):
                accaccs_mapping[str(i)] = i
            cursor.close()

            update_query = "UPDATE accounting_entries SET "
            update_params = {}

            if description != updated_entries_description:
                update_query += "descrip = :descrip, "
                update_params["descrip"] = updated_entries_description
            if aux != updated_entries_aux:
                update_query += "aux_id = :aux_id, "
                update_params["aux_id"] = aux_mapping.get(updated_entries_aux, aux)
            if accaccs != updated_entries_accaccs:
                update_query += "accs_id = :accs_id, "
                update_params["accs_id"] = accaccs_mapping.get(updated_entries_accaccs, accaccs)
            if mov != updated_entries_mov:
                update_query += "mov_type = :mov_type, "
                update_params["mov_type"] = updated_entries_mov
            if date != updated_entries_date:
                update_query += "entry_date = :entry_date, "
                updated_entry_date = datetime.datetime.strptime(updated_entries_date, '%Y-%m-%d %H:%M:%S')
                update_params["entry_date"] = updated_entry_date
            if balance != updated_entries_balance:
                update_query += "amount = :amount, "
                update_params["amount"] = updated_entries_balance
            if status != updated_entries_status:
                update_query += "status = :status, "
                update_params["status"] = updated_entries_status


            # Remove the trailing comma and space
            update_query = update_query.rstrip(", ")

            # Add the WHERE clause
            update_query += " WHERE id = :id"

            # Create a dictionary of parameters for the update query
            update_params["id"] = row_id

            # Execute the update query
            cursor = self.connection.cursor()
            cursor.execute(update_query, update_params)
            self.connection.commit()
            cursor.close()

            QMessageBox.information(None, "Completado", "¡Se actualizaron los datos exitosamente!")

            # Clear the text fields after successful update
            self.clear_text_fields()

            # Refresh the table to reflect the updated data
            self.query_entries()

        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al actualizar: {str(e)}")

    # Funciones encargadas de leer y actualizar el UI masivamente

    def update_button_enabled(self):

        # Se guardan todos los valores en variables cada vez que se actualiza el campo
        accounting_id = self.accountingIdTxt.toPlainText()
        accounting_description = self.accountingDescTxt.toPlainText()
        accounting_acc_type = self.accountingAccTypeTxt.currentText()
        accounting_trx_allowed = self.accountingTrxAllwTxt.currentText()
        accounting_acc_lvl = self.accountingAccLvlTxt.currentText()
        accounting_gnl_acc = self.accountingGnlAccTxt.toPlainText()
        accounting_balance = self.accountingBlnTxt.toPlainText()
        accounting_status = self.accountingStsTxt.currentText()

        acctype_id = self.acctypeIdTxt.toPlainText()
        acctype_desc = self.acctypeDescTxt.toPlainText()
        acctype_orig = self.acctypeOrgTxt.currentText()
        acctype_sts = self.acctypeStsTxt.currentText()

        entries_id = self.entriesIdTxt.toPlainText()
        entries_desc = self.entriesDescTxt.toPlainText()
        entries_accorig = self.entriesAccOrigTxt.currentText()
        entries_accnum = self.entriesAccNumTxt.currentText()
        entries_acctype = self.entriesAccTypeTxt.currentText()
        entries_date = self.entriesDateTxt.toPlainText()
        entries_amt = self.entriesAmountTxt.toPlainText()
        entries_sts = self.entriesStsTxt.toPlainText()

        currency_id = self.currencyIdTxt.toPlainText()
        currency_desc = self.currencyDescTxt.toPlainText()
        currency_rate = self.currencyRateTxt.toPlainText()
        currency_sts = self.currencyStsTxt.currentText()
        
        aux_id = self.auxIdTxt.toPlainText()
        aux_desc = self.auxDescTxt.toPlainText()
        aux_sts = self.auxStatusTxt.currentText()

        # Activa o desactiva los botones basados en la condición de que todos deben tener datos
        enable_button_accounting = all([accounting_id, accounting_description, accounting_acc_type, accounting_trx_allowed, accounting_acc_lvl, accounting_gnl_acc, accounting_balance, accounting_status])
        is_id_duplicate = self.is_id_in_table(self.accountingTable, accounting_id)
        self.accountingInsertBtn.setEnabled(enable_button_accounting and not is_id_duplicate)
        if any([accounting_id, accounting_description, accounting_acc_type, accounting_trx_allowed, accounting_acc_lvl, accounting_gnl_acc, accounting_balance, accounting_status]):
            self.accountingFilterBtn.setEnabled(True)
            self.accountingFilterBtn.setText("Filtrar")
            if all([field for field in [accounting_id, accounting_description, accounting_acc_type, accounting_trx_allowed, accounting_acc_lvl, accounting_gnl_acc, accounting_balance, accounting_status]]):
                self.accountingFilterBtn.setText("Borrar filtros")
                self.accountingFilterBtn.setEnabled(False)
        else:
            if self.is_filtered:
                self.accountingFilterBtn.setEnabled(True)
                self.accountingFilterBtn.setText("Borrar filtros")
                self.is_filtered = True
            else:
                self.accountingFilterBtn.setEnabled(False)
                self.accountingFilterBtn.setText("Filtrar")

        enable_button_acctype = all([acctype_id, acctype_desc, acctype_orig, acctype_sts])
        is_id_duplicate = self.is_id_in_table(self.acctypeTable, acctype_id)
        self.acctypeInsertBtn.setEnabled(enable_button_acctype and not is_id_duplicate)
        if any([acctype_id, acctype_desc, acctype_orig, acctype_sts]):
            self.acctypeFilterBtn.setEnabled(True)
            self.acctypeFilterBtn.setText("Filtrar")
            if all([field for field in [acctype_id, acctype_desc, acctype_orig, acctype_sts]]):
                self.acctypeFilterBtn.setText("Borrar filtros")
                self.acctypeFilterBtn.setEnabled(False)
        else:
            if self.is_filtered:
                self.acctypeFilterBtn.setEnabled(True)
                self.acctypeFilterBtn.setText("Borrar filtros")
            else:
                self.acctypeFilterBtn.setEnabled(False)
                self.acctypeFilterBtn.setText("Filtrar")

        enable_button_entries = any([entries_id, entries_desc, entries_accorig, entries_accnum, entries_acctype, entries_date, entries_amt, entries_sts])
        #is_id_duplicate = self.is_id_in_table(self.entriesTable, entries_id)
        self.entriesInsertBtn.setEnabled(enable_button_entries)
        if any([entries_id, entries_desc, entries_accorig, entries_accnum, entries_acctype, entries_date, entries_amt, entries_sts]):
            self.entriesFilterBtn.setEnabled(True)
            self.entriesFilterBtn.setText("Filtrar")
            if all([field for field in [entries_id, entries_desc, entries_accorig, entries_accnum, entries_acctype, entries_date, entries_amt, entries_sts]]):
                self.entriesFilterBtn.setText("Borrar filtros")
                self.entriesFilterBtn.setEnabled(False)
        else:
            if self.is_filtered:
                self.entriesFilterBtn.setEnabled(True)
                self.entriesFilterBtn.setText("Borrar filtros")
            else:
                self.entriesFilterBtn.setEnabled(False)
                self.entriesFilterBtn.setText("Filtrar")

        enable_button_currency = all([currency_id, currency_desc, currency_rate, currency_sts])
        is_id_duplicate = self.is_id_in_table(self.currencyTable, currency_id)
        self.currencyInsertBtn.setEnabled(enable_button_currency and not is_id_duplicate)
        if any([currency_id, currency_desc, currency_rate, currency_sts]):
            self.currencyFilterBtn.setEnabled(True)
            self.currencyFilterBtn.setText("Filtrar")
            if all([field for field in [currency_id, currency_desc, currency_rate, currency_sts]]):
                self.currencyFilterBtn.setText("Borrar filtros")
                self.currencyFilterBtn.setEnabled(False)
        else:
            if self.is_filtered:
                self.currencyFilterBtn.setEnabled(True)
                self.currencyFilterBtn.setText("Borrar filtros")
            else:
                self.currencyFilterBtn.setEnabled(False)
                self.currencyFilterBtn.setText("Filtrar")

        enable_button_aux = all([aux_id, aux_desc, aux_sts])
        is_id_duplicate = self.is_id_in_table(self.auxTable, aux_id)
        self.auxInsertBtn.setEnabled(enable_button_aux and not is_id_duplicate)
        if any([aux_id, aux_desc, aux_sts]):
            self.auxFetchBtn.setEnabled(True)
            self.auxFetchBtn.setText("Filtrar")
            if all([field for field in [aux_id, aux_desc, aux_sts]]):
                self.auxFetchBtn.setText("Borrar filtros")
                self.auxFetchBtn.setEnabled(False)
        else:
            if self.is_filtered:
                self.auxFetchBtn.setEnabled(True)
                self.auxFetchBtn.setText("Borrar filtros")
            else:
                self.auxFetchBtn.setEnabled(False)
                self.auxFetchBtn.setText("Filtrar")

        button_field_mapping = {
            self.accountingUpdateBtn: {
                'accounting_id': accounting_id,
                'accounting_description': accounting_description,
                'accounting_acc_type': accounting_acc_type,
                'accounting_trx_allowed': accounting_trx_allowed,
                'accounting_acc_lvl': accounting_acc_lvl,
                'accounting_gnl_acc': accounting_gnl_acc,
                'accounting_balance': accounting_balance,
                'accounting_status': accounting_status
            },
            self.entriesUpdateBtn: {
                'entries_id': entries_id,
                'entries_desc': entries_desc,
                'entries_accorig': entries_accorig,
                'entries_accnum': entries_accnum,
                'entries_acctype': entries_acctype,
                'entries_date': entries_date,
                'entries_amt': entries_amt,
                'entries_sts': entries_sts
            },
            self.acctypeUpdateBtn: {
                'acctype_id': acctype_id,
                'acctype_desc': acctype_desc,
                'acctype_orig': acctype_orig,
                'acctype_sts': acctype_sts
            },
            self.currencyUpdateBtn: {
                'currency_id': currency_id,
                'currency_desc': currency_desc,
                'currency_rate': currency_rate,
                'currency_sts': currency_sts
            },
            self.auxUpdateBtn: {
                'aux_id': aux_id,
                'aux_desc': aux_desc,
                'aux_sts': aux_sts
            }
        }
        for button, fields in button_field_mapping.items():
            if self.select_fields is None:
                button.setEnabled(False)
            else:
                try:
                    if all(updated_value == self.select_fields[field] for field, updated_value in fields.items()):
                        button.setEnabled(False)
                    else:
                        button.setEnabled(True)
                except KeyError:
                    button.setEnabled(False)

    def on_table_item_clicked(self, item, table):
        row_index = item.row()
        row = []
        for column in range(table.columnCount()):
            table_item = table.item(row_index, column)
            if table_item is not None:
                row.append(table_item.text())
            else:
                row.append("")

        if self.previous_selected_row == row:
            # Same row selected again (deselecting)
            self.clear_text_fields()
            self.previous_selected_row = None
            self.select_fields = None
            self.accountingDeleteBtn.setEnabled(False)
            self.acctypeUpdateBtn.setEnabled(False)
            self.currencyUpdateBtn.setEnabled(False)
            self.entriesUpdateBtn.setEnabled(False)
            self.auxUpdateBtn.setEnabled(False)
            self.accountingUpdateBtn.setEnabled(False)
            self.acctypeInsertBtn.setEnabled(False)
            self.currencyInsertBtn.setEnabled(False)
            self.entriesInsertBtn.setEnabled(False)
            self.auxInsertBtn.setEnabled(False)
            self.accountingInsertBtn.setEnabled(False)
            
        else:
            # New row selected
            if table == self.accountingTable:
                self.accountingIdTxt.setText(row[0])
                self.accountingDescTxt.setText(row[1])
                self.accountingAccTypeTxt.setCurrentText(row[2])
                self.accountingTrxAllwTxt.setCurrentText(row[3])
                self.accountingAccLvlTxt.setCurrentText(row[4])
                self.accountingGnlAccTxt.setText(row[5])
                self.accountingBlnTxt.setText(row[6])
                self.accountingStsTxt.setCurrentText(row[7])
                self.select_fields = {
                    'accounting_id': row[0],
                    'accounting_description': row[1],
                    'accounting_acc_type': row[2],
                    'accounting_trx_allowed': row[3],
                    'accounting_acc_lvl': row[4],
                    'accounting_gnl_acc': row[5],
                    'accounting_balance': row[6],
                    'accounting_status': row[7]
                }
                self.previous_selected_row = row
                self.accountingDeleteBtn.setEnabled(True)
                self.accountingUpdateBtn.setEnabled(False)
            elif table == self.acctypeTable:
                self.acctypeIdTxt.setText(row[0])
                self.acctypeDescTxt.setText(row[1])
                self.acctypeOrgTxt.setCurrentText(row[2])
                self.acctypeStsTxt.setCurrentText(row[3])
                self.select_fields = {
                    'acctype_id': row[0],
                    'acctype_desc': row[1],
                    'acctype_orig': row[2],
                    'acctype_sts': row[3]
                }
                self.previous_selected_row = row
                self.acctypeDeleteBtn.setEnabled(True)
                self.acctypeUpdateBtn.setEnabled(False)
            elif table == self.currencyTable:
                self.currencyIdTxt.setText(row[0])
                self.currencyDescTxt.setText(row[1])
                self.currencyRateTxt.setText(row[2])
                self.currencyStsTxt.setCurrentText(row[3])
                self.select_fields = {
                    'currency_id': row[0],
                    'currency_desc': row[1],
                    'currency_rate': row[2],
                    'currency_sts': row[3]
                }
                self.previous_selected_row = row
                self.currencyDeleteBtn.setEnabled(True)
                self.currencyUpdateBtn.setEnabled(False)
            elif table == self.auxTable:
                self.auxIdTxt.setText(row[0])
                self.auxDescTxt.setText(row[1])
                self.auxStatusTxt.setCurrentText(row[2])
                self.select_fields = {
                    'aux_id': row[0],
                    'aux_desc': row[1],
                    'aux_sts': row[2]
                }
                self.previous_selected_row = row
                self.auxDeleteBtn.setEnabled(True)
                self.auxUpdateBtn.setEnabled(False)
            elif table == self.entriesTable:
                self.entriesIdTxt.setText(row[0])
                self.entriesDescTxt.setText(row[1])
                self.entriesAccOrigTxt.setCurrentText(row[2])
                self.entriesAccNumTxt.setCurrentText(row[3])
                self.entriesAccTypeTxt.setCurrentText(row[4])
                self.entriesDateTxt.setText(row[5])
                self.entriesAmountTxt.setText(row[6])
                self.entriesStsTxt.setText(row[7])
                self.select_fields = {
                    'entries_id': row[0],
                    'entries_desc': row[1],
                    'entries_accorig': row[2],
                    'entries_accnum': row[3],
                    'entries_acctype': row[4],
                    'entries_date': row[5],
                    'entries_amt': row[6],
                    'entries_sts': row[7]
                }
                self.previous_selected_row = row
                self.entriesDeleteBtn.setEnabled(True)
                self.entriesUpdateBtn.setEnabled(False)
                #ui.previous_selected_row = None

        self.row_selected.emit(row)

    def clear_text_fields(self):
        self.accountingIdTxt.clear()
        self.accountingDescTxt.clear()
        self.accountingAccTypeTxt.setCurrentIndex(-1)
        self.accountingTrxAllwTxt.setCurrentIndex(-1)
        self.accountingBlnTxt.clear()
        self.accountingStsTxt.setCurrentIndex(-1)
        self.accountingAccLvlTxt.setCurrentIndex(-1)
        self.accountingGnlAccTxt.clear()
        ui.previous_selected_row = None
        self.accountingDeleteBtn.setEnabled(False)

        self.acctypeIdTxt.clear()
        self.acctypeDescTxt.clear()
        self.acctypeOrgTxt.setCurrentIndex(-1)
        self.acctypeStsTxt.setCurrentIndex(-1)
        ui.previous_selected_row = None
        self.acctypeDeleteBtn.setEnabled(False)

        self.currencyIdTxt.clear()
        self.currencyDescTxt.clear()
        self.currencyRateTxt.clear()
        self.currencyStsTxt.setCurrentIndex(-1)
        ui.previous_selected_row = None
        self.currencyDeleteBtn.setEnabled(False)

        self.auxIdTxt.clear()
        self.auxDescTxt.clear()
        self.auxStatusTxt.setCurrentIndex(-1)
        ui.previous_selected_row = None
        self.auxDeleteBtn.setEnabled(False)

        self.entriesIdTxt.clear()
        self.entriesDescTxt.clear()
        self.entriesAccTypeTxt.setCurrentIndex(-1)
        self.entriesAccOrigTxt.setCurrentIndex(-1)
        self.entriesAmountTxt.clear()
        self.entriesStsTxt.clear()
        self.entriesDateTxt.clear()
        self.entriesAccNumTxt.setCurrentIndex(-1)
        ui.previous_selected_row = None
        self.entriesDeleteBtn.setEnabled(False)

    def is_id_in_table(self, table, id_value):
        # Iterate over the rows in the table view
        for row in range(table.rowCount()):
            table_item = table.item(row, 0)  # Assuming ID is in the first column
            if table_item is not None and table_item.text() == id_value:
                return True  # ID is found in the table view
        return False  # ID is not in the table view

def handle_row_deselected():
    ui.previous_selected_row = None

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(tabWidget)
    ui.query_accounting_accs()
    ui.query_acctypes()
    ui.query_currency()
    ui.query_auxsys()
    ui.query_entries()
    ui.currencyFetchBtn.setEnabled(False)

    try:
        ui.accountingTable.itemSelectionChanged.disconnect()
    except TypeError:
        pass

    ui.accountingTable.itemSelectionChanged.connect(handle_row_deselected)

    # Botones de vista de cuentas contables 
    ui.accountingInsertBtn.clicked.connect(ui.insert_accounting_data)
    ui.accountingDeleteBtn.clicked.connect(ui.delete_accounting_data)
    ui.accountingFilterBtn.clicked.connect(ui.filter_accounting_accs)
    ui.accountingUpdateBtn.clicked.connect(ui.update_accounting_data)

    # Botones de vista de tipos de cuenta
    ui.acctypeInsertBtn.clicked.connect(ui.insert_acctype)
    ui.acctypeDeleteBtn.clicked.connect(ui.delete_acctype)
    ui.acctypeFilterBtn.clicked.connect(ui.filter_acctype) 
    ui.acctypeUpdateBtn.clicked.connect(ui.update_acctype)

    # Botones de vista de monedas
    ui.currencyInsertBtn.clicked.connect(ui.insert_currency)
    ui.currencyDeleteBtn.clicked.connect(ui.delete_currency)
    ui.currencyFilterBtn.clicked.connect(ui.filter_currency)
    ui.currencyUpdateBtn.clicked.connect(ui.update_currency)

    # Botones de vista de auxiliares
    ui.auxInsertBtn.clicked.connect(ui.insert_aux)
    ui.auxDeleteBtn.clicked.connect(ui.delete_aux)
    ui.auxFetchBtn.clicked.connect(ui.filter_aux)
    ui.auxUpdateBtn.clicked.connect(ui.update_aux)

    # Botones de vista entradas contables
    ui.entriesInsertBtn.clicked.connect(ui.insert_entries)
    ui.entriesFilterBtn.clicked.connect(ui.filter_entries)
    ui.entriesUpdateBtn.clicked.connect(ui.update_entries)
    ui.entriesDeleteBtn.clicked.connect(ui.delete_entries)
    ui.entriesFetchBtn.clicked.connect(ui.query_entries)

    tabWidget.show()
    sys.exit(app.exec_())
