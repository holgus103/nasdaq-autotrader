import const;

class ApplicationState:
   def __init__(self):
      self.history = [];
   
   def history_tick(self, val):
      self.history.append(val);
      # remove elements if the history is too long
      if(len(self.history) > const.MAX_HISTORY_LENGTH):
         self.history = self.history[1:];   