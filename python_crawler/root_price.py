import requests
import bs4
import re
import openpyxl

def open_url(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    res = requests.get(url, headers=headers)
    return res

def find_data(res):
    data = []
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    content = soup.find(id="mp-editor")
    targets = content.find_all("p")
    targets = iter(targets)
    for each in targets:
        if each.text.isnumeric():
            data.append([
               re.search(r'\[(.+)\]',  next(targets).text).group(1),
                re.search(r'\d.*',  next(targets).text).group(),
                re.search(r'\d.*',  next(targets).text).group(),
                re.search(r'\d.*',  next(targets).text).group()])
    return data

def to_excel(data):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    ws = wb.active
    ws.append(["城市", "平均房价", "平均工资", "房价工资表"])
    for each in data:
        ws.append(each)
    wb.save("2017年中国主要城市房价工资比排行榜.xlsx")
    
def main():
    url = "http://www.sohu.com/a/154203859_99913782"
    res = open_url(url)
    data = find_data(res)
    to_excel(data)
if __name__ == "__main__":
    main()
