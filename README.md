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

**How to run a single test**
1. Navigate to `<path/to/project>/fbkr_qa_test`
2. Export path variable `PY=$(pwd)`
3. Navigate to `<path/to/project>/fbkr_qa_test/test_cases/ui`
4. Run command `PYTHONPATH=$PY pytest -k "test_message_captain" -s`

**How to run a test by specifying browser**<br>
1. Navigate to `<path/to/project>/fbkr_qa_test`
2. Export path variable `PY=$(pwd)`
3. Navigate to `<path/to/project>/fbkr_qa_test/test_cases/ui`
4. Run command `PYTHONPATH=$PY pytest  -k "test_message_captain" --browser chrome`

**How to run all tests from one folder**<br>
1. Navigate to `<path/to/project>/fbkr_qa_test`
2. Export path variable `PY=$(pwd)`
3. Navigate to `<path/to/project>/fbkr_qa_test/test_cases/ui`
4. Run command `PYTHONPATH=$PY pytest -k "test_" -s`

**How to run test in headless mode:**<br>
1. Navigate to `<path/to/project>/fbkr_qa_test`
2. Export path variable `PY=$(pwd)`
3. Navigate to `<path/to/project>/fbkr_qa_test/test_cases/ui`
4. Run command `PYTHONPATH=$PY test -k "test_message_captain" --mode headless -s` 

**How to run same test several times:**<br>
1. Navigate to `<path/to/project>/fbkr_qa_test`
2. Export path variable `PY=$(pwd)`
3. Navigate to `<path/to/project>/fbkr_qa_test/test_cases/ui`
4. Run command `PYTHONPATH=$PY test -k "test_message_captain" --count=3 -s` 

**How to run test and generate test report:**<br>
1. Navigate to `<path/to/project>/fbkr_qa_test`
2. Export path variable `PY=$(pwd)`
3. Navigate to `<path/to/project>/fbkr_qa_test/test_cases/ui`
4. Run command `PYTHONPATH=$PY pytest -k "test_" -s --html=../../test_reports/report_name.html -s` 

## STRUCTURE:
**libraries** folder -> Place for common methods and classes to be used across all the
tests<br>
**test_cases** folder-> Place where all the test cases are written. Module used for 
running the tests is pytest. Note that all test modules have name beginning with 'test_'
as required by pytest framework. <br>
**ui**  folder-> This is where all classes and methods for UI tests are stored <br>
**test_data**  folder-> Place for all input test data used in tests<br>

## About tests
- Each test is marked by its type: `end-to-end` for user scenarios tests, `component` for isolated functionality tests
- Tests can be parametrized. Example: login tests
- Tests can be run on chrome or firefox using head or headless mode
- Report can be generated by passing --html parameter (see report example in `test_reports` folder)

## To do
- Crypt .env file
- Add option to pass screen size as parameter when running tests









