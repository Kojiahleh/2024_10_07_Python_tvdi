import requests
from requests import Response

def main():
    url_csv = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=5481753E-52AF-40DA-9A8A-9E192B245E13'
    # res:Response = requests.request("GET",url_csv)

    # if res.status_code == 200:
    try:
        res:Response = requests.request("GET",url_csv)
        res.raise_for_status()
        # print("下載成功")
        res.encoding = 'utf-8'
        content:str = res.text
        with open('a1.csv',newline='',encoding='utf-8',mode='w') as file:
            print(type(file))
            file.write(content)
    # else:
    except Exception as e:
        # print("下載失敗")
        print(e)
    else:
        print("下載,儲檔成功")


if __name__ == '__main__':
    main()