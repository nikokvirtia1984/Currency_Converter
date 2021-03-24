import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Currency Converter')
        self.setWindowIcon(QIcon('exchange.png'))
        self.ui.input_amount1.setPlaceholderText('from currency:')
        self.ui.input_amount2.setPlaceholderText('I have:')
        self.ui.output_amount1.setPlaceholderText('in currency:')
        self.ui.output_amount2.setPlaceholderText('I got:')
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        c = CurrencyConverter()
        input_currency = self.ui.input_amount1.text()
        output_currency = self.ui.output_amount1.text()
        input_amount = int(self.ui.input_amount2.text())

        output_amount = round(c.convert(input_amount, '%s' % input_currency, '%s' % output_currency), 2)

        self.ui.output_amount2.setText(str(output_amount))


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec_())
