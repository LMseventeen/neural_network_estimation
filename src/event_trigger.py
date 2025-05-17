import numpy as np

class EventTrigger:
    def __init__(self, sigma):
        self.sigma = sigma
        self.last_triggered_value = None
        self.trigger_times = []
        
    def check_trigger(self, current_value, time_step):
        if self.last_triggered_value is None:
            self.last_triggered_value = current_value
            self.trigger_times.append(time_step)
            return True
            
        # 事件触发条件
        if self.sigma * np.dot(current_value, current_value) <= \
           np.dot(current_value - self.last_triggered_value, 
                 current_value - self.last_triggered_value):
            self.last_triggered_value = current_value
            self.trigger_times.append(time_step)
            return True
        return False 