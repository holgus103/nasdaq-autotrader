import requests;
import json;

def updateData(url):
   """
      Returns the symbol and the price of an asset.
      Parameters
      -----------
      url: url used for information retrieval

      Returns 
      -----------
      tuple 
      (symbol name, symbol price)
   """
   res = requests.get(url);
   text = res.text;
   text = text[5:];
   jsonData = json.loads(text);
   symbolName = jsonData["PriceUpdate"][0][0][0][17][1];
   symbolPrice = jsonData["PriceUpdate"][0][0][0][17][4];
   print('{0} - {1}'.format(symbolName, symbolPrice));
   return (symbolName, symbolPrice);