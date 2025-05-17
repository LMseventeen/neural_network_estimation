import numpy as np
import matplotlib.pyplot as plt
from src.system import SystemParameters
from src.nonlinear import f, g, hx, sat
from src.event_trigger import EventTrigger
from src.estimator import StateEstimator
from visualization.plots import (plot_states_and_estimates, 
                               plot_estimation_errors,
                               plot_trigger_events,
                               plot_performance_metrics)

def calculate_delay(x, k, params):
    """计算时滞项"""
    x_d = np.zeros(3)
    for m in range(20):
        x_d += 2**(-3-m) * hx(x[:, k-m])
    return x_d

def update_system_state(x, x_d, k, params):
    """更新系统状态"""
    return (params.A @ x + 
            params.B @ f(x) + 
            params.D @ g(x) + 
            params.E @ x_d + 
            params.L.flatten() * np.sin(k) * np.exp(-0.15*k))

def main():
    # 初始化参数
    params = SystemParameters()
    N = 60  # 仿真步数
    
    # 初始化状态
    x = np.zeros((3, N+1))
    x_hat = np.zeros((3, N+1))
    
    # 初始化事件触发机制
    trigger1 = EventTrigger(sigma=0.2)
    trigger2 = EventTrigger(sigma=0.2)
    
    # 初始化估计器
    estimator = StateEstimator(params)
    
    # 主循环
    for k in range(N):
        # 计算时滞
        x_d = calculate_delay(x, k, params)
        
        # 更新系统状态
        x[:, k+1] = update_system_state(x[:, k], x_d, k, params)
        
        # 计算测量输出
        y = params.C @ x[:, k+1]
        y = sat(y)
        
        # 事件触发检查
        trigger1.check_trigger(y[0], k)
        trigger2.check_trigger(y[1], k)
        
        # 状态估计
        x_hat[:, k+1] = estimator.estimate(x_hat[:, k], y, x_d)
    
    # 计算性能指标
    hinf_performance = np.sqrt(np.sum((x - x_hat)**2)) / \
                      np.sqrt(np.sum((np.sin(np.arange(N+1))*np.exp(-0.15*np.arange(N+1)))**2 + 
                                   (np.cos(np.arange(N+1))*np.exp(-0.1*np.arange(N+1)))**2))
    
    trigger_frequency = [len(trigger1.trigger_times)/N, 
                        len(trigger2.trigger_times)/N]
    
    # 绘制结果
    figs = []
    figs.append(plot_states_and_estimates(x, x_hat, N))
    figs.append(plot_estimation_errors(x, x_hat, N))
    figs.append(plot_trigger_events(trigger1.trigger_times, 
                                  trigger2.trigger_times, N))
    figs.append(plot_performance_metrics(hinf_performance, trigger_frequency))
    
    # 显示所有图形
    plt.show()

if __name__ == "__main__":
    main() 