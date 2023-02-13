# PyQt5 REST API File Uploader

This is a PyQt5-based GUI application that allows users to upload a file to a REST API and receive a request ID in response. The request ID can then be used to retrieve the current status of the calculation from the API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Features

* Select a file to upload
* POST file to REST API
* Receive and display request ID
* Use request ID to query the current status of the calculation from the API

## Requirements

You will need to have the following installed on your machine:

* Python 3.x
* PyQt5
* Requests library

## Usage

Clone the repository: 

    git clone https://github.com/[username]/PyQt5-REST-API-File-Uploader.git
    
Install required packages: 

    pip install -r requirements.txt
    
Run the application: 

    python main.py
    
The GUI should appear and you can start using the REST API client by selecting a file and clicking the "Submit" button. The API response and calculation result will be displayed in the GUI.

## Contributing

If you would like to contribute to this repository, please create a pull request with your changes. All contributions are welcome!

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
