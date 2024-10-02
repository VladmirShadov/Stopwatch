# Stopwatch
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle("Stopwatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)

        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.start_button.setObjectName("start")
        self.reset_button.setObjectName("reset")
        self.stop_button.setObjectName("stop")

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-family: calibre;
            }
            QPushButton{
                font-size: 50px;
                border: 3px solid;
            }
            QLabel{
                font-size: 150px;
                color: hsl(123, 88%, 66%);
                background-color: black;
                border-radius: 20px;
            }
            QPushButton#start{
                background-color: hsl(123, 75%, 49%);
            }
            QPushButton#stop{
                background-color: hsl(0, 75%, 49%);
            }
            QPushButton#reset{
                background-color: hsl(207, 75%, 49%);
            }
            QPushButton#start:hover{
                background-color: hsl(123, 75%, 79%);
            }
            QPushButton#stop:hover{
                background-color: hsl(0, 75%, 79%);
            }
            QPushButton#reset:hover{
                background-color: hsl(207, 75%, 79%);
            }
        """)
        self.start_button.clicked.connect(self.start)  # type: ignore
        self.stop_button.clicked.connect(self.stop)  # type: ignore
        self.reset_button.clicked.connect(self.reset)  # type: ignore
        self.timer.timeout.connect(self.update_display)  # type: ignore

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())