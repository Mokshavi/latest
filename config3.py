import requests
from configparser import ConfigParser


class Config:

    def __init__(self):
        self.parser = ConfigParser()
        self.parser.read('database.config')
        # print(self.parser.read('database.config'))

    def headers(self):
        agent = self.parser.get('database_config', 'head')
        return agent

    def credentials(self):
        username = self.parser.get('database_config', 'username')
        password = self.parser.get('database_config', 'password')
        login_data = {"userName": username, "password": password, 'Login': "Log in"}
        # print(login_data)
        return login_data

    def session(self):
        s = requests.session()
        # print(s)
        return s

    def url_store(self):
        url1=self.parser.get('database_config', 'url')
        url2=self.parser.get('database_config','url2')
        url3 = self.parser.get('database_config', 'url3')
        url4 = self.parser.get('database_config', 'url4')
        url5 = self.parser.get('database_config', 'url5')
        # print(url1)
        return url1,url2,url3,url4,url5

    # def boards(self):
    #     boards=self.parser.get('database_config','board_no')
    #     return boards

obj = Config()

# obj.Headers()
# obj.Credentials()
# obj.Session()
# obj.url_store()
#obj.boards()
#print(obj.boards())
# print(obj.url_store()[1])
