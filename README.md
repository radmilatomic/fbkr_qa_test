## FBKR TEST AUTOMATION FRAMEWORK
This is an automation framework to be used to develop tests for FishingBooker test.
Framework includes ***UI*** tests.
Framework is python based, it uses pytest library.

## PREREQUISITES:
Before cloning the project following dependencies need to be installed:
- **git** 
- **python3**
- **pip3** 

## SETUP:
After the prerequisites are installed, clone this project into your working
directory.

- install virtualenv globally (`pip3 install virtualenv`)
- from terminal navigate to `<path/to/project>/fbkr_qa_test`
- run command `virtualenv venv` to create virtual environment
- run command `source venv/bin/activate` to activate virtual environment (you should see venv in brackets before first line in terminal)
- run command `pip3 install -r requirements.txt` to install project based dependencies


### How to run UI tests - examples:

**How to run a test (login test used for an example)**
1. Navigate to <path/to/project>/fbkr_qa_test
2. Export path variable `PY=$(pwd)`
3. Navigate to <path/to/project>/fbkr_qa_test/test_cases/ui
4. Run command `PYTHONPATH=$PY pytest test_login_positive`

**How to run a test with -k flag**<br>
-k flag will run all tests that have the following keyword in their name
1. Navigate to <path/to/project>/fbkr_qa_test
2. Export path variable `PY=$(pwd)`
3. Navigate to <path/to/project>/fbkr_qa_test/test_cases/ui
4. Run command `PYTHONPATH=$PY pytest  -k "test_home"`

**How to run all tests from one folder**<br>
-k flag will run all tests that have the following keyword in their name, so it is enough to run the following command
1. Navigate to <path/to/project>/fbkr_qa_test
2. Export path variable `PY=$(pwd)`
3. Navigate to <path/to/project>/fbkr_qa_test/test_cases/ui
4. Run command `PYTHONPATH=$PY pytest -k "test_" -s`

**How to run test in headless mode:**<br>
1. Navigate to <path/to/project>/fbkr_qa_test
2. Export path variable `PY=$(pwd)`
3. Navigate to <path/to/project>/fbkr_qa_test/test_cases/ui
4. Run command `PYTHONPATH=$PY test -k "test_" --mode headless -s` 

## STRUCTURE:
**libraries** folder -> Place for common methods and classes to be used across all the
tests<br>
**test_cases** folder-> Place where all the test cases are written. Module used for 
running the tests is pytest. Note that all test modules have name beginning with 'test_'
as required by pytest framework. <br>
**ui**  folder-> This is where all classes and methods for UI tests are stored <br>
**test_data**  folder-> Place for all input test data used in tests<br>









