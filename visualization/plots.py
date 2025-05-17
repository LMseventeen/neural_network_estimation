import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def plot_states_and_estimates(x, x_hat, N):
    """绘制系统状态和估计值"""
    fig, axs = plt.subplots(3, 1, figsize=(10, 12))
    time = np.arange(N+1)
    
    for i in range(3):
        axs[i].plot(time, x[i,:], 'k', label=f'x_{i+1}(k)')
        axs[i].plot(time, x_hat[i,:], '--r', label='估计值')
        axs[i].set_xlabel('时间 k')
        axs[i].set_ylabel(f'状态 x_{i+1}')
        axs[i].legend()
    
    plt.tight_layout()
    return fig

def plot_estimation_errors(x, x_hat, N):
    """绘制估计误差"""
    fig, ax = plt.subplots(figsize=(10, 6))
    time = np.arange(N+1)
    errors = x - x_hat
    
    for i in range(3):
        ax.plot(time, errors[i,:], label=f'x_{i+1}误差')
    
    ax.set_xlabel('时间 k')
    ax.set_ylabel('估计误差')
    ax.legend()
    return fig

def plot_trigger_events(trigger_times1, trigger_times2, N):
    """绘制事件触发时刻"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # 传感器1触发事件
    ax1.plot(trigger_times1, [1]*len(trigger_times1), 'g*', label='传感器1触发')
    ax1.plot(np.arange(N), [1]*N, 'k')
    ax1.set_xlabel('时间 k')
    ax1.set_ylabel('触发事件')
    ax1.legend()
    
    # 传感器2触发事件
    ax2.plot(trigger_times2, [2]*len(trigger_times2), 'rx', label='传感器2触发')
    ax2.plot(np.arange(N), [2]*N, 'k')
    ax2.set_xlabel('时间 k')
    ax2.set_ylabel('触发事件')
    ax2.legend()
    
    plt.tight_layout()
    return fig

def plot_performance_metrics(hinf_performance, trigger_frequency):
    """绘制性能指标"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # H∞性能指标
    ax1.bar(['H∞性能指标'], [hinf_performance])
    ax1.set_ylabel('性能值')
    
    # 触发频率
    ax2.bar(['传感器1', '传感器2'], trigger_frequency)
    ax2.set_ylabel('触发频率')
    
    plt.tight_layout()
    return fig 