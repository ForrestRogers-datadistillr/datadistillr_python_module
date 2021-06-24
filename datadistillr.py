import requests
import http.cookiejar
jar = http.cookiejar.CookieJar()

class datadistillr:

    def __init__(self):
        self.login_page = "https://devapp.datadistillr.io/api/login"
        self.logout_page = "https://devapp.datadistillr.io/api/logout"
        self.projects_page = "https://devapp.datadistillr.io/api/projects"


    def login(self, username, password):
        user_info = {"username": str(username), "password": str(password)}
        requests.post(url = self.login_page, params = user_info, cookies = jar)

    def logout(self):
        requests.get(url = self.logout_page, cookies = jar)

    def get_projects(self):
        requests.get(url = self.projects_page, cookies = jar)




