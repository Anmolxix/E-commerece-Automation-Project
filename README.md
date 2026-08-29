# E-Commerce Test Automation Framework

A Selenium + Pytest test automation framework built while learning hybrid framework design, the Page Object Model, and how Pytest integrates with Selenium WebDriver. Built against the [nopCommerce demo store](https://admin-demo.nopcommerce.com/admin/) admin panel.

This is a learning/practice project — it's still a work in progress and will keep growing as I add more test scenarios and framework features.

## What it covers so far

- **Page Object Model** — locators and page actions separated from test logic (`pageObjects/`)
- **Data-driven config** — test data (URL, credentials) read from an external `config.ini` file instead of being hardcoded, using `configparser`
- **Positive & negative test scenarios** — valid login, and invalid-credential login handled as separate test cases
- **Logging** — custom logger that writes test execution steps to a log file for debugging
- **Screenshot on failure** — automatic screenshot capture when a test assertion fails, saved to `Screenshots/`
- **HTML reporting** — Pytest test results exported via `pytest-html`

## Tech stack

- Python
- Selenium WebDriver
- Pytest
- `pytest-html` for reporting
- `configparser` for test data management

## Project structure

```
E-commerece-Automation-Project/
├── Configurations/     # config.ini — base URL, test credentials
├── pageObjects/         # Page Object classes (locators + page actions)
├── testCases/           # Pytest test cases + conftest.py (fixtures/setup)
├── utilities/           # Custom logger and config reader helper classes
├── Screenshots/         # Auto-captured screenshots from failed test runs
├── Reports/              # Generated HTML test reports
├── requirements.txt
└── Run.bat
```

## Running the tests

```bash
pip install -r requirements.txt
pytest -v -s --html=Reports/report.html testCases/
```

## What I'm learning / working on next

- Cleaning up and expanding page objects to cover more of the app
- Adding more test scenarios beyond login/logout
- Exploring parallel test execution with `pytest-xdist`
- Adding Allure reporting alongside the existing HTML report

## Status

🚧 In progress — built as a hands-on way to learn automation framework design, not a finished production suite.
