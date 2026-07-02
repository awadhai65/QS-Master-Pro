from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QMessageBox,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QS Master Pro v0.1")

        self.resize(1200,700)

        central=QWidget()

        self.setCentralWidget(central)

        layout=QVBoxLayout()

        central.setLayout(layout)

        title=QLabel("QS MASTER PRO")

        title.setStyleSheet("font-size:30px;font-weight:bold;")

        layout.addWidget(title)

        self.btn_dxf=QPushButton("Open DXF")

        self.btn_pdf=QPushButton("Open Structural PDF")

        self.btn_mb=QPushButton("Generate Measurement Book")

        self.btn_bbs=QPushButton("Generate BBS")

        layout.addWidget(self.btn_dxf)

        layout.addWidget(self.btn_pdf)

        layout.addWidget(self.btn_mb)

        layout.addWidget(self.btn_bbs)

        self.btn_dxf.clicked.connect(self.open_dxf)

        self.btn_pdf.clicked.connect(self.open_pdf)

    def open_dxf(self):

        filename,_=QFileDialog.getOpenFileName(
            self,
            "Select DXF File",
            "",
            "DXF Files (*.dxf)"
        )

        if filename:

            QMessageBox.information(
                self,
                "DXF Loaded",
                filename
            )

    def open_pdf(self):

        filename,_=QFileDialog.getOpenFileName(
            self,
            "Select Structural PDF",
            "",
            "PDF Files (*.pdf)"
        )

        if filename:

            QMessageBox.information(
                self,
                "PDF Loaded",
                filename
            )
        