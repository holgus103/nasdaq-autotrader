import requests;
import time;
import json;

url = 'https://www.google.com/async/finance_wholepage_price_updates?ei=8-ASYJS0LZnT1fAPw-q6-AI&client=firefox-b-d&yv=3&async=mids:%2Fm%2F02fhwv,currencies:,_fmt:jspb'

while 1:
   res = requests.get(url);
   text = res.text;
   text = text[5:];
   jsonData = json.loads(text);
   symbolName = jsonData["PriceUpdate"][0][0][0][17][1];
   symbolPrice = jsonData["PriceUpdate"][0][0][0][17][4];
   print('{0} - {1}'.format(symbolName, symbolPrice));
   time.sleep(10);
