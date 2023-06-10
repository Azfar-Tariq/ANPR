# Automatic Number Plate Recognition (ANPR) System

This repository contains the source code and resources for an Automatic Number Plate Recognition (ANPR) system. The system is designed to read number plates from images or video streams using OpenCV and perform a database lookup to check if the number plate is registered, allowing the vehicle to enter.

## Features

- Number plate detection: The system uses computer vision techniques provided by OpenCV to detect and extract number plates from images or video frames.
- Optical Character Recognition (OCR): The extracted number plate regions are passed through the EasyOCR library, which performs optical character recognition to read the alphanumeric characters on the plate.
- Database integration: The recognized number plate is compared against a database of registered plates to check for a match. The database can be customized based on your requirements.
- Access control: If the number plate is found in the database, the system grants access to the vehicle. Otherwise, access is denied.

## Requirements

- Python 3.7 or higher
- OpenCV library
- EasyOCR library
- Database (MySQL, SQLite, etc.)

## Installation

1. Clone the repository:

   git clone https://github.com/your-username/ANPR-System.git

2. Navigate to the project directory:

   cd ANPR-System

3. Install the required dependencies using pip:

   pip install -r requirements.txt

4. Configure the database:

   - Create a database and a table to store the registered number plates.
   - Modify the database configuration in the `config.py` file according to your database setup.

5. Run the ANPR system:

   python main.py

## Usage

1. Capture an image or video containing a number plate.

2. The system will process the input and attempt to detect the number plate.

3. The recognized characters will be displayed, and the system will check if the number plate is registered.

4. If the number plate is found in the database, access will be granted. Otherwise, access will be denied.

## Customization

- Database: You can customize the database integration by modifying the `config.py` file. This allows you to use a different database system or change the table structure.

- Number plate detection: The system currently uses OpenCV's built-in methods for number plate detection. You can experiment with different techniques and algorithms to improve the accuracy or adapt the system to specific scenarios.

- OCR: The OCR process is handled by EasyOCR, which supports multiple languages. You can configure the language settings in the `main.py` file to suit your requirements.

## Contributions

Contributions to this project are welcome. If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments

- The project makes use of the following libraries:
  - OpenCV: https://opencv.org/
  - EasyOCR: https://github.com/JaidedAI/EasyOCR

- Special thanks to the developers and contributors of these libraries for their excellent work.

## Contact

If you have any questions or need further assistance, please feel free to contact azfaro2031@gmail.com .
