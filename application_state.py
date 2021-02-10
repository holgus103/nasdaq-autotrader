import const;

class ApplicationState:
   def __init__(self):
      self.history = [];
      self.cash = const.INITIAL_CASH;
   
   def history_tick(self:, val: float):
      self.history.append(val);
      # remove elements if the history is too long
      if(len(self.history) > const.MAX_HISTORY_LENGTH):
         self.history = self.history[1:];   
   