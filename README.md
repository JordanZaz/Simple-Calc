# Simple-Calc

A calculator application that performs both unary and binary operations. It consists of a React frontend and a Django backend, with operations handled by a Python module.

## Features

- Supports the following operators: addition (+), subtraction (-), multiplication (*), division (/), power (**), square root (sqrt), factorial (!), modulus (%), and integer division (//).
- Unary operations: factorial and square root.
- Binary operations: addition, subtraction, multiplication, division, power, modulus, and integer division.
- Step-by-step number input and operation execution for better user experience.
- Error handling: handles various errors like division by zero and invalid inputs gracefully.

## Setup and Installation

### Backend (Django)

1. Navigate to the Django application directory.
2. Set up a virtual environment: `python -m venv venv`.
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/Mac: `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`.
5. Run the Django application: `python manage.py runserver`.

### Frontend (React)

1. Navigate to the React application directory.
2. Install the required packages: `npm install`.
3. Run the React application: `npm start`.

## Usage

### React Frontend

1. Open your browser and navigate to `http://localhost:3000`.
2. Follow the step-by-step prompts to perform calculations.

### CLI

1. Run the script `python app.py` to start the CLI.
2. Follow the prompts to perform calculations through the command line.

## Project Structure

- `src/components/Calc.js`: The React component that handles the frontend part of the calculator.
- `calculator.py`: Contains the Calculator class that performs the calculations.
- `operations.py`: Defines the operators and operations utilized in the calculator.
- `cli.py`: A CLI interface for interacting with the calculator.
- `views.py`: Django view that handles API requests.
- `calculator/urls.py`: Django URL configuration for the calculator API.

## API Endpoints

- POST `/calculate/`: Takes `operator`, `first_number`, and `second_number` as parameters and returns the calculation result or an error message.

## Examples

### React Frontend

1. Navigate to `http://localhost:3000`.
2. Input the operator (e.g., '+').
3. Input the first number (e.g., '5').
4. Input the second number (e.g., '3').
5. The result ('8') will be displayed on the screen.

### CLI

1. Run the script `app.py`.
2. Input the operator (e.g., '+').
3. Input the first number (e.g., '5').
4. Input the second number (e.g., '3').
5. The result ('8') will be displayed in the console.

## Error Handling

- Division by zero: The application prevents division by zero and displays a meaningful error message.
- Invalid inputs: Handles invalid inputs gracefully by displaying appropriate error messages.

## Logging

- The application logs events and errors for debugging and auditing purposes.
