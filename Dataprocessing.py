

import json


def DealFile():
    with open('D:/GetData/Data.json', 'r', encoding="utf-8")as f:
        data = json.load(f)
        print(data)
        Dataprocessing(data)


# 初步提取数据
def Dataprocessing(data):
    data = data["data"]["continent"]
    Asia = data[0]["country"]
    Europe = data[1]["country"]
    NorthAmerica = data[2]["country"]
    SouthAmerica = data[3]["country"]
    Africa = data[4]["country"]
    Oceania = data[5]["country"]
    country = Asia + Europe + NorthAmerica + SouthAmerica + Africa + Oceania

    DealCountry(country)


# 数据格式进行处理
def DealCountry(country):
    for i in range(len(country)):
        name = country[i]["provinceName"]
        value = country[i]["confirmedCount"]
        ChangeDate(name, value)


countryList = []

LList=[]
def ChangeDate(name, value):
    # 读取国家名称中文转英文数据
    with open('D:/GetData/countryC2E.json', 'r', encoding='utf-8') as f:
        c2e = json.load(f)

    try:
        countryDict = {}
        countryDict["name"] = c2e[name]
        countryDict["value"] = value
        countryList.append(countryDict)

    except:
        LList.append(name)

# 数据保存
def SaveDate(country):
    # DataDict={}
    # DataDict["data"] = country
    with open("Data_deal.json", 'w', encoding="utf-8") as f:
        json.dump(country, f)
        print("保存成功！")


if __name__ == '__main__':
    DealFile()
    SaveDate(countryList)

