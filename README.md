## Reporting SDK for Python

**Usage:**

- Download the SDK using one of the following commands: <br/>
`pip install perfecto-reporting`<br/>
`easy_install perfecto-reporting`<br/>
 (Just for illustrating it will be available asap).
 
- imports: 
```python
from reporting import TestContext, PerfectoReportiumClient, PerfectoExecutionContext, TestResultFactory
```

- Creating reporting client (use client as instance variable):
 ```Python
def create_reporting_client(self):
       perfecto_execution_context = PerfectoExecutionContext(self.driver)
       self.reporting_client = PerfectoReportiumClient(perfecto_execution_context)
```

- Starting a new test (first sample unittest, second is freestyle):<br/>
unittest (will use the method name as the test's name):
```python
self.reporting_client.test_start(self.id(),
                TestContext('tag1', 'tag2', 'tag3'))
```
freestyle: 
```python
self.reporting_client.test_start('Test name', TestContext('tags params'))
```

- Log a new test step:<br/>
```python
self.reporting_client.test_step('Description')
```

- End test (Unittest): <br/>
```python
def tearDown(self):
    try:
        if self.currentResult.wasSuccessful():
            self.reporting_client.test_stop(TestResultFactory.create_success())
        else:
            self.reporting_client.test_stop(TestResultFactory.create_failure(self.currentResult.errors,
                                                                             self.currentResult.failures))
        # Print report's url
        print 'Report-Url: ' + self.reporting_client.report_url() + '\n'
    except Exception as e:
        print e.message

    self.driver.quit()
```

Code samples at https://github.com/PerfectoCode/Reporting-Samples/tree/master/Python