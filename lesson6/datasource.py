import requests
def get_sitename()->list[str]:
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        print(e)
    else:
        sitenames = set()
        for rows in data['records']:
            sitenames.add(rows['sitename'])

        sitenames = list(sitenames)
        return sitenames