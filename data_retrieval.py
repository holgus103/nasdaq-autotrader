import requests;
import json;
from typing import Any, Tuple

from requests.models import Response;

def updateData(url: str) -> Tuple[str, float]:
   """
      Returns the symbol and the price of an asset.
      Parameters
      -----------
      url: url used for information retrieval

      Returns 
      -----------
      Tuple[str, float] 
      (symbol name, symbol price)
   """
   res: Response = requests.get(url);
   text: str = res.text;
   text = text[5:];
   jsonData : Any = json.loads(text);
   symbolName: str = jsonData["PriceUpdate"][0][0][0][17][1];
   symbolPrice: str = jsonData["PriceUpdate"][0][0][0][17][4];
   print('{0} - {1}'.format(symbolName, symbolPrice));
   return (symbolName, symbolPrice);