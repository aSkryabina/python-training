from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Ann", middlename="V.", lastname="Skryabina", nickname="askryabina",
                               title="???", company="OOO Big Data Technology", address="St. Petersburg, Novoroshinskaya st. 4",
                               home="8152", mobile="931", work="812", fax="", email="a@a.ru", email2="a2@a.ru", email3="a3@a.ru",
                               homepage="localhost", bday="17", bmonth="December", byear="1987",
                               aday="3", amonth="August", ayear="2017", address2="Murm", phone2="906", notes="All"))
    app.session.logout()