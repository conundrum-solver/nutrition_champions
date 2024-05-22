# Student Attendance Management System

This project is a Django-based web application for managing student attendance through QR code scanning. It includes features for adding students, scanning their attendance, and viewing attendance data on a dashboard.

## Features

- **Add Student**: Add new students to the system with their details.
- **Scan Student**: Scan QR codes to record student attendance.
- **Dashboard**: View and filter attendance data with date range, gender, and class filters.

## Prerequisites

- Python 3.11
- Django 5.0.2
- SQLite (default database)
- Django Plotly Dash
- Other dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/conundrum-solver/nutrition_champions.git
    
    cd nutrition_champions
    ```

2. **Create a virtual environment**:

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

5. **Apply migrations**:

    ```sh
    python manage.py migrate
    ```

6. **Run the development server**:

    ```sh
    python manage.py runserver
    ```

## Usage

### Adding a Student

**Navigate to the homepage. After loggin in, use the navigation buttons to access "adding a new student", "scanning student" and "dashboard"**:
    ```
    http://127.0.0.1:8000/
    ```

## Contact

For any queries or issues, please open an issue on the GitHub repository or contact the project maintainer at [alsagr_88@hotmail.com].
