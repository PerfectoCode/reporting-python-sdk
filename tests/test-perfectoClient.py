import traceback

from Conf import TestConf
import unittest
from selenium.webdriver.common.by import By


class ReportingTests(TestConf):

    def test_python_sdk_should_fail(self):
        for i in range(3):
            try:
                self.reporting_client.step_start('Navigate to google')
                self.driver.get('https://google.com')
                self.reporting_client.reportium_assert('assert something...', 'true')
                self.reporting_client.step_end('End this step!')

                # just out of context command
                self.driver.get('https://google.com')

                self.reporting_client.step_start('Search: PerfectoCode GitHub repo - Should fail')
                self.driver.find_element(By.NAME, 'qq').send_keys('PerfectoCode GitHub')
                self.reporting_client.step_end()
                print("test %s passed",i)
                break
            except Exception as e:
                print("trying test failed " + str(e))
                print(str(e))
                print(e.__doc__)
                print(e.args)
                print(traceback.format_exc())


if __name__ == '__main__':
    unittest.main()
