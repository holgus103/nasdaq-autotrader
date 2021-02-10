from enum import Enum;
from typing import List;

class Direction(Enum):
   UP = 1,
   DOWN = 2


class Candle:
   def __init__(self, history: List[float]) -> None:
      self.close: float = max(history);
      self.open:float = min(history);
      self.direction: Direction = self.open <= self.close and Direction.UP or Direction.DOWN;