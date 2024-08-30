from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSlider Switch Example")

        # Create a central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Create a QSlider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(1)
        self.slider.setValue(0)  # Default to "unchecked" state
        self.slider.setTickPosition(QSlider.NoTicks)
        self.slider.setSingleStep(1)

        # Create a QLabel to display the current state
        self.label = QLabel("Switch is OFF")
        self.label.setAlignment(Qt.AlignCenter)

        # Connect the slider value change to a custom function
        self.slider.valueChanged.connect(self.slider_value_changed)

        # Add the slider and label to the layout
        layout.addWidget(self.slider)
        layout.addWidget(self.label)

        # Set the layout to the central widget
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def slider_value_changed(self, value):
        if value == 1:
            self.label.setText("Switch is ON")
            print("Slider is in the ON position.")
        else:
            self.label.setText("Switch is OFF")
            print("Slider is in the OFF position.")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
