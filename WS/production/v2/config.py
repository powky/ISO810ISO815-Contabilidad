import os
import cx_Oracle

class DevelopmentConfig:
    DEBUG = False
    
    def __init__(self):
        os.environ['TNS_ADMIN'] = '/path/to/wallet/Wallet.zip'
        self.conn = cx_Oracle.connect('username', 'password', 'tnsname')
        self.cursor = self.conn.cursor()

config = {
    'development': DevelopmentConfig()
}