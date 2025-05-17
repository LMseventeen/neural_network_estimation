import numpy as np
import cvxpy as cp
from .nonlinear import f, g

class StateEstimator:
    def __init__(self, params):
        self.params = params
        self.K = self._design_filter_gain()
        
    def _design_filter_gain(self):
        # 简化的滤波器增益设计
        # 实际应用中需要实现完整的LMI求解
        return np.array([[0.1, 0],
                        [0, 0.1],
                        [0, 0.1]])
        
    def estimate(self, x, y, x_d):
        return (self.params.A @ x + 
                self.params.B @ f(x) + 
                self.params.D @ g(x) + 
                self.K @ (y - self.params.C @ x)) 