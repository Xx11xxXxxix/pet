from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                           QHBoxLayout, QProgressBar, QPushButton,
                           QLabel, QMessageBox)
from PyQt6.QtCore import Qt, QTimer

from config.config import Config
from .pet_widget import PetWidget
from database.db_manager import DatabaseManager
from models.pet import Pet

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.init_ui()

    def init_ui(self):
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint| Qt.WindowType.WindowStaysOnTopHint)

        central_widget = QWidget(self)
        central_widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setCentralWidget(central_widget)

        layout=QVBoxLayout(central_widget)
        layout.setContentsMargins(0,0,0,0)

        self.pet_widget=PetWidget()
        layout.addWidget(self.pet_widget)

