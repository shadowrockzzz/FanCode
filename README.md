# FanCode Automation Framework

This repository contains the code for automating tests for the FanCode application. The framework uses Python, pytest, and Playwright to perform API testing and validate user tasks and completion percentages.

## Initial Setup and Running the Tests

Follow the steps below to set up the environment, run the tests, and verify the results:

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/shadowrockzzz/FanCode.git
cd FanCode
```

### 2. Install Python Dependencies
Ensure Python 3.12 or later is installed. Then, install the required Python dependencies:
```bash
pip install -r requirements.txt
```

### 3. Install Playwright Dependencies
Playwright requires some browser binaries to be installed. Run the following command:
```bash
python -m playwright install
```

### 4. Install Node.js Dependencies (for Playwright)
Playwright also requires some Node.js dependencies:
```bash
npm install
```

### 5. Run the Tests
Once the setup is complete, run the tests using pytest:
```bash
pytest
```

### 6. Directory Structure
The project follows this directory structure:

```
.
├── .gitignore           # Git ignore file
├── README.md            # The current file
├── requirements.txt     # Python dependencies
├── tests/               # Folder containing test scripts
│   ├── test_fancode_users.py  # Test file for user tasks
│   └── __init__.py            # Package initialization
├── fancode/             # Main code for API client and validation
│   ├── __init__.py      # Package initialization
│   ├── api_client.py    # API client code
│   └── user_validation.py   # User validation and task completion logic
```
