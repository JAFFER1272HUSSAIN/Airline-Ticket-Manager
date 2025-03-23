import sys
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class BarGraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Bar Graph Display')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Create a Matplotlib figure and canvas for the bar chart
        self.figure = Figure()
        self.figure.set_facecolor('skyblue')  # Set background color to blue
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.plot_bar_chart()

    def plot_bar_chart(self):
        file_path = 'books.csv'
        data = pd.read_csv(file_path)

        # Assuming 'Date' is in the format 'YYYY-MM-DD', you might want to convert it to a datetime object
        data['Date'] = pd.to_datetime(data['Date'])

        # Sorting data by 'Date' for better visualization
        data = data.sort_values(by='Date')

        # Plotting the bar chart on the Matplotlib figure
        ax = self.figure.add_subplot(111)
        ax.bar(data['Date'], data['Flight_Duaration_in_minutes'])
        ax.set_title('Flight Duration Over Time (Bar Chart)')
        ax.set_xlabel('Date')
        ax.set_ylabel('Flight Duration (minutes)')
        ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better readability
        ax.grid(True)

        # Draw the plot on the Matplotlib canvas
        self.canvas.draw()

def run_app():
    app = QApplication(sys.argv)
    window = BarGraphWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()
