import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
import numpy as np

print("Hello, World!")
# Create a simple NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Create a PySide6 application
app = QApplication(sys.argv)

# Create a main window
window = QMainWindow()
window.setGeometry(100, 100, 300, 200)

# Create a label to display the array
label = QLabel(window)
label.setText(f"Array: {arr}")

# Set the label's position and size
label.setGeometry(10, 10, 280, 180)

# Show the main window
window.show()

# Run the application event loop
sys.exit(app.exec())