import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from ui_nhansu import Ui_Form


# ===== DATABASE =====
def connect_db():
    return sqlite3.connect("nhansu.db")


def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nhansu (
            cccd TEXT PRIMARY KEY,
            hoten TEXT,
            ngaysinh TEXT,
            gioitinh TEXT,
            diachi TEXT
        )
    """)
    conn.commit()
    conn.close()


# ===== APP =====
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        create_table()
        self.load_data()

        # ===== BUTTON EVENTS =====
        self.ui.btn_add.clicked.connect(self.them)
        self.ui.btn_update.clicked.connect(self.sua)
        self.ui.btn_delete.clicked.connect(self.xoa)
        self.ui.btn_search.clicked.connect(self.tim)
        self.ui.btn_show.clicked.connect(self.load_data)

        # click table
        self.ui.tableWidget.cellClicked.connect(self.load_row)

    # ===== THÊM =====
    def them(self):
        cccd = self.ui.txt_cccd.text().strip()

        if cccd == "":
            QMessageBox.warning(self, "Lỗi", "CCCD không được rỗng")
            return

        conn = connect_db()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO nhansu VALUES (?, ?, ?, ?, ?)", (
                cccd,
                self.ui.txt_hoten.text(),
                self.ui.txt_ngaysinh.text(),
                self.ui.txt_gioitinh.text(),
                self.ui.txt_diachi.text()
            ))
            conn.commit()
            QMessageBox.information(self, "OK", "Thêm thành công")
            self.load_data()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Lỗi", "CCCD đã tồn tại")

        conn.close()

    # ===== SỬA =====
    def sua(self):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE nhansu
            SET hoten=?, ngaysinh=?, gioitinh=?, diachi=?
            WHERE cccd=?
        """, (
            self.ui.txt_hoten.text(),
            self.ui.txt_ngaysinh.text(),
            self.ui.txt_gioitinh.text(),
            self.ui.txt_diachi.text(),
            self.ui.txt_cccd.text()
        ))

        if cursor.rowcount == 0:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy CCCD")
        else:
            conn.commit()
            QMessageBox.information(self, "OK", "Cập nhật thành công")

        conn.close()
        self.load_data()

    # ===== XÓA =====
    def xoa(self):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM nhansu WHERE cccd=?", (self.ui.txt_cccd.text(),))

        if cursor.rowcount == 0:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy")
        else:
            conn.commit()
            QMessageBox.information(self, "OK", "Xóa thành công")

        conn.close()
        self.load_data()

    # ===== TÌM =====
    def tim(self):
        keyword = self.ui.txt_cccd.text()

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM nhansu
            WHERE cccd LIKE ? OR hoten LIKE ? OR diachi LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))

        data = cursor.fetchall()
        self.show_table(data)

        conn.close()

    # ===== LOAD =====
    def load_data(self):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM nhansu")
        data = cursor.fetchall()

        self.show_table(data)
        conn.close()

    # ===== HIỂN THỊ BẢNG =====
    def show_table(self, data):
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(5)

        for row_idx, row_data in enumerate(data):
            for col_idx, col_data in enumerate(row_data):
                self.ui.tableWidget.setItem(
                    row_idx, col_idx, QTableWidgetItem(str(col_data))
                )

    # ===== CLICK TABLE =====
    def load_row(self, row, column):
        self.ui.txt_cccd.setText(self.ui.tableWidget.item(row, 0).text())
        self.ui.txt_hoten.setText(self.ui.tableWidget.item(row, 1).text())
        self.ui.txt_ngaysinh.setText(self.ui.tableWidget.item(row, 2).text())
        self.ui.txt_gioitinh.setText(self.ui.tableWidget.item(row, 3).text())
        self.ui.txt_diachi.setText(self.ui.tableWidget.item(row, 4).text())


# ===== RUN =====
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())