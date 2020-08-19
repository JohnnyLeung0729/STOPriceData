# This is a sample Python script.
import urllib
import requests
from bs4 import BeautifulSoup
import json
import time
from openpyxl import Workbook
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def read_datafile(filename):
    with open(filename,"r",encoding='UTF-8') as f:
        data = f.read()
        print(data)
    print(f'Hello world~')

def read_webdata(webadd):
    cookie = "cookie: cna=AvAmF6acrXwCAbcPskX0TjJ2; WD_SESSION=1c5e8714-ff5f-4256-ad46-47902e779e9a; isg=BO_vsh4F7FpY6ehtQLx9g0oGfgP5lEO2a2TsrwF8g95lUA9SCWVvBrYS0EjuMxsu"

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Connection': 'keep-alive',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Cookie': cookie,
        'referer': 'https://wangdian.sto.cn/api'
    }
    url = webadd  # csdn 个人中心中，加载名字的js地址
    seesion = requests.session()
    response = seesion.get(url, headers=header)
    # page=urllib.request.urlopen("https://wangdian.sto.cn/api/amount/transfer/searchQuotePrice?current=1&pageSize=100&params=%7B%22siteCode%22%3A%22471000%22%2C%22feeType%22%3A%220%22%7D")
    # print(page.read())
    #response.coding="gbk"
    wbdata = response.text
    print("正在打开请求")
    print(response.url)
    soup = BeautifulSoup(wbdata,'lxml')
    return(soup)

def insertOne(value, sheet, co):
    row = [co, value['id'], value['quoteName'], value['quoteCode'], "https://wangdian.sto.cn/api/amount/transfer/get/stepthree?id="+value['id']+"&action=view", value['siteCode'], value['siteName'], value['usageState'], value['auditState'], value['priority'], value['quoteCategory'], value['transportString'], value['billTypeString'], value['billCategoryString'], value['goodsTypeString'], value['createBy'], value['createUserId'], value['modifiedBy'], value['modifiedUserId']]
    print(type(row))
    sheet.append(row)

def create_exceldoc(diclist):
    book = Workbook()

    sheet = book.create_sheet("申通报价资料", 0)
    sheet.append(["序号", "报价ID", "报价名称", "报价编号","报价网址","所属站点编号","所属站点名称","使用状态","审核状态","优先级","报价类型","运输方式","面单类型","面单类别","物品类别","创建人","创建人编号","修改人","修改人编号"])

    sheets = book.get_sheet_names()
    count = 0
    # 向sheet中插入数据
    # webaddrow=[]
    for its in diclist:
        count = count+1
        insertOne(its, book.get_sheet_by_name(sheets[0]), count)
        # webaddrow.append("https://wangdian.sto.cn/api/amount/transfer/get/stepthree?id="+its['id']+"&action=view")

    # 保存数据到.xlsx文件
    book.save("d:\\申通河南站点报价基础信息.xlsx")
    print(str(count))
    return diclist
    # for x in diclist:
    #     print(x)

def create_priceexceldoc(diclist, filename, fileid, book):
    # book = Workbook()

    sheet = book.create_sheet("申通报价明细资料", 0)
    sheet.append(["报价ID","省","省编号","市","市编号","重量区间","价格公式","重量模式","piecePrice","continuedHeavy","continuedHeavyPrice","surcharge","lowestPrice","weightModeNameG","weightCarriesNumberG","weightDiscardsNumberG","weightModeParameterG","ykg","ykgPrice"])

    sheets = book.get_sheet_names()
    count = 0


    for x in diclist:
        for y in x["area"]:
            row=[fileid, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
            for yy in y["citys"]:
                row[1]= y["provinceName"]
                row[2]= y["provinceId"]
                row[3]= yy["cityName"]
                row[4]= yy["cityId"]
                for z in x["weight"]:
                    row[5]= str(z["startWeight"])+"<=w<="+str(z["endWeight"])
                    row[6]= z["priceExpression"]
                    row[7]= z["weightModeTypeG"]
                    row[8]= z["piecePrice"]
                    row[9]= z["continuedHeavy"]
                    row[10]= z["continuedHeavyPrice"]
                    row[11]= z["surcharge"]
                    row[12]= z["lowestPrice"]
                    row[13]= z["weightModeNameG"]
                    row[14]= z["weightCarriesNumberG"]
                    row[15]= z["weightDiscardsNumberG"]
                    row[16]= z["weightModeParameterG"]
                    row[17]= z["ykg"]
                    row[18]= z["ykgPrice"]
                    book.get_sheet_by_name(sheets[0]).append(row)
                    count= count+1


    # 保存数据到.xlsx文件
    book.save("d:\\" + filename + ".xlsx")
    print(str(count))

    # for x in diclist:
    #     print(x)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    webaddrow={}
    jsonobj=json.loads(read_webdata('https://wangdian.sto.cn/api/amount/transfer/searchQuotePrice?current=1&pageSize=100&params=%7B%22siteCode%22%3A%22471000%22%2C%22feeType%22%3A%220%22%7D').text)
    # print(type(jsonobj))
    jsonobj.pop('success')
    jsonobj.pop('requestId')
    if len(jsonobj.items()) == 1:
        for ite in jsonobj.items():
            webaddrow= create_exceldoc(ite[1]['items'])
    for p in webaddrow:
        jsonobjc=json.loads(read_webdata('https://wangdian.sto.cn/api/amount/transfer/get/stepthree?id=' + p['id'] + '&action=view').text)
        create_priceexceldoc(jsonobjc['data']['stoQuoteRegion'], p['quoteName'], p['id'], Workbook())
        time.sleep(5)




