import time
import pytest
from Amazon.base.Driverclass import Driver

@pytest.fixture(scope='class')
def beforeclass(request):
    print("before class")
    d1 = Driver()
    driver = d1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')

# @pytest.fixture()
# def beforeMethod():
#     print('Before Method')
#     yield
#     print('After Method')
