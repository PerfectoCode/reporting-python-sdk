import unittest
from selenium import webdriver
import sys
import os
sys.path.append(os.path.realpath("../perfecto-reporting"))
from perfecto import *


class TestConf(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.user = os.environ['USEWRNAME']
        self.password = os.environ['PASSWORD']
        self.host = os.environ['LAB']
        self.driver = None
        self.reporting_client = None

        super(TestConf, self).__init__(*args, **kwargs)

    def setUp(self):
        capabilities = {
            'platformName': 'Android',
            'deviceName': '',
            'user': self.user,
            'password': self.password,
            'securityToken' : 'eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlMWRkYTg4Mi0yMGQ4LTRmZjItYWE0YS1jNWQ2M2VjMWI0NWYifQ.eyJqdGkiOiIyNDhlYzE1Yy05OGZmLTRjMTEtYTY2Ny1lOGM2M2Y1MTk3Y2QiLCJleHAiOjAsIm5iZiI6MCwiaWF0IjoxNTk4OTQ0NjU3LCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjkwOTAvYXV0aC9yZWFsbXMvcmVwb3J0aW5nLXN0YWdpbmctcGVyZmVjdG9tb2JpbGUtY29tIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo5MDkwL2F1dGgvcmVhbG1zL3JlcG9ydGluZy1zdGFnaW5nLXBlcmZlY3RvbW9iaWxlLWNvbSIsInN1YiI6IjRkYTM3ZmJiLTYxZjEtNDIxNC04YTFlLWFhNzg2MzIyZmQwYiIsInR5cCI6Ik9mZmxpbmUiLCJhenAiOiJvZmZsaW5lLXRva2VuLWdlbmVyYXRvciIsImF1dGhfdGltZSI6MCwic2Vzc2lvbl9zdGF0ZSI6ImI2N2VkMTdiLWMzYmItNGM2MS1iNWIzLWJmOWE2NTA3YTI0NyIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIG9mZmxpbmVfYWNjZXNzIGVtYWlsIn0.3nKxjZ_wmrdRchPsrps1Zm3UX8XnxMjVK1O0gy7Ag44'
        }
        self.driver = webdriver.Remote('https://' + self.host + '/nexperience/perfectomobile/wd/hub', capabilities)
        self.create_reporting_client()
        self.reporting_client.test_start(self.id(), TestContext('daniela@perfectomobile.com', 'Python', 'unittest'))

    def run(self, result=None):
        self.currentResult = result  # remember result for use in tearDown
        unittest.TestCase.run(self, result)  # call superclass run method

    def tearDown(self):
        try:
            if self.currentResult.wasSuccessful():
                self.reporting_client.test_stop(TestResultFactory.create_success())
            else:
                # self.reporting_client.test_stop(TestResultFactory.create_failure('failure 4096' * 1000))
                
                self.reporting_client.test_stop(TestResultFactory.create_failure(self.currentResult.errors,
                                                                                 self.currentResult.failures))
            # Print report's url
            print 'Report-Url: ' + self.reporting_client.report_url() + '\n'

        except Exception as e:
            print e.message

        self.driver.quit()

    def create_reporting_client(self):
        perfecto_execution_context = PerfectoExecutionContext(self.driver, ['execution tag1', 'execution tag2'], Job('JobName', 1), Project('ProjectName', 'v1.2'))
        self.reporting_client = PerfectoReportiumClient(perfecto_execution_context)
