# PageObject Final Task

This is the final task for the Stepik pytest+Selenium [course](https://stepik.org/lesson/201964/step/15?unit=176022).

## Environment

- **Operating System:** macOS Ventura 13.4
- **Python Version:** 3.9
- **IDE:** PyCharm 2023.1.4 Pro
- **Web Browsers:** 
  - Firefox 117.0.1
  - Chrome 117.0.5938.88

## How to Run

To run the project, follow these steps:

1. **Create a Virtual Environment:**
   
   ```
   python -m venv venv_name
   ```

   Replace `venv_name` with the name you want to give to your virtual environment.

2. **Install Requirements:**

   Activate the virtual environment:

   - On macOS/Linux:

     ```
     source venv_name/bin/activate
     ```

   - On Windows:

     ```
     .\venv_name\Scripts\activate
     ```

   Install the project requirements:

   ```
   pip install -r requirements.txt
   ```

3. **Run the Tests:**

   Run the pytest with the following command:

   ```
   pytest -v --tb=line --language=en -m need_review
   ```

   This will execute the tests and display the results.

---
