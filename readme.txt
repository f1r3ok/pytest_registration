Run the test:
behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features

Open allure report:
rm -r allure/results/history && cp -R allure/reports/history allure/results/history && allure generate allure/results/ -o allure/reports --clean && allure open allure/reports

Run the test:
pytest --alluredir=/tmp/my_allure_results

Run the tests parallel:
pytest -n auto --alluredir=/tmp/my_allure_results

Open allure report:
allure serve /tmp/my_allure_results
allure serve /home/forestdumb/work/pytest_registration/allure_result

Remove report folder:
rm -r /tmp/my_allure_results
