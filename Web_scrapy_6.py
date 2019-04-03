import requests
from bs4 import BeautifulSoup
import json
import large_automation.config3
import sys
import csv

class Web_Scrapy():

    def __init__(self):
        self.head = large_automation.config3.obj.headers()
        self.cred = large_automation.config3.obj.credentials()
        self.url1 = large_automation.config3.obj.url_store()

    def executor(self):
        try:
            with requests.session() as s:
                url_1 = self.url1[0]
                header = json.loads(self.head.replace("'", "\""))
                credentials = self.cred
                r = s.get(url_1, headers=header)
                url_2 = self.url1[1]
                r = s.get(url_2)
                Web_Scrapy.boards(self, r)
        except Exception as e:
            print(e)
            lineno = sys.exc_info()[-1].tb_lineno
            print(lineno)

    def boards(self, r):
        try:
            with requests.session() as s:
                url_1 = self.url1[0]
                header = json.loads(self.head.replace("'", "\""))
                r = s.post(url_1, data=self.cred, headers=header)
                board_no = ["123457855", "111137067", "106606106", "107600350"]
                url_3 = self.url1[2]
                url_4 = self.url1[3]
                for i in board_no:
                    r = s.get(url_3 + i + url_4 + i + "")
                    soup1 = BeautifulSoup(r.content, 'lxml')
                    cards1 = soup1.find("p")
                    cards2 = cards1.text
                    listofcards = []
                    card_Nos = {}
                    card_Nos = json.loads(cards2)
                    asd = card_Nos['cards']
                    for i in range(len(asd)):
                        listofcards.append(card_Nos['cards'][i]['id'])
                    Web_Scrapy.cards(self, listofcards)
        except Exception as e:
            print(e)
            lineno = sys.exc_info()[-1].tb_lineno
            print(lineno)

    def cards(self, li):
        try:
            with requests.session() as s:
                url_1 = self.url1[0]
                header = json.loads(self.head.replace("'", "\""))
                r = s.post(url_1, data=self.cred, headers=header)
                listofcards = li
                url_5 = self.url1[4]
                consession_list=[]
                for i in listofcards:
                    try:
                        r = s.get(url_5 + i + "?id=" + i + "")
                        soup = BeautifulSoup(r.content, 'lxml')
                        card = soup.findAll(text=True)
                        if len(card) > 1:
                            card = card[0] + card[len(card) - 1]
                        elif len(card) == 1:
                            card = card[0]
                        card_Details = json.loads(card)
                        card_body = soup.find('body')
                        plannedFinish = card_Details['plannedFinish']
                        externalLinks = card_Details['externalLinks']
                        customId_ConsessionNo = card_Details['customId']['value']
                        if (externalLinks != []):
                            externalLinks = card_Details['externalLinks'][0]['url']
                        elif (externalLinks == None):
                            externalLinks = card_Details['externalLinks'][0]['label']
                        elif (externalLinks == []):
                            externalLinks = soup.findAll(text=True)[1]
                        card_ID = card_Details['id']
                        lane_ID = card_Details['lane']['id']
                        lane_ClassType = card_Details['lane']['laneClassType']
                        lane_title = card_Details['lane']['title']
                        priority = card_Details['priority']
                        card_size = card_Details['size']
                        card_title = card_Details['title']
                        card_title1 = card_title.split(" ")
                        engieneNo = card_title1[0]
                        engpartNo = str(card_title1[1:])
                        card_type = card_Details['type']['title']
                        if (lane_ClassType != "active"):
                            card_Details_data = {"card_title": card_title, "engieneNo": engieneNo, "partNo": engpartNo,
                                                 "customId_ConsessionNo": customId_ConsessionNo,
                                                 "plannedFinish": plannedFinish, "externalLinks": externalLinks,
                                                 "card_ID": card_ID,
                                                 "lane_ID": lane_ID, "lane_ClassType": lane_ClassType,
                                                 "priority": priority,
                                                 "card_size": card_size, "card_type": card_type}
                            # return card_Details_data
                            print(card_Details_data)

                            with open('Data_Validation.csv', 'w') as f:
                                w = csv.DictWriter(f, card_Details_data.keys())
                                w.writeheader()
                                w.writerow(card_Details_data)
                    except:
                        pass
                #print(consession_list)
        except Exception as e:
            print(e)
            lineno = sys.exc_info()[-1].tb_lineno
            print(lineno)


obj1 = Web_Scrapy()
obj1.executor()