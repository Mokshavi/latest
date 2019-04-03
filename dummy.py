import large_automation.Web_Scrapy5
import csv

card_Details_data = {"card_title": 'abc', "engieneNo": '123', "partNo": 'asd123',
                                                 "customId_ConsessionNo": 'zxcvb',
                                                 "plannedFinish": '12sd56', "externalLinks": 'ert',
                                                 "card_ID": 'rfv',
                                                 "lane_ID": 'asd', "lane_ClassType": 'lkjhg',
                                                 "priority": 'sdf',
                                                 "card_size": '1234', "card_type": 'fgh'}
with open('Data_Validation1.csv', 'w') as f:
    w = csv.DictWriter(f, card_Details_data.keys())
    w.writeheader()
    w.writerow(card_Details_data)