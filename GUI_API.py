# Import required modules
import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QTextEdit

# MainWindow class which contains the GUI elements and functionality
class MainWindow(QMainWindow):
    def __init__(self):
        # Call the parent class's constructor
        super().__init__()

        # Create "Select File" button and connect it to the select_file method
        self.select_file_button = QPushButton("Select File", self)
        self.select_file_button.clicked.connect(self.select_file)
        self.select_file_button.move(100, 100)

        # Create "Send File" button and connect it to the send_file method
        self.send_file_button = QPushButton("Send File", self)
        self.send_file_button.clicked.connect(self.send_file)
        self.send_file_button.move(100, 200)

        # Create "Get Response" button and connect it to the get_response method
        self.get_response_button = QPushButton("Get Response", self)
        self.get_response_button.clicked.connect(self.get_response)
        self.get_response_button.move(100, 300)

        # Create a label to display the selected file path
        self.file_path_label = QLabel(self)
        self.file_path_label.resize(400, 25)
        #self.file_path_label.setWordWrap(True)
        self.file_path_label.move(250, 100)

        # Create a text edit widget to display the response from the server
        self.response_text = QTextEdit(self)
        self.response_text.resize(400, 100)
        self.response_text.move(250, 300)

        # Set the window size and position
        self.setGeometry(100, 100, 800, 500)
        #self.resize(400, 300)

        self.file_selected = False
        self.file_sent = False

    # Method to select a file using the file dialog
    def select_file(self):
        # Get the options for the file dialog
        options = QFileDialog.Options()

        # Show the file dialog and get the selected file name
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*);;Text Files (*.txt)", options=options)

        # If a file is selected, read the contents and update the file path label
        if file_name:
            self.file_path_label.setText(file_name)
            self.file_data = ""
            with open(file_name, "r") as file:
                self.file_data = file.read()
        # If no file is selected, update the file path label to indicate that
        else:
            self.file_path_label.setText("No file selected")
            self.file_data = ""

    # Method to send the selected file to the server
    def send_file(self):
        # Check if a file has been selected
        if self.file_data:
            # Send a POST request to the server with the file data
            response = requests.post("http://192.168.1.111:8080/key", json=self.file_data)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Get the response data as a dictionary
                response_data = response.json()

                # Store the request ID in an instance variable
                self.requestId = response_data["requestId"]
            else:
                # If the request failed, set an error message in the file path label
                self.file_path_label.setText(f"Request failed with status code {response.status_code}")
        else:
            # If no file has been selected, set an error message in the file path label
            self.file_path_label.setText("No file selected")

    # Method to retrieve the response from the server
    def get_response(self):
        # Check if the requestId exists, which means a file has been sent
        if hasattr(self, 'requestId'):
            # Make a GET request to the server to retrieve the response, using the requestId as a parameter
            response = requests.get(f"http://192.168.1.111:8080/return/{self.requestId}")

            # If the status code is 200, meaning the request was successful
            if response.status_code == 200:
                # Get the response data in JSON format
                response_data = response.json()

                # Set the response data in the response text edit widget
                self.response_text.setText(str(response_data))

            # If the status code is not 200, meaning the request was unsuccessful
            else:
                # Set an error message in the response text edit widget
                self.response_text.setText(f"Request failed with status code {response.status_code}")
        # If the requestId does not exist
        else:
            # Set an error message in the response text edit widget
            self.response_text.setText("No requestId found, please send file first")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
