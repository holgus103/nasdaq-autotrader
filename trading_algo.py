from candle import Candle
from application_state import ApplicationState
from typing import List;

class NaiveState(ApplicationState):
   def __init__(self) -> None:
      ApplicationState.__init__(self);
      self.minute_candles: List[Candle] = [];

   def get_candle_history(self, size: int, count_backwards: int) -> List[float]:
      l: int = len(self.history);
      step: int = size * count_backwards
      return self.history[l - step: l - step + size];

   def evaluate_situation(self) -> None: 
      l = len(self.history)
      #searching whether to open a position
      if(len(self.history) > 25):
         for i in range(0, 5):
            self.candles.append(Candle(self.get_candle_history(6, 4 - i)))
