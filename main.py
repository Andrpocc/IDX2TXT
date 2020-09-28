import sys
import os

from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtWidgets import QMainWindow, QFileDialog, QApplication, QDialog, QMessageBox

from idx_converter import IDXConverter
from MainWindow import Ui_MainWindow
from help import Ui_Dialog as HelpUI
from about import Ui_Dialog as AboutUI


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = AboutUI()
        self.ui.setupUi(self)


class HelpDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = HelpUI()
        self.ui.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.out_data = None
        self.file_name = None

        labels = ['Точка', 'Y', 'X', 'H']
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(labels)

        self.ui.Button_load.clicked.connect(self.load_data)
        self.ui.Button_save.clicked.connect(self.save_data)
        self.ui.action_2.triggered.connect(self.show_help)
        self.ui.action_3.triggered.connect(self.show_about)

    def error_message(self, message: str):
        mes = QMessageBox(self)
        mes.setStyleSheet("""
        QMessageBox{
        background-color: grey;
        }
        QLabel{
        font: 63 12pt \"Yu Gothic UI Semibold\";
        text-align: center;
        }
        """)
        mes.setWindowTitle('IDX2TXT - Сообщение об ошибке')
        mes.setText(message)
        mes.exec_()

    def show_help(self):
        help = HelpDialog()
        help.show()
        help.exec()

    def show_about(self):
        about = AboutDialog()
        about.show()
        about.exec()

    def load_data(self):
        load_path = QFileDialog.getOpenFileName(self, self.tr('Выберите IDX файл'),
                                                os.path.join(os.environ['HOMEPATH'], 'Desktop'),
                                                self.tr('IDX files (*.IDX)'))
        if load_path[0] == '':
            self.error_message('Ошибка загрузки IDX файла!')
        else:
            self.file_name = load_path[0].split('/')[-1].upper().replace('.IDX', '')
            print(f'NAME: {self.file_name}')
            converter = IDXConverter(load_path[0])
            self.out_data = converter.converting()

            self.ui.tableWidget.setRowCount(len(self.out_data))
            for n_row, row in enumerate(self.out_data):
                for n_el, el in enumerate(row):
                    item = QTableWidgetItem()
                    item.setText(str(el))
                    self.ui.tableWidget.setItem(n_row, n_el, item)

        print(self.out_data)

    def save_data(self):
        save_path = QFileDialog.getSaveFileName(self, self.tr('Сохранить как'),
                                                os.path.join(os.environ['HOMEPATH'],
                                                             f'Desktop/{self.file_name}'),
                                                self.tr('Text files (*.TXT)'))
        if save_path[0] == '':
            self.error_message('Файл не сохранен!')
        elif self.out_data is None:
            self.error_message('Загрузите IDX файл!')
        else:
            with open(save_path[0], 'w') as file:
                for row in self.out_data:
                    print('\t'.join(row), file=file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
