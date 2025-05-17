import numpy as np

class SystemParameters:
    def __init__(self):
        self.n = 3  # 系统维度
        self.gamma = 0.8  # H∞性能指标
        self.tau_m = 0  # 最小时滞
        self.tau_M = 2  # 最大时滞
        
        # 系统矩阵
        self.A = np.array([[0.5, 0, 0],
                          [0, 0.4, 0],
                          [0, 0, 0.5]])
        
        self.B = np.array([[0.2, -0.3, 0.2],
                          [0, 0.2, 0.1],
                          [-0.1, -0.1, 0.2]])
        
        self.D = np.array([[-0.1, -0.2, 0.1],
                          [0.4, 0.1, -0.2],
                          [0.2, 0.1, -0.1]])
        
        self.E = np.array([[0.4, -0.1, 0.2],
                          [0.1, -0.1, 0],
                          [0, 0.1, -0.1]])
        
        self.L = np.array([[-0.1],
                          [0.2],
                          [0.1]])
        
        self.C = np.array([[0.3, 0.3, 0.2],
                          [-0.5, 0.2, 0.4]])
        
        self.M = np.array([[0.5, -0.7, 0.9]])
        
        self.G = np.array([[0.5],
                          [-0.7]]) 