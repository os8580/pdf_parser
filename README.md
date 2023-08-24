# PDF Data Parser

This script uses the `pdfplumber` library to extract text from a PDF file and parse it into a dictionary.

## Requirements

- Python 3.x
- pipenv

## Installation

1. Clone this repository or download the script.
2. Navigate to the directory where the script is located.
3. Run `pipenv install` to install the required dependencies.

## Usage

1. Open the script in a text editor and specify the path to your PDF file by changing the value of the `input_pdf_file_path` variable in the `if __name__ == "__main__":` block.
2. Run the script using `pipenv run python <script_name>.py`, where `<script_name>` is the name of the script file.
3. The script will parse the data from the PDF file and print the resulting dictionary to the console.
