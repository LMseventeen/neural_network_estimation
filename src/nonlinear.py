import numpy as np

def f(x):
    """非线性函数f的实现"""
    return np.array([
        0.1*x[0] - np.tanh(0.2*x[0]),
        -np.tanh(0.4*x[1]),
        -0.1*x[2] - np.tanh(0.2*x[2])
    ])

def g(x):
    """非线性函数g的实现"""
    return np.array([
        -0.2*x[0] - np.tanh(0.1*x[0]),
        0.3*x[1] - np.tanh(0.1*x[1]),
        -np.tanh(0.1*x[2])
    ])

def hx(x):
    """非线性函数hx的实现"""
    return np.array([
        0.2*x[0] - np.tanh(0.1*x[0]),
        -0.2*x[1] - np.tanh(0.2*x[1]),
        0.4*x[2] - np.tanh(0.2*x[2])
    ])

def sat(x):
    """饱和函数实现"""
    return np.sign(x) * np.minimum(0.02, np.abs(x)) 