import pytest
from selenium import webdriver
from group import Group
from selenium.webdriver.support.ui import Select
from  contact import Contact


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
    create_group(driver, Group(name="12345", header="12345", footer="12345"))
    return_to_groups_page(driver)
    logout(driver)

def test_add_contacts(driver):
    open_home_page(driver)
    login(driver, username="admin", password="secret")
    open_add_new_page(driver)
    create_contact(driver, Contact(firstname="Ann", middlename="V.", lastname="Skryabina", nickname="askryabina",
                                   title="???", company="OOO Big Data Technology", address="St. Petersburg, Novoroshinskaya st. 4",
                                   home="8152", mobile="931", work="812", fax="", email="a@a.ru", email2="a2@a.ru", email3="a3@a.ru",
                                   homepage="localhost", bday="17", bmonth="December", byear="1987",
                                   aday="3", amonth="August", ayear="2017", address2="Murm", phone2="906", notes="All"))
    logout(driver)


def create_contact(driver, contact):
    driver.find_element_by_name("firstname").click()
    driver.find_element_by_name("firstname").clear()
    driver.find_element_by_name("firstname").send_keys(contact.firstname)
    driver.find_element_by_name("middlename").click()
    driver.find_element_by_name("middlename").clear()
    driver.find_element_by_name("middlename").send_keys(contact.middlename)
    driver.find_element_by_name("lastname").click()
    driver.find_element_by_name("lastname").clear()
    driver.find_element_by_name("lastname").send_keys(contact.lastname)
    driver.find_element_by_name("nickname").click()
    driver.find_element_by_name("nickname").clear()
    driver.find_element_by_name("nickname").send_keys(contact.nickname)
    driver.find_element_by_name("title").click()
    driver.find_element_by_name("title").clear()
    driver.find_element_by_name("title").send_keys(contact.title)
    driver.find_element_by_name("company").click()
    driver.find_element_by_name("company").clear()
    driver.find_element_by_name("company").send_keys(contact.company)
    driver.find_element_by_name("address").click()
    driver.find_element_by_name("address").clear()
    driver.find_element_by_name("address").send_keys(contact.address)
    driver.find_element_by_name("home").click()
    driver.find_element_by_name("home").clear()
    driver.find_element_by_name("home").send_keys(contact.home)
    driver.find_element_by_name("mobile").click()
    driver.find_element_by_name("mobile").clear()
    driver.find_element_by_name("mobile").send_keys(contact.mobile)
    driver.find_element_by_name("work").click()
    driver.find_element_by_name("work").clear()
    driver.find_element_by_name("work").send_keys(contact.work)
    driver.find_element_by_name("fax").click()
    driver.find_element_by_name("fax").clear()
    driver.find_element_by_name("fax").send_keys(contact.fax)
    driver.find_element_by_name("email").click()
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(contact.email)
    driver.find_element_by_name("email2").click()
    driver.find_element_by_name("email2").clear()
    driver.find_element_by_name("email2").send_keys(contact.email2)
    driver.find_element_by_name("email3").click()
    driver.find_element_by_name("email3").clear()
    driver.find_element_by_name("email3").send_keys(contact.email3)
    driver.find_element_by_name("homepage").click()
    driver.find_element_by_name("homepage").clear()
    driver.find_element_by_name("homepage").send_keys(contact.homepage)
    Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
    Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
    driver.find_element_by_name("byear").click()
    driver.find_element_by_name("byear").clear()
    driver.find_element_by_name("byear").send_keys(contact.byear)
    Select(driver.find_element_by_name("aday")).select_by_visible_text(contact.aday)
    Select(driver.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
    driver.find_element_by_name("ayear").click()
    driver.find_element_by_name("ayear").clear()
    driver.find_element_by_name("ayear").send_keys(contact.ayear)
    driver.find_element_by_name("address2").click()
    driver.find_element_by_name("address2").clear()
    driver.find_element_by_name("address2").send_keys(contact.address2)
    driver.find_element_by_name("phone2").click()
    driver.find_element_by_name("phone2").clear()
    driver.find_element_by_name("phone2").send_keys(contact.phone2)
    driver.find_element_by_name("notes").click()
    driver.find_element_by_name("notes").clear()
    driver.find_element_by_name("notes").send_keys(contact.notes)
    driver.find_element_by_name("submit").click()


def open_add_new_page(driver):
    driver.find_element_by_link_text("add new").click()


def logout(driver):
    driver.find_element_by_link_text("Logout").click()


def return_to_groups_page(driver):
    driver.find_element_by_link_text("group page").click()


def create_group(driver, group):
    # init group creation
    driver.find_element_by_xpath("//input[@value='New group']").click()
    # fill group form
    driver.find_element_by_name("group_name").click()
    driver.find_element_by_name("group_name").clear()
    driver.find_element_by_name("group_name").send_keys(group.name)
    driver.find_element_by_name("group_header").click()
    driver.find_element_by_name("group_header").clear()
    driver.find_element_by_name("group_header").send_keys(group.header)
    driver.find_element_by_name("group_footer").click()
    driver.find_element_by_name("group_footer").clear()
    driver.find_element_by_name("group_footer").send_keys(group.footer)
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