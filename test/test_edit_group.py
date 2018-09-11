
def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(group_name="11111")
    app.session.logout()