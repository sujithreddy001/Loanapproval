**Project README**

# Loan Approval System

## Overview

This project implements a loan approval system that evaluates loan applications based on various criteria such as credit score, employment status, and the purpose of the loan. It consists of several modules designed to handle different aspects of the loan approval process, including data validation, risk assessment, and approval logic.

## Modules

### 1. LoanApplication

- **Description**: This module defines the `LoanApplication` class, which represents a loan application. It initializes instance variables for each application and creates a form for collecting application data.
- **Methods**:
  - `__init__()`: Initializes instance variables for each loan application.
  
### 2. LoanApplicationModule

- **Description**: This module provides functionality for processing loan applications. It contains a static method `approve_loan()` to evaluate loan applications and determine whether they are approved or rejected based on predefined approval logic.
- **Methods**:
  - `approve_loan(application_data)`: Evaluates loan applications and returns the approval decision.

### 3. RiskAssessment

- **Description**: This module assesses the risk associated with loan applications. It calculates a total score for each application based on credit score, employment status, and loan purpose.
- **Methods**:
  - `__init__(loan_application)`: Initializes instances for risk assessment.
  - `score_calculator()`: Assigns points based on different criteria.
  - `evaluate_total_score()`: Combines points from different criteria to calculate the total score.

### 4. app.py

- **Description**: The main application file that handles HTTP requests and serves as the entry point for the loan approval system. It integrates Flask for web development, handles loan application submissions, and interacts with the MongoDB database for storing application data.
- **Endpoints**:
  - `/submit_loan_applications`: Endpoint for submitting loan applications.
- **Operations**:
  - Extracts data from JSON payload of the request.
  - Validates the required fields.
  - Calculates the total score for the loan application.
  - Determines approval or rejection based on the total score.
  - Inserts application data into the MongoDB collection.
- **Dependencies**:
  - Flask: A web framework for Python.
  - pymongo: A MongoDB driver for Python.
  
### 5. test_loan_approval.py

- **Description**: This module contains unit tests for the loan approval system. It uses the `unittest` module to test the logic of the loan approval process, including approval, rejection, and handling of invalid data.
- **Test Cases**:
  - `test_approved()`: Tests approval logic with valid application data.
  - `test_rejected()`: Tests rejection logic with valid application data.
  - `test_invalid_data()`: Tests handling of invalid application data.
- **Dependencies**:
  - unittest: A built-in Python module for testing.

## Requirements

- Python 3
- Flask
- pymongo
- MongoDB

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/loan-approval-system.git
```

2. Navigate to the project directory:

```bash
cd loan-approval-system
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Submit loan applications using Postman or any HTTP client.

6. Monitor loan applications and results in the MongoDB collection.

7. Run unit tests:

```bash
python test_loan_approval.py
```

## Contributors

- [Sujith](https://github.com/sujithreddy001)

## Acknowledgments

Special thanks to Flask and MongoDB for providing powerful tools for web development and data storage, respectively.

## Contact

For any questions or inquiries, please contact 