# project-p-ui-tests

🔸 A snippet of the framework - as a part of the portfolio - with automated tests created for P.* project (web App for b2b, b2c segments; providing delivery solutions for companies, small businesses, and private clients)

🔸 The framework is designed based on Page Object Model (POM).

🔸 Includes selected test scenarios that:
- validate UI functionality for some of the key user flows 
- are parametrized to run on multiple sets of data for comprehensive coverage
- use fixtures for preconditions setup
- run in each regression testing cycle 

🔸 Also, supporting methods are decorated with step annotations for Allure Report framework, that is integrated into the project. So that reports of test execution can be generated automatically and in an easy-to-read format.

▶️ To install all packages and modules used in the project, simply run the command "pip install -r requirements.txt" in the Terminal of Pycharm.

▶️ To run all tests at once use the command "pytest tests" in the Terminal of Pycharm. Or use the command "pytest ./tests/[name_of_specific_file_with_test.py]" to run a specific test.

▶️ To run test(s) with report auto-generation by Allure, firstly use the command "pytest tests --alluredir results" (for all tests) or "pytest ./tests/[name_of_specific_file_with_test.py] --alluredir results" (for a specific test) in the Terminal of Pycharm. Then run the command “allure serve results” to open the report generated before.

*All code shown as an illustration of personal skills in test automation and is fully created by Ksenia Yelyashevich. Published with the consent of the project team and all identification data deleted


