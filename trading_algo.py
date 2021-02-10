from application_state import ApplicationState


STATE_KEY = 'naive_algorithm';


class NaiveState(ApplicationState):
   def __init__(self):
      ApplicationState.__init__(self);
      self.moving_average = 0;

   def evaluate_situation(self):
      # calculate moving averages
      self.moving_average = float(sum(self.history)) / float(len(self.history));
      print(self.moving_average);