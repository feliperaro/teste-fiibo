# Teste Fiibo

## Description

This project includes a script that automates the process of reading an Excel file and sending this data to an API. The API is a Django project located in the `api` folder.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/feliperaro/teste-fiibo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd teste-fiibo
    ```

3. Create a virtual environment (if you haven't already):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    On Windows:
        ```
        venv\Scripts\activate
        ```

    On macOS and Linux:
        
        ```
        source venv/bin/activate
        ```

5. Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the API

1. Navigate to the `api` directory:

    ```bash
    cd api
    ```

2. Apply any necessary database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Run the Django server:

    ```bash
    python manage.py runserver
    ```

### Running the Script

1. Place your Excel file in the `input` folder.
2. Run the script:

    ```bash
    python script.py
    ```

3. After processing, the Excel file will be moved to the `output` folder.
