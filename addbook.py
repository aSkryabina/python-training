import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(2)
    request.addfinalizer(wd.quit)
    return wd

def test_add_group(driver):
    open_home_page(driver)
    login(driver, username="admin", password="secret")
    open_groups_page(driver)
    create_group(driver, name="12345", header="12345", footer="12345")
    return_to_groups_page(driver)
    logout(driver)


def logout(driver):
    driver.find_element_by_link_text("Logout").click()


def return_to_groups_page(driver):
    driver.find_element_by_link_text("group page").click()


def create_group(driver, name, header, footer):
    # init group creation
    driver.find_element_by_xpath("//input[@value='New group']").click()
    # fill group form
    driver.find_element_by_name("group_name").click()
    driver.find_element_by_name("group_name").clear()
    driver.find_element_by_name("group_name").send_keys(name)
    driver.find_element_by_name("group_header").click()
    driver.find_element_by_name("group_header").clear()
    driver.find_element_by_name("group_header").send_keys(header)
    driver.find_element_by_name("group_footer").click()
    driver.find_element_by_name("group_footer").clear()
    driver.find_element_by_name("group_footer").send_keys(footer)
    # submit group creation
    driver.find_element_by_css_selector("[type=submit]").click()


def open_groups_page(driver):
    driver.find_element_by_link_text("groups").click()


def login(driver, username, password):
    driver.find_element_by_name("user").click()
    driver.find_element_by_name("user").clear()
    driver.find_element_by_name("user").send_keys(username)
    driver.find_element_by_name("pass").click()
    driver.find_element_by_name("pass").clear()
    driver.find_element_by_name("pass").send_keys(password)
    driver.find_element_by_css_selector("[type=submit]").click()


def open_home_page(driver):
    driver.get("http://localhost/addressbook/")