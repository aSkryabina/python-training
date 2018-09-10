import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(2)
    request.addfinalizer(wd.quit)
    return wd

def test_product(driver):
    driver.get("http://localhost/addressbook/")
    driver.find_element_by_name("user").send_keys("admin")
    driver.find_element_by_name("pass").send_keys("secret")
    driver.find_element_by_css_selector("[type=submit]").click()
    driver.find_element_by_xpath("//a[contains(text(),'groups')]").click()
    driver.find_element_by_xpath("//input[@value='New group']").click()
    driver.find_element_by_name("group_name").send_keys("12345")
    driver.find_element_by_name("group_header").send_keys("12345")
    driver.find_element_by_name("group_footer").send_keys("12345")
    driver.find_element_by_css_selector("[type=submit]").click()
    driver.find_element_by_xpath("//a[contains(text(),'group page')]").click()
    driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()