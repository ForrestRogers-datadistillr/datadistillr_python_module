import requests

class datadistillr:

    def __init__(self):
        self.login_page = "https://devapp.datadistillr.io/api/login"
        self.logout_page = "https://devapp.datadistillr.io/api/logout"
        self.projects_page = "https://devapp.datadistillr.io/api/projects"


    def login(self, username, password):
        user_info = {"email": str(username), "password": str(password)}
        requests.post(url = self.login_page, params = user_info)

    def logout(self):
        requests.get(url = self.logout_page)

    def get_projects(self):
        requests.get(url = self.projects_page)



