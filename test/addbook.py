import pytest
from model.group import Group
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="12345", header="12345", footer="12345"))
    app.logout()

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Ann", middlename="V.", lastname="Skryabina", nickname="askryabina",
                                   title="???", company="OOO Big Data Technology", address="St. Petersburg, Novoroshinskaya st. 4",
                                   home="8152", mobile="931", work="812", fax="", email="a@a.ru", email2="a2@a.ru", email3="a3@a.ru",
                                   homepage="localhost", bday="17", bmonth="December", byear="1987",
                                   aday="3", amonth="August", ayear="2017", address2="Murm", phone2="906", notes="All"))
    app.logout()
