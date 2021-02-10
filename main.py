from application_state import ApplicationState
import time;
import data_retrieval;
import trading_algo;
import const;

application_state : ApplicationState = trading_algo.NaiveState()

while 1:
   (ticker, price) = data_retrieval.updateData(const.url);
   application_state.history_tick(val=price);
   # process current state
   application_state.evaluate_situation();
   time.sleep(10);
