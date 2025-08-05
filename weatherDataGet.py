import requests
import pandas as pd
from datetime import datetime

# 抓 API
CWA_API = "CWB-FD756D9D-132A-4DB3-AC63-E1FB7F10E995"
dataset = 'O-A0001-001'
url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/{dataset}?Authorization={CWA_API}&format=JSON"

response = requests.get(url)
data = response.json()

# 抓資料
stations = data['records']['Station']

# 提取需要的欄位
rows = []
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

for s in stations:
    county = s['GeoInfo']['CountyName']
    town = s['GeoInfo']['TownName']
    weather = s['WeatherElement']['Weather']
    temp = s['WeatherElement']['AirTemperature']
    humd = s['WeatherElement']['RelativeHumidity']
    rows.append([now, county, town, weather, temp, humd])

# 存成 DataFrame
df = pd.DataFrame(rows, columns=["時間", "縣市", "鄉鎮", "天氣", "氣溫(°C)", "濕度(%)"])
df

from datetime import datetime

import os
from datetime import datetime

from zoneinfo import ZoneInfo  # Python 3.9+

now = datetime.now(ZoneInfo("Asia/Taipei"))
filename = now.strftime('%Y%m%d_%H%M') + "_weather.csv"
#
# 確保資料夾存在（沒有就自動建立）
os.makedirs("weatherData", exist_ok=True)


filepath = os.path.join("weatherData", filename)

df.to_csv(filepath, index=False, encoding='utf-8-sig')
print(f"✅ 已儲存：{filepath}")