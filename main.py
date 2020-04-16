import requests
from data import Location

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'
html_content = requests.get(url)#讀取網站

json_content = html_content.json()#html轉json
# print(json_content)

records = json_content.get('records')#get records
location = records.get('location')#從records中get records

'''
法一:取得location內的物件
for i in range(len(location)):
    print(location[i])
'''
all_locations = []
#法二
for item in location:
    l = Location()
    l.from_json(item)
    # all_locations.append(l)
    print(l.__dict__)
# print(all_locations)

    # weatherElement = item.get('weatherElement')
    # for element in weatherElement:
    #     elementName = element.get('elementName')
    #     elementValue = element.get('elementValue')
    #     # if elementName ==
    #     print(elementName, elementValue)