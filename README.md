# Selenium Test Automation with Page Object Model

This project demonstrates the use of Selenium WebDriver for automating web application testing using the Page Object Model (POM) design pattern. The tests are written in Python and utilize the `pytest` framework for test execution and reporting.

## Project Structure

- **POM_demo/pages/login_page.py**: Contains the `LoginPage` class, which encapsulates the elements and actions related to the login page of the application under test. This class provides methods to interact with the login page, such as entering a username, entering a password, and clicking the login button.

- **POM_demo/tests/login_test.py**: Contains the test cases for the login functionality. The test uses the `pytest` framework and includes a fixture to set up and tear down the WebDriver instance. The test case `test_login` verifies the login process by entering credentials and asserting the presence of a success message.

## Key Features

- **Page Object Model (POM)**: The project follows the POM design pattern, which enhances test maintenance and reduces code duplication by separating the test logic from the page-specific code.

- **Selenium WebDriver**: Utilized for browser automation, allowing the tests to interact with web elements and perform actions like clicking buttons and entering text.

- **WebDriver Manager**: Automatically manages the browser driver binaries, ensuring compatibility and ease of setup.

- **Pytest Framework**: Provides a simple and scalable way to write and execute test cases, with support for fixtures and assertions.

## How to Run the Tests

1. **Install Dependencies**: Ensure you have Python and pip installed. Then, install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute Tests**: Run the tests using the `pytest` command:
   ```bash
   pytest POM_demo/tests/login_test.py
   ```

3. **View Results**: The test results will be displayed in the console, showing the status of each test case.

## Conclusion

This project showcases the implementation of automated tests for a web application using Selenium WebDriver and the Page Object Model. It demonstrates the ability to write maintainable and scalable test scripts, which is a valuable skill for ensuring the quality and reliability of web applications.